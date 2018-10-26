def main():
    limit = int(input("Max number = ? "))
    number = 2
    list_one = [2]  # The first number of the original list
    list_two = []
    # The second list, which there is going to be only prime numbers in it.
    # It is currently a blank list.
    while number < limit:
        number = number + 1
        list_one.append(number)  # Create list_one by putting in consecutive numbers added by 1
    while len(list_one) > 0:  # While the 
        first = list_one[0]
        list_two.append(first)
        for number in list_one:
            if number % first == 0:
                list_one.remove(number)
    print(list_two)


main()
