def countdigit(n):
    cnt=0
    while(n>0):
        cnt=cnt+1
        n=n//10
    print("Number of digit:",cnt)
    
def main():
    value = int(input("Enter number : "))
    countdigit(value)
	
if __name__ == "__main__":
	main()