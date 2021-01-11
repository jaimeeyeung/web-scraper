import requests
from bs4 import BeautifulSoup

URL = "https://www.monster.com/jobs/search/?q=Software-Developer&where=San-Francisco__2C-CA"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = 'ResultsContainer')
print(results.prettify())

job_elems = results.find_all('section', class_ = 'card-content')
for job_elem in job_elems:
    print(job_elem, end = '\n'*2) # finding all the HTML code for the job listings

#printing out the relevent job info
for job_elem in job_elems: #job_elem is a BeautifulSoup object
    job_title = job_elem.find('h2', class_ = 'title')
    job_comp = job_elem.find('div', class_ = 'company')
    job_location = job_elem.find('div', class_ = 'location')
    print(job_title)
    print(job_comp)
    print(job_location)
    print()

# only retrieving the text, no HTML elements, so that it is easier to read
for job_elem in job_elems:  # job_elem is a BeautifulSoup object
    print(job_title.text.strip())
    print(job_comp.text.strip())
    print(job_location.text.strip())
    print()

python_jobs = results.find_all('h2', string = 'Python Developer')
python_jobs = results.find_all('h2',
                               string=lambda text: 'python' in text.lower()) #trying to find a job with python
print(len(python_jobs))

# this will give you the jobs that include python in the job title
for p_jon in python_jobs:
    link = p_jon.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")
