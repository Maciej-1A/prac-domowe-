#3
# 1. Stwórz pustą listę o nazwie "numbers".
# numbers = []
# print(len(numbers))
# print(numbers)

# 2. Poproś użytkownika o podanie 5 liczb i dodaj je do listy.
# numbers = []
# print(numbers)
# x = 0
# while x < 5:
#     inp = float(input())
#     numbers.append(inp)
#     print(numbers)
#     x += 1
# 
# 3. Oblicz sumę liczb znajdujących się w liście "numbers".
# numbers = [23,24,25,25,69,420]
# print(numbers)
# suma = 0
# x = 0
# while x < len(numbers):
#     suma += numbers[x]
#     x += 1
# print(f"{numbers} - suma = {suma}")

# 4. Znajdź największą liczbę w liście "numbers".
# numbers = [10,2,87,96,69]
# najw = numbers[0]
# x = 0
# while x < len(numbers):
#     if najw < numbers[x]:
#         najw = numbers[x]
#     x += 1
# print(f"najwienksa = {najw}")

# 5. Znajdź najmniejszą liczbę w liście "numbers".
# numbers = [1,10,100,1000]
# najmniejsza = numbers[0]
# x = 0
# while x < len(numbers):
#     if najmniejsza > numbers[x]:
#         najmniejsza = numbers[x]
#     x += 1
# print(f"najmniejsza = {najmniejsza}")

# 6. Policz średnią arytmetyczną liczb w liście "numbers".
# numbers = [3,14,64,16,31,18]
# print(numbers)
# suma = 0
# x = 0
# while x < len(numbers):
#     suma += numbers[x]
#     x += 1
# print(suma/len(numbers))

# # 7. Znajdź ilość liczb parzystych w liście "numbers".
# numbers = [69,64,16,1,7,25]
# x = 0
# parzyste = 0
# while x < len(numbers):
#     if numbers[x] % 2 == 0:
#          parzyste += 1
   
# # 8. Stwórz nową listę o nazwie "duplicates" zawierającą powtarzające się elementy z listy "numbers".
# numbers = [23,24,25,25,69,96,420,69]
# hallucynki = []
# x = 0
# while x < len(numbers):
#     if numbers.count(numbers[x]) > 1 and numbers[x] not in hallucynki:
#         hallucynki.append(numbers[x])
#     x += 1
# print(numbers)
# print(hallucynki)

# # 9. Usuń wszystkie powtarzające się elementy z listy "numbers".
# numbers = [23,24,25,25,69,96,420,69]
# lista2 = []
# x = 0
# while x < len(numbers):
#     if numbers[x] not in lista2:
#         lista2.append(numbers[x])
#     x += 1
# print(lista2)

# # 10. Stwórz nową listę o nazwie "squares" zawierającą kwadraty liczb z listy "numbers".
# numbers = [12,13,50,54,64,7]
# squares = []
# x = 0
# while x < len(numbers):
#     squares.append(numbers[x]**2)
# print(numbers)
#4.
# 1. Wyświetl wszystkie liczby z listy "numbers" w odwrotnej kolejności
# print("9-=-"*10)
# numbers = [1,1,1,2,2,5]
# i = -1
# while i >= -len(numbers):
#     print(numbers[i])
#     i-= 1

# # 2. Poproś użytkownika o podanie liczby. Sprawdź, czy liczba ta znajduje się w liście "numbers".
# print("9-=-"*10)
# numbers = [1,1,1,2,2,5]
# inp = int(input())
# if inp in numbers:
#     print("Tak")
# else:
#     print("Nie")

# # 3. Wyświetl indeks pierwszego wystąpienia danej liczby w liście "numbers".
# print("9-=-"*10)
# numbers = [1,1,1,2,2,5]
# inp = int(input())
# i = 0
# while i < len(numbers):
#     if inp == numbers[i]:
#         print(i)
#         break
#     i += 1

# # 4. Znajdź ilość liczb większych niż 10 w liście "numbers".
# print("9-=-"*10)
# numbers = [1,1,1,2,2,5,11]
# ile = 0
# i = 0
# while i < len(numbers):
#     if numbers[i] > 10:
#         ile += 1
#     i += 1
# print(ile)
# # 5. Posortuj listę "numbers" w kolejności malejącej.
# print("9-=-"*10)
# numbers = [11,2,10,3,1,2,4]
# numbers.sort(reverse=True)
# print(numbers)

# # 6. Znajdź drugą największą liczbę w liście "numbers".
# print("9-=-"*10)
# numbers = [11,2,10,3,1,2,4,11]
# max1 = float('-inf')
# max2 = float('-inf')
# i = 0
# while i < len(numbers):
#     if numbers[i] > max1:
#         max2 = max1
#         max1 = numbers[i]
#     elif numbers[i] > max2 and numbers[i] != max1:
#         max2 = numbers[i]
#     i += 1
# print(f"max1 {max1}")
# print(f"max2 {max2}")

# # 7. Stwórz nową listę o nazwie "doubled_numbers" zawierającą podwojoną wartość każdej liczby z listy "numbers".
# print("9-=-"*10)
# numbers = [1,1,2,2,3,3,4,4,10,10,10,10]
# doubled_numbers = []
# i = 0
# while i < len(numbers):
#     doubled_numbers.append(numbers[i]*2)
#     i += 1
# print(doubled_numbers)    

# # 8. Zlicz ilość wystąpień danej liczby w liście "numbers".
# print("9-=-"*10)
# numbers = [1,1,2,2,3,3,4,4,10,10,10,10]
# i = 0
# inp = float(input("-"))
# ile = 0
# while i < len(numbers):
#     if numbers[i] == inp:
#         ile += 1
#     i += 1
# print(ile)

# # 9. Wyświetl wszystkie liczby z listy "numbers" z ich indeksami.
# print("9-=-"*10)
# numbers = [1,1,2,2,3,3,4,4,10,10,10,10]
# i = 0
# while i < len(numbers):
#     print(f"{i} {numbers[i]}")
#     i += 1