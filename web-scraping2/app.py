# In this project we r Scraping the List of larget comanies in the USA by using BeautifulSoup package 
from bs4 import BeautifulSoup
import requests
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
# print(soup)
# This prints the whole html data of the page 

table = soup.find_all('table')[1]

world_titles = table.find_all('th')
# print(world_titles)
# we are finding the tables which are lables with "th"

world_table_titles = [title.text.strip() for title in world_titles]
# print(world_table_titles)

df = pd.DataFrame(columns = world_table_titles)
# initilizing the columns 

column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

print(df)
# We are representing our data By DataFrames 