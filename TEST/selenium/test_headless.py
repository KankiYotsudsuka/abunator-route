# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:11:57 2020

@author: School
"""


#ヘッドレス（画面に出さない）でテストを行う

from selenium.webdriver import Chrome, ChromeOptions
import time

#driver = webdriver.Chrome("C:/Users/School/Desktop/test/abunator/abunator/test/chromedriver.exe")

options = ChromeOptions()
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
options.add_argument('--headless')
# ChromeのWebDriverオブジェクトを作成する。
driver = Chrome(options=options)

#abunatorを起動
driver.get("https://abunatorroute.azurewebsites.net/")

#タイトルの確認
assert 'abunator' in driver.title

#タイトルが表示されるまでまつ
time.sleep(3)

#スクショをとる
driver.save_screenshot('chrome_abunator_start.png')

#start.click
start=driver.find_element_by_class_name("start")
start.click()

#質問画面は[はい]だけ選択
#nameを参照すると「はい」以外も選択してクリックできる?
#no = driver.find_element_by_name('いいえ')

#Xpathの場合
#driver.findElement(By.xpath("//input[@value='はい']")).click();

#forで質問の絞りこみがおわるまで、breakでぬけるといいのか

no = driver.find_element_by_class_name("button")
no.click()

no = driver.find_element_by_class_name("button")
no.click()

no = driver.find_element_by_class_name("button")
no.click()

no = driver.find_element_by_class_name("button")
no.click()

no = driver.find_element_by_class_name("button")
no.click()

no = driver.find_element_by_class_name("button")
no.click()

no = driver.find_element_by_class_name("button")
no.click()

no = driver.find_element_by_class_name("button")
no.click()

#最初に戻る
back = driver.find_element_by_class_name("start")
back.click()

#図鑑に画面遷移
picbook = driver.find_element_by_class_name("picture_book")
picbook.click()



#図鑑で特定の生物を指定し、画面遷移
#setumei = driver.find_element_by_xpath("//input[@value='1']").click()
setumei = driver.find_element_by_xpath("//input[@src='../static/imgs/1.png']").click()

#図鑑に戻る
back = driver.find_element_by_class_name("start")
back.click()

#最初に戻る
last = driver.find_element_by_tag_name("a")
last.click()

#タイトルが表示されるまでまつ
time.sleep(3)

#スクショをとる
driver.save_screenshot('chrome_abunator_last.png')

#ブラウザ閉じる
driver.quit()
