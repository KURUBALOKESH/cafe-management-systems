# Menu for the cafe
veg_menu = {'pasta': 40, 'pizza': 40, 'burger': 60, 'coffee': 80, 'cooldrink': 20}
non_veg_menu = {'chicken_roast': 80, 'mamaos': 70, 'briyani': 200, 'fish': 120}

print('Veg Menu:\n', veg_menu)
print('Non-Veg Menu:\n', non_veg_menu)

veg_total = 0
non_veg_total = 0


menu_choice = input('What do you want to order, veg or non-veg? ').strip().lower()

if menu_choice == 'non_veg':
    order_item = input('Enter your non-veg item: ').strip().lower()
    if order_item in non_veg_menu:
        print('First order added:', order_item)
        non_veg_total += non_veg_menu[order_item]
    else:
        print('Sorry, we do not have', order_item, 'available.')
        
elif menu_choice == 'veg':
    order_item = input('Enter your veg item: ').strip().lower()
    if order_item in veg_menu:
        print('Your order has been placed:', order_item)
        veg_total += veg_menu[order_item]
    else:
        print('Sorry, we do not have', order_item, 'available.')

while True:
    additional_order = input('Would you like to order more items? (yes or no): ').strip().lower()
    if additional_order == 'yes':
        next_item = input("Enter the item you'd like to add: ").strip().lower()
        if next_item in non_veg_menu:
            print('Order added:', next_item)
            non_veg_total += non_veg_menu[next_item]
        elif next_item in veg_menu:
            print('Order added:', next_item)
            veg_total += veg_menu[next_item]
        else:
            print('Sorry, we do not have', next_item, 'available.')
    elif additional_order == 'no':
        print("Order complete.")
        break
    else:
        print("Invalid response. Please answer with 'yes' or 'no'.")

if menu_choice == 'veg':
    print(f'Total cost of veg items: {veg_total}\nThank you! Please visit again.')
else:
    print(f'Total cost of non-veg items: {non_veg_total}\nThank you! Please visit again.')
