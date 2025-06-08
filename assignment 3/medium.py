# task 1
num_list = [1,2,3,4]
X = 2
Y = 4
sorted_list = []
for num in num_list:
    if num % X == 0 and num % Y != 0:
        sorted_list.append(num)
print(sorted_list)

# task 2
list_of_lists = [["nice", "try"], ["bro","great"]]
gen_list = []
for list in list_of_lists:
    for word in list:
        gen_list.append(word)
print(gen_list)

# task 3
# Complex String Manipulation: Extract and capitalize particular substrings.
my_str = "I gotta lock in!"
extr_substring = my_str[2: 7].upper()
print(extr_substring)

# task 4 
num_list = [4,5,4.4,3,3,1,2,7,1,1]
num_list.sort(reverse=True)
print(num_list)
list_list = []
for num in set(num_list):
    list_list.append([num_list.count(num), num])
print(list_list)
list_list.sort(reverse=True)
final_list =[]
for list in list_list:
    final_list.append(list[1])
print(final_list)

# task 5
num_list1 = [1,2,3,4]
num_list2 = [2,3,4,5]
for num in num_list1:
    if num not in num_list2:
        num_list2.append(num)
print(num_list2)

# task 6
dictionary = {1: [1, 4, 8 ,8], 2: [14, 88]}
result = {}
for x in dictionary:
    result[x] = sum(dictionary[x])
print(result)

# task 7
orig_list = [1, 5678,23,9000]
result = []
for x in orig_list:
    if x > 1488:
        result.append(1488)
    else:
        result.append(x)
print(result)

# task 8
list_of_strings = ["hell yeah", "graphic", "postroenia", "funcii"]
X = 8
num_str = 0
for str in list_of_strings:
    if len(str) > X:
        num_str += 1
print(num_str)

# task 9
list1 = ["hell yeah", "gnarly"]
list2 = [" america", " GOD BLESS"]
result = []
for x in range(min(len(list1), len(list2))):
    result.append(list1[x] + list2[x])
print(result)

# task 10
original_list = [1,2,3,4,5]
X = 2
Y = 3
result = []
for x in original_list:
    if x > X:
        result.append(x * Y)
    else:
        result.append(x)
print(result)
  