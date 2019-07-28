# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере
# #(пробелы важны!). Первая строка содержит следующее значение, а втора строка содержит предыдущее значение введёного
# #числа
# #        Please enter an integer number: 1234
# #        The next number for the number 1234 is 1235.
# #        The previous number for the number 1234 is 1233.
# #     or
# #        Please enter an integer number: 0
# #        The next number for the number 0 is 1.
# #        The previous number for the number 0 is -1.

i=int(input('Please enter an integer number '))
ip1= i+1
im1 = i-1
print('Please enter an integer number:',str(i))
print('The next number for the number',str(i), 'is', str(ip1))
print('The previous number for the number', str(i), 'is', str(im1))