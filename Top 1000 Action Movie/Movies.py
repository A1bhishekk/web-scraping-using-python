from unicodedata import name
import pandas as pd
from bs4 import BeautifulSoup
import requests

movie_name=[]
year=[]
time=[]
genre=[]
rating=[]
votes=[]
gross_collection=[]

for i in range(1,1000,50):
    products_url=(f'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&sort=user_rating,desc&start={i}&ref_=adv_nxt')

    response=requests.get(products_url)
    # print(response.status_code)
    # print(response.content)
    htmlcontent=response.text
    if(response.status_code==200):
        print("Data Fetched successfully",i)
        soup=BeautifulSoup(htmlcontent,'html.parser')

        
        movies_data=soup.find_all('div',attrs={'class':'lister-item mode-advanced'})
        # print(movies_data)
        for store in movies_data:
            name = store.h3.a.text
            movie_name.append(name)
            print(name)

            year_of_release = store.h3.find('span',attrs={'class':'lister-item-year text-muted unbold'}).text
            year.append(year_of_release)
            print(year_of_release)

            runtime=store.p.find('span',attrs={'class':'runtime'}).text
            time.append(runtime)
            # print(runtime)


            genres=store.p.find('span',attrs={'class':'genre'}).text
            genre.append(genres)
            # print(genre)

            rate=store.find('div',attrs={'class':'inline-block ratings-imdb-rating'}).text
            rating.append(rate)
            # print(rate)
            
            value=store.find_all('span',attrs={'name':'nv'})
            vote=value[0].text
            votes.append(vote)
            # print(vote)

            collection=value[1].text if len(value) > 1 else '$na'
            gross_collection.append(collection)
            # print(collection) 

    else:
        print(f"URL NOT FOUND OF PAGE NO.{i}")
    
     # dictionary of lists  
dict = {'NAME': movie_name, 'YEAR': year, 'TIME': time,'GENRE':genre,'RATING':rating,'VOTES':votes,'GROSS_COLLECTION':gross_collection}   
df = pd.DataFrame(dict) 
# saving the dataframe 
df.to_csv('Top_1000_Action_Movie.csv')