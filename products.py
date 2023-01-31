#記帳程式專案
#確認檔案是否存在
import os # operating system
products = []
if os.path.isfile('products.csv'):
	print('Yes')
#讀取檔案
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)	
else:
	print('No')

#輸入商品名稱價格
while True :
	name = input('請輸入商品名稱(結束按q): ')
	if name == 'q' :
		break
	price = input('請輸入商品價格: ')
	prine= int(price)
	products.append([name, price])
print(products)

#印出購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:  #副檔名.csv 可換成.txt檔
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

