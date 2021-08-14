#6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
#составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

a = float(input("Введите сторону треугольника 'a' = "))
b = float(input("Введите сторону треугольника 'b' = "))
c = float(input("Введите сторону треугольника 'c' = "))


if a + b > c and b + c > a and a + c > b:
    if a == b and b == c and a == c:
        print("Треугольник равносторонний")
    elif a == b or b == c or a == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник не существует")

