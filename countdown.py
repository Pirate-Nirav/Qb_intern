import time 

def countdown(t):
    while t:
        mins, secs = divmod(t,60) # this will return two value one is quotient and remainder that mean first one is for minute and other one is for seconds
        timer = '{:02d}:{:02d}'.format(mins,secs) # function is used to format the time as a string in MM:SS format
        #{:02d} means that the number will be displayed as a two-digit number (with a leading zero if necessary).

        print(timer, end='\r')
        '''
        end='\r': By default, print() moves the cursor to a new line after printing. 
        The \r is a carriage return character, which moves the cursor back to the beginning of the line,
        so that the next timer value overwrites the previous one.
        '''
        time.sleep(1)  # with sleep() we can delay the iteration by one second
        t -= 1
    print("Fireeeeee")

t = input("Enter the time in seconds:")

countdown(int(t))#function call invokes the countdown function with the input time (converted to an integer) as the argument.