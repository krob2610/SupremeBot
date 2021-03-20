import requests
import bs4
import time
import os, sys


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SupremeBot:
    def __init__(self, **info):
        self.base = "https://www.supremenewyork.com"
        self.shop_ext = "/shop/all/"
        self.checkout_ext = "/checkout/"
        self.info = info

    def init_browser(self):

        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ['enable-automation'])

        options.add_argument(f"--user-data-dir={self.info['User_Profile']}")
        if getattr(sys, 'frozen', False):
            chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            self.b = webdriver.Chrome(chromedriver_path, chrome_options=options)
        else:
            self.b = webdriver.Chrome(chrome_options=options)
        self.b.get("https://www.supremenewyork.com/shop/all")

    def find_product(self, number):
        try:
            r  = requests.get("{}{}{}".format(self.base, self.shop_ext, self.info["category"][number])).text

            soup = bs4.BeautifulSoup(r, 'lxml')

            temp_tuple = []
            temp_link = []

            for link in soup.find_all("a", href=True):
                temp_tuple.append((link["href"], link.text))
            if self.info["color"][number]:
                for i in temp_tuple:
                    if i[1] == self.info["product"][number] or i[1] ==self.info["color"][number]:
                        temp_link.append(i[0])
                self.final_link = list(set([x for x in temp_link if temp_link.count(x)==2]))[0]
            else:
                 for i in temp_tuple:
                    if i[1] == self.info["product"][number] or i[1] ==self.info["color"][number]:
                        self.final_link = i[0]
                        break
            return True
        except:
            return False
    def visit_site(self,number):
        wait = WebDriverWait(self.b, 10)

        self.b.get("{}{}".format(self.base, str(self.final_link)))
        if self.info["size"][number]:
            element = wait.until(EC.presence_of_element_located((By.ID, "size")))
            select_size = Select(element)
            select_size.select_by_visible_text(self.info["size"][number])

        wait.until(EC.element_to_be_clickable((By.NAME, "commit"))).click()
    def checkout_fun(self, deley):

        self.b.get("https://www.supremenewyork.com/checkout")
        wait = WebDriverWait(self.b, 10)
        wait.until(EC.element_to_be_clickable((By.NAME, "order[billing_name]"))).send_keys(self.info["fullname"])
        wait.until(EC.element_to_be_clickable((By.NAME,"order[email]"))).send_keys(self.info["email"])
        wait.until(EC.element_to_be_clickable((By.NAME, "order[tel]"))).send_keys(self.info["tel"])
        wait.until(EC.element_to_be_clickable((By.NAME,"order[billing_address]"))).send_keys(self.info["address"])
        wait.until(EC.element_to_be_clickable((By.NAME,"order[billing_city]"))).send_keys(self.info["city"])
        wait.until(EC.element_to_be_clickable((By.NAME,"order[billing_zip]"))).send_keys(self.info["zip"])
        wait.until(EC.element_to_be_clickable((By.NAME,"credit_card[cnb]"))).send_keys(self.info["number"])
        wait.until(EC.element_to_be_clickable((By.NAME,"credit_card[ovv]"))).send_keys(self.info["ccv"])



        element =wait.until(EC.presence_of_element_located((By.ID, "order_billing_country")))
        select_country = Select(element)
        select_country.select_by_visible_text(self.info["country"])

        element =wait.until(EC.presence_of_element_located((By.ID, "credit_card_month")))
        select_month = Select(element)
        select_month.select_by_value(self.info["month"])



        element =wait.until(EC.presence_of_element_located((By.ID, "credit_card_year")))
        select_year = Select(element)
        select_year.select_by_visible_text( self.info["year"])


        wait.until(EC.element_to_be_clickable((By.XPATH , "//*[@class='has-checkbox terms']"))).click()
        time.sleep(deley)
        wait.until(EC.element_to_be_clickable((By.NAME,"commit"))).click()

