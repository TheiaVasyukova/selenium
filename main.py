from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()

query = input("Введите запрос для поиска на Википедии: ")

browser.get("https://www.wikipedia.org/")
search_box = browser.find_element(By.NAME, "search")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

while True:
    print("\nВыберите действие:")
    print("1. Листать параграфы текущей статьи")
    print("2. Перейти на одну из связанных страниц")
    print("3. Выйти из программы")
    choice = input("Введите номер действия: ")

    if choice == "1":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print(paragraph.text)
            input("Нажмите Enter для следующего параграфа...")

    elif choice == "2":
        hatnotes = []
        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable":
                hatnotes.append(element)

        if hatnotes:
            hatnote = random.choice(hatnotes)
            link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
            browser.get(link)
            time.sleep(2)
        else:
            print("Связанных страниц не найдено")

    elif choice == "3":
        print("Выход из программы...")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")

browser.quit()

