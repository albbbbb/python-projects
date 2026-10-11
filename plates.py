def main():
    plate = input("Enter plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

        if not 1 < len(s) < 7 :
                return False

        if not s[:2].isalpha():
              return False

        if not s.isalnum():
              return False

        else:
              return True






main()
