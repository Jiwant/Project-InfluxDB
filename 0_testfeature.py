import psutil
import time
for i in range(1, 100):
    print(len(psutil.net_if_stats()))
    time.sleep(2)
