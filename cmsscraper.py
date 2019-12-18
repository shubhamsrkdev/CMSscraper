import os
import time
import requests
from bs4 import BeautifulSoup
from webbot import Browser

url = 'https://td.bits-hyderabad.ac.in/moodle/login/index.php'

web = Browser()
web.go_to(url)

web.click(text="Google") 

web.type('f20160184@hyderabad.bits-pilani.ac.in' , id='identifierId')
web.click(text="Next") 
time.sleep(2)
web.type('valuesrk18#', classname="Xb9hP")
web.click(text="Next") 
time.sleep(2)
web.go_to('https://td.bits-hyderabad.ac.in/moodle/my/')
html = web.get_page_source() 

soup = BeautifulSoup(html)
Courses = soup.find_all("div", class_="column")

for courses in Courses:
	web.go_to(courses.a['href'])
	html = web.get_page_source()
	soup = BeautifulSoup(html)
	Stuff = soup.find_all("div", class_="activityinstance")
	os.mkdir(courses.text)
	for stuff in Stuff:
		print ("Downloading "+stuff.text)
		if 'pdf' in stuff.img['src']:
			filename = stuff.text.replace(' File','') + '.pdf'
		elif 'document' in stuff.img['src']:
			filename = stuff.text.replace(' File','') + '.docx'
		elif 'powerpoint' in stuff.img['src']:
			filename = stuff.text.replace(' File','') +'.ppt'
		elif 'spreadsheet' in stuff.img['src']:
			filename = stuff.text.replace(' File','') + '.xlsx'			
		else:
			continue
		r = requests.get(stuff.a['href'], allow_redirects=True)
		filename = filename.replace('/','').replace('\\','')
		filename = os.path.join(courses.text, filename)
		open(filename, 'wb').write(r.content)

	


