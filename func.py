research_later = "#string to search"

def first_link(research_later):
    from urllib.parse import unquote
    goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + research_later


    r = requests.get(goog_search)

    soup = BeautifulSoup(r.text, "lxml")

    links = soup.select('div > a')
    linkslist=[]
    urllist=[]

    for i in range(len(links)):
        linkslist.append(str(links[i]))

    pattern='<a href="/url?'
    for string in linkslist:
        a = re.search(pattern,string)
        if a is None:
            continue
        else:
            ele=string
            tup = a.span()
            (start,stop)=tup
            raw = ele[start:]
            final_link=raw.split(';')[0][16:-4]
            url = unquote(final_link)
            urllist.append(url)
            
        
    
    return urllist
    




def product_details(prod_link):
    
    from bs4 import BeautifulSoup
    import requests
  
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
  
    webpage = requests.get(prod_link, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

    try:
            title = soup.find("span", attrs={"id": 'productTitle'})
  
            title_value = title.string
  
            title_string = title_value.strip().replace(',', '')
    except AttributeError:
            title_string = "NA"
        
    print("product Title = ", title_string)

    try:
            price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '')
   
    except AttributeError:
            price = "NA"
    print("Products price = ", price)
  
    try:
                rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
    except:
                rating = "NA"
    print("Overall rating = ", rating)
