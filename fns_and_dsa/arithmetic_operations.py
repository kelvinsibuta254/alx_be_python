def perform_operation(num1 = float, num2 = float, operation = str):
    match operation:
        case "add":
            result = num1 + num2
            print(f"The result is {result}")
        case "subtract":
            result = num1 - num2
            print(f"The result is {result}")
        case "multiply":
            result = num1 * num2
            print("The result is {result}")
        case "divide":
            result = num1 / num2
            if result != 0:
                print(f"The result is {result}")
            else:
                print("Cannot complete the operation")
    return result
