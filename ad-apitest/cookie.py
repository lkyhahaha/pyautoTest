from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
base_url = "https://devmarket.banggood.cn"
driver.get(base_url)


# 定义登录方法
def login(username, password):
    # 用户名
    driver.find_element_by_name('username').click()
    driver.find_element_by_name('username').clear()
    driver.find_element_by_name('username').send_keys(username)
    # 密码
    driver.find_element_by_name('password').click()
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys(password)

    driver.find_element_by_class_name('form__submit').click()


username = "likeying@banggood.com"
password = "lky666666-+"
login(username, password)
driver.refresh()
sleep(1)
cookie_list = driver.get_cookies()
cookie = [item["name"] + "=" + item["value"] for item in cookie_list]
cookiestr = ';'.join(item for item in cookie)
print(cookiestr)
driver.close()
