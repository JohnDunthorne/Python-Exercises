# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.


def multi_or_sum(num1, num2):
    total = num1 * num2

    if total <= 1000:
        return total
    else:
        return num1 + num2


total = multi_or_sum(20, 30)
print(total)

total = multi_or_sum(40, 30)
print(total)
