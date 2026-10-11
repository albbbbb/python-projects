def main():
     time_str = input("What time is it? ")
     time_num = convert(time_str)


     if 7.0 <= time_num <= 8.0 :
          print("Time for breakfast!🥞")

     elif 12.0 <= time_num <= 13.0 :
          print("Time for lunch!")

     elif 18.0 <= time_num <= 19.0 :
          print("Time for dinner!")



def convert(time_str):
      hours, minutes = time_str.split(":")
      return int(hours) + int(minutes) / 60




if __name__ == "__main__":
      main()

