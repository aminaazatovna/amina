a = int(input("введите число:"))
b = int(input("введите число:"))
c = input("(+,-,/,*):")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "/":
    print(a / b)
else:
    print(a * b)
