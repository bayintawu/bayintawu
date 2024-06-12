import gspread
from google.oauth2.service_account import Credentials

# Define the scope and credentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Define the credentials
creds = Credentials.from_service_account_file('credentials.json', scopes=scope)

# Authorize gspread
client = gspread.authorize(creds)

# Open the Google Sheets document
sheet = client.open('sample data').worksheet("orders")

new_order = ["000002", "Jelo", "Dan", "I love you too!", "Song1<>Singer1:::Song2<>Singer2"]
sheet.append_row(new_order)



cells = sheet.get_all_values()
for cell in cells:
    print(cell)
# # Create
# new_row = ['value1', 'value2', 'value3']
# sheet.append_row(new_row)

# # Read
# data = sheet.get_all_records()
# print(data)

# # Update
# cell = sheet.find('value1')
# sheet.update_cell(cell.row, cell.col, 'new_value1')

# # Delete
# cell = sheet.find('value2')
# sheet.delete_row(cell.row)
