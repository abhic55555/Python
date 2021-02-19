def printpattern(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*", end=" ")
        print("\r")
            
def main():
    value1 = int(input("Enter no : "))
    printpattern(value1)
	
if __name__ == "__main__":
	main()