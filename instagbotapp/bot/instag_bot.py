from . import instag_scrapping as instag
import pandas as pd

def get_username_data(username):#function to get data from usernames
    #instantiated class(it loads the page)
    instagram=instag.instabot(username)
    
    #method called(it obtains user data and returns a dictionary)
    users=instagram.get_userdata()
    #iter over dictionary
    for user in users:
        #Set information in a dictionary
        follows_list=users.get(user)[0]
        userdata={"Username":user,
        "Publications":follows_list[0],
        "Followers":follows_list[1],
        "Follows":follows_list[2],
        "AboutUser":users.get(user)[1],
        "PhoneNumber":users.get(user)[2]
        }
    return userdata


def get_users_by_list(users_arg):#function to get data from excel list
    
    users_xlsx=pd.read_excel(users_arg)
    tries=False
    rows=0
    while tries == False:
        rows+=1
        try:
            users_list=users_xlsx["users"]
            tries=True
        except:
            users_xlsx=pd.read_excel(users_arg,skiprows=rows)
            tries=False

    user_data_xlsx=pd.DataFrame(columns=["Username","Publications","Followers","Follows","About User"])
        
    for user in users_list:
        instagram=instag.instabot(user)
        user_dict=instagram.get_userdata()      
            
        follows_list=user_dict.get(user)[0]
                
        user_data_xlsx=user_data_xlsx.append({
        "Username":user,
        "Publications":follows_list[0],
        "Followers":follows_list[1],
        "Follows":follows_list[2],
        "About User":user_dict.get(user)[1],
        "Phone Number":user_dict.get(user)[2]
        }, ignore_index=True)
    user_data_xlsx.to_excel(r"instagbotapp/static/instagbotapp/excel_files/user_data.xlsx")
    
    return {"verifications":True}