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
    
def getAccount():
    accounts = []
     while True:
         username = input("Enter username: ").strip().capitalize()
         if username not in accounts:
            accounts.append(username)
            print(f"{username} Account Created")
            conC = input("Do you want to continue? ").lower()
            if conC != yes:
                print("Account list:")
                for x in accounts:
                    print(f"Name: "):
                    break
        else:
            print(f"Is already on the list")
            break
class Person():
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        print("Account Created")
        
    def accountInformation(self):
        print(f"Fullname: {firstname} {lastname}")
        print("Age: ")
        print("Gender: ") 
    

        
