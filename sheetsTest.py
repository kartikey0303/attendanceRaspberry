import gspread
from oauth2client.service_account import ServiceAccountCredentials


def searchRFID(name, wks):
    '''returns the RFID of the person whose name is given'''
    for k in range(2, wks.row_count):
        row = wks.row_values(k)[0:3]
        if row[0] == name:
            return row[2]


def searchName(rfid, wks):
    '''returns the name of person whose RFID is given'''
    for k in range(2, wks.row_count):
        row = wks.row_values(k)[0:3]
        if row[2] == rfid:
            return row[0]

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
Name = searchName("test", wks)
print RFID
print Name
#value = wks.acell('A2').value
#print value

