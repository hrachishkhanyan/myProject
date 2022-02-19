"""IF, ELIF, ELSE"""

# 1. Write a program that will take an input string from the user. If the string starts with "a" or "o", output it as it
# is, otherwise output the reverse of the string.
# Ստուգել, արդյո՞ք ներմուծված սթրինգը սկսվում է a կամ o-ով։ Եթե հա տպենք սթրինգն ինչպես կա, իսկ հակառակ դեպքում՝ սթրինգի
# հակառակը։
from random import randint

# inp = input('Enter a string: ')

# if inp[0] == 'a' or inp[0] == 'o':
#     print(inp)
# else:
#     print(inp[::-1])

# if inp[0] in 'ao':
#     print(inp)
# else:
#     print(inp[::-1])

# if inp.startswith(('a', 'o')):
#     print(inp)
# else:
#     print(inp[::-1])

# 2. Write a program that will ask to input a temperature in Celsius or Fahrenheit units.
# Convert to C if the input is in F units and otherwise if it's in C units.
# Sample input -> 36C
# Output will be -> 96.8F
# Գրել ծրագիր, որը կփոխակերպի Ցելսիուսով/Ֆարենհայթով տրված ջերմաստիճանը Ֆարենհայթի/Ցելսիուսի։ Ջերմաստիճանը պետք է
# ներմուծվի հետևյալ ֆորմատով` 36C, 96.8F և այլն։
# Regular expressions
# inp = input('Enter a temperature (e.g. 36C, 96.8F): ')
# temp = float(inp[:-1])
# unit = inp[-1].lower()
#
# if unit == 'c':
#     print(f'{inp} in Fahrenheit: {temp * 1.8 + 32:.1f}F')
# elif unit == 'f':
#     print(f'{inp} in Celsius: {(temp - 32) / 1.8:.1f}C')
# else:
#     print('Input should be in C or F units.')

# 3. Given and integer, write a program which will output Fizz, if the number is divisible by 3, Buzz, if it's divisible
# by 5, and FizzBuzz if it's divisible by both.
# Գրել ծրագիր, որը կտպի Fizz, եթե ներմուծված թիվը բաժանվում է 3-ի, Buzz, եթե բաժանվում է 5-ի և FizzBuzz, եթե բաժանվում է
# և՛ երեք, և՛ 5-ի։ Հակառակ դեպքում տպել հենց թիվը։

# number = int(input("enter any number\n"))
# result = ""
# if number % 3 == 0:
#     result += "Fizz"
# if number % 5 == 0:
#     result += "Buzz"
# if not result:
#     result += str(number)
# print(result)

# 4. Write a program that will take an example password as an input. If the password contains more than 6 and less than
# 12 characters and it contains both numerical and alphabetical characters and a symbol from "%", print that the
# password is good. Otherwise, prompt the user to change the password next time.
# Պահանջել մուտքագրել ծածկագիր։ Եթե ծածկագիրը պարունակում է 6-ից 12-ից նիշ և պարունակում է թվանշաններ, տառեր և հետևյալ
# սիմվոլներից մեկը "%", տպել, որ ծածկագիրն ուժեղ է։ Հակառակ դեպքում զգուշացրեք օգտատիրոջը, որ ծածկագիրը պետք է
# փոխվի։

# password = input('Enter a password: ')
#
# if 6 < len(password) < 12:
#     if '%' in password:
#         password = password.replace('%', '')
#         if password.isalnum() and not password.isnumeric() and not password.isalpha():
#             print('Good password')
#         else:
#             print('Your password is weak, consider changing it.')
#     else:
#         print('Your password is weak, consider changing it.')
# else:
#     print('Your password is weak, consider changing it.')


# pas = input('Input your password: ')
# is_letter = False
# isNumeric = False
# isSymbol = False
# if 5 < len(pas) < 13:
#     for i in range(len(pas)):
#         if 64 < ord(pas[i]) < 91 or 96 < ord(pas[i]) < 123:
#             is_letter = True
#         elif 47 < ord(pas[i]) < 58:
#             isNumeric = True
#         elif 31 < ord(pas[i]) < 48 or 57 < ord(pas[i]) < 65 or 90 < ord(pas[i]) < 96 or 122 < ord(pas[i]) < 127:
#             isSymbol = True
#     if is_letter and isNumeric and isSymbol:
#         print('Your password is good')
#     else:
#         print('Please change your password')
# else:
#     print('Please change your password')

# s = 'abcdefg'

# for i in range(len(s)):
#     print(s[i])
#
# for char in s:
#     print(char)

# 5. Ask for three numerical inputs. Find the sum of these numbers. If the sum is even, print the square of the sum,
# otherwise print the sum as it is.
# Գտնել ներմուծված երեք թվերի գումարը։ Եթե այն զույգ է, տպել գումարի քառակուսին։ Հակառակ դեպքում տպել գումարը։

# x = int(input('Enter first number: '))
# y = int(input('Enter second number: '))
# z = int(input('Enter third number: '))
# total = x + y + z
#
# if total % 2 == 0:
#     print(total ** 2)
# else:
#     print(total)

# tuple unpacking
# x, y, z = input('Enter first number: '), input('Enter second number: '), input('Enter third number: ')

# x, y, z = input('Enter three numbers (e.g. 2 5 7): ').split()
# total = int(x) + int(y) + int(z)
# print(total)
# total_ = int(x + y + z)
# print(total_)
# if total % 2 == 0:
#     print(total ** 2)
# else:
#     print(total)

# 6. Ask the user for a movie title. If the title starts with a capital letter, print "Great title!", otherwise print
# "Titles start with capital letters...". If the input starts with a special character [!, @, #, $, %, ^, &], print "I
# doubt that this is a title.".
# Պահանջել ներմուծել ֆիլմի վերնագիր։ Եթե վերնագիրը սկսվում է մեծատառով, տպել "Great title!", հակառակ դեպքում տպել
# "Titles start with capital letters..."։ Եթե ներմուծվածը սկսվում է [!, @, #, $, %, ^, &] նշաններով, տպել "I doubt that
# this is a title."․

# title = input('Enter your favourite movie: ')

# if title[0].upper() == title[0]:
#     ...

# if title[0] not in '!@#$%^&':
#     if title[0].isupper():
#         print('Great title')
#     else:
#         print('Titles start with capital letters...')
# else:
#     print('I doubt that this is a title')

# 7. Ask the user to input his/her age. If the user is older than 17, than tell them they're eligible to vote. If they
# are younger than 18, tell them how many years do they have to wait.
# Հարցրեք օգտատիրոջ տարիքը։ Եթե նա 17 տարեկանից մեծ է, նրան տեղյակ պահեք, որ կարող է քվեարկել։ Հակառակ դեպքում ասեք, թե
# քանի տարուց նա կկարողանա դա անել։

# age = int(input('Enter your age: '))
#
# if age > 17:
#     print('You are eligible vote!')
# else:
#     print(f'You still need to wait {18 - age} years to vote...')

# 8. Using 'random' module, generate a random number between -1000 and 1000. If the number is positive, print positive.
# If it's negative, print negative along with the absolute value of the number.
# Օգտագործելով random գրադարանը, գեներացնել [-1000,1000]-ը տիրույթում պատահական թիվ։ Եթե թիվը դրական է, տպել positive.
# Հակառակ դեպքում տպել negative և այդ թվի բացարձակ արժեքը։

# x = randint(-1000, 1000)
#
# if x < 0:
#     print(f'negative: {abs(x)}')
# else:
#     print('positive or zero')
