import time  # Import the time module


def countdown(n):
    while n:
        mins, secs = divmod(n, 60)
        # divmod function divides the number in two parts.
        timer = f'{mins:02d}:{secs:02d}'
        # f string is used to format the output and timer is the variable which holds the time in string format (mins:secs)
        print(timer, end='\r')
        # end='\r' is used to print the output in the same line.
        time.sleep(1)
        # time.sleep function is used to pause the program for 1 second.
        n = n-1
        # n is decremented by 1.
    print('\n')
    print('Time is up!')
    # printing the message when time is up.


n = int(input("Enter the time in seconds : "))
# Taking the time in seconds.
countdown(n)
# calling the function countdown and passing the input as n.
