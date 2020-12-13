def arithmetic_arranger(problems, answers=False):

    arithmetics = []
    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""
    # breaking down the problems list into sub lists
    for item in problems:
        arithmetics.append(item.split(" "))

    # return error if more than 5 problems present
    if len(arithmetics) > 5:
        return ("Error: Too many problems.")

    # looping the arithmetics list
    for items in arithmetics:
        # making sure numbers has only 4 digits
        for item in items:
            if len(item) > 4:
                return ("Error: Numbers cannot be more than four digits.")

        # convert string to numbers. if can't return an error
        try:
            items[0] = int(items[0])
            items[2] = int(items[2])
        except ValueError:
            return ("Error: Numbers must only contain digits.")

        maxLength = len(str(getMax(items)))
        minLength = len(str(getMin(items)))

        # adding row one
        for s in range(2):
            row1 += " "
        if(len(str(items[0])) < len(str(items[2]))):
            for s in range(maxLength - minLength):
                row1 += " "
        row1 += str(items[0])
        for s in range(4):
            row1 += " "
        # adding row two
        row2 += items[1] + " "
        if(len(str(items[2])) < len(str(items[0]))):
            for s in range(maxLength - minLength):
                row2 += " "
        row2 += str(items[2])
        for s in range(4):
            row2 += " "
        # adding row three
        for s in range(maxLength+2):
            row3 += "-"
        for s in range(4):
            row3 += " "
        # adding row four
        answer = 0
        if answers:
            if items[1] == "+":
                answer = items[0] + items[2]
            elif items[1] == "-":
                answer = items[0] - items[2]
            else:
                return ("Error: Operator must be '+' or '-'")

            for s in range((maxLength + 2) - len(str(answer))):
                row4 += " "
            row4 += str(answer)
            for s in range(4):
                row4 += " "

    return (row1 + "\n" + row2 + "\n" + row3 + "\n" + row4)


def getMax(list):
    return max([list[0], list[2]])


def getMin(list):
    return min([list[0], list[2]])


print(arithmetic_arranger(
    ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(
    ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
