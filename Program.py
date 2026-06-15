menu={'Pizza':250, 'Pasta':180, 'Drinks':50}
order={'Pizza': 10, 'Pasta' : 2}






# #1] Add items in the menu
def add_item():
    item_name=input('Enter the new item name to be add in menu :')
    item_price=int(input(f'Enter the price of {item_name} :'))
    menu[item_name]=item_price
    print(menu)






# #2] display all items in the menu 
def display():
    print('Item Name  | (Rs.) Price ')
    for name,price in menu.items():
        print(f'{name}      |  {price}')






# 3] Place an order for customer
def orders():
    order={}
    check=True
    for name, price in menu.items():
        print(name,price)

    while check is True:

        i=input('Enter the item name : ')
        if i in menu:
              q=int(input(f'Enter the quantity you need for {i} :'))
              if i not in order:
                  order[i]=q
              else:
                  order[i]+=q
              print('Item added successfully...')
        else:
            print('Item not availabe!!!')      

        c=input('Do you want to continue (Y/N) : ').lower()
        if c == 'n':
            check = False        
    print(order)

    




#4] remove item from order
def del_item():
    name=input('Enter the item name to remove from order : ')
    if name in order:
        del order[name]
        print('Item removed successfully...')
        
    else:
        print('Item not found!!!')





#5] order summery
def summery():
    print('.Order Summary.')
    if not order:
        print('Not ordered anything...')
    else:
        for name, quantity in order.items():
            print(f'{name}  : {quantity}')
        print(f'Total item : {len(order)}')





#6] Generting the final bill
def Gen_bill():
    if not order:
        print('No bill !!!')
    else:
        sum=0
        for name , quantity in order.items():
                    sum= sum+ (menu[name]*quantity)
                    print(f'{name} : {menu[name]}  :  {quantity}  --> Rs.{menu[name]*quantity}')
        print(f'Total Bill : Rs.{sum}')




while True:
    print('='*40)
    print('\t\tMenu')
    print('='*40)
    print('1. View Menu')
    print('2. Add Item to Menu')
    print('3. Place an order for customer')
    print('4. Remove item from order')
    print('5. Order Summery')
    print('6. Generate Bill')
    print('7. Exit')

    choice=int(input('Enter the choice : '))

    if choice == 1:
        
        display()
    elif choice == 2:
        print()
        add_item()
    elif choice == 3:
        print()
        orders()
    elif choice == 4:
        print()
        del_item()
    elif choice == 5:
        print()
        summery()
    elif choice == 6 :
        print()
        Gen_bill()
    elif choice == 7:
        print('ThankYou...')
        print()
        break
      
