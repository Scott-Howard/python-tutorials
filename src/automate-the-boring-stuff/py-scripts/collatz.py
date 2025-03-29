# collatz sequence 
def collatz(number):
    if number%2 == 0:
        return(int(number/2))
    elif number % 2 ==1:
        return(3*number +1)
    
#use inptuts a number 
number = int(input("Enter an integer: "))
while number != 1:
    number = collatz(number)
    print(number)
  
    