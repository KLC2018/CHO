
string=input()
result=''
index=0
count=0
while index<len(string):
    if count==0:
        result+=string[index]
        count+=1
    else:
        if string[index-1]==string[index]:
            count+=1
        else:
            result+=str(count)
            count=0
            continue
    index+=1
result+=str(count)
print(result)