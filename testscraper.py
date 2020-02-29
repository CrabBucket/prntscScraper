from bs4 import BeautifulSoup
import cfscrape
import shutil
import sys
import time
from random import randrange

def randomurlnums():
    urlnums = randrange(1,9999)
    if urlnums < 1000:
        while len(str(urlnums)) < 4:
            urlnums = '0'+str(urlnums)
    else:
        urlnums= str(urlnums)
    return urlnums
def randomurlletters():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    first = alphabet[randrange(25)]
    second = alphabet[randrange(25)]
    letters = first+second
    return letters


# I sleep inside here because I got an ip banned by cloud flare )=



#this function just takes a url that links to a .png file and saves it in the same directory with given filename
#we have to do this through an http request because of cloudflare
def urlImg2File(url,filename):
    time.sleep(0.1)
    response = scraper.get(url,stream=True)
    #this is where the writing to file happens idk the specifics stolen from stack overflow
    with open(f'{filename}.png','wb') as out_file:
        shutil.copyfileobj(response.raw,out_file)
    del response
random = False
starturl = 'https://prnt.sc/'
if len(sys.argv) == 2 or len(sys.argv) == 1:
    print('random url')
    random = True
    urlnums = 0
    
    if len(sys.argv)==1:
        stop = 100
    else:
        stop = int(sys.argv[1])

    
else:
    
    letters = sys.argv[1]

    urlnums = sys.argv[2]

    #each time we run it goes for 100
    stop = int(urlnums) + int(sys.argv[3])



if(stop>=10000):
    print('start number too high for the amount of pictures you want')
    quit()
#The scraper has to emulate a browser so we have to create an instance of a nodejs server to do that cfscrape allows that and here
#the fake browser is created
scraper = cfscrape.create_scraper()


while int(urlnums) < stop:
    if not random:
        url = starturl + letters + urlnums
    else:
        url = starturl + randomurlletters() + randomurlnums()
    print(url)
    #sleep get url grab data feed it into beautiful soup so we can iterate over it better
    time.sleep(0.1)
    page = scraper.get(url)
    data = page.text
    
    soup = BeautifulSoup(data, 'html5lib')

    image = None
    #for every link we find with the img tag
    for link in soup.find_all('img'):
        #we check if starts with https://image which was gotten through source inspection of prnt.sc
        tempurl = str(link.get('src'))
        if tempurl.startswith('https://image'):
            #increment url number to bruteforce look
            urlnums = str(int(urlnums) + 1)
            #we save our found png with a file name so we can get back to it from the url.
            if not random:
                urlImg2File(tempurl,letters+urlnums)
            else:
                urlImg2File(tempurl,url[16:])
            break
    else:
        urlnums = str(int(urlnums) + 1)
        if random:
            stop+=1
    continue


