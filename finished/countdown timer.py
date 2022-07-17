import time

time_input = input('Enter time: ')
hour = ''
minute = ''
sec = ''
t = True
f = True

if 'h' in time_input.lower():
    for i in time_input.lower():
        if i != 'h' and f:
            hour += i
        else:
            minute = 0
            sec = 0
            f = False
            if i != ' ' and i != 'h':
                if 'm' in time_input.lower():
                    if i != 'm' and t:
                        minute += i
                    else:
                        t = False
                        if i != ' ' and i != 'm':
                            if 's' in time_input.lower():
                                if i != 's':
                                    sec += i
                            else:
                                sec = 0
                                print('Example: 1h 45m 24s')
                elif 's' in time_input.lower():
                    minute = 0
                    if i != 's':
                        sec += i
                    else:
                        print('Example: 1h 24s')

elif 'm' in time_input.lower():
    hour = 0
    for i in time_input.lower():
        if i != 'm' and t:
            minute += i
        else:
            t = False
            if i != ' ' and i != 'm':
                if 's' in time_input.lower():
                    if i != 's':
                        sec += i
                else:
                    sec = 0
                    print('Example: 45m 24s')
            else:
                sec = 0
elif 's' in time_input.lower():
    hour = 0
    minute = 0
    for i in time_input.lower():
        if i != 's':
            sec += i
else:
    print('Example:1h 24m 24s')

try:
    hour = int(hour)
    minute = int(minute)
    sec = int(sec)
except:
    print(hour)
    print(minute)
    print(sec)

hours = 0
minutes = 0
secs = 0

while True:
    time.sleep(1)
    secs += 1
    if secs == 60:
        minutes += 1
        secs = 0
        if minutes == 60:
            hours += 1
            minutes = 0
    print(str(hours) + 'h', str(minutes) + 'm', str(secs) + 's')
    if secs == sec and minutes == minute and hours == hour:
        print('Done!')
        break
