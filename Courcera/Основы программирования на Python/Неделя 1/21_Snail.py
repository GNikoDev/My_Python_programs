print("Высота вертикального шеста:")
h = int(input())
print("Метры вверх за день:")
a = int(input())
print("Метры вниз за день")
b = int(input())
print("Номер дня", int(1 + (h - b - 1) / (a - b)))
