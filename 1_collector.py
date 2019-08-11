import psutil
import timeit
import time
from influxdb import InfluxDBClient
db = InfluxDBClient('localhost', 8086, 'root', 'root', 'ProcessorInfo')
db.create_database("ProcessorInfo")
start = timeit.default_timer()
for i in range(1,10000):
    print(i)
    json_body = [
        {
            "measurement": "records-newwwww-10000",
            "tags": {
                "index": i
            },
            "fields": {
                "cpu_percent_utilization": psutil.cpu_percent(),
                "number_processes": len(psutil.pids()),
                "virtual_memory": psutil.virtual_memory()[1],
                "free_memory": psutil.virtual_memory()[3]
            }
        }
    ]
    db.write_points(json_body)
    time.sleep(1)
stop = timeit.default_timer()
print(f'Time: {stop - start}')
