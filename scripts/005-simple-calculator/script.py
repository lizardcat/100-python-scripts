def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def main():
    print("Simple Calculator")
    print("-" * 20)
    
    while True:
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract") 
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("\nChoose an operation (1-5): ")
        
        if choice == '5':
            print("Thanks for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            if choice == '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):  # Error message
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        
        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()