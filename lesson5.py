# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка

# with open("resources/example.txt", "w") as file:
#     while True:
#         s = input("введите данные: ")
#         if (len(s) > 0):
#             file.write(s+"\n")
#         else:
#             break

# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
# with open("resources/example.txt", "w") as file:
#     while True:
#         s = input("введите данные: ")
#         if (len(s) > 0):
#             file.write(s+"\n")
#         else:
#             break
# with open("resources/example.txt", "r") as file:
#     ls = file.readlines()
# i = 0
# for s in ls:
#     i += 1
#     print("количество слов в строке " + str(i) + ": " + str(len(s.split())))
# print("количество строк: " + str(i))

# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

# from statistics import mean
# with open("resources/example.txt", "w") as file:
#     file.write("Иванов 230543.12\n")
#     file.write("Петров 14543.12\n")
#     file.write("Сидоров 87543.12\n")
#     file.write("Воронин 65543.12\n")
#     file.write("Дроздов 13543.12\n")
#     file.write("Сорокин 17543.12\n")
#     file.write("Жилин 9543.12\n")
#     file.write("Патрушев 38543.12\n")
#     file.write("Лавров 55543.12\n")
#     file.write("Песков 16543.12\n")
#     file.write("Семенов 44543.12\n")
#
# with open("resources/example.txt", "r") as file:
#     ls = file.readlines()
# d = {}
# for s in ls:
#     lsi = s.split()
#     d[lsi[0]] = float(lsi[1])
# print("список сопрудников, имеющих оклад менее 20 000:")
# for key, value in d.items():
#     if (value < 20000):
#         print(key)
#
# print("средний оклад: " + str(mean(d.values())))


# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# d = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
# with open("resources/example2.txt", "r") as file:
#     ls = file.readlines()
# with open("resources/example2new.txt", "w") as file:
#     for s in ls:
#         lsi = s.split()
#         file.write(d[lsi[0]] + " " + lsi[1] + " " + lsi[2] + "\n")


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

# with open("resources/example3.txt", "w") as file:
#     file.write("3 4 5 6 6 7 8 8 9")
# with open("resources/example3.txt", "r") as file:
#     ls = file.readline().split()
# summa = 0
# for n in ls:
#     summa += int(n)
# print(str(summa))