from bs4 import BeautifulSoup, Comment
import pandas as pd
import time
import numpy as np
import requests

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
def tableParser(table_data):
    with open('player_data.csv', 'w', encoding="utf-8") as r:
        #Write the header row if it exists (<th> cells)
        header_row = table_data.find('tr')
        if header_row:
            th_cells = header_row.find_all('th')
            if th_cells:
                # Write each <th> text, padded for neat spacing
                for header in th_cells:
                    r.write(header.text.ljust(30))
                r.write('\n')

        #write the data rows (<td> cells)
        for row in table_data.find_all('tr'):
            td_cells = row.find_all('td')
            if not td_cells:
                # Skip rows with no <td> (could be empty or another header row)
                continue

            for cell in td_cells:
                r.write(cell.text.ljust(30))
            r.write('\n')
tableParser(table_data)













    
