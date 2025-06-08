# task 1
X = 2
num_list = [1,2,3,4]
sorted_list = []
for num in num_list:
    if num > X:
        sorted_list.append(num)
print(sorted_list)
print()

# task 2
num_list = [1,2,3,4]
sum_nums = 0
for num in num_list:
    sum_nums += num
print(sum_nums)
av_in_list = sum_nums/ len(num_list)
print(av_in_list)
print()

# task 3
# Maximum in Filtered List: Find the maximum of numbers less than X. 
# Тут потрібно максимальне значення чи кількість менших елементів?
X = 3
num_list = [1,2,3,4]
sorted_list = []
for num in num_list:
    if num < X:
        sorted_list.append(num)
print(sorted_list)
print(max(sorted_list))
print(len(sorted_list))
print()

# task 4
num_list = [1,2,3,4]
Y = 2
sorted_list = []
for num in num_list:
    if num % Y == 0:
        sorted_list.append(num)
print(sum(sorted_list))
print()

# task 5
num_list = [1,2,3,4]
sqr_list = []
for num in num_list:
    sqr_num = num ** 2
    sqr_list.append(sqr_num)
print(sqr_list)
print()

# task 6
num_list = [-2,-1,1,2]
sorted_list = []
for num in num_list:
    if num >= 0:
        sorted_list.append(num)
print(sorted_list)
print()

# task 7
str_list = ["height", "hey", "bruhh", "hell yeah"]
prefix = "he"
sorted_list = []
for word in str_list:
    if word[0: len(prefix)] == prefix:
        sorted_list.append(word)
print(sorted_list)
print()

# task 8
num_list = [1,2,3,4]
N = 2
num_sum = 0
for i in range(0, N):
    num_sum += num_list[i]
print(num_sum)
print()

# task 9
str_list = ["aboba", "did", "jelking", "guys", "xanax"]
palind_list = []
for word in str_list:
    if list(word) == list(reversed(word)):
        palind_list.append(word)
print(palind_list)

# task 10
num_list = [1,2,3,4]
N = 2
value_list = []
for num in num_list:
    value_list.append(num % N == 0)
print(value_list)