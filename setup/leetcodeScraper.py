from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
def parse(n):
    results = []
    driver = webdriver.Chrome()
    for i in range(1, n+1):
        url = f'https://leetcode.com/problemset/all/?page={i}'
        driver.get(url)
        sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        problems = soup.find_all(class_="h-5 hover:text-blue-s dark:hover:text-dark-blue-s")
        for problem in problems:
            results.append(problem.text)
    driver.quit()
    return results

r = parse(53)
with open("leetcode.json", "w") as f:
    f.write(str(r))
print("Done")