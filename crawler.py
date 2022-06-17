import pychrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from datetime import datetime

def configure():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    executable_path = os.path.join(script_dir, "chromedriver")
    options = webdriver.ChromeOptions()
    options.add_argument("--remote-debugging-port=8000")
    driver = webdriver.Chrome(executable_path=executable_path, chrome_options=options)
    dev_tools = pychrome.Browser(url="http://localhost:8000")
    tab = dev_tools.list_tab()[0]
    return driver, tab


def response_received(requestId, loaderId, timestamp, type, response, frameId, hasExtraInfo):
    if type == 'XHR' and "search" in response["url"]:
        response_body = tab.Network.getResponseBody(requestId=requestId)
        body_data = response_body['body']
        file_name = str(int(datetime.now().timestamp()))
        with open("data/"+file_name+".json","w") as jfile:
            jfile.write(body_data)

def crawl(driver, tab):
    while True:
        try:
            tab.wait(10)
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            tab.wait(5)
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/div[4]/div/div/div[4]/div/button").click()
        except Exception as e:
            print(str(e))
            break

if __name__ == "__main__":
    driver, tab = configure()
    tab.Network.responseReceived = response_received
    tab.start()
    tab.Network.enable()
    driver.get("https://food.grab.com/sg/en/restaurants")
    crawl(driver, tab)
