# Method 1
groceryList = {}
num = 0
while True:
    x = input('Item: ').capitalize().strip()
    if x in groceryList:
        groceryList[x] += 1
    else:
        groceryList[x] = 1
    
    y = input('Do you want to continue?: ')
    if y != 'yes':
        break
    
print('Grocery List')
for items, quantity in groceryList.items():
    num += 1
    print(f'Number: {num} {items} Quantity: {quantity}')
    
    """
    Method 2
    groceryList = []
num = 0

while True:
    x = input('Item: ').capitalize().strip()
    groceryList.append(x)
    
    y = input('Do you want to continue?: ')
    if y.lower() != 'yes':
        break

print('Grocery List')
for item in set(groceryList):
    num += 1
    quantity = groceryList.count(item)
    print(f'Number: {num} Item: {item} Quantity: {quantity}')

    """
        