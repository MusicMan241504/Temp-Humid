import matplotlib.pyplot as plt
import matplotlib
import csv
from datetime import datetime
with open('temps.csv') as file:
    r = csv.reader(file,delimiter=',')
    temp = []
    humid = []
    time = []
    line = 0
    for row in r:
        if line == 0:
            line = line + 1
        else:
            time.append(datetime.strptime(row[0],'%H:%M'))
            temp.append(float(row[1]))
            humid.append(float(row[2]))
time = matplotlib.dates.date2num(time)
fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.plot_date(time,temp,label='Temperature',color=color,xdate=True,ydate=False,linestyle='-',marker=',')
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature (°C)',color=color)
ax1.set_title('My Graph')
ax2 = ax1.twinx()
color = 'tab:red'
ax2.plot_date(time,humid,label='Humidity',color=color,xdate=True,ydate=False,linestyle='-',marker=',')
ax2.set_ylabel('Humidity (%)',color=color)
fig.legend()
fig.autofmt_xdate()
plt.show()
