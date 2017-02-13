# instruction link:
# https://docs.google.com/document/d/1DBgjp7lV_TQkurwoYs3J7Pg0Va4WkAVpbaBEikH-Q1I/edit

#proj2.py
from urllib import request
from bs4 import BeautifulSoup

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here

def nyt_headlines():
	nyt = request.urlopen('http://nytimes.com').read()
	nyt_soup = BeautifulSoup(nyt, 'lxml')
	i = 0
	for h2 in nyt_soup.find_all('h2'):
		if h2.get('class')[0] == "story-heading":
			print(h2.get_text())
			i+=1
			if i > 9:
				break
	
nyt_headlines()

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here

def most_read_michigandaily():
	michidaily = request.urlopen('https://www.michigandaily.com/').read()
	michidaily_soup = BeautifulSoup(michidaily, 'lxml')
	for div in michidaily_soup.find_all('div'):
		if div.get('class'):
			if "view-most-read" in div.get('class'):
				for li in div.find_all('li'):
					print(li.get_text())
			
most_read_michigandaily()


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here

def alt():
	cats = request.urlopen('http://newmantaylor.com/gallery.html').read()
	cats_soup = BeautifulSoup(cats, 'lxml')
	for img in cats_soup.find_all('img'):
		if img.get('alt'):
			print(img.get('alt'))
		else:
			print("No alternative text provided!")
alt()


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here

def in_page(link):
	page = request.urlopen(link).read()
	page_soup = BeautifulSoup(page, 'lxml')
	email_lst = []
	for div in page_soup.find_all('div'):
		if div.get('class'):
			if "field-name-contact-details" in div.get('class'):
				node = div.a.get('href')
				contact = request.urlopen('https://www.si.umich.edu'+node).read()
				contact_soup = BeautifulSoup(contact, 'lxml')
				for div in contact_soup.find_all('div'):
					if div.get('class'):
						if "field-type-email" in div.get('class'):
							email_lst.append(div.a.get_text())
	return email_lst


def umsi_emails():
	email_lst_nested = []
	for i in range(6):
		if i == 0:
			umsi_link = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
		else:
			umsi_link = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4&page='+str(i)
		email_lst_nested.append(in_page(umsi_link))
	email_lst_flat = [item for sublist in email_lst_nested for item in sublist]
	for item in email_lst_flat:
		print("%d %s" % (email_lst_flat.index(item)+1, item))

umsi_emails()

