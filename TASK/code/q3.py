def longestPalin(string):
    maxLength = 1

    start = 0
    length = len(string)

    low = 0
    high = 0


    for i in range(1, length):

        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            low -= 1
            high += 1

        low += 1
        high -= 1
        if string[low] == string[high] and high - low + 1 > maxLength:
            start = low
            maxLength = high - low + 1

        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            low -= 1
            high += 1

        low += 1
        high -= 1
        if string[low] == string[high] and high - low + 1 > maxLength:
            start = low
            maxLength = high - low + 1

    print("Longest palindrome substring is:" )
    print(string[start:start + maxLength])
string = "aaaabbaa"
longestPalin(string)