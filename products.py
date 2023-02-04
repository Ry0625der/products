#記帳程式專案
#確認檔案是否存在
import os # operating system

	
#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return(products)	


#輸入商品名稱價格
def user_input(products):
	while True :
		name = input('請輸入商品名稱(結束按q): ')
		if name == 'q' :
			break
		price = input('請輸入商品價格: ')
		prine= int(price)
		products.append([name, price])
	return(products)

#印出購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:  #副檔名.csv 可換成.txt檔
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	if os.path.isfile('products.csv'):
		print('Yes')
		products = read_file('products.csv')
	else:
		print('No')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products) 
main()