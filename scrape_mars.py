



#dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time





#chrome path
executable_path = {"executable_path":"/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless = False)





# NASA news URL
url = "https://mars.nasa.gov/news/"
browser.visit(url)
html = browser.html
soup = bs(html,"html.parser")




news_title = soup.find("div",class_="content_title").text
news_paragraph = soup.find("div", class_="article_teaser_body").text
print(f"Title: {news_title}")
print(f"Para: {news_paragraph}")


# In[5]:


#visit url for image
url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url_image)
time.sleep(1)
soup = bs(html,"html.parser")





# find the newest image
featured_image_list = []
for image in soup.find_all('div',class_="img"):
    featured_image_list.append(image.find('img').get('src'))





feature_Image = featured_image_list[0]
feature_Image_url = "https://www.jpl.nasa.gov/" + feature_Image
feature_Image_dict = {"image": feature_Image_url}
print("Feature Image URL:", feature_Image_url)





url_Mars_Weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_Mars_Weather)
time.sleep(1)
html = browser.html
soup = bs(html,"html.parser")





weather_info_list = []
for weather_info in soup.find_all('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
    weather_info_list.append(weather_info.text)


]

#latest Mars Information
Latest_Mars_Weather = weather_info_list[0]
mars_weather_dict = {"mar_weather": Latest_Mars_Weather }

print('Latest Mars Weather:',Latest_Mars_Weather)





#Generate DataFrame
df_Mars_Facts = pd.read_html("https://space-facts.com/mars/")
df_Mars_Facts = df_Mars_Facts[0]
df_Mars_Facts.rename_axis({0:"Parameters", 1:"Values"},axis=1, inplace=True)





df_Mars_Facts





#convert the data to a HTML table string
df_Mars_Facts_table = df_Mars_Facts.to_html("df_Mars_Facts_Table.html",index=False)
df_Mars_Facts_dict = {"df_Mars_Facts": df_Mars_Facts_table}





#Set Up for Mars Hemisperes
url_Mars_Hemisperes = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url_Mars_Hemisperes)
html = browser.html
soup = bs(html,"html.parser")





mars_hemisperes_title_list = []
for img_title in soup.find_all('div',class_="description"):
    mars_hemisperes_title_list.append(img_title.find('h3').text)





mars_hemisphere_image_url = []
for image in soup.find_all('div',class_="item"):
    url = "https://astrogeology.usgs.gov/"
    mars_hemisphere_image_url.append(url + image.find('img').get('src'))
mars_hemisphere_image_url






full_image_url = []
for each_url in mars_hemisphere_image_url:
    split_url = each_url.split(".tif_thumb.png")[0]
    image_url = split_url + ".tif/full.jpg"
    full_image_url.append(image_url)




full_image_url




hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": full_image_url[1]},
    {"title": "Cerberus Hemisphere", "img_url": full_image_url[0]},
    {"title": "Schiaparelli Hemisphere", "img_url": full_image_url[1]},
    {"title": "Syrtis Major Hemisphere", "img_url": full_image_url[2]},
]





image_one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
image_two = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
image_three = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
image_four = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

full_image = {"image_one": image_one, "image_two":image_two, "image_three":image_three, "image_four":image_four}





full_image['image_one']

