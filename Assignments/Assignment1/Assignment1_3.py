def Add(value1,value2):
    ret = value1+value2
    print("addition of {} and {} is {}".format(value1,value2,ret))
	
def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))
    Add(value1,value2)
	
if __name__ == "__main__":
	main()