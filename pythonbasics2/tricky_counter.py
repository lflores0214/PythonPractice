# counter
# count the items in our list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(my_list, 0))


def tricky_counter(arr):
    counter = 0

    for i in arr:
        counter += i
    return counter


print(tricky_counter(my_list))
