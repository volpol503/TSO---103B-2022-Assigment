#13. Оценка
#Условие: Дано целое число k. Выведите строку-описание оценки по
#пятибалльной шкале, соответствующей числу k. Если k не лежит в диапазоне
#от 1 до 5, то требуется вывести сообщение об ошибке.

#Формат выходных данных: Требуется вывести «very poor» (плохо), 
#«less than satisfactory» (неудовлетворительно), 
#«satisfactory» (удовлетворительно),
#«good» (хорошо), «excellent» (отлично) или 
#«error» (ошибка) в зависимости от значения k

n = int(input())
if n == 1:
   print('very poor')
elif n == 2:
   print('less than satisfactory') 
elif n == 3:
   print('satisfactory')
elif n == 4:
   print ('good') 
elif n == 5:
   print('excellen') 
else:
   print('error')
