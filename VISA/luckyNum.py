import sys

data=[10,1,2,3,4,5,6,7,8,9,10]
for line in sys.stdin:
    data.append(line)
def recurdiv(number):
    if (number%5==0):

        return (1+recurdiv(number/5.0))
    elif (number%3==0):
        return (1+recurdiv(number/3.0))
    else:
        return 0

for a in data:
    if a.equals(data[0]):
        pass
    else:
        print recurdiv(a)