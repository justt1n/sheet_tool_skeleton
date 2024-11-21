from oauth2client.service_account import ServiceAccountCredentials
import gspread


class GSheet():

    def __init__(self, keypath="key.json"):
        self.client = self.get_gspread(keypath)


    def get_gspread(self, keypath="key.json"):
        scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(keypath, scope)
        client = gspread.authorize(creds)
        return client
    
    def get_sheet(self, sheet_name):
        return self.client.open(sheet_name)

    def read_sheet_data(self, sheet_name):
        sheet = self.get_sheet(sheet_name)
        return sheet.sheet1.get_all_values()

