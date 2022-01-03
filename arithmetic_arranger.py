def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        return "ERROR: Too many problems."

    arranged_problems = ""

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for problem in problems:
        space1 = ""
        space2 = ""
        space4 = ""
        parts = problem.split()

        if parts[1] != '+' and parts[1] != '-':
            return "Error: Operator must be '+' or '-'."

        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."

        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if len(parts[0]) >= len(parts[2]):
            size = len(parts[0]) + 2
            space1 = "  "
            for k in range(size - len(parts[2]) - 2):
                space2 = space2 + " "
        else:
            size = len(parts[2]) + 2
            for k in range(size - len(parts[0])):
                space1 = space1 + " "

        dash = ""
        for k in range(size):
            dash = dash + "-"
        
        line1 = line1 + space1 + parts[0] + "    "
        line2 = line2 + parts[1] + " " + space2 + parts[2] + "    "
        line3 = line3 + dash + "    "

        if answer:
            if parts[1] == '+':
                result = str(int(parts[0]) + int(parts[2]))
                for k in range(size - len(result)):
                    space4 = space4 + " "
            else:
                result = str(int(parts[0]) - int(parts[2]))
                for k in range(size - len(result)):
                    space4 = space4 + " "
        
        line4 = line4 + space4 + result + "    "

            

    arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4

    return arranged_problems