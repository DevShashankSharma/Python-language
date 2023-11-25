import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hr = int(time.strftime('%H'))

if(hr < 12):
    print("Good Morning")
elif(hr < 16):
    print("Good Afternoon")
elif(hr < 20):
    print("Good Evening")
else:
    print("Good Night")