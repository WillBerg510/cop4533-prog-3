import random

k = input("Input k (number of letters in alphabet): ")
while (not k.isdigit()) or int(k) < 1:
  k = input("k must be an integer of at least 1.\nInput k (number of letters in alphabet): ")
k = int(k)

length = input("Input length of string: ")
while (not length.isdigit()) or int(length) < 1:
  length = input("Length must be an integer of at least 1.\nInput length of string: ")
length = int(length)

file_name = input("Input file name without extension: ")

with open(f"../data/{file_name}.in", "w") as file:
  file.write(f"{k}\n")
  for i in range(0, k):
    file.write(f"{chr(97 + i)} {random.randint(0, 30)}\n")
  string = ""
  for i in range(0, 2):
    string = ""
    for j in range(0, length):
      string += chr(97 + random.randint(0, k - 1))
    file.write(string)
    if (i == 0):
      file.write("\n")