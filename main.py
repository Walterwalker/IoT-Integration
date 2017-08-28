# First step is data collection
# Lets start with collecting data from the smart band
# We have two options 1. Using MiFit App ( I am using Mi Band 2 reason being dead cheap and better customization ). 2.Google Fit Data


#this part of the code is for blocking websites

import time
#hosts_path="hosts.txt"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
redirect_v6="::1"
website_list=["www.facebook.com","facebook.com","fb.com","instagram.com","yt.com","yt.in","quora.com","youtube.com","https://www.quora.com"]
y=15

while True:
    if y<70:
        print("you need to concentrate more")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass   
                else:
                    file.write(redirect+" "+ website+"\n")
                    file.write(redirect_v6+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
            print("You can visit the websites, please keep the track of time...great going")
    time.sleep(5)
    
  

This part of the code is to scrape the productivity score from selenium web app
    
    def auto():
    driver=webdriver.Chrome('C:/Users/Owner/chromedriver.exe')
    driver.get('https://www.rescuetime.com/dashboard')
    driver.find_element_by_name("email").send_keys("wwalker@gmail.com")
    driver.find_element_by_name("password").send_keys("**************")
    driver.find_element_by_name("button").click()
    global a
    a=int(driver.find_element_by_class_name("score").text)
    driver.close()
    t = Timer(secs, auto)
    t.start()
    print(a)
auto()

issues found so far:
    
    streaming real time data and working on it
    mutli processing.
    IFTTT inetgration with weather underground is a bit easy but integration with automate app is really worst...should change it soon

