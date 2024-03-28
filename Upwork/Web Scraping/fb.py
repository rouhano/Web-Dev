from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import mysql.connector
import time
import datetime
import csv
import os

# Set up database connection
# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="",
#     database="gaido"
# )

# # Set up cursor
# mycursor = mydb.cursor()

# # Set up SQL query
# sql = "INSERT INTO jobs (job_name, job_company, job_location, job_link, job_description, job_reqs_list, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

# Set up the Selenium driver with the options to maximize the browser window

url = input("Enter the facebook group url: \n")

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Navigate to the website

driver.get(url)

# Get the original URL
original_url = driver.current_url


# Wait for the job list to load
fb_feed = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located(
    (By.XPATH, '//*[@id="mount_0_0_my"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div[2]/div/div/div/div[2]/div[2]')))

# //*[@id="mount_0_0_my"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/div/div/div/div/div[8]/div/div

name = driver.find_element(By.XPATH, '//*[@id=":r2p:"]/span/span/a/strong').text
print("NAMEEEEE: ", name)
# # Loop through job listings
# jobs = []
# for i in range(1, 3):
#     try:
#         # Get current timestamp
#         current_timestamp = datetime.datetime.now()
        
#         # Wait for the ith job listing to be present on the page
#         jobs_list = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
#             (By.XPATH, '//*[@id="next-app"]/div[3]/div[2]/div[1]/div[2]/div[' + str(i) + ']')))
        
#         # Wait before hovering on the element
#         time.sleep(1)
        
#         # Hover on the element
#         hover = ActionChains(driver).move_to_element(jobs_list)
#         hover.perform()
        
#         # Wait before clicking on the element
#         time.sleep(1)
        
#         # Click on the element
#         jobs_list.click()
        
#         # Wait before fetching the popped-up element
#         time.sleep(1)
        
#         # Fetch the popped-up element
#         new_tab_job_details = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
#             (By.XPATH, '//*[@id="next-app"]/div[3]/div/main/section[1]')))
#         job_link = driver.current_url
#         print("Job Link: " + job_link)

#         job_name = driver.find_element(
#             By.XPATH, '//*[@id="jobDetaiPagelHead"]/div/div[1]/div[1]/h1').text
#         print("JOB TITLE: " + job_name)

#         job_company = driver.find_element(
#             By.XPATH, '//*[@id="next-app"]/div[3]/div/aside/section[2]/a[1]/h5').text
#         print("JOB Company: " + job_company)

#         job_salary = driver.find_element(
#             By.XPATH, '//*[@id="jobDetaiPagelHead"]/div/div[1]/div[2]').text
#         print("Salary: " + job_salary)

#         job_location = driver.find_element(
#             By.XPATH, '//*[@id="jobDetaiPagelHead"]/div/div[2]').text.split('\n')[0]
#         print("Location: " + job_location)


#         job_skill_parent = driver.find_element(
#             By.XPATH, '//*[@id="next-app"]/div[3]/div/main/section[1]/div[2]/div[2]')
#         job_skill_children = job_skill_parent.find_elements(
#             By.XPATH, '*')
        
#         job_skills = []
#         # print(type(len(job_skill_children)))
#         for skill in range(len(job_skill_children)):
#             # if(job_skills == ""):                
#             #     job_skills = job_skill_children[skill].text
#             # else:
#             #     job_skills = ",".join([job_skills, job_skill_children[skill].text])
#             if(not(job_skill_children[skill].text == '')):
#                 job_skills.append(job_skill_children[skill].text)
#         print("Job Skills: ", job_skills)
        
#         # //*[@id="next-app"]/section/div/div/main/section[1]/div[2]/div[3]

#         job_description = driver.find_element(
#             By.XPATH, '//*[@id="next-app"]/div[3]/div/main/section[1]/div[2]/div[3]/div').text
#         print("Description: " + job_description)


#         job_req_parent = driver.find_element(
#             By.XPATH, '//*[@id="next-app"]/div[3]/div/main/section[1]/div[4]/div[2]/div[1]')
#         job_req_child_quali = job_req_parent.find_element(
#             By.XPATH, '//*[@id="next-app"]/div[3]/div/main/section[1]/div[4]/div[2]/div[1]/ul')
#         # job_quali_child_list = job_req_child_quali.find_element(
#         #     By.XPATH, '//*[@id="next-app"]/section/div/div/main/section[1]/div[4]/div[2]/ul')
#         job_quali_child_contents = job_req_child_quali.find_elements(
#             By.XPATH, '*')

#         job_qualifications = []
#         for i in range(len(job_quali_child_contents)):
#             # if(job_qualifications == ""):                
#             #     job_qualifications = job_quali_child_contents[i].text
#             # else:
#             #     # job_qualifications = ",".join([job_qualifications, job_quali_child_contents[i].text])
#             if(not(job_quali_child_contents[i].text == '')):
#                 job_qualifications.append(job_quali_child_contents[i].text)
#         print("\nJob Qualifications: ", job_qualifications)

#         job_skills.extend(job_qualifications)
#         print("Combined: ", job_skills)
#         val = (str(job_name), str(job_company), str(job_location), str(
#             job_link), str(job_description), str(job_skills), str(current_timestamp), str(current_timestamp))

#         # mycursor.execute(sql, val)
#         # mydb.commit()
#         jobs.append(str(job_name), str(job_company), str(job_location), str(
#             job_link), str(job_description), str(job_skills))
#         # Get the current URL
#         current_url = driver.current_url
        
#         # Check if the current URL is not the original URL
#         if current_url != original_url:
#             print("Redirected to another page. Going back to original URL.")
#             driver.back()
#             continue
#     except:
#         print("Error occurred. Skipping to the next job listing.")
#         pass

# Close the driver
# mycursor.close()
# mydb.close()
driver.quit()

# Print "FINISHED" when done
print("FINISHED")

# print("JOBSSSS: \n",jobs)
# Define the CSV file path
# csv_file_path = 'jobs.csv'

# # Check if the CSV file already exists
# file_exists = os.path.isfile(csv_file_path)

# # Open the CSV file in append mode if it exists, otherwise create a new file
# mode = 'a' if file_exists else 'w'

# # Open the CSV file in the appropriate mode
# with open(csv_file_path, mode, newline='', encoding='utf-8') as csvfile:
#     # Create a CSV writer object
#     writer = csv.DictWriter(csvfile, fieldnames=jobs[0].keys())

#     # Write the headers to the CSV file if it is a new file
#     if not file_exists:
#         writer.writeheader()

#     # Write the job data to the CSV file
#     writer.writerows(jobs)

# print('Job data has been saved to', csv_file_path)
