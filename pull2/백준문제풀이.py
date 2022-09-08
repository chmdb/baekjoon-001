# 숫자의 개수 
# a = int(input())
# b = int(input())
# c = int(input())
# result = list(str(a * b * c))
# for i in range(10):
#     print(result.count(str(i)))

# 숫자의 합
# n = input()
# print(sum(map(int,input())))

# N 찍기
#a = int(input())
#for i in range(a):
 #   print(i+1)

# 공
# N = int(input())
# cups = [1, 2, 3]
# for _ in range(N):
#     x, y = map(int, input().split())
#     xb = cups.index(x)
#     yb = cups.index(y)

#     cups[xb] , cups[yb] = cups[yb] , cups[xb]

# print(cups[0])


#8진수 2진수

# x = int(input())
# print(int(x,8))
# print(int(bin(x)))

# A+B - 5

# while True:
#     some , thing = map(int, input().split())
#     if some == 0 and thing == 0:
#         break
#     print(some+thing)

#별찍기 - 2

# a=int(input())
# for i in range(1,a+1):
#     print(" "*(a-i) + "*"*i)

# 별찍기 - 3

# a=int(input())
# for i in range(1,a+1):
#      print("*"*(a+1-i) )

# 팩토리얼
# n = int(input())

# result = 1
# if n > 0:
#     for i in range(1, n+1):
#         result *= i
# print(result)

#곱셈
# num1 = int(input())
# num2 = int(input())

# print(num1 * (num2%10))
# print(num1 * ((num2%100)//10))
# print(num1 * (num2//100))
# print(num1 * num2)


# 별찍기 - 4

# a=int(input())
# for i in range(1,a+1):
#       print(" "*(i-1) + "*"*(a+1-i))

# 기찍N

# n = int(input())
# for i in range(n):
#     print(n-i)

# 상수

# a, b = input().split()
# c = (int(str(a)[::-1]))
# d = (int(str(b)[::-1]))

# if c > d :
#     print(c)
# else:
#     print(d) 

# 나머지

# n= []
# for _ in range(10):
#     a= int(input())
#     b= a % 42
#     n.append(b)

# s = set(n)
# print(len(s))    

#  알파벳 찾기

# S = input()
# abc ='abcdefghijklmnopqrstuvwxyz'

# for i in abc:
#     if i in S:
#         print(S.index(i), end= ' ')
#     else:
#         print( -1, end =' ')

# 초콜릿 자르기

# a,b = input().split() #split 때문에 문자열 상태

# print(int(a)*int(b)-1)

# 홀수

# import sys
# input = sys.stdin.readline
# s = []
# for i in range(7):
#     a = int(input())
#     if a % 2 != 0: s.append(a)
# if s:
#     print(sum(s))
#     print(min(s))
# else:
#     print(-1)

# 피보나치 수
# n = int(input())
# f = [0,1]
# for i in range(2, n+1):
#     p = f[i-1]+f[i-2]
#     f.append(p)
# print(f[n])

# 알파벳 개수 
# S = input() # 단어 S를 입력받습니다

# for i in range(97, 123): # 소문자 a-z의 아스키 코드 값 범위 지정
#   print(S.count(chr(i)), end=' ') # chr로 아스키 코드를 문자열로 변환 후 count

# 음계  다시 풀기 
# a = list(map(int, input().split()))
# if a == sorted(a):
#     print("ascending")
# elif a == sorted(a, reverse=True):
#     print("descending")
# else:
#     print("mixed")

# 평균
# n = int(input())
# test_list = list(map(int, input().split()))
# max_score = max(test_list)

# new_list = []
# for score in test_list : 
#     new_list.append(score/max_score*100)
# avg = sum(new_list)/n
# print(avg)

# 시험 성적
# test_score = int(input())
# if 100 >= test_score >= 90 :
#     print("A")
# elif 89 >= test_score >= 80 :
#     print("B")
# elif 79 >= test_score >= 70 :
#     print("C") 
# elif 69 >= test_score >= 60 :
#     print("D")
# else:
#     print("F")

#부녀회장이 될 테야  나중에 다시 풀어보기
# T = int(input())

# for _ in range(T):

#     k = int(input())

#     n = int(input())

#     people = [ i for i in range(1, n+1)]

#     for __ in range(k):

#         for j in range(1,n):

#             people[j] += people[j-1]

#     print(people[-1])


# 세수 정렬
# a = list(map(int, input().split()))
# a.sort()
# print(a[0],a[1],a[2])

# TV크기 

# D, H, W = map(int,input().split())
# gap = (D/int(H**2+W**2)**0.5)
# print(int(gap*H),int(gap*W))

#A+B - 7
# n = int(input())
# for i in range(1,n+1):
#     a, b = map(int, input().split())
#     print(f"Case #{i} : {a+b}")

# 평균 점수 다른풀이 실패!
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# f = []
# f.append(a)
# f.append(b)
# f.append(c)
# f.append(d)
# f.append(e)

# for i in range(5):
#     if f < 40:
#         f.replace(i,40)
# result = 0
# for val in f:
#     result += val 
# print(result / len(f))        

# 평균 점수 정답 풀이
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# if a < 40:
#     a = 40
# if b < 40:
#     b = 40    
# if c < 40:
#     c = 40
# if d < 40:
#     d = 40
# if e < 40:
#     e = 40        
# n = (a+b+c+d+e) / 5
# print(int(n))

# 상근날드 새롭지만 비효율적인 방법
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# if a > b:
#     next = b
# elif b > a:
#     next = a
# elif a == b:
#     next = a    

# if b > c :
#    day = c
# elif c > b  :
#     day = b    
# elif b == c :
#     day = c

# if next > day :
#     burger = day
# elif day > next : 
#     burger = next
# elif day == next :
#     burger = next

# if d > e :
#     side = e
# elif e > d :
#     side = d
# elif d == e:
#     side = d
# print(burger+side-50)             


#손익분기점 
# a,b,c = map(int,input().split())


# if b >= c: 
#         print(-1)
# else:
#          print(a//(c-b)+1)        


# 주사위 세개  max 사용해서 풀수 있다고함
# a,b,c = map(int,input().split())

# if a == b == c :
#     print(10000+a*1000)
# elif a == b :
#     print(1000+a*100)
# elif b == c :
#     print(1000+c*100)
# elif c == a:
#     print(1000+a*100)

# else :
#     if a>b>c :
#         print(a*100)  
#     elif a< b >c :
#         print(b*100)
#     elif a < b < c :
#         print(c*100)  
#     elif a > b < c :
#         print(a*100)                           

# 10부제

# a = input()
# b = list(map(int,input().split()))
# print(b.count(a))

# 과자 
# k,n,m = map(int,input().split())
# if k*n > m:
#     t=k*n 
#     print(t-m)
# else:
#     print(0)

# 사분면 고르기
# x = int(input())
# y = int(input())
# if x>0:
#     if y>0:
#         print(1) 
#     elif y<0:
#         print(4)
# if x<0:
#     if y>0:
#         print(2)
#     elif y<0:
#         print(3)                    

# 윤년
# n = int(input())

# if n%4==0 :

#     if n%100==0 and n%400 !=0:
#         print (0)
#     else:
#         print(1)    
# else:
#     print(0)            

#  방학 숙제

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# if b%d == 0:
#     kor = b//d 
# elif b%d != 0:
#     kor = b//d +1 
# if c%e == 0 :
#     mt = c//e 
# elif c%e != 0:
#     mt = c//e +1 

# if kor >= mt:
#     print(a-kor)
# elif mt >= kor:
#     print(a-mt)    

# 삼각형 외우기
# a = int(input())
# b = int(input())
# c = int(input())

# if a == b == c == 60:
#     print('Equilateral')
# elif a+b+c == 180 and (a==b or b==c or c==a):
#     print('Isosceles')
# elif a+b+c == 180 and (a!=b  or b!=c or c!=a):
#     print('Scalene')    
# elif a+b+c !=180:
#     print('Error')

# 정육각형과 삼각형
# l = int(input())
# result = (3**(1/2) / 4) * l**2 
# print(float(result))

# 파일 옮기기 
# a , b = map(int, input().split())
# c , d = map(int, input().split())

# print(min(a+d,c+b))

# 시험공부 했던거
# def asterisk_test_2(*args):
#     x,y,*z = args
#     return x,y,z
# print (asterisk_test_2(3,4,5,10,20))

# 별찍기 - 5
# a = int(input())

# for i in range(1,a+1):
#     print(' '*(a-i) + '*'*(2*i-1))

# 윷놀이
# a = []
# b = []
# c = []
# a = map(int,input().split())
# b = map(int,input().split())
# c = map(int,input().split())

# sum_a = sum(a)
# sum_b = sum(b)
# sum_c = sum(c)

# if sum_a == 3:
#     print('A')
# elif sum_a == 2:
#     print('B')
# elif sum_a == 1:
#     print('C')
# elif sum_a == 0:
#     print('D')
# elif sum_a == 4:
#     print('E')

# if sum_b == 3:
#     print('A')
# elif sum_b == 2:
#     print('B')
# elif sum_b == 1:
#     print('C')
# elif sum_b == 0:
#     print('D')
# elif sum_b == 4:
#     print('E')

# if sum_c == 3:
#     print('A')
# elif sum_c == 2:
#     print('B')
# elif sum_c == 1:
#     print('C')
# elif sum_c == 0:
#     print('D')
# elif sum_c == 4:
#     print('E')

# 별찍기 - 6
# a = int(input())
# for i in range(0, a):
#     print(' '*i + '*'*(2*a-(2*i+1)))

# 최댓값
# from copy import copy
# a = []
# for i in range(9):
#     a.append(int(input()))

# temp = []
# temp = copy(a)
# temp.sort()
# print(temp[-1])
# for i in range(len(a)):
#     if temp[-1] == a[i]:
#         top = a[i]
#         print(a.index(top)+1)
#         break

# 더하기 사이클 
# number = int(input())
# temp = number
# i = 0
# while(True):
#     i += 1
#     if temp>=10:
#         ten = temp//10
#         one = temp%10
#         hap = ten+one
#     else:
#         ten = 0
#         one = temp
#         hap = ten+one
#     if hap >=10:
#         one1 = hap%10
#         temp = one*10+one1
#     else:
#         temp=one*10+hap
  
#     if number == temp:
#         print(i)
#         break
  



# A+B - 4 10951
# while 1:
#     try:
#         a,b =map(int, input().split())
#         print(a + b)
#     except:
#         break

# 직사각형에서 탈출   min 쓰면 쉬운거였어..
# x,y,w,h = map(int,input().split())
# print(min(x,y,w-x,h-y))

# 네번째 점


# x_list = []
# y_list = []

# for i in range(3):
#     x,y = map(int, input().split())
#     x_list.append(x)
#     y_list.append(y)

# for i in range(3):
#     if x_list.count(x_list[i]) == 1:
#         x4 = x_list[i]
#     if y_list.count(y_list[i]) == 1:
#         y4 = y_list[i]
    
# print(x4, y4)
    

# 별찍기 - 7

# a = int(input())
# for i in range(1,a):
#     print(' '*(a-i) + '*'*(2*i-1))
# for i in range(0, a):
#     print(' '*i + '*'*(2*a-(2*i+1)))

# 별찍기 - 9
# a = int(input())
# for i in range(0, a-1):
#     print(' '*i + '*'*(2*a-(2*i+1)))
# for i in range(1,a+1):
#     print(' '*(a-i) + '*'*(2*i-1))

# import sys
# N = int(input())
# for i in range(N):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)


# 설탕 배달 
# N = int(input())
# bag = 0

# while N >= 0:
#     if N % 5 == 0:
#         bag += (N // 5) 
#         print(bag)
#         break
#     N -= 3  
#     bag +=1
# else:
#     print(-1)


# 베스트 셀러

# N = int(input())
# booklist = []
# for i in range(N):
#     booklist.append(input())
# booklist.sort()
# set_list = list(set(booklist))
# set_list.sort()
# booklist.append(0)
# count = 1
# count_list = []

# for i in range(len(booklist)):
#     if booklist[i] != booklist[i+1]:
#         count_list.append(count)
#         count = 1
        
#         if booklist[i+1] == 0:
#             break
#         continue
#     count += 1
# print(set_list[count_list.index(max(count_list))]    


# RGB거리  실패 모르겠다~

# N = int(input())
# index_list = []
# Min_Value = []
# min_val = []
# for i in range(0,N):
#     RGB_list = list(map(int,input().split()))
#     min_val[i] = min(RGB_list)                     
#     index_list.append(RGB_list.index(min_val[i]))
#     Min_Value.append(min(RGB_list))
# for i in range(0,N):
# RGB_list = [list(map(int,input().split())) for _ in range(N)]
# RG
# for i in range(0,N):
#     for j in range(0,N):
#         if RGB_list[i][j] != RGB_list[i+1][j]:
#             Min_Value.append(min(RGB_list[i]))

# print(RGB_list)
# print(Min_Value)
# print(index_list)

# DFS와 BFS  포기

# class Graph():
#     def __init__(self,size) :
#         self.Szie = size
#         self.graph 



# 요세푸스 문제


#  내가 풀고 실패한것

# front = 0
# rear = 0
# circle = []
# queue = []
# temp = []
# N , K = map(int, input().split())
# for i in range(1,N+1):
#     for k in range(1,N+1):
#         circle.append(k)

# for j in range(K-1,len(circle),K):
#     if circle[j] not in temp:
#         queue.append(temp)
#         temp.append(circle[j])
#         continue

# print(queue)
# front = K
# rear = first+
# temp = circle[rear]
# circle[rear].pop()

# 정답풀이 내가 푼거 아님  
# N,K = map(int,input().split())
# arr = [i for i in range(1,N+1)]

# circle = []
# temp = 0

# for t in range(N):
#     temp += K-1  
#     if temp >= len(arr):   # 리스트를 다 돌고 그 이후 순서 맞게 가기 위함 
#         temp = temp%len(arr)
#     circle.append(str(arr.pop(temp)))

# print("<",", ".join(circle)[:],">", sep='')

# 보물 
# 조건 무시하고 풀었음
# answer = 0
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# for i in range(N):
#     A.sort()
#     B.sort()
#     B = B[::-1]
#     answer += A[i] * B[i]

# print(answer)

# 정답 내 풀이 아님
# n = int(input())

# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))

# s = 0
# for i in range(n):
#     s += min(a_list) * max(b_list)
#     a_list.pop(a_list.index(min(a_list)))
#     b_list.pop(b_list.index(max(b_list)))

# print(s)


# 기타줄 1049번
# guitar_strings , brand = map(int,input().split()) 
# price_list = []
# for i in range(brand):
#     price_6, price_1= (map(int,input().split()))
#     price_list.append((price_6, price_1))

# min_price = guitar_strings * min(map(min, price_list))  # 기타줄 * 낱개로 살때

# for i in range(len(price_list)):
#     for j in range(len(price_list)):
#         min_index_6 = price_list[i][0]
#         if min_price > min_index_6*(guitar_strings//6+1):       # 6개 묶음 으로 나눴을때 더 작으면 min_price 로 넣어줌
#             min_price = min_index_6*(guitar_strings//6+1)

# min_index_1 = min(map(min, price_list))         # 가장 작은 낱개


# for i in range(len(price_list)):
#     for j in range(len(price_list)):
#         min_index_6 = price_list[i][0]
#         min_index_6 = min_index_6 * (guitar_strings//6)                 
#         if min_price > min_index_6+((guitar_strings%6)*min_index_1):    # 묶음 + 낱개 일때 더 작으면 min_price 로 넣어줌
#             min_price = min_index_6+((guitar_strings%6)*min_index_1)


# print(min_price)



#  퇴사 14501번  일단 보류

# N = int(input())

# consulting = []
# dp_sum = []
# temp = N
# for i in range(N):
#     Ti , Pi = (map(int,input().split()))
#     consulting.append((Ti,Pi))
# for i in range(len(consulting)):
#     for j in range(len(consulting)):
#         if N < consulting[i][0]+i:
#             pass

#         if consulting[i][0] < temp:
#             temp = temp - consulting[i][0]
#             dp = consulting[i][1]
#             dp_sum.append(dp)
#             if min(map(min,consulting)) != consulting[i][1]:
#                 dp = consulting[i][1]
#                 dp_sum.append(dp)


# print(dp_sum)


#  트리순회 1991번 못품

# class TreeNode():
#     def __init__(self):
#         self.left = None
#         self.data = None
#         self.right = None

# def preoder(node):
#     if node == None:
#         return
#     preoder(node.left)
#     preoder(node.right)



# def inoder(node):
#     if node == None:
#         return
#     inoder(node.left)
#     inoder(node.right)


# def postoder(node):
#     if node == None:
#         return
#     postoder(node.left)
#     postoder(node.right)