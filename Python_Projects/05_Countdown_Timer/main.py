import time

def countdown(t):
    while t:
        mins, secs = divmod(t ,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer)
        time.sleep(1)
        t -= 1
    
    print("00:00")
    print("\nTimer Completed!\n")

t = input("\nEnter time in seconds: ") 

try:
    countdown(int(t))
except ValueError:
    print("Invalid syntax! Please enter number.")
    