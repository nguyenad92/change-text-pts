from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import datetime

import configparser

config = configparser.ConfigParser()
config.read('secret.config')

DRIVER_PATH = r"C:\Users\nguye\Desktop\Live\edge-driver\msedgedriver.exe"

username = config['SECRET']['USERNAME']
password = config['SECRET']['PASSWORD']

def get_title():
    today = datetime.date.today()
    if today.weekday() == 6:
        today += datetime.timedelta(7)
    else:
        while today.weekday() != 6:
            today += datetime.timedelta(1)
    
    
    return today

def get_description():
    content = 'SAU GIỜ THỜ PHƯỢNG: \nĐể tìm hiểu thêm về nhà thờ: http://gracealliancechurch.org \nCần cầu nguyện hoặc các vấn đề khác: http://bit.ly/gracealliance\nCách dâng hiến:\nDâng hiến trên mạng (online): http://bit.ly/gracetithe\nDâng hiến bằng chi phiếu :\nXin quý vị viết chi phiếu cho: Grace Alliance Church\nVà gửi về:\nGrace Alliance Church\n555 Los Coches St.\nMilpitas, CA 95035'
    return content


def Edge(username, password):
    EM_title = 'GAC EM Sunday Service | ' + get_title().strftime('%B %d, %Y')
    VN_title = 'Lễ thờ phượng Chúa Nhật | ' + get_title().strftime('%B %d, %Y')
    nextSun = get_title().strftime('%d')
    VN_thumbnails = r'C:\Users\nguye\Desktop\Live\VN-YOUTUBE.png'
    driver = webdriver.Edge(DRIVER_PATH)
    driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
    sleep(3)
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
    driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    sleep(3)
    driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    sleep(5)
    driver.get('https://studio.youtube.com/channel/UC/livestreaming')
    # main_page = driver.current_window_handle
    sleep(5)
    driver.find_element_by_xpath('//ytcp-button[@id="schedule-button"]').click()

    sleep(5)
    driver.find_element_by_xpath('/html/body/ytcp-app/ytls-popup-container/paper-dialog[1]/ytls-duplicate-broadcast-renderer/div[4]/div[1]/ytls-button-renderer/a/paper-button').click()
    sleep(5)
    # add title
    driver.find_element_by_xpath('/html/body/ytcp-app/ytls-popup-container/paper-dialog[2]/ytls-broadcast-setup-renderer/div/div[1]/div[1]/ytls-metadata-collection-renderer/div[2]/ytls-metadata-control-renderer[1]/div/ytls-mde-title-renderer/paper-input/paper-input-container/div[2]/div/iron-input/input').send_keys(VN_title)
    sleep(5)
    # add description
    driver.find_element_by_xpath('/html/body/ytcp-app/ytls-popup-container/paper-dialog[2]/ytls-broadcast-setup-renderer/div/div[1]/div[1]/ytls-metadata-collection-renderer/div[2]/ytls-metadata-control-renderer[3]/div/ytls-mde-description-renderer/paper-textarea/paper-input-container/div[2]/div/iron-autogrow-textarea/div[2]/textarea').send_keys(get_description())
    sleep(5)
    # add thumbnails
    # driver.find_element_by_xpath('/html/body/ytcp-app/ytls-popup-container/paper-dialog[2]/ytls-broadcast-setup-renderer/div/div[1]/div[1]/ytls-metadata-collection-renderer/div[2]/ytls-metadata-control-renderer[6]/div/ytls-thumbnail-control-renderer/div[1]/div/ytls-button-renderer/a/paper-button').send_keys(VN_thumbnails)
    sleep(5)
    # choose date
    # s_time = Select(driver.find_element_by_xpath('//*[@id="input-24"]/input'))
    # s_time.select_by_index(8)
    driver.find_element_by_xpath('//*[@id="input-24"]/input').click()
    driver.find_element_by_xpath('/html/body/ytcp-app/ytls-popup-container/paper-dialog[2]/ytls-broadcast-setup-renderer/div/div[1]/div[1]/ytls-metadata-collection-renderer/div[2]/ytls-metadata-control-renderer[5]/div/ytls-input-date-time-renderer/div/div[1]/paper-dialog/app-datepicker/div/neon-animated-pages/div/div[3]/div[{}]'.format(nextSun)).click()
    sleep(5)
    # choose time
    driver.find_element_by_xpath('//*[@id="input-25"]/input').click()
    driver.find_element_by_xpath('/html/body/ytcp-app/ytls-popup-container/paper-dialog[2]/ytls-broadcast-setup-renderer/div/div[1]/div[1]/ytls-metadata-collection-renderer/div[2]/ytls-metadata-control-renderer[5]/div/ytls-input-date-time-renderer/div/div[2]/paper-dropdown-menu/paper-menu-button/iron-dropdown/div/div/paper-listbox/paper-item[115]').click()
    # s_time = Select(driver.find_element_by_id('time-entries'))
    # print(s_time.options)
    # upload thumbsnail
    # driver.find_element_by_xpath('/html/body/ytcp-app/ytls-popup-container/paper-dialog[2]/ytls-broadcast-setup-renderer/div/div[1]/div[1]/ytls-metadata-collection-renderer/div[2]/ytls-metadata-control-renderer[6]/div/ytls-thumbnail-control-renderer').click()
    # click create
    # driver.find_element_by_xpath('/html/body/ytcp-app/ytls-popup-container/paper-dialog[2]/ytls-broadcast-setup-renderer/div/div[1]/div[2]/div/ytls-button-renderer/a/paper-button').click()
    sleep(5)



Edge(username, password)
