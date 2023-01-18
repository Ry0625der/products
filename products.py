#記帳程式專案
products = []
while True :
	name = input('請輸入商品名稱(結束按q): ')
	if name == 'q' :
		break
	price = input('請輸入商品價格: ')
	p = [name, price]
	products.append(p)
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:  #副檔名.csv 可換成.txt檔
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')


