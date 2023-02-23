import gspread, datetime
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# GOOGLE DOC / SHEETS CONNECTION

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

cli = gspread.authorize(creds) 

sheet = cli.open("G-Recorder").sheet1  # Open the spreadhseet

row = sheet.row_values(1)

col = sheet.col_values(1)

col2 = sheet.col_values(1)

numRows = sheet.row_count  # Get the number of rows in the sheet
#####################################################################################################################################
colorama_init()

name = f"""

░██████╗░░░░░░░██████╗░███████╗░█████╗░░█████╗░██████╗░██████╗░███████╗██████╗░
██╔════╝░░░░░░░██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░██╗░█████╗██████╔╝█████╗░░██║░░╚═╝██║░░██║██████╔╝██║░░██║█████╗░░██████╔╝
██║░░╚██╗╚════╝██╔══██╗██╔══╝░░██║░░██╗██║░░██║██╔══██╗██║░░██║██╔══╝░░██╔══██╗
╚██████╔╝░░░░░░██║░░██║███████╗╚█████╔╝╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║
░╚═════╝░░░░░░░╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
|
|
|
{Fore.GREEN}When you're ready to logout. Type "logout" as the customer name.{Style.RESET_ALL}
_____________________________________________________________________________________________
"""

print(f"{Fore.GREEN}{name}{Style.RESET_ALL}")

# define the header row and write it to the worksheet
header_row = ['CUSTOMER NAME', 'CUSTOMER EMAIL', 'CUSTOMER PHONE #', 'PRODUCT', 'QUANTITY', 'PRICE']
sheet.append_row(header_row)
time = (f'{datetime.datetime.utcnow()}')

# loop to record orders
while True:
    # get input from the user
    cxname = input('Enter Customers Name: ')
    if cxname == 'logout':
        break
    else:
        email = input('Enter Customers Email: ')
        number = int(input('Enter Customers Phone #: '))
        product = input('Enter Product Name / ID: ')
        quantity = int(input('Enter Product Quantity: '))
        price = float(input('Enter Total Price: '))
    
    # write the data to the worksheet
    row = [cxname, email, number, product, quantity, price, time]
    sheet.append_row(row)
    
    print(f'{Fore.GREEN}Order recorded successfully!{Style.RESET_ALL}\n')

print(f'{Fore.RED}Recording orders is finished.{Style.RESET_ALL}')