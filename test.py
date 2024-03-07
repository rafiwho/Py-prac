PI = 3.14

def circle_area(r):
    return PI * r* r

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return (base * height)/2

print("Choose a shape to calculate the area:")
print("1. Circle\n2. Rectangle\n3. Triangle")

yo = int(input("Enter your choice (1/2/3): "))

if yo == 1:
    r = float(input("Enter the radius of the circle: "))
    print(f"Area of the circle: {circle_area(r):.2f}")
elif yo == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print(f"Area of the rectangle: {rectangle_area(length, width)}")
elif yo == 3:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(f"Area of the triangle: {triangle_area(base, height)}")
else:
    print("Invalid choice. Please choose 1, 2, or 3.")
