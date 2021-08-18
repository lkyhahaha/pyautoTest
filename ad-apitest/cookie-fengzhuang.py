from time import sleep

from selenium import webdriver


class Cookie():
    def setupClass(self):
        self.driver = webdriver.Chrome()
        base_url = "https://devmarket.banggood.cn"
        self.driver.get(base_url)

    # 定义登录方法
    def login(self, username, password):
        # 用户名
        self.driver.find_element_by_name('username').click()
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)
        # 密码
        self.driver.find_element_by_name('password').click()
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys(password)

        self.driver.find_element_by_class_name('form__submit').click()
        self.driver.refresh()
        sleep(1)

    def getcookie(self):
        cookie_list = self.driver.get_cookies()
        cookie = [item["name"] + "=" + item["value"] for item in cookie_list]
        cookiestr = ';'.join(item for item in cookie)
        print(cookiestr)

    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    username = "likeying@banggood.com"
    password = "lky666666-+"
    Cookie.login(username, password)
    Cookie.getcookie()