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
print(products[0])  #存取二維
print(products[0][1])

for p in products:
	print(p[0], '的價格是', p[1])

