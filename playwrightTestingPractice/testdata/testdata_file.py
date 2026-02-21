import openpyxl

categories_list=['Featured', 'Latest Products', 'Bestsellers', 'Specials', 'Brands Scrolling List']
currency_list=['US Dollar','Euro','Pound Sterling']
search_keywords=["Makeup"]

incorrect_login_details={"username":"yestreday","password":"yesterday#23"}

login_correct_incorrect_password={"username":"qualityengineerrole1239","password":"9estuser@1234"}
incorrect_login_correct_password={"username":"yesterday","password":"Testuser@1234"}
login_correct_empty_password={"username":"yesterday","password":""}
empty_login_correct_password={"username":"","password":"Testuser@1234"}
empty_login_empty_password={"username":"","password":""}
class Data:
    
    def data_login_details(self):
        file_path="C:/Users/86885/Testing/PlaywrightAutomationstore/playwrightTestingPractice/testdata/username_password_various_combinations.xlsx"
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        usernames = [cell.value for cell in sheet['A'] if cell.row > 1]
        passwords=[cell.value for cell in sheet['B'] if cell.row > 1 ]
        # Inside your Data class or where list1 is create

        # WRONG (Current): list1 = [{"user": [...]}, {"pass": [...]}]
        # RIGHT (Fixed): list1 = [{"user": "u1", "pass": "p1"}, {"user": "u2", "pass": "p2"}]

        list1 = []
        for u, p in zip(usernames, passwords):
                list1.append({"user": u, "pass": p})
        print(list1)
                
        return list1
    
    def forgot_login_details(self):
        file_path="C:/Users/86885/Testing/PlaywrightAutomationstore/playwrightTestingPractice/testdata/forgot_login_details_lastname_email_combinations.xlsx"
        workbook=openpyxl.load_workbook(file_path)
        sheet=workbook.active
        last_name=[cell.value for cell in sheet['A'] if cell.row >1 ]
        email_add=[cell.value for cell in sheet['B'] if cell.row>1]
        forgot_list=[]
        for l,e in zip(last_name,email_add):
            forgot_list.append({"last_name":l,"email":e})
        print(forgot_list)
        return forgot_list
            
            
            

                    
                
