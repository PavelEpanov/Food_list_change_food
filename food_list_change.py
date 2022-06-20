def main():
    food = []  # Создаём пустой список, предназначенный для записи названий еды

    while True:  # Добавляем значения в список
        food.append(input("Введите название еды: "))
        again = int(input("Если хотите внести еще название - напишите '1': "))
        if again != 1:
            break

    print("Вот список с едой: ")  # Показываем значения списка
    for value in food:
        print(value)

    num = int(input("Если хотите изменить название еды, то введите '3': "))
    try:  # Проверка на ошибку
        if num == 3:
            item_change = input(
                "Введите название еды, которую хотите поменять: ")  # Находим значение еды, которую хотим поменять
            item = input("Введите название новой еды: ")

            # Находим индекс первого значения в списке
            index_change = food.index(item_change)

            # Меняем значение по первому индексу на новое значение
            food[index_change] = item

            print("Новый список еды: ")  # Выводим новый список
            for line in food:
                print(line)
    except ValueError:  # Информация об ошибке
        print("Эта еда не была найдена")

    delete = int(input("Если вы хотите удалить еду из списка введите - '5': "))

    try:
        if delete == 5:
            change_item_delete = input(
                "Введите название еды, которую хотите удалить: ")  # Получаем значение еды, которую хотим удалить
            food.remove(change_item_delete)  # Удаляем эту еду

            print("Новый список: ")
            for i in food:  # Выводим новый список
                print(i)

    except ValueError:
        print("Эта еда не найдена в списке")


main()
