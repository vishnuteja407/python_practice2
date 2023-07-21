# import tkinter as tk
# from tkinter import messagebox

# def validate_login():
#     username = entry_username.get()
#     password = entry_password.get()
    
#     # Check if username and password are valid
#     if username == "admin" and password == "password":
#         messagebox.showinfo("Login", "Login successful!")
#     else:
#         messagebox.showerror("Login", "Invalid username or password")

# # Create the main window
# window = tk.Tk()
# window.title("DNAC Details Screen")
# window.geometry('340x240')
# window.configure(background='white')

# # Create and pack the username label and entry field
# label_ip = tk.Label(window, text="IP Address:")
# label_ip.pack(fill="both", expand=True)
# entry_ip = tk.Entry(window)
# entry_ip.pack(fill="both", expand=True)

# # Create and pack the username label and entry field
# label_username = tk.Label(window, text="Username:")
# label_username.pack()
# entry_username = tk.Entry(window)
# entry_username.pack()

# # Create and pack the password label and entry field
# label_password = tk.Label(window, text="Password:")
# label_password.pack()
# entry_password = tk.Entry(window, show="*")
# entry_password.pack()

# # Create and pack the login button
# button_login = tk.Button(window, text="Submit")
# button_login.pack()

# # Run the main window's event loop
# window.mainloop()

import requests
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from requests.auth import HTTPBasicAuth
import getpass
import base64

ca_bundle_path = "/Users/vibodapa/Library/Python/3.9/lib/python/site-packages/certifi/cacert.pem"

# from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable SSL certificate verification
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ip_address = input("Enter DNAC IP address::::::  ")
username = input("Enter DNAC username::: ")
password = getpass.getpass("Enter DNAC password:::::")

# Encoding Baisc Auth
userpass = f'{username}:{password}'
encoded_auth = base64.b64encode(userpass.encode()).decode()
print(encoded_auth)

base_url = f"https://{ip_address}/dna/intent/api/v1"
print(base_url)

#Login API
header = {"Authorization": "Basic "+ encoded_auth, "Content-Type": "application/json"}
print(header)
response = requests.post(base_url+"/auth/token", headers=header, verify=False)
print(response.status_code)
print(response.text)

