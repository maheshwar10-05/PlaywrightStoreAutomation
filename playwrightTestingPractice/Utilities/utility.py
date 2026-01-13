import json
import os

# 1. Get the directory where utility.py is located
current_dir = os.path.dirname(__file__)

# 2. Construct the path to the JSON file dynamically
# This goes up one level from 'Utilities' then into 'Testdata'
json_path = os.path.join(current_dir, "..", "Testdata", "registerdetails.json")

# 3. Open the file using the dynamic path
with open(json_path) as file:
    # ... your existing code ...
    user_login2=json.load(file)
    user_credentials2 = user_login2["user_details"]
    print(user_credentials2)

with open("../Testdata/registerdetails.json") as file:
    user_data = json.load(file)
    userdetails = user_data["User_details_enter_create_account"]
    print(userdetails)

with open("../Testdata/logindetails.json") as file1:
    user_login=json.load(file1)
    user_credentials = user_login["user_login_details"]
    print(user_credentials)

with open("../Testdata/logindetails2.json") as file2:
    user_login2=json.load(file2)
    user_credentials2 = user_login2["user_details"]
    print(user_credentials2)