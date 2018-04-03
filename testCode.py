length = 14
print(length)
maxNum = 22
time = 0
while length != maxNum and time <= 10:
    time += 1
    if length < maxNum:
        length += 5
    else:
        length -= 3
    print(length, time)
print(length)
print(time)
