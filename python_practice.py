#
# CICS 397A Homework 0
#
# Fill in the bodies of the missing functions as specified by the comments and docstrings.
#


# Exercise 1
#
def is_odd(lst):
    """Return True if the given list has an odd number of elements, False otherwise
        
    Hint: check out the Python docs on built-in functions for getting the length of a sequence:
    https://docs.python.org/3/library/functions.html#len 
    """
    #
    # fill in function body here
    #
    return len(lst)%2==1  # fix this line!


# Exercise 2
#
def length_sum(list_of_seqs):
    """Calculate the sum of the lengths of an arbitrary list of sequences (tuples, lists, or strings).
    """
    total = 0
    i = 0
    while i < len(list_of_seqs):
        total = total + len(list_of_seqs[i])
        i = i + 1

    return total  # fix this line!


# Exercise 3
#
def max_both(first, second):
    """Return the largest element that appears in both lists.
    
    Hint: you might want to use the built-in max function:
    https://docs.python.org/3/library/functions.html#max     
    """
 
    first_set = set(first)
    second_set = set(second)
    both_set = (first_set & second_set)

    return max(both_set)  # fix this line!


# Exercise 4
# 
def max_jr(lst):
    """Return the second largest item in a list."""
    
    lst.remove(max(lst))

    return max(lst)  # fix this line!
    

# Exercise 5
# 
def splice_em(list_one, list_two):
    """Splice two equal-length lists together.
    
    Returns a list with alternating elements from the two lists.  For example:
    splice_em(['a', 'b', 'c'], [1, 2, 3]) => ['a', 1, 'b', 2, 'c', 3]
    
    Hint: you'll probably want to use a for or while loop to iterate.  The enumerate() or zip() 
    built-in functions might be helpful here: https://docs.python.org/3/library/functions.html
    
    """
    ret_lst = list_one + list_two
    ret_lst[::2] = list_one
    ret_lst[1::2] = list_two

    return ret_lst


# Exercise 6
#
def is_downhill(numbers):
    """  Returns True if list of numbers is non-increasing, False otherwise.

    For example, [10, 8, 8, 3, 0] is non-increasing, [10, 8, 6, 7] is not.
    """
 
    res=False
    x=[]
    x.extend(numbers)
    numbers.sort()
    if(x==numbers):
        res=True
    return res  # fix this line!
    

# Exercise 7
# 
def smallest_champ(lst1, lst2):
    """Find the smallest element of lst1 that is larger than every element of lst2.

    If no element in lst1 is larger than those in lst2, return None.
    """
   
    return min(i for i in lst1 if i > max(lst2))  # fix this line!


# Exercise 8
# 
def reverse_dict_list(d):
    """Reverse a dictionary that maps keys to lists of values.
    
    Given a dictionary that maps each key k1, k2, etc. to a list of values v1, v2, ..., create a 
    new dictionary keyd by v1, v2, mapping them to lists k1, k2, etc.  

    For example, reverse_dict_list({'a':[1, 2, 3], 'b':[1, 3, 5, 7], 'c':[4, 5, 6]}) should return 
    the dictionary {1:['a', 'b'], 2:['a'], 3:['a', 'b'], 5:['b', 'c'], 7:['b'], 4:['c'], 6:['c']}
    """
    keylist = []
    for x in range(len(list(d.values()))):

        keylist = keylist + list(d.values())[x]
        newkey = []
        [newkey.append(x) for x in keylist if x not in newkey]
        d1_5 = []
        d2 = {}

        for x in range(len(list(d))):
            for y in range(len(newkey)):
                if (newkey[y]) in (d[list(d)[x]]):
                    if newkey[y] not in d2:

                        d2[newkey[y]] = list(d)[x]
                        d2[newkey[y]] = list()
                    if newkey[y] in d2:

                        d2[newkey[y]].append(list(d)[x])
                    else:
                        d2 = (newkey[y] ,"not in", [list(d)[x]])
        return(d2)

    #return {keylist}  # fix this line!


# Exercise 9
#
def char_counts(some_text):
    """Return a dictionary containing each character in the text as keys, and the number of times
    they occur as values.

    Hint: recall that since a string is a sequence, you can loop through it as you would a list.
    For help with dictionaries, see the Python docs: 
    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    """
    tots = {}

    for i in some_text:
        if i in tots:
           tots[i] += 1
        else:
            tots[i] = 1
    return tots

# Exercise 10
# 
def is_subseq(little, big):
    """Determine whether sequence little is a subsequence of big.
    
    If A is a subsequence of B, you can produce B by inserting some number of elements into A
    without reording the existing elements.  For example, [6, 7, 0] is a subsequence of 
    [8, 6, 7, 5, 3, 0, 9], but [3, 6], and [1, 8, 6] are not.

    Hint: for each 
    """
    #
    # fill in function body here
    #
    for i in range(len(little)):
        if little[i] not in big:
            return False
        for j in range(len(big)):
            if (little[j] in big) and (big.index(little[i+1]) > big.index(little[i])):
                return True
    return None  # fix this line!
             

# The main() function below will be executed when your program is run.  Note that Python does not 
# require a main() function, but it is considered good style.  The comments on each line show
# what shold be output if your code is running correctly.
def main():
    print("1.", is_odd(["one", "two", "three", "four"]))               # False
    print("2.", length_sum([[2, 4], (6, 8), "who do we"]))             # 13
    print("3.", max_both([10, 100, 1, 0], [99, 1, 50, 101, 100]))      # 100
    print("4.", max_jr([1, 3, 0, 9]))                                  # 3
    print("5.", splice_em(['r', 'd', 'c', 'p'], [2, 2, 3, 0]))         # ['r', 2, 'd', 2, 'c', 3, 'p', 0]
    print("6.", is_downhill([10, 9, 9, 9, 4, 5, 3, 1]))                # False
    print("7.", smallest_champ([99, 39, 59, 49, 9], [10, 20, 30, 40])) # 49
    print("8.", reverse_dict_list({1:['h', 'e', 'y'], 2:['h', 'o']}))  # {'h': [1, 2], 'e': [1], 'y': [1], 'o': [2]}
    print("9.", char_counts("wowie zowie"))                            # {'w': 3, 'o': 2, 'i': 2, 'e': 2, ' ': 1, 'z': 1}
    print("10.", is_subseq([1, 2], [6, 3, 1, 1, 9, 2, 2]))             # True


###################################

# The line below is a common Python idiom for creating Python programs that have useful functions.  
# For more info, see: https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == '__main__':

    main()

