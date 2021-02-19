def countdigit(n):
    sum=0
    while(n>0):
        sum=sum+(n % 10) 
        n=n//10
        
    print("sum of digit:",sum)
    
def main():
    value = int(input("Enter number : "))
    countdigit(value)
	
if __name__ == "__main__":
	main()