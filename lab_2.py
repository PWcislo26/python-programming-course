# Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
# wyświetli każde z nich.

def a(names: list):
    for name in names:
        print(name)


# Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych
# liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci. Zadanie
# należy wykonać w 2 wersjach:

def b_1(numbers: list):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    return numbers


print(b_1([1, 2, 3, 4, 5]))


def b_2(numbers: list):
    numbers = [number * 2 for number in numbers]
    return numbers


print(b_2([1, 2, 3, 4, 5]))


# Utwórz pętlę iterującą po liście zawierającej 10 liczb (rekomendowane
# wykorzystanie funkcji range ), która wyświetla jedynie parzyste elementy.

def even_numbers():
    numbers = [i for i in range(10)]
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            print(numbers[i])


even_numbers()


# Utwórz pętlę iterującą po liście zawierającej 10 liczb (rekomendowane
# wykorzystanie funkcji range ), która wyświetla co drugi element.

def second_numbers():
    numbers = [i for i in range(10)]
    for i in range(0, len(numbers), 2):
        print(numbers[i])


second_numbers()
