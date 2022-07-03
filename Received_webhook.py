import json
from flask import Flask,request
# .......
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
from time import sleep
print('ddd')
# pair = ''cd
# interval_chart = ''
# def reseive_tradingview():
#     global pair
#     global interval_chart
#     tradingview_url = 'https://www.tradingview.com/chart/'
#     user_name = 'hooshefaal7325'
#     password = '@Hooshefaal9492'
#     driver_patth = './selenuim_driver/chromedriver.exe'
#     options = webdriver.ChromeOptions()
#     options.add_argument('--ignore-certificate-arrors')
#     options.add_argument('--ignore-ssl-arrors')
#     deiver = webdriver.Chrome(driver_patth, chrome_options=options)
    
#     deiver.get(tradingview_url)
#     sleep(5)
#     deiver.find_element_by_xpath('/html/body/div[5]/div/div/div/article/div/div/div/button[2]').click()
#     deiver.find_element_by_xpath('//*[@id="header-toolbar-start-trial"]/div').click()
#     sleep(5)
#     deiver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span').click()
#     sleep(3)
#     deiver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div[1]/input').send_keys(user_name)
#     deiver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/input').send_keys(password)
#     deiver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div/div/div/div/div/div/form/div[5]/div[2]/button/span[2]').click()
#     sleep(20)
#     try:
#         deiver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div[2]/div/div[1]/section/div[1]/button[3]').click()  
#     except:
#         pass
#     deiver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]').click()
#     sleep(3)
#     deiver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input').send_keys(pair)
#     sleep(2)
#     deiver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[4]/div/div/div[2]/div[1]').click()
#     sleep(2)
#     deiver.find_element_by_xpath('/html/body').send_keys(str(interval_chart))
#     deiver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[1]/div/form/span/span[1]/input').send_keys(Keys.ENTER)
#     deiver.find_element_by_xpath('//*[@id="header-toolbar-screenshot"]').click()
#     sleep(2)
#     deiver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[3]/div[2]/div/div/span[2]/span').click()
#     sleep(7)
#     matn = pyperclip.paste()
#     return matn
    
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# app = Flask(__name__)
# @app.route("/",methods=['POST'])
# def webhook():
#     global pair
#     global interval_chart
#     data =json.loads(request.data)
#     pair = data['pair']
#     time_frame = data['time']
#     # snapshot_url = reseive_tradingview()
#     # print(snapshot_url)
#     return {
#         'pair':str(data['pair']),
#         'time':str(data['time'])
#     }
# # while True:
# #     webhook()


    
    
    

