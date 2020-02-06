import time
from selenium import webdriver
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('headless')
options.add_argument('window-size=0x0')
def get_page_html():
    print('opening browser')
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    custom_query="How to buy stocks"
    url="https://www.google.com/search?q="+custom_query
    url=url.replace(' ','+')
    print('Url: ',url)
    print('sending url')
    driver.get(url)
    time.sleep(7)
    return driver




def get_url(page_source,total_urls):
    bs=BeautifulSoup(page_source,features='html.parser');
    print('**********displaying the links')
    counter=0
    starting_index=40
    url_list=[]
    for link in bs.find_all('a', href=True):
        counter=counter+1
        if counter>starting_index:
            url=str(link['href'])
            if url.startswith("https") and 'https://www.youtube' not in url:
                if(not len(url_list)>total_urls-1):
                    url_list.append(link['href'])
    if url_list:
        return url_list
    else:
        return 'No url found'



def get_paragraph(driver,urls):
    print(urls)
    for data in urls:
        driver.get(data)
        time.sleep(6)
        print('data is')
        bs1=BeautifulSoup(driver.page_source,features='html.parser')
        all_paragraphs=bs1.find_all('p')
        if len(all_paragraphs) >0:
            print('Data extracted from {}'.format(data))
            for line in all_paragraphs:
                print(line.getText())
            print('**********************')


driver=get_page_html()
print("Title ",driver.title)

total_urls=3
urls=get_url(driver.page_source,total_urls);

get_paragraph(driver,urls)