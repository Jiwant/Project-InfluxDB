import time
from influxdb import InfluxDBClient
db = InfluxDBClient('localhost', 8086, 'root', 'root', 'ProcessorInfo')
for i in range(1, 10):
    rs = db.query(f'select cpu_percent_utilization from "records-new-10" where index=~/{i}/')
    #rs = db.query(f'select cpu_percent_utilization from "records-new-10" where index=~/8/')
    print(f"{i}:{list(rs.get_points())[0]['cpu_percent_utilization']}")
    time.sleep(1)