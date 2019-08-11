import time
from influxdb import InfluxDBClient
db = InfluxDBClient('localhost', 8086, 'root', 'root', 'ProcessorInfo')
for i in range(1, 100):
    rs = db.query(f'select * from "records-new" where "index"={i}')
    print(f"{i}:{list(rs.get_points(measurement='cpu_percent_utilization'))}")
    time.sleep(1)