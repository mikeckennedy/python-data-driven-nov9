def is_even(n):
    return n % 2 == 0


def filter_nums(numbers, test):
    for n in numbers:
        if test(n):
            yield n


# subset = filter_nums(range(1, 50), is_even)
subset = filter_nums(range(1, 500), lambda x: x % 6 == 1 and x < 100)

for s in subset:
    print(s, end=',')


    #
    # def filter_nums(numbers, test):
    #     matches = []
    #     for n in numbers:
    #         if test(n):
    #             matches.append(n)
    #
    #     return matches
