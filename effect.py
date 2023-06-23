from numba import cuda
from numba.cuda import jit
import cv2
import numpy as np
import math
block_size = (8, 8, 8)
import time
import GPUtil
from shared_mem import MemoryManager
from LoadingWindow import create_loading_window

@cuda.jit
def edge_detection_kernel_images(input_images, output_edges, threshold1, threshold2):
    i, row, col = cuda.grid(3)
    if i < input_images.shape[0] and row < input_images.shape[1] and col < input_images.shape[2]:
        if i >= 0 and row > 0 and row < input_images.shape[1]-1 and col > 0 and col < input_images.shape[2]-1:
            gx = input_images[i, row, col, 2] - input_images[i, row, col-1, 2] + 2 * (input_images[i, row, col+1, 2] - input_images[i, row, col-1, 2]) - input_images[i, row, col, 2] + input_images[i, row, col+1, 2]
            gy = input_images[i, row, col, 2] - input_images[i, row-1, col, 2] + 2 * (input_images[i, row+1, col, 2] - input_images[i, row-1, col, 2]) - input_images[i, row, col, 2] + input_images[i, row+1, col, 2]
            gradient = math.sqrt(gx ** 2 + gy ** 2)

            if gradient > threshold1 and gradient < threshold2:
                output_edges[i, row, col, 0] = 255
                output_edges[i, row, col, 1] = 255
                output_edges[i, row, col, 2] = 255
            else:
                output_edges[i, row, col, 0] = 0
                output_edges[i, row, col, 1] = 0
                output_edges[i, row, col, 2] = 0

@cuda.jit
def blur_kernel_images(input_images, output_images, kernel_size):
    image_index, row, col = cuda.grid(3)
    
    if image_index < input_images.shape[0] and row < input_images.shape[1] and col < input_images.shape[2]:
        kernel_radius = kernel_size // 2
        
        pixel_sum_b = 0.0
        pixel_sum_g = 0.0
        pixel_sum_r = 0.0
        count = 0
        
        for i in range(-kernel_radius, kernel_radius + 1):
            for j in range(-kernel_radius, kernel_radius + 1):
                blur_row = min(max(row + i, 0), input_images.shape[1] - 1)
                blur_col = min(max(col + j, 0), input_images.shape[2] - 1) 
                pixel_sum_b +=   input_images[image_index][blur_row][blur_col][0] 
                pixel_sum_g += input_images[image_index][blur_row][blur_col][1]
                pixel_sum_r += input_images[image_index][blur_row][blur_col][2]
                count +=1
        output_images[image_index][row][col][0] = pixel_sum_b / count
        output_images[image_index][row][col][1] = pixel_sum_g / count
        output_images[image_index][row][col][2] = pixel_sum_r / count
@cuda.jit
def sepia_kernel(input_images, output_images):
    image_index, row, col = cuda.grid(3)

    if image_index < input_images.shape[0] and row < input_images.shape[1] and col < input_images.shape[2]:
        r = input_images[image_index,row, col, 0]
        g = input_images[image_index,row, col, 1]
        b = input_images[image_index,row, col, 2]

        out_r = min(0.393 * r + 0.769 * g + 0.189 * b, 255)
        out_g = min(0.349 * r + 0.686 * g + 0.168 * b, 255)
        out_b = min(0.272 * r + 0.534 * g + 0.131 * b, 255)

        output_images[image_index,row, col, 0] = out_r
        output_images[image_index,row, col, 1] = out_g
        output_images[image_index,row, col, 2] = out_b
@cuda.jit
def bgr_to_grayscale_kernel(input_images, output_images):
    image_index,row, col = cuda.grid(3)

    if image_index < input_images.shape[0] and row < input_images.shape[1] and col < input_images.shape[2]:
        r = input_images[image_index,row, col, 0]
        g = input_images[image_index,row, col, 1]
        b = input_images[image_index,row, col, 2]
        gray = 0.2989 * r + 0.587 * g + 0.114 * b
        output_images[image_index,row, col, 0] = gray
        output_images[image_index,row, col, 1] = gray
        output_images[image_index,row, col, 2] = gray

@cuda.jit
def vignette_kernel(input_images, output_images, center_x, center_y, strength):
    img_idx, row, col = cuda.grid(3)
    if img_idx < output_images.shape[0] and row < output_images.shape[1] and col < output_images.shape[2]:
        y = row / output_images.shape[1] - center_y
        x = col / output_images.shape[2] - center_x
        distance = math.sqrt(x**2 + y**2)
        vignette = 1.0 - (distance * strength)
        vignette = max(vignette, 0.0)
        for channel in range(output_images.shape[3]):
            output_images[img_idx, row, col, channel] = input_images[img_idx, row, col, channel] * vignette
@cuda.jit
def change_brightness_kernel(input_images, output_images, alpha, beta):
    img_idx, row, col = cuda.grid(3)
    if img_idx < output_images.shape[0] and row < output_images.shape[1] and col < output_images.shape[2]:
        for channel in range(output_images.shape[3]):
            output_images[img_idx, row, col, channel] = alpha * input_images[img_idx, row, col, channel] + beta
            if(output_images[img_idx, row, col, channel] > 255):
                output_images[img_idx, row, col, channel] = 255

class Effect():
    
    def grayscale(self, frames):
        grid_size = ((frames.shape[0] - 1) // block_size[0] + 1, (frames.shape[1] - 1) // block_size[1] + 1, (frames.shape[2] - 1) // block_size[2] + 1)
        frames_processed_cnt =0
        im_size = frames[0].nbytes  /  1000000
        single_transfer_size = 2.2* im_size

        #loading window
        p = create_loading_window(frames.shape[0])
        manager = MemoryManager(name='mymemory', to_create=True)

        while(frames_processed_cnt < frames.shape[0]):
            gpus = GPUtil.getGPUs()
            free_memory = gpus[0].memoryFree
            frames_next_transfer_count = int(free_memory // (single_transfer_size))
            if(frames_next_transfer_count > frames.shape[0]):
                frames_next_transfer_count = frames.shape[0]
            gpu_images = cuda.to_device(frames[frames_processed_cnt:frames_next_transfer_count])
            gpu_edges = cuda.device_array_like(frames[frames_processed_cnt:frames_next_transfer_count])
            bgr_to_grayscale_kernel[grid_size, block_size](gpu_images, gpu_edges)
            frames[frames_processed_cnt:frames_next_transfer_count] =  gpu_edges.copy_to_host()
            frames_processed_cnt = frames_processed_cnt + frames_next_transfer_count
            print(frames_processed_cnt)
            manager.put(frames_processed_cnt)
        
        manager.block.close()
        manager.block.unlink()

    def grayscale_preview(self, frame, grid_size):
        f =np.asarray([frame])
        gpu_image = cuda.to_device(f)
        gpu_edges = cuda.device_array_like(f)
        print(gpu_edges.shape)
        bgr_to_grayscale_kernel[grid_size, block_size](gpu_image, gpu_edges)
        return gpu_edges.copy_to_host()
    def edge_detection_preview(self, frame,grid_size):
        f =np.asarray([frame])
        gpu_image = cuda.to_device(f)
        gpu_edges = cuda.device_array_like(f)
        print(gpu_edges.shape)
        edge_detection_kernel_images[grid_size, block_size](gpu_image, gpu_edges,100,200)
        return gpu_edges.copy_to_host()

    def edge_detection(self, frames):
        p = create_loading_window(frames.shape[0])
        manager = MemoryManager(name='mymemory', to_create=True)
        
        grid_size = ((frames.shape[0] - 1) // block_size[0] + 1, (frames.shape[1] - 1) // block_size[1] + 1, (frames.shape[2] - 1) // block_size[2] + 1)
        frames_processed_cnt =0
        im_size = frames[0].nbytes  /  1000000
        single_transfer_size = 2.2* im_size

        while(frames_processed_cnt < frames.shape[0]):
            gpus = GPUtil.getGPUs()
            free_memory = gpus[0].memoryFree
            frames_next_transfer_count = int(free_memory // (single_transfer_size))
            if(frames_next_transfer_count > frames.shape[0]):
                frames_next_transfer_count = frames.shape[0]
            gpu_images = cuda.to_device(frames[frames_processed_cnt:frames_next_transfer_count])
            gpu_edges = cuda.device_array_like(frames[frames_processed_cnt:frames_next_transfer_count])
            edge_detection_kernel_images[grid_size, block_size](gpu_images, gpu_edges,100,200)
            frames[frames_processed_cnt:frames_next_transfer_count] =  gpu_edges.copy_to_host()
            frames_processed_cnt = frames_processed_cnt + frames_next_transfer_count
        
        manager.block.close()
        manager.block.unlink()

    def gaussian_blur(self, frames):
        grid_size = ((frames.shape[0] - 1) // block_size[0] + 1, (frames.shape[1] - 1) // block_size[1] + 1, (frames.shape[2] - 1) // block_size[2] + 1)
        frames_processed_cnt =0
        im_size = frames[0].nbytes  /  1000000
        single_transfer_size = 2.2* im_size

        p = create_loading_window(frames.shape[0])
        manager = MemoryManager(name='mymemory', to_create=True)

        while(frames_processed_cnt < frames.shape[0]):
            gpus = GPUtil.getGPUs()
            free_memory = gpus[0].memoryFree
            frames_next_transfer_count = int(free_memory // (single_transfer_size))
            if(frames_next_transfer_count > frames.shape[0]):
                frames_next_transfer_count = frames.shape[0]
            gpu_images = cuda.to_device(frames[frames_processed_cnt:frames_next_transfer_count])
            gpu_edges = cuda.device_array_like(frames[frames_processed_cnt:frames_next_transfer_count])
            blur_kernel_images[grid_size, block_size](gpu_images, gpu_edges,5)
            frames[frames_processed_cnt:frames_next_transfer_count] =  gpu_edges.copy_to_host()
            frames_processed_cnt = frames_processed_cnt + frames_next_transfer_count
            manager.put(frames_processed_cnt)

        manager.block.close()
        manager.block.unlink()

    def gaussian_blur_preview(self, frame,grid_size):
        f =np.asarray([frame])
        gpu_image = cuda.to_device(f)
        gpu_edges = cuda.device_array_like(f)
        print(gpu_edges.shape)
        blur_kernel_images[grid_size, block_size](gpu_image, gpu_edges,5)
        return gpu_edges.copy_to_host()
    
    def sepia_preview(self, frame,grid_size):
        f =np.asarray([frame])
        gpu_image = cuda.to_device(f)
        gpu_edges = cuda.device_array_like(f)
        print(gpu_edges.shape)
        sepia_kernel[grid_size, block_size](gpu_image, gpu_edges)
        return gpu_edges.copy_to_host()

    def sepia(self, frames):
        grid_size = ((frames.shape[0] - 1) // block_size[0] + 1, (frames.shape[1] - 1) // block_size[1] + 1, (frames.shape[2] - 1) // block_size[2] + 1)
        frames_processed_cnt =0
        im_size = frames[0].nbytes  /  1000000
        single_transfer_size = 2.2* im_size

        p = create_loading_window(frames.shape[0])
        manager = MemoryManager(name='mymemory', to_create=True)

        while(frames_processed_cnt < frames.shape[0]):
            gpus = GPUtil.getGPUs()
            free_memory = gpus[0].memoryFree
            frames_next_transfer_count = int(free_memory // (single_transfer_size))
            if(frames_next_transfer_count > frames.shape[0]):
                frames_next_transfer_count = frames.shape[0]
            gpu_images = cuda.to_device(frames[frames_processed_cnt:frames_next_transfer_count])
            gpu_edges = cuda.device_array_like(frames[frames_processed_cnt:frames_next_transfer_count])
            sepia_kernel[grid_size, block_size](gpu_images, gpu_edges)
            frames[frames_processed_cnt:frames_next_transfer_count] =  gpu_edges.copy_to_host()
            frames_processed_cnt = frames_processed_cnt + frames_next_transfer_count
            manager.put(frames_processed_cnt)

        manager.block.close()
        manager.block.unlink()

    def vignette_preview(self, frame,grid_size):
        f =np.asarray([frame])
        gpu_image = cuda.to_device(f)
        gpu_edges = cuda.device_array_like(f)
        print(gpu_edges.shape)
        vignette_kernel[grid_size, block_size](gpu_image, gpu_edges,0.5,0.5, 1.5)
        return gpu_edges.copy_to_host()

    def vignette(self, frames):
        grid_size = ((frames.shape[0] - 1) // block_size[0] + 1, (frames.shape[1] - 1) // block_size[1] + 1, (frames.shape[2] - 1) // block_size[2] + 1)
        frames_processed_cnt = 0
        im_size = frames[0].nbytes  /  1000000
        single_transfer_size = 2.2* im_size

        p = create_loading_window(frames.shape[0])
        manager = MemoryManager(name='mymemory', to_create=True)

        while(frames_processed_cnt < frames.shape[0]):
            gpus = GPUtil.getGPUs()
            free_memory = gpus[0].memoryFree
            frames_next_transfer_count = int(free_memory // (single_transfer_size))
            if(frames_next_transfer_count > frames.shape[0]):
                frames_next_transfer_count = frames.shape[0]
            gpu_images = cuda.to_device(frames[frames_processed_cnt:frames_next_transfer_count])
            gpu_edges = cuda.device_array_like(frames[frames_processed_cnt:frames_next_transfer_count])
            vignette_kernel[grid_size, block_size](gpu_images, gpu_edges,0.5,0.5,1.5)
            frames[frames_processed_cnt:frames_next_transfer_count] =  gpu_edges.copy_to_host()
            frames_processed_cnt = frames_processed_cnt + frames_next_transfer_count
            manager.put(frames_processed_cnt)

        manager.block.close()
        manager.block.unlink()

    def brightness(self, frames):
        grid_size = ((frames.shape[0] - 1) // block_size[0] + 1, (frames.shape[1] - 1) // block_size[1] + 1, (frames.shape[2] - 1) // block_size[2] + 1)
        frames_processed_cnt = 0
        im_size = frames[0].nbytes  /  1000000
        single_transfer_size = 2.2* im_size

        p = create_loading_window(frames.shape[0])
        manager = MemoryManager(name='mymemory', to_create=True)

        while(frames_processed_cnt < frames.shape[0]):
            gpus = GPUtil.getGPUs()
            free_memory = gpus[0].memoryFree
            frames_next_transfer_count = int(free_memory // (single_transfer_size))
            if(frames_next_transfer_count > frames.shape[0]):
                frames_next_transfer_count = frames.shape[0]
            gpu_images = cuda.to_device(frames[frames_processed_cnt:frames_next_transfer_count])
            gpu_edges = cuda.device_array_like(frames[frames_processed_cnt:frames_next_transfer_count])
            change_brightness_kernel[grid_size, block_size](gpu_images, gpu_edges,1.0,-30)
            frames[frames_processed_cnt:frames_next_transfer_count] =  gpu_edges.copy_to_host()
            frames_processed_cnt = frames_processed_cnt + frames_next_transfer_count
        
        manager.block.close()
        manager.block.unlink()

    def brightness_preview(self, frame,grid_size):
        f =np.asarray([frame])
        gpu_image = cuda.to_device(f)
        gpu_edges = cuda.device_array_like(f)
        print(gpu_edges.shape)
        change_brightness_kernel[grid_size, block_size](gpu_image, gpu_edges,1.0,-30)
        return gpu_edges.copy_to_host()