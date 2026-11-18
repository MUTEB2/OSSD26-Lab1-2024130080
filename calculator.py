"""Simple Calculator"""
from utils import parse_number


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def main():
    a = parse_number(input("a = "))
    b = parse_number(input("b = "))
    print("a + b =", add(a, b))
    print("a - b =", sub(a, b))


if __name__ == "__main__":
    main()
