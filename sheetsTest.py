import gspread
from oauth2client.service_account import ServiceAccountCredentials


def searchRFID(name, wks):
    '''returns the RFID of the person whose name is given'''
    print wks.row_count
    for k in range(2, wks.row_count):
        row = wks.row_values(k)[0:3]
        if row[0] == name:
            return row[2]


def searchName(rfid):
    '''returns the name of person whose RFID is given'''


GDOCS_OAUTH_JSON = 'raspberryTest.json'

GDOCS_SPREADSHEET_NAME = 'PythonTest'

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name(GDOCS_OAUTH_JSON, scope)
print 'received'

gc = gspread.authorize(credentials)

wks = gc.open(GDOCS_SPREADSHEET_NAME).sheet1

name  = [item for item in wks.col_values(1) if item]

for item in name:
    print item

RFID = searchRFID("Kartikey", wks)
print RFID
#value = wks.acell('A2').value
#print value

