#write a program to create area calculator


print(  """
   press 1 to find the area of square
   press 2 to find the area of rect
   press 3 to find the area of circle
   press 4 to find the area of triangle
   
   """)
    
choice = int(input("Enter Your choice for find area : "))

if choice == 1:
    side = float(input("Enter the length of a side of the square: "))
    area = side * side
    print("The area of the square is:", area)
    
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is:", area) 
    
elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = (22/7)* radius**2 
    print("The area of the circle is:", area)
    
elif choice == 4:
    base = float(input("Enter the length of the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)
    
else:
    print("Invalid choice, please choose a number between 1 and 4.")
