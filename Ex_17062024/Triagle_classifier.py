lenght1 = int (input("Enter the side of the triangle\n"))
lenght2 = int (input("Enter the side of the triangle\n"))
lenght3 = int (input("Enter the side of the triangle\n"))

if (lenght1 == lenght2 == lenght3):
    print ("Equilateral")

elif ((lenght1 == lenght2) or (lenght2 == lenght3) or (lenght1 == lenght3)):
    print("Isocelas")

else:
    print("scalene")