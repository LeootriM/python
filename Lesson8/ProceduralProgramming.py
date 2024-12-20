def calculate_area(length, width):
    return length * width

def calculate_perimeter(length,width):
    return 2 *(length + width)

length = 5
width = 9

area = calculate_area(length,width)
perimeter = calculate_perimeter(length,width)

print(f"Area is: {area}")
print(f"Perimeter  is: {perimeter}")