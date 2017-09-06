#这个模块是记录程序的运行时间
import datetime

starttime = datetime.datetime.now()
#long running
for i in range(1000):
    for j in range(1000):
        x = i
endtime = datetime.datetime.now()
computer_time = (endtime - starttime).seconds

print(starttime)
print(endtime)
print(computer_time)
print(type(computer_time))


with open('time_recod.txt', 'w') as f:
    f.write(starttime.strftime('%a, %b %d %H:%M')+'\n')
    f.write(endtime.strftime('%a, %b %d %H:%M')+'\n')
    f.write(str(computer_time))
