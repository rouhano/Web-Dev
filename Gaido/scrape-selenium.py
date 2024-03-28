from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.bossjob.ph/jobs?q='

driver = webdriver.Chrome()
driver.get(url)

# time.sleep(5)
wait = WebDriverWait(driver, 20)


# jobs = wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[1]/div[1]/div[1]')))
# print(jobs)
# jobs1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[1]/div[1]/div[1]')
# print(jobs1.text)
# for job in jobs:

# job_title =  wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[2]/div/div/div[2]/div[5]/ul/li[1]')))

# job_skills =  wait.until(EC.visibility_of_element_located(
#     (By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[2]/div/div/div[2]/div[5]/ul')))

job_skills =  wait.until(EC.visibility_of_all_elements_located(
    (By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[2]/div/div/div[2]/div[5]/ul/li[1]')))


job_title = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/a/span')
print(job_title.text)


responsibilities = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/ul')
res_list = []
for respo in responsibilities:
    jobs2 = respo.find_element(
        By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/ul/li[1]').text
    res_list.append(respo.text)

responsibilities_list = res_list[0].split("\n")
print(responsibilities_list)

print("---------------------------")

# requirements = driver.find_element(By.CLASS_NAME, 'JobDetail_jobDetailSectionBody__EzTzQ JobDetail_jobDetailRequirementSectionBody__aBY_t')
# req_list = []
# for require in requirements:
#     jobs2 = require.find_element(
#         By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/ul/li[1]').text
#     req_list.append(respo.text)

# requirements_list = req_list[0].split("\n")
# print(requirements_list)


jobs1 = driver.find_elements(By.CLASS_NAME, 'JobDetail_jobDetailSkillsItem__OEQMn')
skills_list = []
for skills in jobs1:
    jobs2 = skills.find_element(
        By.XPATH, '//*[@id="__next"]/div[1]/div[4]/div/div[2]/div[2]/div/div/div[2]/div[5]/ul/li[1]/span').text
    skills_list.append(skills.text)
print(skills_list)




