import os
import psutil
import time

for i in range(1, 100):
    #print(psutil.cpu_percent(), psutil.virtual_memory(), psutil.virtual_memory()[1], psutil.virtual_memory()[3], psutil.Process(os.getpid()))
    print(f'Cpu Percent Usage={psutil.cpu_percent()} ,Virtual Memory={psutil.virtual_memory()[1]}, Free Memory={psutil.virtual_memory()[3]}')
    time.sleep(2)