item_name1 = input('Enter item name: ')
item_price1 = float(input('Enter item cost: '))

item_name2 = input('Enter item name: ')
item_price2 = float(input('Enter item cost: '))

item_name3 = input('Enter item name: ')
item_price3 = float(input('Enter item cost: '))

item_name4 = input('Enter item name: ')
item_price4 = float(input('Enter item cost: '))

item_name5 = input('Enter item name: ')
item_price5 = float(input('Enter item cost: '))

Subtotal = (item_price1 + item_price2 + item_price3 + item_price4 + item_price5)
print('Subtotal = $', Subtotal)

SalesTax = (Subtotal * 0.07)
print('Sales tax = $', round(SalesTax, 2))

Total = (round(Subtotal + SalesTax, 2))
print('Total = $', Total)
