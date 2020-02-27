def classify_triangle(x, y, z):
    a = min(x, y, z)
    c = max(x, y, z)
    b = x + y + z - a - c
    square_a = a ** 2
    square_b = b ** 2
    square_c = c ** 2
    if c < a + b and c > b - a:
        if a == b == c:
            return f"this is a equilateral triangle"
        elif a == b or b == c or a == c:
            return f"this is a isosceles triangle"
        elif square_a + square_b == square_c:
            return f"this is a right triangle"
        else:
            return f"this is a scalene triangle"
    else:
        return f"this is not a triangle"
