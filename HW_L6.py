import requests
from bs4 import BeautifulSoup

import pandas as pd # for Ex.2

req = requests.get("https://www.scrapethissite.com/pages/simple/")

a = req.content
c = req.text

soup = BeautifulSoup(a, "html.parser")

# Ex 1 - Extract

# a) Country Name

print("Ex 1.a): ")

country_names = [h3.get_text(strip = True) for h3 in soup.find_all('h3', class_='country-name')]

for country_name in country_names:
    print(country_name)

print("\n")

# b) Capital

print("Ex 1.b): ")

country_capitals = [span.get_text(strip = True) for span in soup.find_all('span', class_='country-capital')]

for country_capital in country_capitals:
    print(country_capital)

print("\n")

# c) Population  

print("Ex 1.c): ")

country_populations = [span.get_text(strip = True) for span in soup.find_all('span', class_='country-population')]

for country_population in country_populations:
    print(country_population)

print("\n")

# d) Area 
 
print("Ex 1.d): ")
 
country_areas = [span.get_text(strip = True) for span in soup.find_all('span', class_='country-area')]

for country_area in country_areas:
    print(country_area)

print("\n")

# Ex 2 - Create an excel file with columns "CountryName", "Capital", "Population", "Area" and populate it with the information extracted from the website

"""

print("Ex 2: ")

countries = soup.find_all('div', class_='country')

country_names = []
country_capitals = []
country_populations = []
country_areas = []

for country in countries:
    
    country_name = country.find('h3', class_='country-name').get_text(strip=True)
    country_names.append(country_name)
    
    capital = country.find('span', class_='country-capital').get_text(strip=True)
    country_capitals.append(capital)
    
    population = country.find('span', class_='country-population').get_text(strip=True)
    country_populations.append(population)
    
    area = country.find('span', class_='country-area').get_text(strip=True)
    country_areas.append(area)

df = pd.DataFrame({
    'CountryName': country_names,
    'Capital': country_capitals,
    'Population': country_populations,
    'Area': country_areas
})

excelFilename = '/C/Users/Desktop/countries.xlsx'
df.to_excel(excel_filename, index=False)

print("--------------Excel file succesfully created! :)")
print("\n")

"""

# Ex 3 - Extract the links from SCRAPE THIS SITE, SANDBOX, LESSONS, FAQ

print("Ex 3: ")

links = {}

nav_links = soup.find_all('a', class_='nav-link')

for nav_link in nav_links:
    links[nav_link.get_text(strip=True)] = nav_link['href']

for href in links.items():
    print(href)
    
print("\n")

# Ex 4 - Extract LESSONS AND VIDEOS HARTLEY BRODY 2018

print("Ex 4: ")

footer_section = soup.find('section', id='footer')
footer_text = footer_section.get_text(strip=True)

print(footer_text)

print("\n")
