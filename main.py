list1 = input("Введите первую строку: ")
list2 = input("Введите вторую строку: ")

sorted_list1 = sorted(list1.lower())
sorted_list2 = sorted(list2.lower())


if sorted_list1 == sorted_list2:

	print("Анограммны!")

else:

	print("Не анограммны!")