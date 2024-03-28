import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


# Get the Facebook group URL from the user
group_url = input('Enter the Facebook group URL: ')

options = Options()
options.add_argument("--start-minimized")
driver = webdriver.Chrome(options=options)

# Function to check if the 'Q' key was pressed twice
def is_q_pressed(keys):
    return len(keys) >= 2 and keys[-1].upper() == 'Q' and keys[-2].upper() == 'Q'

# Function to scrape the post details
def scrape_post(post):
    name_element = post.find_element(By.XPATH , '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]')
    caption_element = post.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div/div')

    name = name_element.text
    caption = caption_element.text
    # Check if the post has photos
    # photos = []
    # photo_elements = post.find_elements(By.XPATH, '//*[@id=":r17:"]/div[1]/a')
    # for photo_element in photo_elements:
    #     photos.append(photo_element.get_attribute('href'))

    return name, caption

# Load the group page
driver.get(group_url)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# Wait for the page to load
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div[1]/div[2]/div[2]')))
# print("asdasdasd")
print("zxczxczs")
                                        

keys = []
scroll_count = 3

while True:
    scroll_count += 1
    print("\nScroll Count:", scroll_count)
    time.sleep(3)
    container = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div[1]/div[2]/div[2]')
    
    post_xpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div['+ str(scroll_count) + ']'
    posts = container.find_element(By.XPATH, post_xpath)
    
    # last_post = container.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]')
    # posttt = driver.find_elements(By.CLASS_NAME, 'x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z')
    # num_elements = len(posttt)
    # print("Number of elements found:", num_elements)
    # Scroll to the last post element
    # driver.execute_script("arguments[0].scrollIntoView();", last_post)
    
    # # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
    name, caption = scrape_post(posts)
    print('Name:', name)
    print('Caption:', caption)
    print('\n+---------------------+\n')


    # Delay for 5 seconds before scrolling again
    time.sleep(1)

# Close the browser
driver.quit()
