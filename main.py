import random

import none as none
import null as null
import re


# 1.
# binary = random.randint(1, 6)
# print(binary)

# 2.
# counter = 0
# for i in range(5):
#     counter = counter + 1
#     binary = random.randint(1, 6)
#     print(counter, ". wurf:")
#     print(binary)
#
# counter = 0
# for i in range(5):
#     counter = counter + 1
#     binary = random.randint(1, 6)
#     print(counter, ". wurf:")
#     print(binary)
#

# 3.
# string = ""
# while string != "n":
#     string = input("Wie oft soll ich würfeln?\n")
#     num = int(string)
#     counter = 0
#     while (counter < num) and (counter < 30):
#         counter = counter + 1
#         binary = random.randint(1, 6)
#         print(counter, ". wurf:")
#         print(binary)
#     string = input("Wie oft soll ich würfeln?\n")
# print("Tschüss")


# 4. Ada
# name = input("Hallo, was ist dein Name?")
# alter = int(input(name + ", ist ein sehr schöner Name. Wie alt bist du eigentlich?"))
# if alter < 18:
#     print("So jung")
# if alter > 18:
#     print("So alt")
# frage = input("Bist du beindruckt wie Intelligent ich bin? (ja/nein)")
# if frage == "ja":
#     print("Dankeschön")
# if frage == "nein":
#     print("):")
#
# frage = ""
# while frage != "tschüs":
#     frage = input("Frag mich was du wilst: ")
#     if None != re.search("alt", frage):
#         print("Ich bin 21 Jahre alt.")
#     if None != re.search("name", frage) or None != re.search("heißt", frage):
#         print("Ich heiße Ada")
#
# print("Tschüs")



# 5. Zahlenraten
# guess = null
# secret_num = random.randint(1, 100)
# count = 0
# limit = 6
# while guess != secret_num and count < limit:
#     count = count + 1
#     guess = int(input("Rate: "))
#
#     if guess < secret_num:
#         print("Zu niedrig, du Landratte!")
#     if guess > secret_num:
#         print("Zu hoch!")
#
# if guess == secret_num:
#     print(str(secret_num) + ", ist richtig!")
# else:
#     print("Game over")
