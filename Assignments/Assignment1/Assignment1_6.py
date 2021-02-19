def checkNumber(value1):
    if value1 > 0:
        print ("Positive number")
    elif value1 < 0:
        print("Negative Number")
    else:
        print("Zero")
def main():
    value1 = int(input("Enter number : "))
    checkNumber(value1)
	
if __name__ == "__main__":
	main()