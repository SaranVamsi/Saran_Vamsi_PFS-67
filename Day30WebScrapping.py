'''
Web Scraping - Process of automatically collecting info from websites using a program

Where is it used:

1)Extracting article headlines
2)Collecting product data
3)Gathering job listings
4)Collecting publicly availabe reasearch data

1. Website

Contains information you want

2. Python program

Downloads the webpage using requests

3. Extract information

Uses BeautifulSoup to find the required data

4. Output

Displays or saves the extracted data

Important Python libraries: 

1) Requets Modules - The request library allows python to send HTTP request to websites and recieve 
                     their response.
   o/p : HTML Code 

2) BeautifulSoup - Requests download HTML, but we need a convenient way to find a particular
                   ele inside it.
   o/p : list of quotes, with each quote printed on a separate
         line.

3) pandas - Stores and analyzes collected data

4) csv - Saves data in CSV files




Status Codes:
1. 200 - request successful
2. 201 - Created
3. 301 or 302 - redirected
4. 403 - Access Forbidden
5. 404 - Page not found
6. 500 - Server Error
'''


# import requests

# url = "https://www.brandforce.com/domain/Username.com"

# response = requests.get(url)

# print(response.status_code)
# print(response.text)


# import requests

# url = "https://www.brandforce.com/domain/Username.com"
# try :
#     response = requests.get(url, timeout = 10)
#     response.raise_for_status()
#     print(response.text)
# except requests.requestException as error :
#     print("Request Failed: ", error)

# from bs4 import BeautifulSoup

# html = """
# <html>
# <head>
#     <title>My First Website</title>
# </head>
# <body>
#     <h1>Welcome to python</h1>
#     <p>Learn web scraping</p>
# </body>
# </html>
# """

# soup = BeautifulSoup(html, "html.parser")

# print(soup.title)
# print(soup.title.get_text())
# print(soup.h1.get_text())
# print(soup.p.get_text())



# soup.find("p")
 

# import requests
# from bs4 import BeautifulSoup

# url = "https://theuselessweb.com"
# resp = requests.get(url, timeout=10)
# resp.raise_for_status()

# soup = BeautifulSoup(resp.text, "html.parser")
# title = soup.title.get_text(strip=True)
# heading = soup.find("h1").get_text(strip=True)

# print("Title", title)
# print("Heading", heading)


# import requests
# from bs4 import BeautifulSoup
# url = "https://theuselessweb.com"
# resp = requests.get(url, timeout = 10)
# resp.raise_for_status()
# soup = BeautifulSoup(resp.text, "html.parser")
# link = soup.find_all("a")
# for link in link :
#     text = link.get_text(strip = True)
#     url = link.get("href")
#     print("Link: ", text)
#     print("URL: ", url)


