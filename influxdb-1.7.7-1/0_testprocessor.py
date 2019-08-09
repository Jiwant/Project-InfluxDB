import os
import psutil
import time

for i in range(1, 100):
    print(psutil.cpu_percent(), psutil.virtual_memory(), psutil.Process(os.getpid()))
    time.sleep(2)