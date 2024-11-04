def my_function(x):
    if x==0:
        return -1
    position=0
    while x & 1==0:
        x>>=1
        position +=1
    return position

number=8
print(my_function(number))