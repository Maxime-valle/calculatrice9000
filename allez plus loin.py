
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


history = []

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Show History")
print("6.Clear History")

while True:
    
    choice = input("Enter choice(1/2/3/4/5/6): ")

   
    if choice in ('1', '2', '3', '4', '5', '6'):
        if choice == '5':
            print("History:")
            for item in history:
                print(item)
            continue
        elif choice == '6':
            history.clear()
            print("History cleared.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(num1, "+", num2, "=", result)
            history.append(f"{num1} + {num2} = {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(num1, "-", num2, "=", result)
            history.append(f"{num1} - {num2} = {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(num1, "*", num2, "=", result)
            history.append(f"{num1} * {num2} = {result}")

        elif choice == '4':
            result = divide(num1, num2)
            print(num1, "/", num2, "=", result)
            history.append(f"{num1} / {num2} = {result}")
        
     
        next_calculation = input("Faisons le prochain calcul? (oui/non): ")
        if next_calculation == "non":
          break
    else:
        print("Invalid Input")