#產生隨機數1 ~ 100
#讓使用者'重複'猜數字
#猜對即終止
#猜錯要告訴使用者比數自大/小

import random
r = random.randint(1 ,100)
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('恭喜猜中了!!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')