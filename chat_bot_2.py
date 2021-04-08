# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from data import promo1, promo2, otvet11, otvet21, otvet31, otvet22, otvet12, url1, url2
import time
import random
import requests
import os
from urllib.request import urlopen
import bs4
from selenium.webdriver.chrome.options import Options


class InstagramBot():

    def __init__(self, config_filename):
        # Делаем из файла data.txt словарь 'ключ\значение' для передачи значений в переменные класса InstagramBot
        global val
        config_data = dict()
        fileconfig = open(config_filename, encoding="utf-8-sig")  #  обязательно ставим utf-8-sig
        for f in fileconfig:
            (key, val) = f.strip().split(' = ')
            val = val.strip('\'')
            config_data[key] = val
        fileconfig.close()

        self.username = config_data['username']
        self.password = config_data['password']
        self.avtobot1 = config_data['promo1']
        self.avtobot2 = config_data['promo2']
        self.message1 = config_data['otvet11']
        self.message12 = config_data['otvet12']
        self.url1 = config_data['url1']
        self.message2 = config_data['otvet21']
        self.message21 = config_data['otvet22']
        self.url2 = config_data['url2']
        self.message3 = config_data['otvet31']
        time.sleep(random.randrange(3, 6))

        options = FirefoxOptions()
        options.add_argument("--headless")
        self.browser = webdriver.Firefox(options=options)  # options=options


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
        username_input.send_keys(self.username)

        time.sleep(random.randrange(3, 6))

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(self.password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(random.randrange(3, 6))

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
        try:
            browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div[1]/button").click()
        except:
            browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/button").click()
        time.sleep(random.randrange(7, 12))
        # подтверждаем
        browser.find_element_by_xpath("/html/body/div[5]/div/div/div").find_element_by_xpath(
            "/html/body/div[5]/div/div/div/div[2]/button[1]").click()
        time.sleep(random.randrange(6, 13))
        # идем на главную страницу
        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[1]/div/a").click()
        time.sleep(random.randrange(4, 7))

    def home_exit_2(self):
        browser = self.browser
        # идем на главную страницу
        time.sleep(random.randrange(3, 7))
        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[1]/div/a").click()


    def check_user(self):  # в данный момент этот метод НЕ ИСПОЛЬЗУЕТСЯ!!!
        # Проверяем ник пользователя в списке юзеров, купивших скрипт
        time.sleep(random.randrange(3, 7))
        user_data = dict()  # создаем новый список с юзерами
        html2 = urlopen('https://promo22.site/user.txt')
        code = list(str(bs4.BeautifulSoup(html2.read(), 'html.parser')).split('\n'))
        for f in code:
            (key, val) = f.strip().split(' = ')
            val = val.strip('\'')
            user_data[key] = val
        print(user_data)

        self.user_proverka = self.username
        for elem in user_data.values():
            if self.user_proverka == elem:
                print('Пользователь в списке найден. Все ОК.')
            else:
                print('нет совпадений...')


    # метод работает как "Автоотчетчик"
    def auto_otvet(self):

        browser = self.browser
        api_token = '1431354839:AAHc0xVFBva7VVZ0UzR39LlHTJY_UfyRazM'  # токен Телеграм-бота

        # отключаем всплывающее окно №1 __ Включить уведомления
        if self.xpath_exists("/html/body/div[4]/div/div"):
            browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]").click()
        time.sleep(random.randrange(6, 9))

         # выбираем первый неотвеченный КОНТАКТ
        try:
            browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]").click()
        except:
            browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]").click()
        print(f"Проверяю первый КОНТАКТ в списке.")
        time.sleep(random.randrange(6, 10))

        # проверяем совпадения с АВТОТВЕТОМ
        if browser.find_elements_by_xpath("//*[contains(text(),'{}')]".format(self.avtobot1)):
            print(f"Поиск работает. Есть совпадение на промокод " + self.avtobot1)
            text_message_area = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_message_area.clear()
            time.sleep(random.randrange(4, 8))
            text_message_area.send_keys(self.message1)
            time.sleep(random.randrange(5, 8))
            text_message_area.send_keys(Keys.ENTER)
            text_message_area = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_message_area.clear()
            time.sleep(random.randrange(4, 9))
            text_message_area.send_keys(self.message12)
            time.sleep(random.randrange(4, 8))
            text_message_area.send_keys(Keys.ENTER)
            print(f"Сообщения 1 успешно отправлены!")
            # кидаем в ТЕЛЕГУ уведомление через бота @BoomBarashka_Bot
            insta_user = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div").text
            requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
                chat_id='-1001278740849',
                text="Сообщение от Инстаграм-бота.\nНовый запрос в Инстаграм по промокоду\n" + self.avtobot1 + "\nот пользователя: " + insta_user
            ))
            # дальше отправка КАРТИНКИ
            time.sleep(random.randrange(7, 9))
            send_img_input = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input")
            img_path = "C:\\untitled\\insta_bot\\img_2.jpg"
            send_img_input.send_keys(img_path)
            print(f"Изображение 1 успешно отправлено!")
            time.sleep(random.randrange(4, 8))
            # отправляем ссылку на ИГ-пост
            text_message_area = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_message_area.clear()
            time.sleep(random.randrange(5, 8))
            text_message_area.send_keys(self.url1)
            time.sleep(random.randrange(4, 9))
            text_message_area.send_keys(Keys.ENTER)
            print(f"Ссылка на пост успешно отправлена!")

            # дальше отправка ССЫЛКИ или сылку на пост в ИГ
            print("Возврат в норм режим.")
            time.sleep(random.randrange(7, 9))
            self.home_exit()

        elif browser.find_elements_by_xpath("//*[contains(text(),'{}')]".format(self.avtobot2)):
            print(f"Поиск работает. Есть совпадение на АВТООТВЕТ " + self.avtobot2)
            text_message_area = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_message_area.clear()
            time.sleep(random.randrange(4, 9))
            text_message_area.send_keys(self.message2)
            time.sleep(random.randrange(4, 9))
            text_message_area.send_keys(Keys.ENTER)
            text_message_area = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_message_area.clear()
            time.sleep(random.randrange(4, 8))
            text_message_area.send_keys(self.message21)
            time.sleep(random.randrange(4, 8))
            text_message_area.send_keys(Keys.ENTER)
            print(f"Сообщения ВТОРОЙ ПРОМО успешно отправлены!")
            time.sleep(random.randrange(5, 10))
            # кидаем в ТЕЛЕГУ уведомление через бота @BoomBarashka_Bot
            insta_user = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div").text
            time.sleep(random.randrange(3, 9))
            requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
                chat_id='-1001278740849',
                text="Сообщение от Инстаграм-бота.\nНовый запрос в Инстаграм по промокоду\n" + self.avtobot2 + "\nот пользователя: " + insta_user
            ))
            # отправка КАРТИНКИ
            time.sleep(random.randrange(5, 9))
            send_img_input = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input")
            img_path = "C:\\untitled\\insta_bot\\img_3.jpg"
            send_img_input.send_keys(img_path)
            print(f"Изображение 2 успешно отправлено!")
            text_message_area = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_message_area.clear()
            time.sleep(random.randrange(3, 8))
            text_message_area.send_keys(self.url2)
            time.sleep(random.randrange(4, 9))
            text_message_area.send_keys(Keys.ENTER)
            print(f"Ссылка на пост успешно отправлена!")
            print(f"Продолжаю работу в стелс-режиме...")
            time.sleep(random.randrange(4, 8))
            self.home_exit()
        else:
            print(f"Во входящем сообщении нет совпадений.")
            text_message_area = browser.find_element_by_xpath(
                "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_message_area.clear()
            time.sleep(random.randrange(5, 9))
            text_message_area.send_keys(self.message3)
            time.sleep(random.randrange(5, 9))
            text_message_area.send_keys(Keys.ENTER)
            print(f"Сообщение 'заглушка' успешно отправлено!")
            time.sleep(random.randrange(4, 9))
            # идем на главную страницу
            self.home_exit()


    # метод проверяет входящие сообщения на наличе новых. ИЩЕТ КРАСНЫЙ ЗНАЧЕК на самолетике
    def check_inbox_direct(self):

        browser = self.browser
        time.sleep(random.randrange(7, 10))

        # ищем КРАСНЫЙ КРУЖОЧЕК о входящем, если нашли то идем в Директ. Если нет, остаемся на главной
        red = True
        while red:
            red_circle = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div"
            if not self.xpath_exists(red_circle):
                time22 = random.randrange(2, 4)
                if time22 == 1:
                    print(f"Можете заняться своими делами. Работаю...")
                elif time22 == 2:
                    print(f"Поддержка в Телегам YaDiCaprio")
                else:
                    print(f"От Севильи до Гренады...")
                time.sleep(random.randrange(3, 8))
                os.system("mode con cols=70 lines=20")  # Задаем размер консоли
                os.system('cls||clear')  # Чистим КОНСОЛЬ от сообщений.
                time.sleep(random.randrange(3, 6))
            else:
                print("Есть входящие!!!")
                red = False

        direct_message = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
        time.sleep(random.randrange(4, 7))
        direct_message.click()
        print(f"Имитирую поведение реального человека.")
        # отключаем всплывающее окно №1 __ Включить уведомления
        if self.xpath_exists("/html/body/div[5]/div/div"):
            browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        time.sleep(random.randrange(4, 7))
        print(f"Найдено входящее сообщение в Директ. Проверяю.")


    # метод проверяет новые непрочитанные сообщения в ЗАПРОСах
    def check_zapros(self):
        browser = self.browser
        time.sleep(random.randrange(6, 13))

        # Идем в Директ проверить новые запросы
        print("Проверяю в Директ, есть ли новые запросы")
        browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
        time.sleep(random.randrange(5, 15))

        # если есть, то отключаем всплывающее окно №1 __ Включить уведомления
        try:
            obhod = "/html/body/div[5]/div/div"
            if self.xpath_exists(obhod):
                print("Временный обход УВЕДОМЛЕНИЙ ИГ...")
                time.sleep(random.randrange(7, 11))
                browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
            else:
                print("Уведомления ИГ выключены. Работаю...")
        except:
            obhod = "/html/body/div[4]/div/div"
            if self.xpath_exists(obhod):
                print("Временный обход УВЕДОМЛЕНИЙ ИГ...")
                time.sleep(random.randrange(7, 11))
                browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
            else:
                print("Уведомления ИГ выключены. Работаю...")

        # Идем в список "запросов на рассмотрении"
        zapros = "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/button"
        if self.xpath_exists(zapros):
            time.sleep(random.randrange(7, 14))
            print("Есть новые запросы на переписку.")
            browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/button").click()
            # Кликаем по первому запросу
            print("Проверяю первый запрос.")
            browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div[2]/div/a").click()
            # Нажимаем кнопку "Принять"
            time.sleep(random.randrange(6, 12))
            browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]").click()
            print("Принял первый в списке запрос.")
            time.sleep(random.randrange(6, 12))
            # идем ПОКА на главную страницу
            print("Работаю...")
            browser.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[1]/div/a").click()
            time.sleep(random.randrange(6, 12))
        else:
            #  Если списка нет, то идем обратно на главную
            print("Нет новых запросов. Работаю...")
            browser.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[1]").click()
            time.sleep(random.randrange(7, 16))

    def prog_exit(self):  # метод выходит из программы
        print('все')
        exit()


my_bot = InstagramBot('./data.txt')
time.sleep(random.randrange(2, 4))
user_data = dict()  # создаем новый словарь с юзерами
html2 = urlopen('https://promo22.site/user.txt')
code = list(str(bs4.BeautifulSoup(html2.read(), 'html.parser')).split('\n'))
for f in code:
    (key, val) = f.strip().split(' = ')
    val = val.strip('\'')
    user_data[key] = val

user_proverka = my_bot.username
for elem in user_data.values():
    if user_proverka == elem:
        print('Ваш Инстаграм в списке найден. Все ОК. Начинаю работать.')
        my_bot.login()
        green = True
        while green:
            my_bot.check_inbox_direct()
            my_bot.auto_otvet()
            if not green:
                break
    else:
        print('Ваш Инстаграм не найден в списке...')
        # time.sleep(random.randrange(1, 3))