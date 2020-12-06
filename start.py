from selenium import webdriver
from time import sleep

profile = webdriver.FirefoxProfile()
profile.set_preference("permissions.default.image", 2)
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('https://www.instagram.com')

def loginUSERPASS(rootusername,rootpassword):
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys(rootusername)
    password_input.send_keys(rootpassword)
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep(2)
    cookies = browser.get_cookies()
    print(cookies)
    for cookie in cookies:
        browser.add_cookie(cookie)
def loginCOOKIE(cookies):
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.refresh()
def followUsername(username):
    browser.get('https://www.instagram.com/' + username + '/')
    if browser.title == "Page Not Found • Instagram" or browser.title=='Content Unavailable • Instagram':
        print("404-ERROR " + browser.title)
    else:
        status=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]").text
        if status.startswith(username)==True:
            if status.endswith('Follow')==True:
                if status.split()[1]=="Verified":
                    follow_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button")
                else:
                    follow_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button") 
                follow_button.click()
                print('U ARE FOLLOWING @'+username)
                return 0
            elif status.endswith('Requested')==True:
                print('U ARE REQUESTED @'+username)
                return 1
            elif status.endswith('Message')==True:
                print("U ARE FOLLOWED @"+username)
                return 2
#loginUSERPASS('USERNAME', 'PASSWORD')
#loginCOOKIE()
#followUsername('apple')
browser.close()
