def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = {"top": [], "bottom": [], "line": [], "result": []}

    for problem in problems:
        operand1, operator, operand2 = problem.split()
        
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        arranged_problems["top"].append(operand1.rjust(width))
        arranged_problems["bottom"].append(operator + operand2.rjust(width - 1))
        arranged_problems["line"].append('-' * width)

        result = str(eval(problem))
        arranged_problems["result"].append(result.rjust(width))

    arranged_problems_str = (
        "    ".join(arranged_problems["top"]) + "\n" +
        "    ".join(arranged_problems["bottom"]) + "\n" +
        "    ".join(arranged_problems["line"])
    )

    if show_answers:
        arranged_problems_str += "\n" + "    ".join(arranged_problems["result"])

    return arranged_problems_str
