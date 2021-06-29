# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def print_menu():
    print (30 * "-", "MENU", 30 * "-")
    print ("1.- Realizar operaciones básicas")
    print ("2.- Realizar operaciones avanzadas")
    print ("3.- Salir")
    print (66 * "-")

loop=True

while loop:
    print_menu()
    
    principal = input("Elije tu opción [1 - 3]: ")

    if principal == 1:
        print ("Operaciones básicas, has elegido.")

        print("Select operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        while True:
            # Take input from the user
            choice = input("Enter choice( 1 / 2 / 3 / 4 ): ")

            # Check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))

                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))

                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))

                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
                break
            else:
                print("Invalid Input")
    elif principal == 2:
            print ("Operaciones avanzadas, has elegido.")

    elif principal == 3:
        print ("Saliendo")
        loop=False