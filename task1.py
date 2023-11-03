"""
Написать функцию triangle, принимающую 1 аргумент — сторону
равностороннего треугольника, и возвращающую 2 значения (с помощью кортежа):
периметр и площадь треугольника.
"""
def triangle(side):
    perimeter = 3 * side
    area = (side**2 * (3**0.5)) / 4
    return (perimeter, area)

side_length = float(input("Введите длину стороны равностороннего треугольника: "))
result = triangle(side_length)
print("Периметр треугольника:", result[0])
print("Площадь треугольника:", result[1])

