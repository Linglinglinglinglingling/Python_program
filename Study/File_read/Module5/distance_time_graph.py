import matplotlib.pyplot as plt
read_velocity=open('velocity_data.txt','r')
time_list=[]
distance_list=[]
for line in read_velocity:
    line_list=line.split(',')
    time_list.append(line_list[0])
    distance_list.append(int(line_list[0])*int(line_list[1]))

read_velocity.close()
#matplot can operate on the integer-string e.g '1' or '1/n'
plt.plot(time_list,distance_list,'r')
plt.axis([0,10,0,500])
plt.show()
