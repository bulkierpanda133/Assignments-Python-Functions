import time


def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "error : division by zero is not allowed"
    return result


def main():
    while True:
     name = input("welcome to my calculatoe app\n what is your name: ")
     time.sleep(1)
     print(f"select operation {name}")
     time.sleep(1)
     print("1. addition")
     time.sleep(1)
     print("2. subtraction")
     time.sleep(1)
     print("3. multiplication")
     time.sleep(1)
     print("4. division")
     time.sleep(1)
     print("5. quit")
     time.sleep(1)
     

     operation = input("enter a choice (1/2/3/4/5): ")
     
     if operation == '5':
      time.sleep(1)
      print(f"exiting the calculator. goodbye {name} !")
      time.sleep(2)
      break


     if operation not in ['1','2','3','4',]:
        print(f"invalid input {name} ")
        continue
    
     try:
        time.sleep(1)
        num1 = float(input(f"enter first number {name}\n "))
        time.sleep(1)
        num2 = float(input(f"enter second number {name}\n "))
     except ValueError:
        print(f"invalid number input {name}")
        continue
     time.sleep(1)
     if operation == "1":
        print(f"the result is: {add(num1, num2)}")
        time.sleep(1)
     elif operation == "2":
        print(f"the result is: {subtract(num1, num2)}")
        time.sleep(1)
     elif operation == "3":
        print(f"the result is: {multiply(num1, num2)}")
        time.sleep(1)
     elif operation == "4":
        print(f"the result is: {divide(num1, num2)}")


if __name__=="__main__":
    main()
