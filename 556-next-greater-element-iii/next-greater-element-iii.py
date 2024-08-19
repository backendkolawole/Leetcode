class Solution:
    def nextGreaterElement(self, n: int) -> int:
        array = [char for char in str(n)]
        # print(''.join(array))
        length = len(array)
        index = len(array) - 2

        while (index >= 0 and array[index] >= array[index + 1]):
            index -=1

        if (index == -1):
            return -1

        swap = length - 1

        while (array[swap] <= array[index]):
            swap -=1

        array[index], array[swap] = array[swap], array[index]

        i = index + 1
        j = length - 1

        while i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

        result = int(''.join(array))
        return -1 if pow(2, 31) - 1 < result else result
        