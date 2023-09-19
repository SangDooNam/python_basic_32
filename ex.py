""" Task - Unique sort

You are given a list of strings. Implement a method `unique_char_sort` to 
sort the list of strings by the number of unique characters in the strings.
"""


# def unique_char_sort(list):
    
#     return sorted(list, key= lambda x : len(set(x)))



# strings = ['Digital', 'Career', 'Institute', 'Lecture', 'Exercise']

# print(unique_char_sort(strings))


# def unique_char_sort(list):
    
#     for element in set(list):
#         for i in element:
#             sorted(list, key = len)
    


# def item_in_set(s):
#     return len(set(s))



# def unique_char_sort(lst):
    
#     print(sorted(lst, key= item_in_set))



# strings = ['Digital', 'Career', 'Institute', 'Lecture', 'Exercise']

# unique_char_sort(strings)



""" Output:

```
> unique_char_sort(strings)

['Career', 'Digital', 'Lecture', 'Institute', 'Exercise']"""


def unique_char_sort(lst):
    
    return sorted(lst, key=lambda x : len(set(x)))

strings = ['Digital', 'Career', 'Institute', 'Lecture', 'Exercise']

print(unique_char_sort(strings))
