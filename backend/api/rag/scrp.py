from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# WebDriver のセットアップ
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# スクレイピングしたいページのURLを指定
url = 'https://example.com/page-with-threadview'
driver.get(url)

# class="threadview_response_body" の要素を取得
elements = driver.find_elements(By.CLASS_NAME, 'threadview_response_body')

# 各要素の内容を表示
for element in elements:
    print(element.text)

# ブラウザを閉じる
driver.quit()

