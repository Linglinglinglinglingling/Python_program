a=open('test_write.txt','w+')
#a=open('test_write.txt','r')
line1='P'+'\n'
line2='Y'+'\n'
line3='T'+'\n'
line_together=line1+line2+line3
a.readlines()
# a.write(line1)
# a.write(line2)
# a.write(line3)
a.write(line_together)