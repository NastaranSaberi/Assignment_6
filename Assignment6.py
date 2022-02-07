from pyfiglet import figlet_format
import qrcode
from termcolor import colored


def add_product():
    new_product = {}
    n= int(input('How many products do you want to add?'))
    for i in range (n):
        new_product['id'] = input('Please enter new product id :') 
        new_product['name'] = input('Please enter new product name :') 
        new_product['price'] = input('Please enter new product price :')
        new_product['count'] = input('Please enter new product count :') 
        PRODUCTS.append(new_product)
        
    show_new_list()



def Edit_product():
    show_list()
    edit_name = input('Enter the name of the product you want to edit:')
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name'] == edit_name :
            choice_edit = int(input(' 1-edit id \n 2-edit name \n 3-edit price \n 4-edit count \n Please choose a number: '))
            if choice_edit == 1:
                PRODUCTS[i]['id'] = input('enter new id:')
            elif choice_edit == 2:
                PRODUCTS[i]['name'] = input('enter new name:')
            elif choice_edit == 3:
                PRODUCTS[i]['price'] = input('enter new price:')
            elif choice_edit == 4:
                PRODUCTS[i]['count'] = input('enter new count:')
    
            show_new_list()



def Delete_product():
    show_list()
    delete_name = input('Enter the product name you want to delete:')
    for i in range (len(PRODUCTS)):
        if PRODUCTS[i]['name'] == delete_name :
            del PRODUCTS[i]
            break

    show_new_list()



def Search_product():
    search_name = input('Enter the product name you want to search:')
    for i in range(len(PRODUCTS)):
        if search_name == PRODUCTS[i]['name']:
            print(PRODUCTS[i])
    store()


shopping_list = []

def buy():
    f = False
    Total_price=0
    while True:
        buy_id = input('Please enter the product id you want :')
        for i in range(len(PRODUCTS)):
            if buy_id == PRODUCTS[i]['id']:
                f = True
                number_product = int(input('How many of the product do you want?'))
                if int(PRODUCTS[i]['count'] )>= number_product:
                    PRODUCTS[i]['count'] = int(PRODUCTS[i]['count']) - number_product
                    shopping_list.append({'id':PRODUCTS[i]['name'],
                                        'name':PRODUCTS[i]['name'],
                                        'price':PRODUCTS[i]['price'],
                                        'cont':number_product})
                    Total_price  += (int(PRODUCTS[i]["price"]) * number_product)
                    print(colored('Your purchase was successful','green'))
                    print(shopping_list,'\n','Total price:',Total_price)
                    purchasing_process()
                    break 
                elif int(PRODUCTS[i]['count']) < number_product:
                    print(colored('Sorry!\nThis number of product is Currently not available in the store.','red'))
                    purchasing_process()
                    break
        if f == False:
            print(colored('sorry!\nThis product is currently not available in the store.','red'))
            purchasing_process()
            


def purchasing_process():
    choice_buy = int(input("Do you want another product ? (1-Yes 2-No)"))
    if choice_buy == 1:
        buy()
    elif choice_buy == 2:
        store()



def qr_code():
    qrcode_id = input('Please enter the product id you want creat Qr code :')
    f=0
    for i in range(len(PRODUCTS)):
        if qrcode_id == PRODUCTS[i]['id']:
            img = qrcode.make(PRODUCTS[i]['id'])
            img.save('qrcode.png')
            print(colored('The code was created','green'))
            f=1
    if f == 0:
        print(colored('There is no product with this id.','red'))
    store()



def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])




def exit_shopping():
    new_products = ''
    for i in range(len(PRODUCTS)):
        if i == len(PRODUCTS)-1:
            new_product   = PRODUCTS[i]['id'] + ',' + PRODUCTS[i]['name'] + ',' + PRODUCTS[i]['price'] + ',' + PRODUCTS[i]['count'] 
        else:
            new_product  = PRODUCTS[i]['id'] + ',' + PRODUCTS[i]['name'] + ',' + PRODUCTS[i]['price'] + ',' + PRODUCTS[i]['count'] + '\n'
        new_products += new_product 
    file = open('database.txt' , 'w')
    file.write(new_products)
    exit()




def show_list_1():
    show_list()
    store()



def show_new_list():
    print(colored('Your request was successful.','green'))
    choice_show =int(input('Do you want to see the new list? (1-Yes 2-No)'))
    if choice_show == 1:
        show_list()
        store()
    elif choice_show == 2:
        store()



def load():
    myfile = open('database.txt','r')
    date = myfile.read()
    product_list = date.split('\n')

    for i in range(len(product_list)):
        product_info = product_list[i].split(',')
        mydict = {}
        mydict['id'] = product_info[0]
        mydict['name'] = product_info[1]
        mydict['price'] = product_info[2] 
        mydict['count'] = product_info[3]
        PRODUCTS.append(mydict)

PRODUCTS = []

load()




def show_menu():
    print('1-Add Product')
    print('2-Edit Product')
    print('3-Delete Product')
    print('4-Search')
    print('5-Show List')
    print('6-Buy')
    print('7-Qr Code')
    print('8-Exit')
    


    

def store():
    print((colored(figlet_format("Nastaran Stor"), color="magenta")))
    show_menu()
    choice = int(input('\nPlease choose a number: '))

    if choice == 1:
        add_product()
    elif choice == 2:
        Edit_product()
    elif choice == 3:
        Delete_product()
    elif choice == 4:
            Search_product()
    elif choice == 5:
        show_list_1()
    elif choice == 6:
        buy()
    elif choice == 7:
        qr_code()
    elif choice == 8:
        exit_shopping()

store()

   




