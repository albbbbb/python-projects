def main():
    camelCase = input("camelCase: ")
    snake = camel_to_snake(camelCase)
    print("snake_case:", snake)

def camel_to_snake(camelCase):
    snake = ""
    for c in camelCase:
        if c.isupper():
            snake += "_" + c.lower()
        else:
            snake += c
    return snake



main()
