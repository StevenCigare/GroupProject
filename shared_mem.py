from multiprocessing import shared_memory

class MemoryManager():
    def __init__(self, name:str, to_create=False):
        if to_create == True:
            self.block = shared_memory.SharedMemory(name=name, create=True, size=10)
        else:
            self.block = shared_memory.SharedMemory(name=name)

        self.buffer = self.block.buf
        self.buffer[:10] = b'ssssssssss'
    
    def put(self, num) -> None:
        mystr = str(num).encode()
        self.buffer[:len(mystr)] = mystr
    
    def get(self) -> int:
        for idx in range(5):
            mybyte = self.buffer[idx:idx+1]
            if mybyte == b's':
                current_frame = idx
                break
        #f.write(self.buffer[:current_frame])
        current_frame = bytes(self.buffer[:current_frame])
        current_frame = int(current_frame.decode())


        return current_frame

    

