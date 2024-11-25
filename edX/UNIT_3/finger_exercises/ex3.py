def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    def convert_L(L):
        """
        L: list of strings
        
        return: list of integers (length of respective string elements)
        """
        return [len(string_element) for string_element in L]

    def x_bar(L):
        """
        L: list of integers

        return: int
        """
        total_sum = 0

        for integer_value in L:
            total_sum += integer_value
            
        return total_sum / len(L)
    
    ###

    # ensure L is not empty
    if not L:
        return float('NaN')

    # convert: original list of strings => list of integers
    L = convert_L(L)

    partial_sum = 0
    average = x_bar(L)

    for integer_value in L:
        partial_sum += (integer_value - average)**2

    return (partial_sum / len(L))**0.5

L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))

L = ['a', 'z', 'p']
print(stdDevOfLengths(L))

L = []
print(stdDevOfLengths(L))

L = [10, 4, 12, 15, 20, 5]