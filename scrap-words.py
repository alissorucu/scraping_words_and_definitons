from selenium import webdriver
import time

driver = webdriver.Chrome()


def scrapWords(choice):
    driver.get("https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000")
    driver.find_element_by_xpath("//*[@id='wordlistsFilters']").click()
    driver.find_element_by_xpath("//*[@id='filterList']").click()
    driver.find_element_by_xpath("//*[@id='filterList']/option[1]").click()
    driver.find_element_by_xpath("//*[@id='ox5000']/ul/li[1]").click()
    if choice == 1:
        driver.find_element_by_xpath("//*[@id='ox5000']/ul/li[2]").click()
    elif choice == 2:
        driver.find_element_by_xpath("//*[@id='ox5000']/ul/li[3]").click()
    elif choice == 3:
        driver.find_element_by_xpath("//*[@id='ox5000']/ul/li[4]").click()
    elif choice == 4:
        driver.find_element_by_xpath("//*[@id='ox5000']/ul/li[5]").click()
    elif choice == 5:
        driver.find_element_by_xpath("//*[@id='ox5000']/ul/li[6]").click()



    time.sleep(1)

    driver.find_element_by_xpath("//*[@id='onetrust-accept-btn-handler']").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#saveFilters > span").click()

    words = driver.find_elements_by_xpath("//*[@id='wordlistsContentPanel']/ul/li/a")

    # to avoid same words
    lastWord = "_"
    for item in words:
        word = str(item.text).replace(" ", "")
        if lastWord != word:
            if word != "":
                print('"' + word + '"' + ",")
                lastWord = word

    driver.close()


while True:

    try:
        option = int(input("[1] A1\n[2] A2\n[3] B1\n[4] B2\n[5] C1\n\noption:"))
        if option > 6 or option < 1:
            print("\nChoice must be 1 or 2!!!!!!!!!! \n")
            continue
    except ValueError:
        print("\nChoice must be integer!!!!!!!!!!\n")
        continue
    scrapWords(option)
