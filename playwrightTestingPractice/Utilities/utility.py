import json

with open("../Testdata/registerdetails.json") as file:
    user_data = json.load(file)
    userdetails = user_data["User_details_enter_create_account"]
    print(userdetails)

with open("../Testdata/logindetails.json") as file1:
    user_login=json.load(file1)
    user_credentials = user_login["user_login_details"]
    print(user_credentials)