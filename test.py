nums = [0,1,2,3,4,5,6,7,8,9,10]

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

for x in my_range(5):
    if x == 3:
        break
    print(x)
