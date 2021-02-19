def printeven(value):
    for i in range(1,value*2+1):
        if i%2==0:
            print (i, end = " ")
    
def main():
    value = int(input("Enter number : "))
    printeven(value)
	
if __name__ == "__main__":
	main()