from urllib import response
import pandas as pd
from bs4 import BeautifulSoup
import requests
titles=[]
prices=[]

images=[]
# for multipage
for i in range(1,42):
    products_url=(f'https://www.flipkart.com/search?q=top+mobile+smart+phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=top+mobile+smart+phone%7CMobiles&requestId=2d6af715-bf8d-4b0d-85f8-f6d0505df691&as-searchtext=top+mo&page={str(i)}')

    response=requests.get(products_url)
    # print(response.status_code)
    # print(response.content)
    htmlcontent=response.content
    
    
    if(response.status_code==200):
        print("Data Fetched successfully",i)
        soup=BeautifulSoup(htmlcontent,'html.parser')
        
        for d in soup.find_all('div',attrs={'class':'_2kHMtA'}):
              title=d.find('div',attrs={'class':'_4rR01T'})
              print(title.string)
              titles.append(title.string)

              price=d.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
              print(price.string)
              prices.append(price.string)

              

              image=d.find('img',attrs={'class':'_396cs4 _3exPp9'})
              print(image.get('src'))
              images.append(image.get('src'))
       
    else:
        print(f"URL NOT FOUND OF PAGE NO.{i}")
 # dictionary of lists  
dict = {'Title': titles, 'Price': prices, 'Images': images}   
df = pd.DataFrame(dict) 
# saving the dataframe 
df.to_csv('Top_1000_SmartPhone.csv')
df.to_json('Top_1000_SmartPhone.json')

        
