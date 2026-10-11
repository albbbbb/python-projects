expression = input("Expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
else:
    print("Invalid operator")


expression_to_float = float(result)
print(expression_to_float)
