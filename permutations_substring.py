"""Given two strings, a and b,
find all permutations of
a within b

>>> a = "abbcd"
>>> b = "babcdbaefdbbacbddfae"
>>> print permutations(b,a)
['babcd', 'dbbac']
"""


permus = []

def permutations(string, substring):
    
    if type(string) == "string":
        string = string.split()


    if len(string) < 1:
        return permus
    
    perm = ""
    step =0
    for i in range(step, len(substring)):
        if string[i] in substring: 
            perm += string[i]
        else:
            step = i
            return permutations(string[step+1::], substring)

    permus.append(perm)
    return permutations(string[len(substring)::], substring)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; YOU FOUND SUCCESS! ***\n"




    
