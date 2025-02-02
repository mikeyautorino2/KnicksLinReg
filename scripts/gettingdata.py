from bs4 import BeautifulSoup, Comment
import requests
import pandas as pd
import csv

url = "https://www.basketball-reference.com/leagues/NBA_2025_advanced.html#advanced"
#Mimick human request header to access data
HEADERS = {
    "Accept" : "*/*",
    "Accept-encoding" : "gzip, deflate, br, zstd",
    "Accept-language": "men-US,en;q=0.9",
    "User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
response = requests.get(url , headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")
table_data = soup.find_all('table',id="advanced")
table_data = table_data[0]
import csv

headers = []
header_row = table_data.find('tr')  #the first <tr> contains headers
if header_row:
    headers = [th.text.strip() for th in header_row.find_all('th')[1:]]#skip rk for formatting 

data = []
for row in table_data.find_all('tr'):
    td_cells = row.find_all('td')
    if not td_cells:
        # skip rows with no <td> (could be empty or header row)
        continue

    row_data = []
    for cell in td_cells:
        # checking if the <td> contains an <a> tag
        link = cell.find('a')
        if link:
            row_data.append(link.text.strip())  # text from <a> and strip whitespace
        else:
            row_data.append(cell.text.strip())  # text from <td> and strip whitespace
    data.append(row_data)

# Write headers and data to a CSV file
with open('output.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=' ')
    if headers:
        writer.writerow(headers)  # Write header row
    writer.writerows(data)  
      # Write data rows
