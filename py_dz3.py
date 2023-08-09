#Задача 1 

input1 = set('2 4 6 8 10 12 10 8 6 4 2'.split())
input2 = '3 6 9 12 15 18'

output = []

for i in input2.split():
    if i in input1 and i not in output:
        output.append(int(i))

output.sort()
output = ' '.join(str(i) for i in output)

print(output if output else 'Числа не повторяються')

# Задача 2 

input1 = 1, 2, 3, 4, 5, 6, 7, 8
maxk = (0, 0)

for i in range(len(input1) - 1):
    summ = input1[i] + input1[i-1] + input1[i+1]
    if summ > maxk[0]:
        maxk = summ, i+1

print(f'Макс. кол-во ягод {maxk[0]}, собрано для куста {maxk[1]}')