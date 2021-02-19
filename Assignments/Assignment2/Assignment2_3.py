def factorial(value1):    
    if value1 > 0:
        factorial = 1
        for i in range(1,value1 + 1):
            factorial = factorial*i
        print("The factorial of {} is {}".format(value1,factorial))
    elif value1==0:
        print("The factorial of 0 is 1 ")
    else:-
        print("Invalid number")    
	
def main():
    value1 = int(input("Enter first number : "))
    factorial(value1)
	
if __name__ == "__main__":
	main()