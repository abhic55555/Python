import Arithmetic
	
def main():
    value1 = int(input("Enter first no : "))
    value2 = int(input("Enter second no : "))
    Arithmetic.add(value1,value2)
    Arithmetic.sub(value1,value2)
    Arithmetic.mult(value1,value2)
    Arithmetic.div(value1,value2)
	
if __name__ == "__main__":
	main()