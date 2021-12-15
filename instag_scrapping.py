import os
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

class instabot(webdriver.Chrome):
    def __init__(self, driver_path, user_url):
        self.chrome_configs=webdriver.ChromeOptions()
        self.chrome_configs.add_experimental_option("excludeSwitches",["enable-logging"])
        self.chrome_configs.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        self.chrome_configs.add_argument("--headless")
        self.chrome_configs.add_argument("--disable-dev-shm-usage")
        self.chrome_configs.add_argument("--no-sandbox")
        super().__init__(os.environ.get(driver_path),options=self.chrome_configs)
        self.get(f"https://www.instagram.com/{user_url}/")
        self.implicitly_wait(20)

    def get_userdata(self):
        users={}
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
        
        users.update({self.username:[follow_list,about_user.text]})
        return users