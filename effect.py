import cv2
import numpy as np


class Effect():

    def gunnar_farneback_optical_flow(self, frames):

        changedFrames = []

        # Convert to gray scale
        prvs = cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY)
        # Create mask
        hsv_mask = np.zeros_like(frames[0])
        # Make image saturation to a maximum value
        hsv_mask[..., 1] = 255
        
        # Till you scan the video
        for frame in frames[1:30]:
            
            # Capture another frame and convert to gray scale
            next = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            # Optical flow is now calculated
            flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            # Compute magnite and angle of 2D vector
            mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
            # Set image hue value according to the angle of optical flow
            hsv_mask[..., 0] = ang * 180 / np.pi / 2
            # Set value as per the normalized magnitude of optical flow
            hsv_mask[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
            # Convert to rgb
            rgb_representation = cv2.cvtColor(hsv_mask, cv2.COLOR_HSV2BGR)
        
            #cv2.imshow('frame2', rgb_representation)
            kk = cv2.waitKey(20) & 0xff
            # Press 'e' to exit the video
            if kk == ord('e'):
                break
            # Press 's' to save the video
            elif kk == ord('s'):
                pass
                #cv2.imwrite('Optical_image.png', frame2)
                #cv2.imwrite('HSV_converted_image.png', rgb_representation)

            changedFrames.append(rgb_representation)

            prvs = next
        
        return changedFrames
        #capture.release()
        #cv2.destroyAllWindows()

    def gunnar_farneback_optical_flow_preview(self, frame, prev_frame):
        # Convert to gray scale
        prvs = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        # Create mask
        hsv_mask = np.zeros_like(prev_frame)
        # Make image saturation to a maximum value
        hsv_mask[..., 1] = 255
        
        # Capture another frame and convert to gray scale
        next = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # Optical flow is now calculated
        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        # Compute magnite and angle of 2D vector
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        # Set image hue value according to the angle of optical flow
        hsv_mask[..., 0] = ang * 180 / np.pi / 2
        # Set value as per the normalized magnitude of optical flow
        hsv_mask[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        # Convert to rgb
        rgb_representation = cv2.cvtColor(hsv_mask, cv2.COLOR_HSV2BGR)
        return rgb_representation

    def edge_detection_preview(self, frame):
       img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       img_blur = cv2.GaussianBlur(img_gray,(3,3), 0)

       sobel_x = cv2.Sobel(src = img_blur, ddepth=cv2.CV_64F,dx=1,dy=0,ksize=17)
       sobel_y = cv2.Sobel(src = img_blur, ddepth=cv2.CV_64F,dx=0,dy=1,ksize=17)
       sobel_xy = cv2.Sobel(src = img_blur, ddepth=cv2.CV_64F,dx=1,dy=1,ksize=17)
       edges = cv2.Canny(image=img_blur, threshold1=5,threshold2=200)
       edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
       return edges

    def edge_detection(self, frames):
        changed_frames = []
        for frame in frames:
            changed_frames.append(self.edge_detection_preview(frame))
    
    def gaussian_blur(self, frames):
        changedFrames = []
        for frame in frames:
            changedFrames.append(cv2.GaussianBlur(frame, (15,15), 0))

        return changedFrames

    def gaussian_blur_preview(self, frame):
        return cv2.GaussianBlur(frame, (15,15), 0)

