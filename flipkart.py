from urllib import response
import pandas as pd
from bs4 import BeautifulSoup
import requests
products_url='https://www.flipkart.com/search?q=top+mobile+smart+phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=top+mobile+smart+phone%7CMobiles&requestId=2d6af715-bf8d-4b0d-85f8-f6d0505df691&as-searchtext=top%20mo'

response=requests.get(products_url)
# print(response.status_code)
# print(response.content)
htmlcontent=response.content

soup=BeautifulSoup(htmlcontent,'html.parser')

titles=[]
prices=[]
ratings=[]
images=[]

# dictionary of lists  
dict = {'Title': titles, 'Price': prices, 'Rating': ratings, 'Images': images}  

for d in soup.find_all('div',attrs={'class':'_2kHMtA'}):
    title=d.find('div',attrs={'class':'_4rR01T'})
    # print(title.string)
    titles.append(title.string)

    price=d.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    # print(price.string)
    prices.append(price.string)

    rating=d.find('div',attrs={'class':'_3LWZlK'})
    # print(rating.text)
    ratings.append(rating.text)

    image=d.find('img',attrs={'class':'_396cs4 _3exPp9'})
    # print(image.get('src'))
    images.append(image.get('src'))


df = pd.DataFrame(dict) 

# saving the dataframe 
df.to_csv('TopMobile.xlsx')
df.to_csv('TopMobile.csv')

print("done")

