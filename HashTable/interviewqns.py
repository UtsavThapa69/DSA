#common element in two list using a hash table i.e. dictionary
def common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True

    return False

def common1(list1, list2):
    return bool(set(list1) & set(list2))

def  common2(list1, list2): #Fastest
    return not set(list1).isdisjoint(list2)
#i am using set as well cuz set does the work of the dictionary without the need of a dummy value


#finding duplicates
def duplicates(nums):
    seen = {}
    dupli = []

    for  num in nums:
        if num in seen:
            if seen[num] == 1:
                dupli.append(num)
            seen[num] += 1
        else:
            seen[num] = 1

    return dupli

def duplicates1(nums): #cuz i dont see why the order and value matters if i am only returning duplicates
    seen = set()
    dupli = set()

    for num in nums:
        if num in seen:
            dupli.add(num)
        else:
            seen.add(num)

    return dupli

#first non-repeating character, order matters
def first_non_repeating(string):#the method i came up with 
    seen = {}
    dupli = {}
    for char in string:
        if char in seen:
            dupli[char] = 1
        else:
            seen[char] = 1

    for char in seen:
        if char not in dupli:
            return char
    return None

def first_non_repeating(string):
    frequency = {}
    for  char in string:
        frequency[char] = frequency.get(char, 0) + 1
    for char in frequency:
        if  frequency[char] == 1:
            return char
    return None