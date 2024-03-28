import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape job details
def scrape_job_details(job_url):
    job_page = requests.get(job_url)
    job_soup = BeautifulSoup(job_page.content, 'html.parser')
    job_details = {}

    # Get job title
    job_title = job_soup.find('h1', class_='job-header-title').text.strip()
    job_details['Title'] = job_title

    # Get job company
    job_company = job_soup.find('a', class_='job-header-company').text.strip()
    job_details['Company'] = job_company

    # Get job location
    job_location = job_soup.find('span', class_='job-header-location').text.strip()
    job_details['Location'] = job_location

    # Get job description
    job_description = job_soup.find('div', class_='job-description').text.strip()
    job_details['Description'] = job_description

    # Get job requirements
    job_requirements = job_soup.find('div', class_='job-requirements').text.strip()
    job_details['Requirements'] = job_requirements

    # Get job skills/software
    job_skills = []
    job_softwares = []
    job_tags = job_soup.find_all('div', class_='job-tags')
    for tag in job_tags:
        if tag.find('span', class_='job-tag skill-tag'):
            skill = tag.find('span', class_='job-tag skill-tag').text.strip()
            job_skills.append(skill)
        elif tag.find('span', class_='job-tag software-tag'):
            software = tag.find('span', class_='job-tag software-tag').text.strip()
            job_softwares.append(software)
    job_details['Skills'] = ', '.join(job_skills)
    job_details['Software'] = ', '.join(job_softwares)

    return job_details

# Function to scrape job listings
def scrape_job_listings(job_title):
    url = 'https://www.bossjob.ph/jobs?q=' + job_title.replace(' ', '+')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    job_listings = soup.find_all('div', class_='card-content')

    # Write job details to CSV file
    with open(job_title + '_jobs.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Title', 'Company', 'Location', 'Description', 'Requirements', 'Skills', 'Software']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for job_listing in job_listings:
            # Get job URL
            job_url = job_listing.find('a', class_='job-title')['href']

            # Scrape job details
            job_details = scrape_job_details(job_url)

            # Write job details to CSV file
            writer.writerow(job_details)

    print('Job listings saved to ' + job_title + '_jobs.csv')

# Example usage
job_title = input('Enter job title: ')
scrape_job_listings(job_title)
