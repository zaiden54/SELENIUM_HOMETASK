import codecs
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe")



def main():
    try:
        driver.get("https://www.wildberries.ru/")
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        goods_arr = driver.find_elements(By.CLASS_NAME, "goods__item")
        # goods_str = ''
        goods_dict = {}

        for good in goods_arr:

            good_title = good.find_elements(By.CSS_SELECTOR, ".goods-card__description span")[1].text
            good_link = good.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            good_price = good.find_element(By.CSS_SELECTOR, '.goods-card__price ins').text
            
            # goods_str = goods_str + f'{good_title} --- {good_price} --- {good_link}\n'

            good_dict = {}

            good_dict['good_price'] = good_price
            good_dict['good_link'] = good_link

            goods_dict[f'{good_title}'] = good_dict  

        driver.close()

        # with codecs.open("parseRes.txt", "w", "utf-16") as stream:   # or utf-8
        #     stream.write(goods_str)

        with open('parseRes.json', 'w', encoding='utf-8') as fp:
            json.dump(goods_dict, fp, indent=4, ensure_ascii=False)

    except Exception as ex:
        print("An error occured: \n" + str(ex))
        driver.close()


main()