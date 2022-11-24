import random
from math import sqrt, cos, factorial, sin, pow, pi, exp

import numpy as np


def Lab1():
    # Formula 1
    print('Введите значение:')
    alpha = float(input())
    # alpha = 1

    formula1top = (round(sin(2 * alpha), 3)) + (round(sin(5 * alpha), 3)) - (round(sin(3 * alpha), 3))
    formula1bot = (round(cos(alpha), 3)) + 1 - 2 * (pow(round(sin(2 * alpha), 3), 2))
    result1 = round(formula1top / formula1bot, 3)
    print("Formula 1:")
    print(result1)

    # Formula 2
    result2 = 2 * (round(sin(alpha), 3))
    print("Formula 2:")
    print(result2)


# Lab 2.1
def Lab21(x, radius=2):
    global y
    first = -9 / 2 * radius
    second = -5 / 2 * radius
    third = -4 / 2 * radius
    fourth = 0 / 2 * radius
    fifth = 3.14 / 2 * radius
    if (x > 5 / 2 * radius) or (x < -9 / 2 * radius):
        print("Ошибка! Выход за рамки диапазона")  # error

        # окружность / circle
    if (x >= first) and (x <= second):
        y = -sqrt(-45 - x ** radius - 14 * x) + radius
    elif (x >= second) and (x <= third):  # прямая (константа) / constant graph y = 2
        y = 2
    elif (x >= third) and (x <= fourth):  # прямая / straight
        y = 0.5 * x
    elif (x >= fourth) and (x <= fifth):  # синус / sinus function
        y = sin(x)
    else:  # прямая / straight line y = kx + b 45deg
        y = 2 * x / (5 - pi) + 2 - 10 / (5 - pi)

    return y


# Lab 2.2
def Lab22():
    print('Введите значение Radius:')
    radius_s = int(input())
    print('Введите значение X:')
    x_s = float(input())
    print('Введите значение Y:')
    y_s = float(input())

    if (y_s > 2 * radius_s) or (x_s < -2 * radius_s):
        print("НЕТ попадания")
    else:
        if y_s > 0:  # для верхней окружности / upper circle
            if x_s < 0:  # проверка: в левой четверти / check: left quarter
                if (x_s + radius_s) ** 2 + (y_s - radius_s) ** 2 <= radius_s ** 2:  # в окружности / inside circle
                    if (abs(x_s) <= abs(radius_s)) and (y_s <= radius_s):  # исключенная область / excluded area
                        print("НЕТ попадания")
                    else:
                        print("ЕСТЬ попадание")
                elif abs(x_s) < radius_s and y_s < radius_s:  # малая область под окружностью / tiny bit under circle
                    print("ЕСТЬ попадание")
                else:
                    print("НЕТ попадания")
            else:  # если в правой четверти / if in right quarter
                print("НЕТ попадания")
        elif x_s > 0:  # для нижней окружности / for lower circle
            if (x_s - radius_s) ** 2 + (y_s + radius_s) ** 2 <= radius_s ** 2:
                print("НЕТ попадания")
            else:
                print("ЕСТЬ попадание")
        else:
            print("НЕТ попадания")


# Lab 3.1
def Lab31():
    radius = 2
    print("Enter dx:")
    dx = float(input())
    iFloat = -9.0

    listX = []
    while iFloat < 5 + dx:
        listX.append(iFloat)
        iFloat = iFloat + dx

    listY = [Lab21(i, radius) for i in listX]

    print(f'Значения X и Y c шагом dx = {dx}')
    for x, y in zip(listX, listY):
        print(f'|\t{round(x, 2)} \t|\t {round(abs(y), 2)}\t|')


# Lab 3.2
def Lab32():
    for i in range(10):
        Lab22()


# Lab 3.3
def Lab33():
    print("Enter xStart:")
    xStart = float(input())
    print("Enter xEnd:")
    xEnd = float(input())
    print("Enter dx:")
    dx = float(input())
    print(f'\t\t|\t\t X \t\t|\t\t L \t\t|\t\t TAILOR \t\t|\t\t N \t\t|\t\t')

    iFloat = float(xStart)
    while iFloat < float(xEnd):
        x = round(iFloat, 2)

        tailor = 0.0
        n = 0
        while abs((round(tailor, 8)) - round(exp(x), 8)) >= 0.01:
            tailor = tailor + round((x ** n / factorial(n)), 8)
            n = n + 1
        print(f'\t\t|\t\t{x}\t\t|\t\t{round(exp(x), 2)}\t\t|\t\t{round(tailor, 2)}\t\t|\t\t{n}\t\t|\t\t')
        iFloat = round((iFloat + dx), 2)


# Lab 4

# Shell sort
def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
    array.reverse()


def Lab4():
    print("Введите n (размер массива):")
    n = int(input())
    listLab = []

    # Filling listLab
    for i in range(n):
        print(f"Введите |{i}| элемент списка")
        listLab.append(int(input()))

    # Multiply all even indexes elements
    multresult = 1
    for i in range(len(listLab)):
        if i % 2 == 0:
            multresult *= listLab[i]
    print(f"Произведение всех элементов массива с четными индексами: {multresult}")

    # Sum of elements between first and last 0 element
    firstnull = -1
    lastnull = -1
    sumresult = 0
    for i in range(len(listLab)):
        if listLab[i] == 0 and firstnull == -1:
            firstnull = i
        elif listLab[i] == 0 and firstnull != -1:
            lastnull = i

    for i in range(firstnull, lastnull):
        sumresult += listLab[i]
    print(f"Сумма всех элементов между первым и последним нулевым элементом: {sumresult}")

    # Shell sort
    shellSort(listLab, n)

    print("Отсортированный массив (сортировка Шелла): ")
    for i in range(len(listLab)):
        print(listLab[i])


# Lab 5
def Lab5_countColumnsWithZero(array):
    result_zeroes = 0
    for x in array.T:
        for y in x:
            if y == 0:
                result_zeroes += 1
                break
    return result_zeroes


def Lab5_findLongestRepeatingNumbersRow(array):
    maxCount = 0
    longest_found_row = int(-1)

    for row_index, row in enumerate(array):
        actualCount = 1
        for column_index, column in enumerate(row):
            if column_index == len(row) - 1:
                break
            if column == row[column_index + 1]:
                actualCount += 1
            else:
                actualCount = 1
            if actualCount > maxCount:
                maxCount = actualCount
                longest_found_row = row_index

    return longest_found_row


def Lab5():
    rows = int(input("Введите количество строк:"))
    columns = int(input("Введите количество столбцов:"))
    array = np.random.randint(5, size=(rows, columns))

    # Randomized matrix
    print(array)

    # 5.1
    print(f"Столбцы содержащие ноль: |{Lab5_countColumnsWithZero(array)}|")
    # 5.2
    rowCheckingResult = Lab5_findLongestRepeatingNumbersRow(array)
    if rowCheckingResult == -1:
        print("Повторений нет!")
    else:
        print(f"Наибольшее повторение в строке: |{rowCheckingResult + 1}|")


# Lab 6
class SingleBedRoom:
    guest_surname: str
    guest_initials: str

    def __init__(self, name: str = None, initials: str = None):
        self.guest_surname: str = name or "Guest absent"
        self.guest_initials: str = initials or "No initials"

    def change_guest_name(self, new_surname: str, new_initials: str):
        self.guest_surname = new_surname
        self.guest_initials = new_initials

    def change_guest_name_input(self):
        self.guest_surname = input("Enter new guest surname: \n")
        self.guest_initials = input("Enter new guest initials: \n")

    def print_guest_name(self):
        print(f"Guest's name:\t | {self.guest_surname} {self.guest_initials} |")

    def is_guest_in_room_with_surname(self, search_surname):
        if search_surname.lower() == self.guest_surname.lower():
            return True
        return False

    def is_guest_in_room_with_initials(self, search_initials):
        if search_initials.lower() == self.guest_initials.lower():
            return True
        return False


class DoubleBedRoom:
    first_guest_surname: str
    first_guest_initials: str
    second_guest_surname: str
    second_guest_initials: str

    def __init__(
            self,
            surname_first: str = None,
            initials_first: str = None,
            surname_second: str = None,
            initials_second: str = None,
    ):
        self.first_guest_surname = surname_first or "Guest absent"
        self.first_guest_initials = initials_first or "Initials absent"
        self.second_guest_surname = surname_second or "Guest absent"
        self.second_guest_initials = initials_second or "Initials absent"

    def change_guest_names_both(
            self,
            name_first: str = None,
            initials_first: str = None,
            name_second: str = None,
            initials_second: str = None,
    ):
        self.first_guest_surname = name_first or "unknown"
        self.first_guest_initials = initials_first or "Initials absent"
        self.second_guest_surname = name_second or "unknown"
        self.second_guest_initials = initials_second or "Initials absent"

    def change_guest_name_input(self):
        print("Which guest's name do you want to change? (1 or 2)")
        guest_choice: int
        try:
            guest_choice = int(input())
        except:
            print("Not a number.")
            return

        if guest_choice == 1:
            self.first_guest_surname = input("Enter new guest name: \n")
            self.first_guest_initials = input("Enter new guest initials: \n")
        elif guest_choice == 2:
            self.second_guest_surname = input("Enter new guest name: \n")
            self.second_guest_initials = input("Enter new guest initials: \n")
        else:
            print("You can only input 1 or 2.")
            self.change_guest_name_input()

    def print_guest_names(self):
        print(f"First guest's name:\t | {self.first_guest_surname} {self.first_guest_initials} |")
        print(f"Second guest's name:\t | {self.second_guest_surname} {self.second_guest_initials} |")

    def is_guest_in_room_with_surname(self, search_surname):
        if search_surname.lower() == self.first_guest_surname.lower():
            return True
        elif search_surname.lower() == self.second_guest_surname.lower():
            return True
        return False

    def is_guest_in_room_with_initials(self, search_initials):
        if search_initials.lower() == self.first_guest_initials.lower():
            return True
        elif search_initials.lower() == self.second_guest_initials.lower():
            return True
        return False

    # Print all guests in all rooms


def print_all_guests(single_bedrooms_list, double_bedrooms_list):
    for room_index, room in enumerate(single_bedrooms_list):
        room_number = room_index
        print(f"Guest in single room number |{room_number}| :")
        room.print_guest_name()

    for room_index, room in enumerate(double_bedrooms_list):
        room_number = room_index + len(single_bedrooms_list)
        print(f"Guests in double room number |{room_number}| :")
        room.print_guest_names()


def Lab6():
    # Creating lists of single- and double- rooms
    single_bedrooms_list = [SingleBedRoom() for i in range(5)]
    double_bedrooms_list = [DoubleBedRoom() for i in range(10)]

    # Initialize lists with random names
    random_names_list = [
        "Petrov",
        "Sidorov",
        "Ivanov",
        "Kasparov",
        "Vavilov",
        "Davidov",
        "Maksimov",
        "Svistunov",
        "Korneplod",
        "Kurilov",
        "Dmitrov",
        "Danilov",
        "Brusilov",
        "Abdulla",
        "Naumov",
        "Rudov",
        "Bozhenkov",
        "Gigachadov",

    ]

    random_initials_list = [
        "A.D.",
        "C.D.",
        "M.M.",
        "D.N.",
        "F.D.",
        "S.D.",
        "N.N.",
        "V.A.",
        "D.P.",
        "K.K.",
        "A.V.",
        "I.I.",
        "K.K.",
        "D.A.",
        "S.A.",
        "R.P."
    ]

    for room in single_bedrooms_list:
        room.change_guest_name(
            new_surname=random.choice(random_names_list),
            new_initials=random.choice(random_initials_list)
        )

    for room in double_bedrooms_list:
        room.change_guest_names_both(
            name_first=random.choice(random_names_list),
            initials_first=random.choice(random_initials_list),
            name_second=random.choice(random_names_list),
            initials_second=random.choice(random_initials_list),
        )

    # Print randomized lists of rooms
    print_all_guests(single_bedrooms_list, double_bedrooms_list)

    # Search for a guest

    # Main program cycle with user choice
    while True:
        input_user_options = input("Search guest (1), Change guest info (2), Print all guests (3)?:")

        match input_user_options:
            # Search guest by surname (and initials)
            case "1":
                input_guest_surname = input("Please, input guest's surname:")

                # Search guest by surname, check amount of guests with same surname
                guests_with_searched_surname = 0
                saved_guest_room_number = 0
                guest_is_in_single_room = False

                for room_index, room in enumerate(single_bedrooms_list):
                    if room.is_guest_in_room_with_surname(input_guest_surname):
                        guests_with_searched_surname += 1
                        saved_guest_room_number = room_index
                        guest_is_in_single_room = True

                for room_index, room in enumerate(double_bedrooms_list):
                    if room.is_guest_in_room_with_surname(input_guest_surname):
                        guests_with_searched_surname += 1
                        saved_guest_room_number = room_index
                        guest_is_in_single_room = False

                if guests_with_searched_surname == 0:
                    print("Guest is not found.")
                elif guests_with_searched_surname == 1:
                    if guest_is_in_single_room == True:
                        print(f"Guest is found: room number |{saved_guest_room_number}|")
                    else:
                        print(f"Guest is found: room number |{saved_guest_room_number + len(single_bedrooms_list)}|")
                else:
                    # If there are multiple guests with searched surname, also input initials
                    print("There are more than one guests with such surname, please specify initials:")
                    input_guest_initials = input()

                    guest_with_initials_was_found = False
                    for room_index, room in enumerate(single_bedrooms_list):
                        if room.is_guest_in_room_with_surname(
                                input_guest_surname) and room.is_guest_in_room_with_initials(input_guest_initials):
                            print(f"Guest is found: room number |{room_index}|")
                            guest_with_initials_was_found = True

                    for room_index, room in enumerate(double_bedrooms_list):
                        if room.is_guest_in_room_with_surname(
                                input_guest_surname) and room.is_guest_in_room_with_initials(input_guest_initials):
                            print(f"Guest is found: room number |{room_index + len(single_bedrooms_list)}|")
                            guest_with_initials_was_found = True

                    if guest_with_initials_was_found == False:
                        print("Guest with such surname and initials wasn't found.")

            # Change guest's info
            case "2":
                input_room_number: int
                try:
                    input_room_number = int(input("Please, input room number:"))
                except:
                    print("Incorrect input: Not a number (must be integer).")
                    return
                if input_room_number < (len(single_bedrooms_list) - 1) and input_room_number >= 0:
                    single_bedrooms_list[input_room_number].change_guest_name_input()
                elif input_room_number > len(single_bedrooms_list) + len(double_bedrooms_list) - 1:
                    print("There is no room with such number.")
                elif input_room_number < 0:
                    print("Room number must be bigger than 0.")
                else:
                    double_bedrooms_list[input_room_number - len(single_bedrooms_list)].change_guest_name_input()

            # Print all guests in the hotel
            case "3":
                print_all_guests(single_bedrooms_list, double_bedrooms_list)
            case default:
                print("Unknown choice - choose between 1, 2, 3.")


# Labs execution
choice = int(input("Task number (1, 21, 22, 31, 32, 33, 4, 5, 6)?:"))

match choice:
    case 1:
        Lab1()
    case 21:
        Lab21(0)
    case 22:
        Lab22()
    case 31:
        Lab31()
    case 32:
        Lab32()
    case 33:
        Lab33()
    case 4:
        Lab4()
    case 5:
        Lab5()
    case 6:
        Lab6()
    case default:
        print("Unknown")
