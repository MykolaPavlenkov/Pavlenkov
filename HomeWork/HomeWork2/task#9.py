# '''' n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому
# школьнику? Сколько яблок останется в корзинке? Программа получает на вход числа `n` и `k` и должна вывести искомое
# количество яблок (два числа).
p = int(input('Введите с клавиатуры количество школьников: '))
a = int(input('Введите с клавиатуры количество яблок: '))
s = a//p
print("В результате каждому школьнику достанется целых", s , "яблок(а) ")
s = a%p
print("А также в корзине останется", s, "яблок (а)")