# Task1

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
array_1 += array_3 + array_2
array_1 = sorted(array_1)
print("Задача 1 ")
print("Решение без множеств: ", end="")
for i in range(len(array_1)-2):
    if array_1[i] == array_1[i+1] and array_1[i] == array_1[i+2]:
        print(array_1[i], end=" ")
# //////////////////////////////////////////////////////
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
array_4 = set(array_1) & set(array_2) & set(array_3)
print(f"\nРешение с множествами: {array_4}" )

# ////////////////////////////////////////
print("Задача 2")
array_2 += array_3
print("Решение без множества: ", end="")
for i in array_1:
    if i not in array_2:
        print(i, end=" ")
# /////////////////////////////
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
array_4 = set(array_1) - set(array_2) - set(array_3)
print(f"\nРешение с множествами: {array_4}")

