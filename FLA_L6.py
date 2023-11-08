import requests
from bs4 import BeautifulSoup

req = requests.get("http://books.toscrape.com/")

a = req.content
c = req.text 
 
soup = BeautifulSoup(a, "html.parser")

# Ex 1 - Extract BOOKS TO SCRAPE WE LOVE BEING SCRAPED!

print("Ex 1: ")
header1 = soup.find("header").text
print(header1)

print("\n")


# Ex 2 - Extract PAGE 1 FROM 50

print("Ex 2: ")
li1 = soup.find("li", attrs = {"class" : "current"}).text
print(li1)

print("\n")


# Ex 3 - Extract the content CONTENT OF THE BUTTON TAG

print("Ex 3: ")
button1 = soup.find("button").text
print(button1)

print("\n")


# Ex 4 - Use the name of the class (product_pod) in order to extract the products title and price
# Create a regular expression in order to get the title from it
# Create a regular expression in order to get the price from it

print("Ex 4: ")

products = soup.find_all("article", class_="product_pod")

for product in products:
    
    reg1 = product.find("h3").find("a")["title"]
    reg2 = product.find("p", class_="price_color").text
    print(reg1, reg2)
    
print("\n")

    
# Ex 5 - Extract all the book categories (hint: find all class, iterate through the result and find li)

print("Ex 5: ")

div = soup.find('div', class_='side_categories')

if div:
    
    ul = div.find('ul')
    
    if ul:
        
        lis = ul.find_all('li')
        
        titles = [li.get_text(strip=True) for li in lis]
        
        for title in titles:
            print(title)
 
print("\n")

# Ex 6 - Extract the content of img alt="" (hint: find all img, regex for alt content)

print("Ex 6: ")
 
images = soup.find_all('img')

content = [image['alt'] for image in images if 'alt' in image.attrs]

print(content)

