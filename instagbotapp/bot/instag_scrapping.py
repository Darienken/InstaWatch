from selenium import webdriver
import os
import re

class instabot(webdriver.Chrome):
    #__init__(username) recives username and loads the user page
    def __init__(self, user_url):
        driver_path=os.environ.get("CHROMEDRIVER_PATH")
        #setting configurations
        self.chrome_configs=webdriver.ChromeOptions()
        self.chrome_configs.add_experimental_option("excludeSwitches",["enable-logging"])
        self.chrome_configs.add_argument("--headless")
        self.chrome_configs.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        self.chrome_configs.add_argument("--disable-dev-shm-usage")
        self.chrome_configs.add_argument("--no-sandbox")
        #calling __init__ father and passing throught arguments the configurations and driver path
        super().__init__(driver_path,options=self.chrome_configs)
        #loading user page
        self.url=f"https://www.instagram.com/{user_url}/"
        self.get(self.url)
        #waiting time for each action performed
        self.implicitly_wait(10)

    def login(self):#login method
        #set username
        self.username_login=self.find_element_by_name("username")
        self.username_login.click()
        self.username_login.send_keys(os.environ.get("INSTA_USER"))
        #set passwrd
        self.passwrd_login=self.find_element_by_name("password")
        self.passwrd_login.click()
        self.passwrd_login.send_keys(os.environ.get("INSTA_PASS"))
        #login!
        self.btn_login=self.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div")
        self.btn_login.click()

    def get_userdata(self):#method to get data from users 
        users={}
        try:
            container_descript=self.find_element_by_class_name("wW3k-")
            self.username_container=container_descript.find_element_by_class_name("XBGH5")
            self.username = self.username_container.find_element_by_tag_name(
                "h2"
            ).get_attribute("innerHTML")
            followers_container=container_descript.find_element_by_class_name("k9GMp")
            followers_list=followers_container.find_elements_by_class_name("g47SY")
            follow_list=[]
            for follower in followers_list:
                follow_list.append(follower.get_attribute("innerHTML"))

            about_user=container_descript.find_element_by_class_name("QGPIr")

            phone_number=self.get_phonenumber(about_user.text)
            users.update({self.username:[follow_list,about_user.text,phone_number]})
        except:
            self.login()
            if self.find_element_by_class_name("olLwo").get_attribute("innerHTML") == "Save Your Login Info?" or self.find_element_by_class_name("olLwo").get_attribute("innerHTML") == "¿Guardar tu información de inicio de sesión?":
                self.get(self.url)
            container_descript=self.find_element_by_class_name("wW3k-")
            self.username_container=container_descript.find_element_by_class_name("XBGH5")
            self.username = self.username_container.find_element_by_tag_name(
                "h2"
            ).get_attribute("innerHTML")

            followers_container=container_descript.find_element_by_class_name("k9GMp")
            followers_list=followers_container.find_elements_by_class_name("g47SY")
            follow_list=[]
            for follower in followers_list:
                follow_list.append(follower.get_attribute("innerHTML"))

            about_user=container_descript.find_element_by_class_name("QGPIr")

            phone_number=self.get_phonenumber(about_user.text)
            users.update({self.username:[follow_list,about_user.text,phone_number]})
        return users
    
    def get_phonenumber(self, text):#method to get phone number
        phone_pattern=re.compile(r"((\+593|593)? \d{2} \d{3} \d{4}|(\+593|593)?\d{7,10})")
        phone_number=phone_pattern.finditer(text)
        phone_numbers=""
        for number in phone_number:
            phone_numbers+=f"{number.group()} - "
        return phone_numbers
