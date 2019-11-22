from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime


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
        self.verifica_box()

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

    def seguir_like(self):
        driver = self.driver
        time.sleep(2)
        search_input = driver.find_element_by_xpath(
            "//input[@placeholder='Search']")
        search_input.clear()
        time.sleep(2)
        search_input.send_keys('programadoresdepre')
        time.sleep(2)
        span = driver.find_element_by_xpath("//span[@class='Ap253']")
        span.click()
        time.sleep(2)
        photos = driver.find_elements_by_xpath(
            "//div[@class='v1Nh3 kIKUG  _bz0w']")
        photos[0].click()
        time.sleep(2)
        timer = driver.find_element_by_xpath("//time[@class='_1o9PC Nzb55']")
        timer_text = timer.get_attribute('datetime')
        timer_ano = timer_text[0:4]
        timer_mes = timer_text[5:7]
        timer_dia = timer_text[8:10]
        timer_hora = timer_text[11:13]
        timer_minuto = timer_text[14:16]
        date_now = datetime.now()
        date_ano = str(date_now)[0:4]
        date_mes = str(date_now)[5:7]
        date_dia = str(date_now)[8:10]
        date_hora = str(date_now)[11:13]
        date_minuto = str(date_now)[14:16]
        time_sum = int(timer_hora*60)+int(timer_minuto)
        date_sum = int(date_hora*60)+int(date_minuto)
        total = time_sum-date_sum
        print(t)

    def verifica_box(self):
        driver = self.driver
        time.sleep(3)
        box = driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]")
        box.click()
        self.seguir_like()


fire = Instagram('_rogerio.junior', 'rogerio0089')
fire.login()
