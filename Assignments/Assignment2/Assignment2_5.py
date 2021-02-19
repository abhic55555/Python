def primenumber(value):
    if value > 1:
        for i in range(2, value):
            if (value % i) == 0:
                print("It is not Prime Number")
                break
        else:
            print("It is Prime Number")
    
def main():
    value1 = int(input("Enter first no : "))
    primenumber(value1)
	
if __name__ == "__main__":
	main()