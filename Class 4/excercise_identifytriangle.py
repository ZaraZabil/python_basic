print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x+y>z and y+z>x and x+z>y:
    if x==y and y==z and z==x:
        print("triangle is equilateral triangle")
    elif x==y or y==z or z==x:
        print("triangle is isocelse  triangle")
    else:
        print("triangle is scalene triangle")
else:
    print("This will not form a triangle!")