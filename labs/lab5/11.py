import requests from bs4 import BeautifulSoup  
url = "https://news.ycombinator.com/"  
response = requests.get(url)  
soup = BeautifulSoup(response.text, 'lxml')  
titles = soup.find_all('a', class_='storylink')  
for title in titles:  
    print(title.text)