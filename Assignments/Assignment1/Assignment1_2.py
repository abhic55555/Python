def ChkNum(value1):
 if (value1 % 2) == 0:
    print("Even number")
 else:
    print("ODD number")
	
def main():
    value1 = int(input("Enter number : "))
    ChkNum(value1)
	
if __name__ == "__main__":
	main()