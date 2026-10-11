while True:
    try:
        x,y = input("Fraction: ").split("/")
        num, den = int(x), int(y)
        frac = num / den
        percentage = round(frac * 100)

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break

    except (ValueError, ZeroDivisionError):
        continue



