from lib import add_numbers, add_three_numbers


def main():
   #Викликає функції з модуля lib та виводить результати.
    result1 = add_numbers(5, 7)
    result2 = add_three_numbers(5, 7, 3)

    print("Сума двох чисел:", result1)
    print("Сума трьох чисел:", result2)


if __name__ == "__main__":
    main()