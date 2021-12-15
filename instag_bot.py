import instag_scrapping as instag
import instag_interface as instag_inter
from tkinter import Tk

def get_username_data(username):
    
    instagram=instag.instabot("CHROMEDRIVER_PATH",username)
    
    with open("user_data.txt","a",encoding="utf-8") as user_txt:
        users=instagram.get_userdata()
        for user in users:
            follows_list=users.get(user)[0]
            
            datas=f"""
Instagram User = {user}\n
Publications = {follows_list[0]}\n
Followers = {follows_list[1]}\n
Follows = {follows_list[2]}\n
About User = {users.get(user)[1]}
            """
        
        user_txt.write(f"{datas}")


if __name__ == "__main__":
    app=Tk()
    app.geometry("1000x1000")
    instag_inter.interface(app).pack()
    app.mainloop()
    
