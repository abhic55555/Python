def printpattern(n):    
    for i in range(n,0,-1):
        for j in range(0,i):            
            print("*", end=" ")
        print("\r")
        
   
def main():
    value1 = int(input("Enter no : "))
    printpattern(value1)
	
if __name__ == "__main__":
	main()