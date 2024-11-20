# Menu for the cafe
veg_menu = {
    'idli': 40,
    'plain_dosa': 50,
    'masala_dosa': 70, 
    'puri': 80, 
    'veg_fried_rice': 100, 
    'paneer_butter_masala': 150
}

non_veg_menu = {
    'chicken_biryani': 220, 
    'egg_dosa': 80,
    'chicken_fried_rice': 120,
    'fish_curry': 200, 
    'mutton_curry': 250
}

print('Veg Menu:\n', veg_menu)
print('Non-Veg Menu:\n', non_veg_menu)

veg_total = 0
non_veg_total = 0
order_details = []
menu_choice = input('What do you want to order, veg or non-veg ')

if menu_choice == 'non_veg':
    order_item = input('Enter your non-veg item: ')
    quantity=int(input('enter many quantity u want:'))
    if order_item in non_veg_menu:
        item_cost=non_veg_menu[order_item]*quantity
        non_veg_total += item_cost
        order_details.append({'item':order_item,'quantity':quantity,'cost':item_cost})
        print(f'First order added: {order_item} (quantity: {quantity}, Cost: {item_cost})')
    else:
        print('Sorry, we do not have', order_item, 'available.')

elif menu_choice == 'veg':
    order_item = input('Enter your veg item: ')
    quantity=int(input('enter many quantity u want:'))
    if order_item in veg_menu:
       item_cost=veg_menu[order_item]*quantity
       veg_total += item_cost
       order_details.append({'item':order_item,'quantity':quantity,'cost':item_cost})
       print(f'First order added: {order_item} (quantity: {quantity}, Cost: {item_cost})')
    else:
        print('Sorry, we do not have', order_item, 'available.')

else:
    print("Invalid choice. Please start again and choose 'veg' or 'non-veg'.")
    exit()

# Continue ordering process
while True:
    additional_order = input('Would you like to order more items? (yes or no): ')
    if additional_order == 'yes':
        next_item = input("Enter the item you'd like to add: ")
        quantity=int(input('enter many quantity u want:'))
        if menu_choice == 'non_veg' and next_item in non_veg_menu:
           item_cost=non_veg_menu[order_item]*quantity
           non_veg_total += item_cost
           order_details.append({'item':next_item,'quantity':quantity,'cost':item_cost})
           print(f'First order added: {next_item} (quantity: {quantity}, Cost: {item_cost})')
        elif menu_choice == 'veg' and next_item in veg_menu:
             item_cost=veg_menu[next_item]*quantity
             veg_total += item_cost
             order_details.append({'item':next_item,'quantity':quantity,'cost':item_cost})
             print(f'First order added: {next_item} (quantity: {quantity}, Cost: {item_cost})')
        else:
            print('Sorry, we do not have', next_item, 'available.')
    elif additional_order == 'no':
        print("Order complete.")
        break
    else:
        print("Invalid response. Please answer with 'yes' or 'no'.")

print("\n===== Final Bill =====")

final_total = 0
for order in order_details:
    print(f"{order['item']} (Quantity: {order['quantity']}) - Cost: {order['cost']}")
    final_total += order['cost']
print(f"Total Bill Amount: {final_total}")
print("Thank you! Please visit again.")
