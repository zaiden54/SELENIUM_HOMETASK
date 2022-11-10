from selenium import webdriver 
from selenium.webdriver.common.by import By
import codecs
import time

driver = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe")



def main():
    try:
        driver.get("https://www.wildberries.ru/")
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        goods_arr = driver.find_elements(By.CLASS_NAME, "goods__item")

        goods_str = ''

        for good in goods_arr:
            good_title = good.find_elements(By.CSS_SELECTOR, ".goods-card__description span")[1].text
            print(good_title)
            goods_str = goods_str + good_title + "\n"

        


        with codecs.open("parseRes.txt", "w", "utf-16") as stream:   # or utf-8
            stream.write(goods_str)

    except Exception as ex:
        print("An error occured: \n" + str(ex))


main()