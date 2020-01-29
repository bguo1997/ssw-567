def classify_triangle(x,y,z):
    a=min(x,y,z)
    c=max(x,y,z)
    b= x+y+z-a-c
    A = a ** 2
    B = b ** 2
    C = c ** 2
    if c < a + b and c > b - a:
        if a == b == c:
            return f"this is a equilateral triangle"
        elif a==b or b==c or a==c:
            return f"this is a isosceles triangle"
        elif A + B == C:
            return f"this is a right triangle"
        else:
            return f"this is a scalene triangle"
    else:
        return f"this is not a triangle"


if __name__ == "__main__":
   x=int(input('please input the first side:'))
   y=int(input('please input the second side:'))
   z=int(input('please input the last side:'))
   print(classify_triangle(x,y,z))
