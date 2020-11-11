import json
# 1

# f = open(file = '/home/user/class8.txt', mode = 'r+')
# suma = 0
# n = 0
# for i in f:
#     g = int(i[len(i)-2])
#     suma += g
#     n += 1
#     if g < 3:
#         print(i[:-1])
# print('Средний балл: %.2f' % (suma/n))


# 2

# fname = input('Файл: ')
# f = open(fname,'w+')
# while True:
#     s = input()
#     if s == '': break
#     f.write(s+'\n')
# f.close()



# 3

# f = open('/home/user/Рабочий стол/text2.txt')
# line = 0
# for i in f:
#     line += 1
 
#     flag = 0
#     word = 0
#     for j in i:
#         if j != ' ' and flag == 0:
#             word += 1
#             flag = 1
#         elif j == ' ':
#             flag = 0
 
#     print(i,len(i),'симв.',word,'сл.')
 
# print(line,'стр.')
# f.close()


# 4
# num = [1 ,2 ,3 ,4 ,5 , 6, 7, 8, 9 ]

# with open ("/home/user/nums.txt", "r+") as file:
#     file.writelines(str(sum(num)))
#     print(file)

# 5


# Fin = open ( "/home/user/input.txt" , 'a+') 
# str = Fin.readline().split()
# x = int(str[0])
# y = int(str[1])
# print(x+y)

# 6
# with open('input.txt', 'r') as f:
#     mass = []
#     full_f = f.read()
#     for i in full_f.split():
#         mass.append(int(i))
# with open('output.txt', 'w') as fs:
#     print(max(mass), file=fs)
#     print(min(mass), file=fs)

# 7
	

# with open('/home/user/sort.txt') as t:
#     nums = t.read().splitlines()
#     hm =[]
#     for i in list(sorted(nums)):
#         ok = sum(map(int,i))
#         hm.append(ok)
 
# with open('/home/user/sorted.txt', 'w') as w:
#     print(sorted(hm), file=w)

#  8) Распаковать json файл и получить значение у ключа “age”
# x = '{"name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print('value key -', y["age"])


# 9

# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# y = json.dumps(x)
# print(y)