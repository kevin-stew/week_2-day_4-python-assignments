def even_numbers(list1):
    even_list = []

    for num in list1:
        if num % 2 == 0:
            even_list.append(num)

    return even_list

print(even_numbers([2, 7, 10, 11, 12]))
