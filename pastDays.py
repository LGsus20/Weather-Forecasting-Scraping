from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

WEBSITE = 'https://www.tiempo3.com/north-america/mexico/baja-california/mexicali?page=past-weather#day=23&month=9'
PATH = "Z:\ChromeDriver\chromedriver.exe"
DATAPATH = 'Z:\ElTruDataSet'

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE)
driver.maximize_window()

time.sleep(4)
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

dayWasntTracked = False
pastDay = "1 de enero"


def getData():
    strDateOfData = driver.find_elements(by='xpath', value=f'/html/body/header/div[3]/div[2]/span')
    yearDateOfData = driver.find_elements(by='xpath', value=f'/html/body/div[11]/div[2]/div[1]/span')

    # REMOVED FOR NOW
    # if (yearDateOfData[0].text != "2023"): driver.find_element(by="xpath", value='/html/body/div[11]/div[1]/button[2]').click()

    try:
        driver.find_elements(by='xpath', value=f'/html/body/div[11]/div[2]/div[2]/div/table/thead/tr/td[24]')
        dayWasntTracked = False

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

            hourDataList.append(hourData[0].text)
            tempDataList.append(tempDataFloat)
            climateDataList.append(climateData[0].text)
            rainDataList.append(rainData[0].text)
            humidityDataList.append(humidityData[0].text)
            cloudDataList.append(cloudData[0].text)
            windDirectionList.append(windDirection[0].text)
            windVelocityList.append(windVelocity[0].text)
            windGustList.append(windGust[0].text)
            visibilityList.append(visibilityData[0].text)
    except:
        dayWasntTracked = True

    if (dayWasntTracked == False):
        data = {
        'dateOfData' : (f'{strDateOfData[0].text}-{yearDateOfData[0].text}'),
        'hourDataList' : hourDataList,
        'tempDataList' : tempDataList,
        'climateDataList' : climateDataList,
        'rainDataList' : rainDataList,
        'humidityDataList' : humidityDataList,
        'cloudDataList' : cloudDataList,
        'windDirectionList' : windDirectionList,
        'windVelocityList' : windVelocityList,
        'windGustList' : windGustList,
        'visibilityList' : visibilityList,
        }
        return data
    else:
        data = {
        'dateOfData' : (f'NO DATA'),
        'hourDataList' : f'NO DATA',
        'tempDataList' : f'NO DATA',
        'climateDataList' : f'NO DATA',
        'rainDataList' : f'NO DATA',
        'humidityDataList' : f'NO DATA',
        'cloudDataList' : f'NO DATA',
        'windDirectionList' : f'NO DATA',
        'windVelocityList' : f'NO DATA',
        'windGustList' : f'NO DATA',
        'visibilityList' : f'NO DATA',
        }
        return data


for i in range(364):
    time.sleep(1)
    wait = WebDriverWait(driver, 10)

    [webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform() for _ in range(3)]
    # try:
    #     dayOfTomorrow = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[11]/div[1]/button[2]')))
    #     driver.find_element(by="xpath", value='/html/body/div[11]/div[1]/button[2]').click()
    # except:
    #     try:
    #         dayOfTomorrow = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[11]/div[1]/button[2]')))
    #         driver.find_element(by="xpath", value='/html/body/div[11]/div[1]/button[2]').click()
    #     except:
    #         print("2023 BTT COULDN'T BE CLICKED")


    # GET DATA
    data = getData()

    try:
        dayOfTomorrow = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/a[2]/button')))
        driver.find_element(by="xpath", value='/html/body/div[5]/a[2]/button').click()
        print("DIA: {0}".format(data["dateOfData"]))

    except:
        wait = WebDriverWait(driver, 3)
        webdriver.ActionChains(driver).send_keys(Keys.HOME).perform()
        dayOfTomorrow = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/a[2]/button')))
        driver.find_element(by="xpath", value='/html/body/div[5]/a[2]/button').click()
        print("DIA: {0}".format(data["dateOfData"]))

    if (pastDay != data["dateOfData"]):
        with open(f'DataSet2024.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            csv_writer.writerow(data["dateOfData"])
            for i1, i2, i3, i4, i5, i6, i7, i8, i9, i10 in zip(data["hourDataList"], data["tempDataList"], data["climateDataList"], data["rainDataList"],
                                                               data["humidityDataList"], data["cloudDataList"], data["windDirectionList"],
                                                               data["windVelocityList"],
                                                               data["windGustList"], data["visibilityList"]):
                csv_writer.writerow([i1, i2, i3, i4, i5, i6, i7, i8, i9, i10])

        hourDataList.clear()
        tempDataList.clear()
        climateDataList.clear()
        rainDataList.clear()
        humidityDataList.clear()
        cloudDataList.clear()
        windDirectionList.clear()
        windVelocityList.clear()
        windGustList.clear()
        visibilityList.clear()

        pastDay = data["dateOfData"]
    else:
        i -= 1
        try:
            print("Trying to fix duplicate day")
            hourDataList.clear()
            tempDataList.clear()
            climateDataList.clear()
            rainDataList.clear()
            humidityDataList.clear()
            cloudDataList.clear()
            windDirectionList.clear()
            windVelocityList.clear()
            windGustList.clear()
            visibilityList.clear()
            print("Data about error: " + data["dateOfData"])
            dayOfTomorrow = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/a[2]/button')))
            driver.find_element(by="xpath", value='/html/body/div[5]/a[2]/button').click()
            print("Fix sucessful")
        except:
            print("Fix unsucessful")