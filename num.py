#產生隨機數1 ~ 100
#讓使用者'重複'猜數字
#猜對即終止
#猜錯要告訴使用者比數自大/小

import random
start = input('請輸入隨機數字的開始值')
end = input('請輸入隨機數字的結束值')
start = int(start)
end = int(end)

count = 0
r = random.randint(start ,end)
while True:
	count = count + 1 #快寫法: "count += 1"
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('恭喜猜中了!!')
		print('這是你猜的第', count,'次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count,'次')
