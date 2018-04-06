from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import xlwt
import time

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('ignore-certificate-errors')
options.add_argument("test-type")
options.add_argument("no-sandbox")
options.add_argument("disable-gpu")
options.binary_location = "/usr/bin/chromium-browser"
browser = webdriver.Chrome(options=options)
browser.set_page_load_timeout(120)
browser.set_script_timeout(120)

wkbook = xlwt.Workbook()
sheet = wkbook.add_sheet("sheet 1")
xlsFileName = "/usr/src/app/test.xls"

try:
    browser.get("http://www.dianping.com/shoplist/search/8_10_0_score")
    count = 0
    while (True):
        elements = WebDriverWait(driver=browser, timeout=120).until(
            lambda x: x.find_elements(By.CSS_SELECTOR,
                                      "body > div.main_w > div.content_e > div.content-ranklist > section > table > tbody > tr")
        )
        for element in elements:
            try:
                element.find_element(By.CLASS_NAME, "td-div-shopName")
            except Exception:
                continue
            print(element.find_element(By.CLASS_NAME, "td-div-shopName").text)
            print(element.find_element(By.CLASS_NAME, "td-div-avgPrice").text)
            sheet.write(count, 0, element.find_element(By.CLASS_NAME, "td-div-shopName").text)
            sheet.write(count, 1, element.find_element(By.CLASS_NAME, "td-div-avgPrice").text)
            count = count + 1
        wkbook.save(xlsFileName)
        time.sleep(2)
        try:
            browser.find_element(By.CSS_SELECTOR,
                                 "body > div.main_w > div.content_e > div.content-ranklist > div.panel-wrap > div > a.next").click()
            print("next page")
        except Exception:
            print("last page")
            break
        time.sleep(2)

finally:
    wkbook.save(xlsFileName)
    browser.close()
