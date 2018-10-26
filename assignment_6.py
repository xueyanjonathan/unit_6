# Jonathan Lin
# 10/26/2018
# List
# Using lists and loops to create The Sieve of Eratosthenes


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
    while len(list_one) > 0:  # While there are still numbers in the original list, the loop will continue.
        first = list_one[0]
        list_two.append(first)  # Add the first number, which will be the prime number in list one, into list two.
        for number in list_one:  # Looping all numbers
            if number % first == 0:
                # If a number in the list divided by the first number has no remainder,
                # it is the multiple of the prime number, and it will be removed from the list.
                list_one.remove(number)
    print(list_two)


main()
