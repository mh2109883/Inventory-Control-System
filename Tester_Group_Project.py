#GROUP4
import os
EXIT_MENU =9

def main():
    try:
        os.system('cls') # Clears the screen. for Mac, use os.system('clear')
        while True:#for displying menu
            display_menu()
            choice = int(input("Enter a choice: "))
            if choice == 1:
                addItem()
            elif choice == 2:
                code = int(input('Enter the code of the asset to update: '))
                update_item(code)
            elif choice == 3:
                code = int(input('Enter the code of the asset to be removed: '))
                remove_item(code)
            elif choice == 4:   
                display_inventory()
            elif choice ==5:
                display_reorder_list()
            elif choice == 6:
                parts_above_given_price()
            elif choice == 7:
                parts_above_average_p()
            elif choice == 8:
                stock_statistics()
            elif choice== EXIT_MENU:
                print("Thanks for using the Inventory Control System\nGood Bye")
                break
            else:
                print('Please enter a value choice')
    except Exception as e:
        print("\n---------------------------------")
        print("*** System Crashed ****")
        print("---------------------------------")
        print("Problem : ",e)
        print("---------------------------------")
        print("*** Please Try Again ****")
        
def addItem():
    input_file = open('inventory.csv','r')#to open a file in read mode
    headers=input_file.readline()#read the header and it is neccery to avoid string data.
    for line in input_file.readlines():#reading all data.
        code_str,others = line.split(',',1)#getting code number for the last item.
    input_file.close()
    partNo = int(code_str) + 1   
    print("Stock Control - Add Item:")
    print("=========================")
    car_make =input("Enter the car make: ")
    car_model = input("Enter the car model: ")
    part_name=input("Enter part name: ")
    price = float(input('Enter price: '))
    quantity = int(input("Enter quantity: "))
    new_asset = f'{partNo},{part_name},{car_make},{car_model},{quantity},{price}\n'
    wanna_save= input("Save (Y/N): ")
    if wanna_save=="Y" or "y":
        inventory = open('inventory.csv','a')
        inventory.write(new_asset)
        inventory.close()
        print(".....Record saved.")

def update_item(partNo):
    input_file = open('inventory.csv','r')
    headers = input_file.readline()
    temp_file = open('temp.csv','w')#creating the temporary file to update the existing data.
    temp_file.write(headers)
    for asset in input_file.readlines():#to reade the data from the original file.
        code,name,make,model,quantity,value = asset.split(',')
        if partNo == int(code): #
            print("Asset details: ")
            display_header()
            display(asset)#displaying the detail of the assest to be edited. 
            quantity = int(quantity)
            value = float(value)
            new_quantity = int(input(f'Current qunatity is {quantity}. Enter quantity to add or subtract: '))
            if new_quantity<0 and (quantity+new_quantity<0):#for checking whether the input is negative and the current quantity is greater than the input.
              print("Not Enough Item in the inventory")
            else:
              quantity = quantity+new_quantity
              new_value = float(input(f'Current price is {value}. Enter new price or -1 to leave unchanged: '))
            if new_value>0:
                value = new_value
            updated_asset = f'{partNo},{name},{make},{model},{quantity},{value}\n'
            temp_file.write(updated_asset)
        else:
            temp_file.write(asset)
    temp_file.close()
    input_file.close()
    os.remove('inventory.csv')#deleting original file 
    os.rename('temp.csv', 'inventory.csv')#renaming as now  temp is original file .
    input('\nPress Enter to return')  

def remove_item(partNo):
    input_file = open('inventory.csv','r')
    headers = input_file.readline()
    temp_file = open('temp.csv','w')
    temp_file.write(headers)
    for asset in input_file.readlines():
        code,name,make,model,quantity,value = asset.split(',')
        if partNo != int(code):
            updated_asset = f'{code},{name},{make},{model},{quantity},{value}'
            temp_file.write(updated_asset)
    temp_file.close()
    input_file.close()
    os.remove('inventory.csv')# deleting original file 
    os.rename('temp.csv', 'inventory.csv')#renaming as now  temp is original file .
    input('\nPress Enter to return')

def display_header():
    input_file = open('inventory.csv','r')
    header = input_file.readline()#it is sequence reader
    input_file.close()
    header1, header2, header3, header4, header5, header6 = header.strip('\n').split(',')
    print(f'{header1:11s}{header2:22s}{header3:15s}{header4:9s}{header5:10s}{header6}')

def display(the_asset):#the input for this function is complete line.
    code_str,name, type,model,quantity_str,value_str=the_asset.split(',')
    code = int(code_str)
    quantity = int(quantity_str)
    value = float(value_str)
    print(f'{code:>3d}    {name:23s}  {type:14s} {model:10s} {quantity:6d} {value:10,.2f}')

def display_inventory():
    infile = open('inventory.csv','r')
    for line in infile:
        data = line.rstrip('\n')
        data = data.split(',')
        print(f'{data[0]:<8s}{data[1]:<25s}{data[2]:<12s}{data[3]:<14s}{data[4]:<12s}{data[5]:<8s}')
    infile.close()

def display_reorder_list():
    print('Parts with Quantity less than 4')
    infile = open('inventory.csv', 'r')
    header = infile.readline()
    header = header.rstrip('\n')
    header = header.split(',')#converting header into the list
    print(f'{header[0]:<8s}{header[1]:<25s}{header[2]:<12s}{header[3]:<14s}{header[4]:<12s}{header[5]:<8s}')
    for line in infile:
        data = line.rstrip('\n')
        data = data.split(',')
        if int(data[4]) < 4:#checkin quntatity is less than 4 
            print(f'{data[0]:<8s}{data[1]:<25s}{data[2]:<12s}{data[3]:<14s}{data[4]:<12s}{data[5]:<8s}')
    infile.close()

def parts_above_given_price():
    P = float(input('Enter a price: '))
    infile = open('inventory.csv', 'r')
    header = infile.readline()
    header = header.rstrip('\n')
    header = header.split(',')
    print(f'{header[0]:<8s}{header[1]:<25s}{header[2]:<12s}{header[3]:<14s}{header[4]:<12s}{header[5]:<8s}')
    for line in infile:
        data = line.rstrip('\n')
        data = data.split(',')
        if float(data[5]) > P:#checking if the item price is greater than user entered price. 
            print(f'{data[0]:<8s}{data[1]:<25s}{data[2]:<12s}{data[3]:<14s}{data[4]:<12s}{data[5]:<8s}')
    infile.close()

def parts_above_average_p():
    infile = open('inventory.csv', 'r')
    header = infile.readline()
    header = header.rstrip('\n')
    header = header.split(',')
    Sum = 0
    count = 0
    for line in infile:
        data = line.rstrip('\n')
        data = data.split(',')
        Sum = Sum + float(data[5])#suming the price of all items.
        count = count + 1#suming the number of item
    infile.close()
    avg = Sum / count
    print('Tha Average Price is: ',avg)
    print('Parts Above Average: ')
    infile = open('inventory.csv', 'r')
    header = infile.readline()
    header = header.rstrip('\n')
    header = header.split(',')
    print(f'{header[0]:<8s}{header[1]:<8s}{header[2]:<8s}{header[3]:<8s}{header[4]:<14s}{header[5]:<8s}')
    for line in infile:
        data = line.rstrip('\n')
        data = data.split(',')
        if float(data[5]) > avg:
            print(f'{data[0]:<8s}{data[1]:<25s}{data[2]:<12s}{data[3]:<14s}{data[4]:<12s}{data[5]:<8s}')
    infile.close()

def stock_statistics():
    infile = open('inventory.csv', 'r')
    header = infile.readline()
    header = header.rstrip('\n')
    header = header.split(',')
    Sum = 0
    SumAll = 0
    count = 0
    price = []
    quan = []
    for line in infile:
        data = line.rstrip('\n')
        data = data.split(',')
        Sum = Sum + float(data[5])#suming all price of an item
        SumAll = SumAll + (float(data[5]) * int(data[4]))#suming (total price * quntatity) of every item.
        price.append(float(data[5]))
        quan.append(int(data[4]))
        count = count + 1
    infile.close()
    avg = Sum / count
    print('The current Value of Stock: ',SumAll)
    print('Tha Average Price is: ', avg)
    print('Most Expensive: ', max(price))#getting the max value from the price list 
    print('Least Expensive: ',min(price))#getting the min value from the price list
    print('Least Stock: ',min(quan))#getting the min value form the quan list
 
def display_menu():
    class color:
        BOLD = '\033[1m'
        END='\033[0m'
    menu="Inventory Control System "
    print(color.BOLD + menu + color.END)
    menu2= '''\t[1] Add part
    \t[2] Update part
    \t[3] Remove part
    \t[4] Display inventory
    \t[5] Display re-order list
    \t[6] Parts above a given price
    \t[7] Parts above the average price
    \t[8] Stock statistics
    \t[9] Exit'''
    print(menu2)

main()

