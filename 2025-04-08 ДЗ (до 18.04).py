# Модуль 3 Циклы Часть 1

# Задание 1
# a=int(input("введите число A "))
# b=int(input("введите число B "))
# if a>b: a,b=b,a
# while a != b:
#     if a%7==0:
#         print(a, end=', ')
#     a+=1

# Задание 2
# a=int(input("введите число A "))
# b=int(input("введите число B "))
# if a>b: a,b=b,a
# a1=a; b2=b; a3=a; a4=a # 4 промежуточных переменных для разных (четырех) этапов решения
# print("1) все числа от A до B (включительно):")
# while a1<=b: print(a1, end=', ');a1+=1
# print()
# print("2) все числа от A до B (включительно) в убывающем порядке:")
# while b2>=a: print(b2, end=', ');b2-=1
# print()
# print("3) все числа от A до B, кратные 7:")
# while a3 != b:
#     if a3%7==0: print(a3, end=', ');
#     a3+=1
# print()
# count=0
# while a4 != b:
#     if a4%5==0: count+=1
#     a4+=1
# print("4) количество чисел от A до B, кратное 5:", count)

# Задание 3
# a=int(input("введите число A "))
# b=int(input("введите число B "))
# if a>b: a,b=b,a
# a1=a; a2=a; a3=a; a4=a  # 4 промежуточных переменных для разных (четырех) этапов решения
# print("1) числа кратные 3:")
# while a1 != b:
#     if a1%3==0: print("Fizz", end=', ');
#     a1+=1
# print()
#
# print("2) числа кратные 5:")
# while a2 != b:
#     if a2%5==0: print("Buzz", end=', ');
#     a2+=1
# print()
#
# print("3) числа кратные 3 и 5:")
# while a3 != b:
#     if a3%15==0: print("Fizz Buzz", end=', ');
#     a3+=1
# print()
#
# print("4) числа не кратные 3 и 5:")
# while a4 != b:
#     if a4%3 != 0:
#         if a4%5 != 0:
#             print(a4, end=', ')
#     a4+=1
