#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = sys.argv[2]
    operand_1 = sys.argv[1]
    operand_2 = sys.argv[3]
    result = None
    if operator == '+':
        result = add(operand_1, operand_2)
    elif operator == '-':
        result = sub(operand_1, operand_2)
    elif operator == '*':
        result = mul(operand_1, operand_2)
    elif operator == '/':
        result = div(operand_1, operand_2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{:n} {} {:n} = {:n}".format(operand_1, operator, operand_2, result))
    sys.exit(0)
