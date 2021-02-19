def Addfactor(value):
  factor = [1]
  for i in range(2,value):
     if value%i==0:
         factor.append(i)
  return sum(factor)
  
def main():
    value1 = int(input("Enter no : "))
    ret=Addfactor(value1)
    print("Sum of factor is {} ".format(ret))
	
if __name__ == "__main__":
	main()