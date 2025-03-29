# collatz sequence 
def collatz(number):
    if number%2 == 0:
        return(int(number/2))
    elif number % 2 ==1:
        return(3*number +1)
    
#user inptuts a number 
try:
    number = int(input("Enter an integer: "))
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError:
    print("please enter an integer")
    