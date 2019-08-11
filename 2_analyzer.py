import time
from influxdb import InfluxDBClient
db = InfluxDBClient('localhost', 8086, 'root', 'root', 'ProcessorInfo')
for i in range(1, 10000):
    not_exist = True
    while(not_exist):
        try:
            rs = db.query(f'select cpu_percent_utilization from "records-newwwww-10000" where index=~/{i}/')
            print(f"{i}: {list(rs.get_points())[0]['cpu_percent_utilization']}")
            not_exist = False
        except:
            #print("Inside Except Loop")
            not_exist = True
            time.sleep(0.5)
    #rs = db.query(f'select cpu_percent_utilization from "records-new-10" where index=~/8/')
    #time.sleep(1)