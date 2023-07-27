import os
from datetime import datetime
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Access the environment variables
username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# setting the options
options = webdriver.ChromeOptions()

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; Ubuntu 22.04) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0>"

options = webdriver.ChromeOptions()
options.add_argument('--display=:99')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--headless')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument(f'user-agent={USER_AGENT}')


class RentBot:
    """
    A class representing a rental property bot that automates searching and sending inquiries.

    Attributes:
        user_data (dict): A dictionary containing user-specific data such as 'full_name', 'your_email',
                          'your_phone', 'message', and 'params'.
        url (str): The URL of the website from which the bot will scrape rental property listings.
        max_price (int): The maximum price limit for the rental properties the bot will consider.

    Methods:
        __init__(self, user_data, url, max_price):
            Initializes the Rent_Bot object with the provided user_data, url, and max_price.
            It sets up the Selenium WebDriver for scraping.

        log_in(self, username, password):
            Logs into the website with the given username and password.
            This method is used to access specific features that require authentication.

        run_bot(self):
            Runs the bot to search for rental properties based on the user's preferences and sends inquiries.
            It navigates through the website, filters listings based on parameters in 'user_data', and sends inquiries
            for suitable properties. The bot tracks viewed links to avoid duplicate inquiries.
    """
    def __init__(self,user_data, url, max_price):
        self.user_data = user_data
        self.url = url
        self.max_price = max_price
        self.driver = webdriver.Chrome()
   
    def log_in(self,user_name, user_password):
        """
        log_in(self, username, password):
        Logs into the website with the given username and password.
        This method is used to access specific features that require authentication.
        """
        elem = self.driver.find_element(By.ID, 'username')
        elem.send_keys(user_name)
        password_elem = self.driver.find_element(By.ID, 'password')
        password_elem.send_keys(user_password)
        time.sleep(5)
        login_parent = self.driver.find_element(By.CLASS_NAME, 'login__cta-section')
        login_button = login_parent.find_element(By.TAG_NAME, 'input')
        login_button.click()

    def run_bot(self):
        """
        run_bot(self):
            Runs the bot to search for rental properties based on the user's preferences and sends inquiries.
            It navigates through the website, filters listings based on parameters in 'user_data', and sends inquiries
            for suitable properties. The bot tracks viewed links to avoid duplicate inquiries.
        """

        # fixed variables
        _new_hits = 0

        # start by getting the query URL
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)

        try:
            pop_up = self.driver.find_element(By.XPATH, '//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]')
            pop_up.click()
            
        except NoSuchElementException:
            print("There wasnt any pop up")

        # check if there are any new places that match my query
        trigger = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/div[1]/div/h1')

        if not trigger.text.startswith("0"): # if not 0 places

            print(trigger.text)
            
            parent_ul = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/ul')

            a = parent_ul.find_elements(By.TAG_NAME, 'a')

            # check my record to see if i already sent a message to the ad
            file_name = self.user_data["full_name"]
            file_name = file_name.replace(" ", "")

            if os.path.isfile(file_name+".txt"):
                with open(file_name+".txt", "r", encoding="utf-8") as file:
                    viewed_links = file.read()
            else:
                with open(file_name+".txt", "w+", encoding="utf-8") as file:
                    viewed_links = file.read()

            copy_a_href = [link.get_attribute("href") for link in a]

            first_iteration = True

            for url in copy_a_href:
                if url in viewed_links:
                    print("The URL was already hit")
                    continue

                copy_url = url
                self.driver.get(url)
                body = self.driver.find_element(By.TAG_NAME, 'body')
                body.send_keys(Keys.PAGE_DOWN)

                # Check a few parameters
                month_or_week = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/div[1]/div/div[2]/div[1]/h2')
                parameters = self.driver.find_elements(By.CLASS_NAME, 'styles__ListLabel-sc-15fxapi-10')

                today = datetime.now().date()

                for parameter in parameters:
                    value_text = parameter.find_element(By.XPATH, '..').text
                    split_str = value_text.split(": ")

                    if split_str[0] == "Available From":
                        days_difference = 0
                        if split_str[1] != "Immediately":
                            # Split the string and remove the comma and ordinal indicators
                            date_string = split_str[1].replace(',', '').replace('st', '').replace('nd', '').replace('rd', '').replace('th', '').replace(" ", "")
                            number_in_date = re.search(r'\d+', date_string)

                            if len(number_in_date.group()) <= 5:
                                date_string = date_string[
                                    :date_string.index(
                                    number_in_date.group())] +"0"+ date_string[
                                    date_string.index(number_in_date.group()
                                                      ):
                                    ]
                       
                            target_date = datetime.strptime(date_string, "%b%d%Y").date()
                            days_difference = (target_date - today).days

                    if (
                        self.user_data["params"][split_str[0]] != split_str[1]
                        or split_str[0] not in self.user_data["params"]["ignore"]
                        or self.user_data["params"]["Available From"] <= days_difference
                    ):
                        continue
                    
                if month_or_week.text.endswith("week"):
                    match = re.search(r'\d+', month_or_week.text)
                    price = int(match.group())
                    if price * 4 > self.max_price:
                        continue
                    else:
                        print(f"its {price * 4} per month")
                time.sleep(5)

                try:
                    login_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div[2]/div/div[1]/div[2]/div[2]/button')
                    login_button.click()

                except NoSuchElementException:
                    continue
                    
                #log in
                if first_iteration:
                    first_iteration = False

                    time.sleep(5)
                    self.log_in(user_name=username,user_password=password)
                    
                # fill in the form
                time.sleep(5)
                name = self.driver.find_element(By.ID, 'keyword1')
                name.send_keys(self.user_data['full_name'])
                email = self.driver.find_element(By.ID, 'keyword2')
                email.send_keys(self.user_data['your_email'])
                phone = self.driver.find_element(By.ID, 'keyword3')
                phone.send_keys(self.user_data['your_phone'])
                message = self.driver.find_element(By.ID, 'message')
                message.send_keys(self.user_data['message'])

                time.sleep(2)

                body = self.driver.find_element(By.TAG_NAME, 'body')
                body.send_keys(Keys.PAGE_DOWN)

                time.sleep(3)
                try:
                    submit_button = self.driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/form/div/div[5]/div/button')
                    submit_button.click()
                except NoSuchElementException:
                    print("It didnt find the send button by xpath")
                try:
                    parent = self.driver.find_element(By.XPATH, '//*[@id="contact-form-modal"]/div[2]/form/div/div[5]/div')
                    submit_button = parent.find_element(By.TAG_NAME, 'button')
                    submit_button.click()
                except NoSuchElementException:
                    print("It didnt find the send button from parent")

                file_name = self.user_data["full_name"]
                file_name = file_name.replace(" ", "")

                with open(file_name+".txt", "a",encoding="utf-8") as file:
                    file.write("{}\n".format(copy_url))

                time.sleep(3)
                try:
                    close_button = self.driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div[1]/button')
                    close_button.click()
                except NoSuchElementException:
                    print("It didnt find the close button from full xpath")
               

                _new_hits += 1
                time.sleep(3)
            print(_new_hits)
            self.driver.close()

        else:
            print("There are no new places")
            self.driver.close()



