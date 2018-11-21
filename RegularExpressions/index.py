import re
File_Name = input('Enter File Name ')
if len(File_Name) < 1: File_Name = 'sample.txt'
handle = open(File_Name)
list = []
for line in handle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+',line)
    for index,num in enumerate(numbers):
        numbers[index] = float(num)
    if len(numbers) > 0:
        list.append(sum(numbers))
print(sum(list))
