from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from data import username, password
import time
import random
from selenium.webdriver.chrome.options import Options
import requests
import os

class InstagramBot():

    def __init__(self, username, password):

       # chrome_options = Options()   # запускаем браузер в "тихом режиме"
       # chrome_options.add_argument("--headless")   # запускаем браузер в "тихом режиме"
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome("C:\\untitled\\insta_bot\\chromedriver\\chromedriver.exe")
        # дальше это промо-КОДЫ для ответов
        self.avtobot1 = "Промо22"
        self.avtobot2 = "Кариб12"
        self.messa1_1 = "Проверочка 1 на мессу1"
        self.messa1_2 = "Проверочка 2 на мессу2"



    # метод закрытия браузера
    def close_browser(self):

        self.browser.close()
        self.browser.quit()

    # метод логин
    def login(self):

        browser = self.browser
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(random.randrange(5, 9))

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(random.randrange(5, 9))

    # метод проверяет по xpath существует ли элемент на странице
    def xpath_exists(self, url):

        browser = self.browser
        try:
            browser.find_element_by_xpath(url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    # метод удаляет чат и идет на главную
    def home_exit(self):
        browser = self.browser
        # ищем кнопку с настройкой чата
        browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button").click()
        time.sleep(random.randrange(7, 12))
        # нажмаем на кнопку "Удалить чат"
        browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/button/div").click()
        time.sleep(random.randrange(7, 12))
        # подтверждаем
        browser.find_element_by_xpath("/html/body/div[5]/div/div").find_element_by_xpath(
            "/html/body/div[5]/div/div/div/div[2]/button[1]").click()
        time.sleep(random.randrange(6, 13))
        # идем на главную страницу
        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[1]/div/a").click()
        time.sleep(random.randrange(2, 5))

    # метод работает как "Автоотчетчик"
    def auto_otvet(self):

        browser = self.browser
        api_token = '1431354839:AAHc0xVFBva7VVZ0UzR39LlHTJY_UfyRazM'  # токен Телеграм-бота

        # отключаем всплывающее окно №1 __ Включить уведомления
        if self.xpath_exists("/html/body/div[5]/div/div"):
            browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        time.sleep(random.randrange(2, 4))

         # выбираем первый неотвеченный КОНТАКТ
        first_contact = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a")
        first_contact.click()
        print(f"Нашли первый КОНТАКТ с неотвеченным сообщением.")
        time.sleep(random.randrange(5, 12))

        # проверяем совпадения с АВТОТВЕТОМ
        if browser.find_elements_by_xpath("//*[contains(text(),'{}')]".format(self.avtobot1)):
            print(f"Поиск работает. Есть совпадение на АВТООТВЕТ " + self.avtobot1)
            text_message_area = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_message_area.clear()
            time.sleep(random.randrange(7, 13))
            message = self.messa1_1
            text_message_area.send_keys(message)
            time.sleep(random.randrange(7, 12))
            text_message_area.send_keys(Keys.ENTER)
            print(f"Сообщение 1 успешно отправлено!")
            # кидаем в ТЕЛЕГУ уведомление через бота @BoomBarashka_Bot
            insta_user = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div").text
            requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
                chat_id='-1001278740849',
                text="Сообщение от Инстаграм-бота.\nНовый запрос в Инстаграм по промокоду\n" + self.avtobot1 + "\nот пользователя: " + insta_user
            ))
            # дальше отправка КАРТИНКИ
            time.sleep(random.randrange(7, 9))
            send_img_input = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input")
            img_path = "C:\\untitled\\insta_bot\\img_4.jpg"
            send_img_input.send_keys(img_path)
            print(f"Изображение 1 успешно отправлено!")
            time.sleep(random.randrange(6, 12))
            # дальше отправка ССЫЛКИ или сылку на пост в ИГ
            print("Удаляем чат и идем на главную.")
            self.home_exit()

        elif browser.find_elements_by_xpath("//*[contains(text(),'{}')]".format(self.avtobot2)):
            print(f"Поиск работает. Есть совпадение на АВТООТВЕТ " + self.avtobot2)
            text_message_area = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_message_area.clear()
            time.sleep(random.randrange(7, 13))
            message = self.messa1_2
            text_message_area.send_keys(message)
            time.sleep(random.randrange(7, 12))
            text_message_area.send_keys(Keys.ENTER)
            print(f"Сообщение 2 успешно отправлено!")
            time.sleep(random.randrange(9, 12))
            # кидаем в ТЕЛЕГУ уведомление через бота @BoomBarashka_Bot
            insta_user = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div").text
            requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
                chat_id='-1001278740849',
                text='Поиск работает.\nНовый запрос в ИГ по промокоду\n' + self.avtobot2 + '\n от пользователя: ' + insta_user
            ))
            # отправка КАРТИНКИ
            time.sleep(random.randrange(9, 12))
            send_img_input = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input")
            img_path = "C:\\untitled\\insta_bot\\img_5.jpg"
            send_img_input.send_keys(img_path)
            print(f"Изображение 2 успешно отправлено!")
            print("Удаляем чат и идем на главную.")
            self.home_exit()
        else:
            print(f"Нет совпадений. Идем на главную.")
            time.sleep(random.randrange(8, 17))
            # идем на главную страницу
            browser.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[1]/div/a").click()
            time.sleep(random.randrange(2, 5))


    # метод проверяет входящие сообщения на наличе новых. ИЩЕТ КРАСНЫЙ ЗНАЧЕК на самолетике
    def check_inbox_direct(self):

        browser = self.browser
        time.sleep(random.randrange(3, 7))

        # ищем КРАСНЫЙ КРУЖОЧЕК о входящем, если нашли то идем в Директ. Если нет, остаемся на главной
        red = True
        while red:
            red_circle = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div"
            if not self.xpath_exists(red_circle):
                print(f"Пока нет входящих сообщений. Ждемс...")
                time.sleep(random.randrange(9, 12))
            else:
                print("Есть входящие!!!")
                red = False

        direct_message = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
        time.sleep(random.randrange(4, 9))
        direct_message.click()
        print(f"Нажимаем на кнопку НЕ СЕЙЧАС")
        # отключаем всплывающее окно №1 __ Включить уведомления
        if self.xpath_exists("/html/body/div[5]/div/div"):
            browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        time.sleep(random.randrange(3, 9))
        print(f"Нашли входящий, идем в Директ, в функцию auto_otvet")


    # метод отправки сообщения в директ ВСЕГО ОДНОМУ КОНТАКТУ
    def send_direct_message(self, username22="", message="", img_path=''):

        browser = self.browser
        time.sleep(random.randrange(2, 4))

        direct_message_button = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a"

        if not self.xpath_exists(direct_message_button):
            print("Кнопка отправки сообщений не найдена!")
            self.close_browser()
        else:
            print("Отправляем сообщение...")
            direct_message = browser.find_element_by_xpath(direct_message_button).click()
            time.sleep(random.randrange(2, 4))

        # отключаем всплывающее окно
        if self.xpath_exists("/html/body/div[5]/div/div"):
            browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        time.sleep(random.randrange(2, 4))

        send_message_button = browser.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/button").click()
        time.sleep(random.randrange(2, 4))

        # выбиваем имя пользователя котрому хотим отправить сообщение

        user_input = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input")
        user_input.send_keys(username22)
        time.sleep(random.randrange(3, 7))

        user_list = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button")
        user_list.click()
        time.sleep(random.randrange(1, 3))

        next_button = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button")
        next_button.click()
        time.sleep(random.randrange(2, 4))

        # отправка текстового сообщения
        if message:
            text_message_area = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_message_area.clear()
            text_message_area.send_keys(message)
            time.sleep(random.randrange(2, 4))
            text_message_area.send_keys(Keys.ENTER)
            print(f"Сообщение успешно отправлено!")
            time.sleep(random.randrange(2, 4))

        # отправка изображения
        if img_path:
            send_img_input = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input")
            send_img_input.send_keys(img_path)
            print(f"Изображение успешно отправлено!")
            time.sleep(random.randrange(2, 4))

        self.close_browser()




# my_bot.send_direct_message(username22, "Привет. Как у тебя дела?", "C:\\untitled\\insta_bot\\img_2.jpg")
