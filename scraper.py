import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 1. Configuration
url = "https://kissanstore.pk/wheat-price-in-pakistan/"

# 2. Fetch the webpage
# Adding a 1-second delay to respect robots.txt (Assignment Requirement)
time.sleep(1)
page = requests.get(url)
print(f"Page Response: {page}")

soup = BeautifulSoup(page.text, 'html')
print(soup)

print(soup.prettify())

print(soup.find('table').prettify())

soup.find_all('table')

target_table = soup.find('table')
headers = target_table.find_all('th')

table_titles = [title.get_text(separator=' ', strip=True) for title in headers]
print("Found these headers:", table_titles)

df = pd.DataFrame(columns=table_titles)

df

rows = target_table.find_all('tr')

for row in rows[1:]:
    row_data = row.find_all(['td', 'th'])
    
    individual_row_data = [data.get_text(strip=True) for data in row_data]
    if len(individual_row_data) == len(df.columns):
        length = len(df)
        df.loc[length] = individual_row_data
print(df.head())

df.to_csv('kissan_wheat_prices.csv', index=False)