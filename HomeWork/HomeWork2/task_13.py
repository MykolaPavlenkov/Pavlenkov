#В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то
#же время, было решено выделить кабинет для каждого класса и купить в них новые парты. За каждой партой может сидеть
#не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт
#чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из
#трех классов.

i1 =int(input('введите количество учеников в класе №1 '))
i2 =int(input('введите количество учеников в класе №2 '))
i3 =int(input('введите количество учеников в класе №3 '))
p1=(i1//2)+(i2//2)+(i3//2)
print("чтобы всем ученикам хватило нужно закупить парт:", p1)