import math
import sys
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://gatech.co1.qualtrics.com/jfe/form/SV_3wMI1pXNJOwLJL8")

pers_info_path = sys.argv[1]
pers_info_file = open(pers_info_path)
pers_info_lines = pers_info_file.readlines()
ra_name = pers_info_lines[0].strip()
ra_community = pers_info_lines[1].strip()
ra_building = pers_info_lines[2].strip()

interactions_path = sys.argv[2]
interactions_data = pd.read_csv(interactions_path)

for index, interaction in interactions_data.iterrows():
    start = time.time()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"QR~QID36\"]")))
    res_com_dropdown = Select(driver.find_element(By.XPATH, "//*[@id=\"QR~QID36\"]"))
    res_com_dropdown.select_by_visible_text(str(ra_community))

    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"NextButton\"]")))
    driver.find_element(By.XPATH, "//*[@id=\"NextButton\"]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"QR~QID45\"]")))

    time.sleep(1)
    name_dropdown = Select(driver.find_element(By.XPATH, "//*[@id=\"QR~QID45\"]"))
    name_dropdown.select_by_visible_text(str(ra_name))

    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"NextButton\"]")))
    driver.find_element(By.XPATH, "//*[@id=\"NextButton\"]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"QR~QID2\"]")))

    resident_name = interaction["Name"]
    driver.find_element(By.XPATH, "//*[@id=\"QR~QID2\"]").send_keys(resident_name)

    building_dropdown = Select(driver.find_element(By.XPATH, "//*[@id=\"QR~QID39\"]"))
    building_dropdown.select_by_visible_text(str(ra_building))

    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"NextButton\"]")))
    driver.find_element(By.XPATH, "//*[@id=\"NextButton\"]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"QR~QID94\"]")))

    floor_dropdown = Select(driver.find_element(By.XPATH, "//*[@id=\"QR~QID94\"]"))
    floor_dropdown.select_by_index(int(interaction["Floor"]))

    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"NextButton\"]")))
    driver.find_element(By.XPATH, "//*[@id=\"NextButton\"]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"QR~QID79\"]")))

    time.sleep(1)
    apt_dropdown = Select(driver.find_element(By.XPATH, "//*[@id=\"QR~QID79\"]"))
    apt_dropdown.select_by_visible_text(str(interaction["Apt"]))

    time.sleep(1)
    bedroom_dropdown = Select(driver.find_element(By.XPATH, "//*[@id=\"QR~QID91\"]"))
    bedroom_dropdown.select_by_visible_text(str(interaction["Bedroom"]))

    interaction_date = str(interaction["mm-dd-yyyy"])
    driver.find_element(By.XPATH, "//*[@id=\"QR~QID3\"]").send_keys(interaction_date)

    for method in str(interaction["Methods"]):
        driver.find_element(By.XPATH, f"//*[@id=\"QID48-{method}-label\"]").click()

    for topic in str(interaction["Topics"]):
        driver.find_element(By.XPATH, f"//*[@id=\"QID41-{topic}-label\"]").click()

    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"NextButton\"]")))
    driver.find_element(By.XPATH, "//*[@id=\"NextButton\"]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"QR~QID49\"]")))

    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"QR~QID49\"]").send_keys(
        str(interaction["Optional"]) if not math.isnan(float(interaction["Optional"])) else ""
    )

    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"NextButton\"]")))
    driver.find_element(By.XPATH, "//*[@id=\"NextButton\"]").click()

    end = time.time()

    print(end - start)