from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path=r'C:\Users\sociu\Desktop\geckodriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        login_a = driver.find_element_by_xpath(
            "//a[@href='/accounts/login/?source=auth_switcher']")
        login_a.click()
        time.sleep(5)
        username_login = driver.find_element_by_xpath(
            "//input[@name='username']")
        username_login.clear()
        time.sleep(2)
        username_login.send_keys(self.username)
        password_login = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_login.clear()
        time.sleep(2)
        password_login.send_keys(self.password)
        password_login.send_keys(Keys.RETURN)
        time.sleep(5)
        self.deixar_de_seguir()

    def deixar_de_seguir(self):
        driver = self.driver
        driver.get('https://www.instagram.com/' + self.username + '/')
        time.sleep(3)
        href_following = driver.find_elements_by_xpath(
            "//a[@href='/" + self.username + "/following/']")
        href_following[0].click()
        time.sleep(2)
        #Verificação e contador de usuarios#
        arrow_down = driver.find_element_by_xpath("//div[@class='PZuss']")
        action = ActionChains(self.driver)
        action.double_click(arrow_down).perform()
        for i in range(5):
            action.send_keys(Keys.ARROW_DOWN).perform()
        button_following = driver.find_elements_by_xpath(
            "//button[contains(text(), 'Following')]")
        for button in range(len(button_following)):
            time.sleep(30)
            button_following[button].click()
            time.sleep(30)
            button_unfollow = driver.find_element_by_xpath(
                "//button[contains(text(), 'Unfollow')]")
            button_unfollow.click()


fire = Instagram('', '')
fire.login()
