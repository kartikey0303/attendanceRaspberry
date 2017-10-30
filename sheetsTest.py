import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials


GDOCS_OAUTH_JSON = 'raspberryTest.json'

GDOCS_SPREADSHEET_NAME = 'PythonTest'

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name(GDOCS_OAUTH_JSON, scope)
print 'received'

gc = gspread.authorize(credentials)

wks = gc.open(GDOCS_SPREADSHEET_NAME).sheet1

value = wks.acell('A2').value
print value

