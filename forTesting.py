from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
import csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

WEBSITE = 'https://www.tiempo3.com/north-america/mexico/baja-california/mexicali?page=past-weather#day=01&month=1'
PATH = "Z:\ChromeDriver\chromedriver.exe"
DATAPATH = 'Z:\ElTruDataSet'

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE)
driver.maximize_window()

time.sleep(8)
hourDataList = ["HORA:"]
tempDataList = ["TEMPERATURA (°C):"]
climateDataList = ["CLIMA:"]
rainDataList = ["PRECIPITACIONES (mm)"]
humidityDataList = ["HUMEDAD:"]
cloudDataList = ["NUBOSIDAD:"]
windDirectionList = ["DIRECCION DEL VIENTO:"]
windVelocityList = ["VELOCIDAD DEL VIENTO (Km/h):"]
windGustList = ["RAFAGA DEL VIENTO (Km/h):"]
visibilityList = ["VISIBILIDAD (Km):"]
dateOfData = "NA"


def getData():
    for i in range(24):
        hourData = driver.find_elements(by='xpath',
                                        value=f'/html/body/div[11]/div[2]/div[2]/div/table/thead/tr/td[{i + 1}]')
        tempData = driver.find_elements(by='xpath',
                                        value=f'/html/body/div[11]/div[2]/div[2]/div/table/tbody/tr[1]/td[{i + 1}]/span[1]')
        tempDataFloat = tempData[0].text.replace(',', '.')

        climateData = driver.find_elements(by='xpath',
                                           value=f'/html/body/div[11]/div[2]/div[2]/div/table/tbody/tr[2]/td[{i + 1}]/div')
        rainData = driver.find_elements(by='xpath',
                                        value=f'/html/body/div[11]/div[2]/div[2]/div/table/tbody/tr[3]/td[{i + 1}]/span[1]')
        humidityData = driver.find_elements(by='xpath',
                                            value=f'/html/body/div[11]/div[2]/div[2]/div/table/tbody/tr[5]/td[{i + 1}]')
        cloudData = driver.find_elements(by='xpath',
                                         value=f'/html/body/div[11]/div[2]/div[2]/div/table/tbody/tr[10]/td[{i + 1}]')
        windDirection = driver.find_elements(by='xpath',
                                             value=f'/html/body/div[11]/div[2]/div[2]/div/table/tbody/tr[9]/td[{i + 1}]')
        windVelocity = driver.find_elements(by='xpath',
                                            value=f'/html/body/div[11]/div[2]/div[2]/div/table/tbody/tr[6]/td[{i + 1}]/span[1]')
        windGust = driver.find_elements(by='xpath',
                                        value=f'/html/body/div[11]/div[2]/div[2]/div/table/tbody/tr[7]/td[{i + 1}]/span[1]')
        visibilityData = driver.find_elements(by='xpath',
                                              value=f'/html/body/div[11]/div[2]/div[2]/div/table/tbody/tr[11]/td[{i + 1}]/span[1]')

        strDateOfData = driver.find_elements(by='xpath', value=f'/html/body/header/div[3]/div[2]/span')
        yearDateOfData = driver.find_elements(by='xpath', value=f'/html/body/div[11]/div[2]/div[1]/span')

        data = {
        'dateOfData' : (f'{strDateOfData[0].text} {yearDateOfData[0].text}'),
        'hourDataList' : hourDataList.append(hourData[0].text),
        'tempDataList' : tempDataList.append(tempDataFloat),
        'climateDataList' : climateDataList.append(climateData[0].text),
        'rainDataList' : rainDataList.append(rainData[0].text),
        'humidityDataList' : humidityDataList.append(humidityData[0].text),
        'cloudDataList' : cloudDataList.append(cloudData[0].text),
        'windDirectionList' : windDirectionList.append(windDirection[0].text),
        'windVelocityList' : windVelocityList.append(windVelocity[0].text),
        'windGustList' : windGustList.append(windGust[0].text),
        'visibilityList' : visibilityList.append(visibilityData[0].text),
        }
        return data



for i in range(50):

    wait = WebDriverWait(driver, 10)
    try:
        dayOfTomorrow = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/a[2]/button')))
        driver.find_element(by="xpath", value='/html/body/div[5]/a[2]/button').click()
        print("DIA: {0}".format(i))

    except:
        print('PENE')
        wait = WebDriverWait(driver, 3)
        webdriver.ActionChains(driver).send_keys(Keys.HOME).perform()
        dayOfTomorrow = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/a[2]/button')))
        driver.find_element(by="xpath", value='/html/body/div[5]/a[2]/button').click()
        time.sleep(1)

    time.sleep(1)
