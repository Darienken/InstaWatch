import instag_scrapping as instag
import instag_interface as instag_inter
import pandas as pd
from tkinter import Tk

def get_username_data(username):
    
    instagram=instag.instabot("driver/chromedriver.exe",username)
    users=instagram.get_userdata()
    try:
        user_data_xlsx=pd.read_excel("user_data.xlsx")
        
        for user in users:
            follows_list=users.get(user)[0]
            user_data_xlsx=user_data_xlsx.append({
            "Username":user,
            "Publications":follows_list[0],
            "Followers":follows_list[1],
            "Follows":follows_list[2],
            "About User":users.get(user)[1]
            }, ignore_index=True)
        
        user_data_xlsx.to_excel("user_data.xlsx")
    
    except FileNotFoundError:
        user_data_xlsx=pd.DataFrame(columns=["Username","Publications","Followers","Follows","About User"])

        for user in users:    
            follows_list=users.get(user)[0]
            user_data_xlsx=user_data_xlsx.append({
            "Username":user,
            "Publications":follows_list[0],
            "Followers":follows_list[1],
            "Follows":follows_list[2],
            "About User":users.get(user)[1]
            }, ignore_index=True)
                
        user_data_xlsx.to_excel("user_data.xlsx")
    
    #with open("user_data.txt","a",encoding="utf-8") as user_txt:
        
            #datas=f"""
#Instagram User = {user}\n
#Publications = {follows_list[0]}\n
#Followers = {follows_list[1]}\n
#Follows = {follows_list[2]}\n
#About User = {users.get(user)[1]}
            #"""
        
        #user_txt.write(datas)

def get_users_by_list():
    users_xlsx=pd.read_excel("users.xlsx")
    tries=False
    rows=0
    while tries == False:
        rows+=1
        try:
            users_list=users_xlsx["Users"]
            tries=True
        except:
            users_xlsx=pd.read_excel("users.xlsx",skiprows=rows)
            tries=False
    
    try:
        user_data_xlsx=pd.read_excel("user_data.xlsx")
        
        for user in users_list:
            instagram=instag.instabot("driver/chromedriver.exe",user)
            user_dict=instagram.get_userdata()      
            
            follows_list=user_dict.get(user)[0]
                
            user_data_xlsx=user_data_xlsx.append({
            "Username":user,
            "Publications":follows_list[0],
            "Followers":follows_list[1],
            "Follows":follows_list[2],
            "About User":user_dict.get(user)[1]
            }, ignore_index=True)
                
        user_data_xlsx.to_excel("user_data.xlsx")

    except FileNotFoundError:
        user_data_xlsx=pd.DataFrame(columns=["Username","Publications","Followers","Follows","About User"])
        
        for user in users_list:
            instagram=instag.instabot("driver/chromedriver.exe",user)
            user_dict=instagram.get_userdata()      
            
            follows_list=user_dict.get(user)[0]
                
            user_data_xlsx=user_data_xlsx.append({
            "Username":user,
            "Publications":follows_list[0],
            "Followers":follows_list[1],
            "Follows":follows_list[2],
            "About User":user_dict.get(user)[1]
            }, ignore_index=True)
                
        user_data_xlsx.to_excel("user_data.xlsx")
        
        #for user in user_dict:
            #follows_list=user_dict.get(user)[0]
            #datas=f"""
#Instagram User = {user}\n
#Publications = {follows_list[0]}\n
#Followers = {follows_list[1]}\n
#Follows = {follows_list[2]}\n
#About User = {user_dict.get(user)[1]}
            #"""
            #with open("user_data.txt","a",encoding="utf-8") as user_txt:
                #user_txt.write(datas)



if __name__ == "__main__":
    app=Tk()
    app.geometry("1000x1000")
    instag_inter.interface(app).pack()
    app.mainloop()
    
