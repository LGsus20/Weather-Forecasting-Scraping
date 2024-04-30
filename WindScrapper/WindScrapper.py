from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

month = 3
has31days = 32
has30days = 31
for i in range (1,has31days):
    WEBSITE = f'https://www.tiempo3.com/north-america/mexico/baja-california/mexicali?page=past-weather#day={i}&month={month}'
    driver.get(WEBSITE)
    # Weird stuff that happens to solve all the bugs I had with scrolling to the button
    time.sleep(2)
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as per your requirement
    year2022 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div[1]/button[2]")))
    if (year2022.text == "2022"):
        try:
            year2022.click()
        except:
            time.sleep(2)
            year2022.click()

        print(f"\n\n\nDAY: {i}")
        with open("results.txt", "a") as file:
            # file.write(f"DAY: #{i}\n")
            for iteration in range(1,25):
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"/html/body/div[10]/div[2]/div[2]/div/table/tbody/tr[6]/td[{iteration}]/span[1]")))
                text = element.text
                file.write(text + "\n")
                print(text)
        time.sleep(2)
    else:
        print("YEAR MISSING, PLEASE ADJUST THE BUTTON ACCORDINGLY")
        quit()

time.sleep(10)


