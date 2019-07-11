from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def chrome():
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])##去掉selenium的标识header
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver