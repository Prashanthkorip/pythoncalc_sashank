import logging

# Configure logging
logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add(x, y):
    result = x + y
    logging.info(f"Add: {x} + {y} = {result}")
    return result

def subtract(x, y):
    result = x - y
    logging.info(f"Subtract: {x} - {y} = {result}")
    return result

def multiply(x, y):
    result = x * y
    logging.info(f"Multiply: {x} * {y} = {result}")
    return result

def divide(x, y):
    if y == 0:
        logging.error("Division by zero!")
        raise ValueError("Cannot divide by zero!")
    result = x / y
    logging.info(f"Divide: {x} / {y} = {result}")
    return result

# if __name__ == "__main__":
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")

#     choice = input("Enter choice (1/2/3/4): ")

#     if choice in ('1', '2', '3', '4'):
#         if choice == '1':
#             print("Result:", add(num1, num2))
#         elif choice == '2':
#             print("Result:", subtract(num1, num2))
#         elif choice == '3':
#             print("Result:", multiply(num1, num2))
#         elif choice == '4':
#             try:
#                 print("Result:", divide(num1, num2))
#             except ValueError as e:
#                 print(e)
#     else:
#         print("Invalid Input")
