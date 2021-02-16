hour, minute = map(int,input().split())


if (minute-45<0):
    minute = minute-45+60
    if (hour == 0):
        hour = 23
    else:
        hour -= 1
else:
    minute = minute-45

print(hour,minute)