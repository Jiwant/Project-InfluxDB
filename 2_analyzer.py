import time
from influxdb import InfluxDBClient
import matplotlib.pyplot as plt
import numpy
db = InfluxDBClient('localhost', 8086, 'root', 'root', 'ProcessorInfo')

index_val_list = []
cpu_percent_utilization_val_list = []
number_processes_val_list = []
virtual_memory_val_list = []
free_memory_val_list = []

for i in range(1, 20):
    not_exist = True
    while(not_exist):
        try:
            rs = db.query(f'select * from "records-presentation-final-13" where index=~/{i}/')
            data_point = list(rs.get_points())[0]
            print(data_point)
            index_val = data_point['index']
            index_val_list.append(index_val)
            time_val = data_point['time']
            cpu_percent_utilization_val = data_point['cpu_percent_utilization']
            cpu_percent_utilization_val_list.append(cpu_percent_utilization_val)
            number_processes_val = data_point['number_processes']
            number_processes_val_list.append(number_processes_val)
            virtual_memory_val = data_point['virtual_memory']
            virtual_memory_val_list.append(virtual_memory_val)
            free_memory_val = data_point['free_memory']
            free_memory_val_list.append(free_memory_val)
            not_exist = False
        except:
            #print("Inside Except Loop")
            not_exist = True
            time.sleep(0.5)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(index_val_list, cpu_percent_utilization_val_list)
axs[0, 0].set_title('CPU Percent Utilization')
axs[0, 1].plot(index_val_list, number_processes_val_list)
axs[0, 1].set_title('Number of Processes')
axs[1, 0].plot(index_val_list, virtual_memory_val_list)
axs[1, 0].set_title('Virtual Memory')
axs[1, 1].plot(index_val_list, free_memory_val_list)
axs[1, 1].set_title('Free Memory')
plt.show()