def printstar(value):
    for i in range(value):
        print("*", end=" ")
    
def main():
    value = int(input("Enter number : "))
    printstar(value)
	
if __name__ == "__main__":
	main()