# 1
# numbers = [int(x) for x in input().split()]
# numbers.reverse()
# print(numbers)
# top = max(numbers)
# print((numbers[0]),numbers.index(top))
# 2
# score = int(input())
# if 100 >= score >= 90:
#     print("A")
# elif 90 > score >= 80:
#     print("B")
# elif 80 > score >= 70:
#     print("C")
# else:
#     print("D")

# 3
# import random
# x = [random.randint(0, 100) for p in range(0, 51)]
# y = []
# y.append(x)
# result = list(set(x))
# if len(x) != len(y):
#     print("O")

# 4
a = int(input())
b = 0

for i in range(2, a):
    if a%i == 0:
        b = 1

if b == 1 or a == 1 or a == 0:
    print("X") 
else:
    print("소수 입니다.") 

# 5
# a = 5
# for i in range(1,a):
#     print(' '*(a-i) + '*'*(2*i-1))
# for i in range(0, a):
#     print(' '*i + '*'*(2*a-(2*i+1)))

# 6





#8
# para1,para2 = map(int, input().split())
# numbers = list(map(int, input().split()))
# res = []

# for i in range(0,para1):
#   for j in range(i+1,para1):
#     for k in range(j+1,para1):
#       res.append(numbers[i]+numbers[j]+numbers[k])

# res.sort(reverse = True)
# result = []
# for value in res:
#     if value not in result:
#         result.append(value)

# print(result[para2 -1])