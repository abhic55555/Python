def printpattern(n):    
    for i in range(0,n):
        k=1
        for j in range(0,i+1):            
            print(k, end=" ")
            k=k+1
        print("\r")
        
   
def main():
    value1 = int(input("Enter no : "))
    printpattern(value1)
	
if __name__ == "__main__":
	main()