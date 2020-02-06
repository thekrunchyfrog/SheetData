import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('toysCred.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Toy Inventory')
worksheet = sheet.worksheet('GI JOE')

telemedicine = worksheet.get_all_records()
print(telemedicine)
