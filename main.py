from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import csv

WEBSITE = 'https://www.tiempo3.com/north-america/mexico/baja-california/mexicali?page=today'
PATH = "Z:\ChromeDriver\chromedriver.exe"
DATAPATH = 'Z:\ElTruDataSet'


service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE)

hourBtt = driver.find_element(by='xpath', value='//*[@id="intervals-1"]')
hourBtt.click()

time.sleep(8)
hourDataList = ["HORA:"]
tempDataList = ["TEMPERATURA:"]
climateDataList = ["CLIMA:"]
rainDataList = ["PROBABILIDAD LLUVIA"]
humidityDataList = ["HUMEDAD:"]
cloudDataList = ["NUBOSIDAD:"]
windDirectionList = ["DIRECCION DEL VIENTO:"]
windVelocityList = ["VELOCIDAD DEL VIENTO (Km/h):"]
windGustList = ["RAFAGA DEL VIENTO (Km/h):"]
visibilityList = ["VISIBILIDAD:"]

for i in range(24):
    hourData = driver.find_elements(by='xpath', value=f'/html/body/div[6]/div[2]/table/thead/tr/td[{i + 1}]')
    tempData = driver.find_elements(by='xpath', value=f'/html/body/div[6]/div[2]/table/tbody/tr[1]/td[{i + 1}]')
    climateData = driver.find_elements(by='xpath', value=f'/html/body/div[6]/div[2]/table/tbody/tr[2]/td[{i + 1}]/div')
    rainData = driver.find_elements(by='xpath', value=f'/html/body/div[6]/div[2]/table/tbody/tr[3]/td[{i + 1}]')
    humidityData = driver.find_elements(by='xpath', value=f'/html/body/div[6]/div[2]/table/tbody/tr[5]/td[{i + 1}]')
    cloudData = driver.find_elements(by='xpath', value=f'/html/body/div[6]/div[2]/table/tbody/tr[10]/td[{i + 1}]')
    windDirection = driver.find_elements(by='xpath', value=f'/html/body/div[6]/div[2]/table/tbody/tr[9]/td[{i + 1}]/span')
    windVelocity = driver.find_elements(by='xpath', value=f'/html/body/div[6]/div[2]/table/tbody/tr[6]/td[{i + 1}]/span[1]')
    windGust = driver.find_elements(by='xpath', value=f'/html/body/div[6]/div[2]/table/tbody/tr[7]/td[{i + 1}]/span[1]')
    visibilityData = driver.find_elements(by='xpath', value=f'/html/body/div[6]/div[2]/table/tbody/tr[12]/td[{i + 1}]/span[1]')

    hourDataList.append(hourData[0].text)
    tempDataList.append(tempData[0].text)
    climateDataList.append(climateData[0].text)
    rainDataList.append(rainData[0].text)
    humidityDataList.append(humidityData[0].text)
    cloudDataList.append(cloudData[0].text)
    windDirectionList.append(windDirection[0].text)
    windVelocityList.append(windVelocity[0].text)
    windGustList.append(windGust[0].text)
    visibilityList.append(visibilityData[0].text)


with open('dataSet24feb.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    for i1, i2, i3, i4, i5, i6, i7, i8, i9, i10 in zip(hourDataList, tempDataList, climateDataList, rainDataList,
                                                  humidityDataList, cloudDataList, windDirectionList, windVelocityList,
                                                  windGustList, visibilityList):
        csv_writer.writerow([i1, i2, i3, i4, i5, i6, i7, i8, i9, i10])


# DELAY OF 10 SECONDS
time.sleep(10)
# DELAY END


