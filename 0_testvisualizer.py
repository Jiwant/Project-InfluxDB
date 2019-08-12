import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('example.csv', 'r').read()
    lines = graph_data.split('\n')
    index_val_list = []
    cpu_utilization_percent_list = []
    for line in lines:
        if len(line) > 1:
            record = line.split(',')
            index_val = record[0]
            cpu_utilization_percent = record[2]
            number_of_processes = record[3]
            virtual_memory = record[4]
            free_memory = record[5]
            index_val_list.append(int(index_val))
            cpu_utilization_percent_list.append(float(cpu_utilization_percent))
        ax1.clear()
        ax1.plot(index_val_list, cpu_utilization_percent_list)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()