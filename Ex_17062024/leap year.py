year = int(input("Enter the any Year\n"))

if (year % 4 == 0 and year != 100) or (year % 400 == 0):
    print ("leap year")

else:
   print ("Not a leap year")

