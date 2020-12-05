#!/usr/bin/env python
# coding: utf-8

# In[33]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[5]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[6]:

def scrape():

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)


    # In[10]:


    html = browser.html
    soup = bs(html, "html.parser")
    print(soup.prettify)


    # In[11]:


    element = soup.select_one("ul.item_list li.slide")
    title = element.find("div", class_="content_title").get_text()
    print(title)


    # In[12]:


    paragraph = element.find("div", class_="article_teaser_body").get_text()
    print(paragraph)


    # In[25]:


    url_2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_2)


    # In[26]:


    click_one = browser.find_by_id("full_image").click()


    # In[27]:


    click_two = browser.find_link_by_partial_text("more info").click()


    # In[28]:


    html_2 = browser.html
    soup_2 = bs(html_2, "html.parser")
    print(soup_2.prettify)


    # In[29]:


    image = soup_2.find("figure.lede a img")


    # In[31]:


    image = soup_2.find_all("figure", class_="lede")
    results = image[0].a["href"]
    print(results)


    # In[32]:


    featured_image_url = "https://www.jpl.nasa.gov"+ results
    print(featured_image_url)


    # In[35]:


    url_3 = "https://space-facts.com/mars/"
    html_file = pd.read_html(url_3)
    print(html_file)


    # In[38]:


    len(html_file)


    # In[42]:


    df = html_file[0]


    # In[43]:


    df.columns=["Facts", "Values"]


    # In[45]:


    df_html = df.to_html(index = False)


    # In[46]:


    url_4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_4)


    # In[47]:


    html_4 = browser.html
    soup_4 = bs(html_4, "html.parser")
    print(soup_4.prettify)


    # In[50]:


    items = soup_4.find_all("div", class_="item")
    items


    # In[51]:


    item_list = []

    for item in items:
        url_re = item.find("a")["href"]
        title = item.find("div", class_="description").find("a").find("h3").text
        url_fin = "https://astrogeology.usgs.gov" + url_re
        browser.visit(url_fin)
        html_4 = browser.html
        soup_4 = bs(html_4, "html.parser")
        img_fin = soup_4.find("div", class_= "downloads").find("ul").find("li").find("a")["href"]
        item_list.append({"Title":title, "Final_image": img_fin})

    print(item_list)


    # In[ ]:
    nasa_scrape = {"title":title, "paragraph":paragraph, "df_html":df_html, "item_list":item_list} 
    return nasa_scrape
    



