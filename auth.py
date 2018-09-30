from utils import clear
import webbrowser
#import authserver

auth_link = "https://cloud.digitalocean.com/v1/oauth/authorize?client_id=88e7abf72a6444bd4da54a860b3f827cd44379a25aad922673d08855fc286ba6&redirect_uri=http://127.0.0.1:8080/callback&response_type=code"

def get_oauth():
    clear()
    print("API access to the digitalocean api is required for this program to work.")
    user_choice = str.lower(input("Would you like to be redirected to your browser to give this program api access?(Y/N)"))

    if user_choice == "y":
        webbrowser.open(auth_link)
    else:
        clear()
        print("API access is required for this program to work please select (Y) to grant access")