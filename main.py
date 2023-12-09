from arithmetic_arranger import arithmetic_arranger

operand_list = []
operand_limit = 5

while operand_limit > 0:
    while True:
        try:
            operand_1 = int(input("Choose the first operand: "))
            if operand_1 > 10000:
                print("Error: Numbers must be less than or equal to 10000.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.")

    while True:
        operator = input("Choose the operator (+ or -): ")
        if operator not in ['+', '-']:
            print("Error: Operator must be '+' or '-'.")
            continue
        break

    while True:
        try:
            operand_2 = int(input("Choose the second operand: "))
            if operand_2 > 10000:
                print("Error: Numbers must be less than or equal to 10000.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.")

    operand_list.append(f"{operand_1} {operator} {operand_2}")
    operand_limit -= 1

    another_entry = input("Do you want to enter more problems? (yes/no): ").lower()
    if another_entry != "yes":
        break
    
    if operand_limit == 0:
        print("Error: Too many problems.")
        break

print(arithmetic_arranger(operand_list, True))
