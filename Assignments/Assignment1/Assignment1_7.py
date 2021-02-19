def DivisibleByFive(value1):
    return True if (value1 % 5) ==0 else False
	
def main():
    value1 = int(input("Enter number : "))
    print(DivisibleByFive(value1))
	
if __name__ == "__main__":
	main()