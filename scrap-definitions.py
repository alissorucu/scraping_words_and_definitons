import selenium.common.exceptions
from selenium import webdriver
import random

driver = webdriver.Chrome()
words = [
    "abandon",
    "ability",
    "able",
    "about",
    "above",
    "abroad",
    "absolute",
    "absolutely",
    "academic",
    "accept",
    "acceptable",
    "access",
    "accident",
    "accommodation",
    "accompany",
]


# There are different scrap methods for different cambridge definition pages

def scrapMethod0():
    # Even though we are wanting one definition some words have various definitions
    # this situation raises IndexError, there is a try-except block to different cambridge definition pages

    try:
        item = driver.find_elements_by_xpath(
            "//*[@id='page-content']/div[2]/div[4]/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div")
        return item[0].text
    except IndexError:
        item = driver.find_element_by_xpath(
            "//*[@id='page-content']/div[2]/div[4]/div/div/div/div[3]/div[1]/div[2]/div/div[2]/div")
        return item.text


def scrapMethod1():
    try:
        item = driver.find_elements_by_xpath(
            "//*[@id='page-content']/div[2]/div[4]/div/div/div/div[3]/div[1]/div[2]/div/div[3]/div/div[2]/div")
        return item[0].text
    except IndexError:
        item = driver.find_element_by_xpath(
            "//*[@id='page-content']/div[2]/div[4]/div/div/div/div[3]/div[1]/div[2]/div/div[3]/div/div[2]/div")
        return item.text


def scrapDefinitions(option):
    for i in range(len(words)):
        driver.get("https://dictionary.cambridge.org/tr/s%C3%B6zl%C3%BCk/ingilizce-t%C3%BCrk%C3%A7e/" + words[i])

        # Some words are not in the cambridge dictionary, So cambridge dictionary navigating to homepage
        # this situation raises error. We have to control current url every page change

        if driver.current_url != "https://dictionary.cambridge.org/tr/s%C3%B6zl%C3%BCk/ingilizce-t%C3%BCrk%C3%A7e/" + \
                words[i]:
            continue
        else:
            try:
                definition = scrapMethod0()
            except selenium.common.exceptions.NoSuchElementException:

                definition = scrapMethod1()
            if option == 1:
                answers = []
                trueIndex = random.randint(0, 3)

                answers.append(words[random.randint(0, len(words) - 1)])
                answers.append(words[random.randint(0, len(words) - 1)])
                answers.append(words[random.randint(0, len(words) - 1)])
                answers.append(words[random.randint(0, len(words) - 1)])
                answers[trueIndex] = words[i]
                print(
                    f'Question({trueIndex}, "{definition}", ["{answers[0]}", "{answers[1]}", "{answers[2]}", "{answers[3]}"]),')
            if option == 2:
                print(f'Vocabulary("{words[i]}","{definition}"),')

    driver.close()


while True:

    try:
        choice = int(input("[1] Scrap data for Questions\n[2] Scrap data for definition-word game\n\nchoice:"))
        if choice > 2 or choice < 1:
            print("\nChoice must be 1 or 2!!!!!!!!!! \n")
            continue
    except ValueError:
        print("\nChoice must be integer!!!!!!!!!!\n")
        continue
    scrapDefinitions(choice)

