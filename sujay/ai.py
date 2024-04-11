from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pathlib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


warnings.simplefilter("ignore")
url = "https://pi.ai/talk"
scriptDirectory = pathlib.Path().absolute()
chrome_driver_path = 'chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)

def setup():
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[2]/button')))
    # Click the button
    button.click()

    button1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div/div/div/div/div[1]/button[2]')))
    # Click the button
    button1.click()

    text_area = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="m_login_email"]')))

    # Enter text into the text area
    text_area.send_keys("9563902229")

    text_area1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="m_login_password"]')))

    #Enter text into the text area
    text_area1.send_keys("sujay12e")

    button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_password_step_element"]/button')))
    # Click the button
    button2.click()


    button4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button')))
    # Click the button
    button4.click()

    text_area2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea')))
    #Enter text into the text area
    text_area2.send_keys("hey")
    button3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/button')))
    # Click the button
    button3.click()


def command(query):

    text_area2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea')))
    #Enter text into the text area
    text_area2.send_keys(query)

    button3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/button')))
    # Click the button
    button3.click()

def voice1():
    a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button[2]')))
    a.click()
    b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[1]/button[1]')))
    b.click()
    a.click()
def voice2():
    a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button[2]')))
    a.click()
    b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[1]/button[2]')))
    b.click()
    a.click()
def voice3():
    a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button[2]')))
    a.click()
    b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[1]/button[3]')))
    b.click()
    a.click()
def voice4():
    a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button[2]')))
    a.click()
    b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[1]/button[4]')))
    b.click()
    a.click()
def voice5():
    a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button[2]')))
    a.click()
    b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[1]/button[5]')))
    b.click()
    a.click()
def voice6():
    a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button[2]')))
    a.click()
    b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[1]/button[6]')))
    b.click()
    a.click()
def voice7():
    a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button[2]')))
    a.click()
    b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[1]/button[7]')))
    b.click()
    a.click()
def voice8():
    a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button[2]')))
    a.click()
    b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[1]/button[8]')))
    b.click()
    a.click()


