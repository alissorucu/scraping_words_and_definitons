import selenium.common.exceptions
from selenium import webdriver
import time
import random

driver = webdriver.Chrome()

words = ["about",
           "above",
           "across",
           "action",
           "activity",
           "actor",
           "actress",
           "add",
           "address",
           "adult",
           "advice",
           "afraid",
           "after",
           "afternoon",
           "again",
           "age",
           "ago",
           "agree",
           "air", ]


def scrapQuestions(words):
    lastList = []
    for i in range(len(words)):
        driver.get(f"https://translate.google.com/?hl=tr&sl=en&tl=tr&text={words[i]}&op=translate")

        time.sleep(1.2)
        try:
            definition = driver.find_element_by_class_name('fw3eif').text
        except selenium.common.exceptions.NoSuchElementException:
            continue

        answers = []
        trueIndex = random.randint(0, 3)

        answers.append(words[random.randint(0, len(words) - 1)])
        answers.append(words[random.randint(0, len(words) - 1)])
        answers.append(words[random.randint(0, len(words) - 1)])
        answers.append(words[random.randint(0, len(words) - 1)])
        answers[trueIndex] = words[i]
        print(
            f'Question({trueIndex}, "{definition}", ["{answers[0]}", "{answers[1]}", "{answers[2]}", "{answers[3]}"]),')

        try:
            example = driver.find_element_by_class_name('MZgjEb').text
        except selenium.common.exceptions.NoSuchElementException:
            continue
        answers = []
        trueIndex = random.randint(0, 3)

        answers.append(words[random.randint(0, len(words) - 1)])
        answers.append(words[random.randint(0, len(words) - 1)])
        answers.append(words[random.randint(0, len(words) - 1)])
        answers.append(words[random.randint(0, len(words) - 1)])
        answers[trueIndex] = words[i]
        example = example.replace(words[i], "__________")
        lastList.append(
            f'Question({trueIndex},"{example}",["{answers[0]}", "{answers[1]}", "{answers[2]}", "{answers[3]}"]),')
    print("#######################################################################\n")
    print("#######################################################################\n")
    for item in lastList:
        print(item)

    print("---------------------------------------------------------------------")
    print("---------------------------------------------------------------------")
    print("---------------------------------------------------------------------")
    print("---------------------------------------------------------------------")


scrapQuestions(words)
