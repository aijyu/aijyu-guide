# 必要なものもろもろをインポート
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time as timer

# driverを起動
driver = webdriver.Edge()

# ランダムな３０個の検索キーワード（Cpilotさんに頼んだら普通に作成してくれたｗ）
words = [
    "apple", "banana", "chocolate", "dog", "elephant",
    "flower", "guitar", "hiking", "internet", "jazz",
    "kangaroo", "lemon", "mountain", "notebook", "ocean",
    "piano", "quantum", "rainbow", "sunset", "tiger",
    "umbrella", "volcano", "waterfall", "xylophone", "yoga",
    "zebra", "astronomy", "beach", "coffee", "dragon"
]

# １検索につき３ポイント、最大９０ポイントだから、３０回繰り返せばよい
for i in range(30):
    # 検索ページへ行く
    driver.get("https://www.bing.com/?form=ML2PCO")
    # 気長に、機械に負担をかけぬよう、待ちましょう☕~
    timer.sleep(5.0)
    # 検索ボックスを取得
    target = driver.find_element(By.ID, "sb_form_q")
    # 検索ボックスにwordsの検索キーワードを入力
    target.send_keys(words[i])
    # 検索ボックス内でEnter！　→　検索される
    target.send_keys(Keys.ENTER)
    
    # 待つことは大切です（カップラーメンだって3分も待つでしょう？（私は７分ぐらいでも可））
    timer.sleep(5.0)

# 以上です！とても単純ですね！ｗ
