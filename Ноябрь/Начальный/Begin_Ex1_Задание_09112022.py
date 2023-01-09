# Известны оценки студента по 10 предметам первого 
# курса. Они вводятся по одному на строку. Определите
# средний балл студента по всем предметам

# входные данные    |    выходные данные
# 4                 |    4.4000
# 5
# 3
# 5
# 4
# 3
# 5
# 5
# 5
# 5

#git remote set-url origin https://volpol503:AcsessToken@github.com/volpol503/repository.git

# Список оценок

numbers = [4, 5, 3, 5, 4, 3, 5, 5, 5,5]

# Переменная, в которой хранится сумма
sum = 0

# Итерация цикла
for value in numbers:
    sum += value

print("Сумма равна", sum/10)

# Альтернативное решение через цикл for i in fange(10)

summ = 0

for i in range (10):
  t = int(input())
  summ += t
print(summ/10)