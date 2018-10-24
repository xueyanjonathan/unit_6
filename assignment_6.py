def list():
    limit = int(input("Max number = ? "))
    number = 2
    list_one = [2]
    list_two = []
    while number < limit:
        number = number + 1
        list_one.append(number)
    print(list_one)
    first = list_one[0]
    list_two.append(first)
    for number in list_one:
        if number % first == 0:
            list_one.remove(number)
    print([list_two])

list()

