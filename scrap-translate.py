import selenium.common.exceptions
from selenium import webdriver
import time
import random
driver = webdriver.Chrome()

words = [
"again",
"age",
"ago",
"agree",
"air",
"airport",
"all",
"also",
"always",
"amazing",
"and",
"angry",
"animal",
"another",
"answer",
"any",
"anyone",
"anything",
]


lastList=[]
questionList=[]
exampleList=[]

for i in range(len(words)):
    driver.get(f"https://translate.google.com/?hl=tr&sl=en&tl=tr&text={words[i]}&op=translate")
    print("loading",end="...")
    time.sleep(0.3)
    print("..",end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="\n")

    definitions = driver.find_elements_by_class_name('fw3eif')



    while True:
        print("\n" + words[i] + " definitions:")
        for e in range(len(definitions)):
            print(f"[{e}] {definitions[e].text}")
            time.sleep(0.1)

        try:
            defDecision=int(input("[99] delete this word\n\nchoice:"))
            if defDecision>= len(definitions):
                if defDecision==99:
                    break
                else:
                    print(str(defDecision)+" there isn't" )
                    continue
            else:
                break

        except ValueError:
            print("choice must be integer")
            continue

    examples = driver.find_elements_by_class_name('MZgjEb')



    if defDecision!=99:
        print(words[i] + " example sentences")
        while True:
            for q in range(len(examples)):
                print(f"[{q}] " + examples[q].text)
                time.sleep(0.1)
            try:
                exDecision = int(input("[99] don't choose any example\n\nchoice:"))
                if exDecision >= len(definitions):
                    if exDecision == 99:
                        break
                    else:
                        print(str(exDecision) + " there isn't")
                        continue
                else:
                    break

            except ValueError:
                print("choice must be integer")
                continue

    if defDecision!=99:
        if exDecision!=99:
            lastList.append([words[i], definitions[defDecision].text, examples[exDecision].text])
        else:
            lastList.append([words[i], definitions[defDecision].text, "null"])


for a in range(len(lastList)):
    answers = []
    trueIndex = random.randint(0, 3)

    answers.append(words[random.randint(0, len(words) - 1)])
    answers.append(words[random.randint(0, len(words) - 1)])
    answers.append(words[random.randint(0, len(words) - 1)])
    answers.append(words[random.randint(0, len(words) - 1)])
    answers[trueIndex] = lastList[a][0]
    questionList.append(f'Question({trueIndex}, "{lastList[a][1]}", ["{answers[0]}", "{answers[1]}", "{answers[2]}", "{answers[3]}"]),')

for b in range(len(lastList)):
    answers = []
    trueIndex = random.randint(0, 3)

    answers.append(words[random.randint(0, len(words) - 1)])
    answers.append(words[random.randint(0, len(words) - 1)])
    answers.append(words[random.randint(0, len(words) - 1)])
    answers.append(words[random.randint(0, len(words) - 1)])
    answers[trueIndex] = lastList[b][0]
    lastList[b][2].replace(lastList[b][0],len(lastList[b][0])*"_")
    exampleList.append(f'Question({trueIndex},"{lastList[b][2]}",["{answers[0]}", "{answers[1]}", "{answers[2]}", "{answers[3]}"])')

for question in questionList:
    print(question)
for example in exampleList:
    print(example)

