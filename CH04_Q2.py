f=open("C:/Python/sample.txt",'r')
lines=f.readlines()
sum=0
for line in lines:
	sum+=int(line)
average=sum/len(lines)
print(sum)
print(average)