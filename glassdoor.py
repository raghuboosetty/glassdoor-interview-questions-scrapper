import ipdb,time,sys,json,os
# from selenium import webdriver
import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from urllib.parse import urlparse
from getpass import getpass
# from config import Config

CHROMEDRIVER_PATH = "/opt/homebrew/bin/chromedriver"
# CHROMEDRIVER_PATH = "chromedriver_mac_arm64/chromedriver"
# CHROMEDRIVER_PATH = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"

class Glassdoor:
  def __init__(self, url):
    self.url = url
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    service = ChromeService(executable_path=CHROMEDRIVER_PATH)
    self.driver = webdriver.Chrome(service=service, options=options)
    self.wait = WebDriverWait(self.driver, 10)
    
  def saveCookies(self):
    # Get and store cookies after login
    cookies = self.driver.get_cookies()

    # Store cookies in a file
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)
    print('New Cookies saved successfully')

  def loadCookies(self):
    # Check if cookies file exists
    if 'cookies.json' in os.listdir():

      # Load cookies to a vaiable from a file
      with open('cookies.json', 'r') as file:
        cookies = json.load(file)
        
      # Set stored cookies to maintain the session
      for cookie in cookies:
        self.driver.add_cookie(cookie)
    else:
      print('No cookies file found')
      
    self.driver.refresh() # Refresh Browser after login
    
  def run(self):
    self.driver.maximize_window()
    self.driver.get(self.url)
    self.loadCookies()
    

    # clicking google to manually signin
    time.sleep(5)
    button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='SignInButton']")))
    button.click()
    
    time.sleep(1)
    button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='googleBtn']")))
    button.click()
    time.sleep(60)
    
    time.sleep(100)
    self.saveCookies()
    
    questions = self.driver.find_elements(By.CSS_SELECTOR, "p[class='interview-details__interview-details-module__textStyle']")
    if len(questions) == 0:
      questions = self.driver.find_elements(By.CSS_SELECTOR, "span[class='mb-sm']")
      
    # questions = self.driver.find_elements(By.CSS_SELECTOR, "div[data-test='question-container']")
    # self.driver.find_elements(By.CSS_SELECTOR, "span")
    # ipdb.set_trace()
    
    for question in questions:
      print(question.text())

    # Close the browser
    self.driver.quit()


print("Please share Glassdoor interview review page URL:")
url = str(input())

glassdoor = Glassdoor(url)
# ipdb.set_trace()
glassdoor.run()