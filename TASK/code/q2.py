import itertools

def printLargest(numbers):

    result = []
    for permutation in itertools.permutations(str(number) for number in numbers):
        result.append(''.join(permutation))

    maximum = max(result, key=int)
    print(int(maximum))
numbers = [3, 30, 34, 5, 9]
printLargest(numbers)