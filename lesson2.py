# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

ob = [1, 2.6, "Hello", True]
for ob_type in ob:
    print(type(ob_type))

# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

list = input("введите элементы:").split()
i = 0
while i < len(list):
    if i+1 == len(list):
        break
    a = list[i]
    list[i] = list[i+1]
    list[i+1] = a
    i += 2
print(list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

m = int(input("введите месяц в виде целого числа: "))
d = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
     10: "Осень", 11: "Осень", 12: "Зима"}
print(d[m])

l = ["Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима", "Зима"]
print(l[m - 1])

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

list = input("введите строку из нескольких слов: ").split()
i = 0
while i < len(list):
    print(str(i + 1) + ". " + list[i][:10])
    i += 1

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
i = int(input("введите рейтинг: "))
my_list.append(i)
my_list.sort(reverse=True)
print(my_list)

# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.

products = []
i = 1
while True:
    if input("Желаете добавить товар? (y/n)") == "n":
        break
    name = input("Введите название: ")
    price = int(input("Введите цену: "))
    count = int(input("Введите количество: "))
    ed = input("Введите единицу измерения: ")
    pr = {"название": name, "цена": price, "количество": count, "eд": ed}
    products.append((i, pr))
    i += 1

if len(products) == 0:
    print("Нет данных для анализа.")
    exit()

analytics = {}
for key in products[0][1]:
    analytics[key] = []

for product_cort in products:
    for key in product_cort[1]:
        value = analytics[key]
        value.append(product_cort[1][key])
        analytics[key] = value
print(analytics)