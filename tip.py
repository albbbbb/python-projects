def main():
    dollars = dollars_to_float(input("How much did the meal cost?"))
    percentage = percent_to_float(input("What percentage would you like to tip?"))
    tip = dollars * percentage
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
        return float(d[1:])

def percent_to_float(p):
         return float(p[:-1]) / 100





main()
