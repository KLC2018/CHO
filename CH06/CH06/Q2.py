def CheckString(str):
    if str.count('1')!=1: return False
    if str.count('2')!=1: return False
    if str.count('3')!=1: return False
    if str.count('4')!=1: return False
    if str.count('5')!=1: return False
    if str.count('6')!=1: return False
    if str.count('7')!=1: return False
    if str.count('8')!=1: return False
    if str.count('9')!=1: return False
    if str.count('0')!=1: return False
    return True

num_string=input()
temp=num_string.split()
result=''
for i in temp:
    if CheckString(i)==True: result+='true '
    else: result+='false '
print(result)
