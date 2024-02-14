import os, sys
import urllib.parse
import validators
import requests
from datetime import datetime

print("Number of argumets: ", len(sys.argv))  #ile argumentów przekazał użytkownik podczas uruchamiania programu, pierwszym jest
                                              # zawsze nazwa uruchomionego programu - z terminala np. python main.py onet.pl
print("Arguments list:", sys.argv)

url = "https://duckduckgo.com"
if len(sys.argv) > 1:
    url = sys.argv[1]

print("Website to download: ", url)

sciptDir = os.path.dirname(__file__)
os.chdir(sciptDir)
print("Current working dir: ", os.getcwd())

if not os.path.exists("/websites"):
    os.mkdir("/websites")


parseUrl = urllib.parse.urlparse(url)
print(parseUrl) #ParseResult(scheme='https', netloc='duckduckgo.com', path='', params='', query='', fragment='')


#pip install validators # ściągamy bo chcemy sprawdzać czy adres jest prawidłowy
validFlag = validators.url(url)
if validFlag:
    print("Url: ", url, " is valid")
else:
    print("Url: ", url, " is invalid")
    raise Exception("Bad URL!")


# zaczynamy pobieranie zawartości strony
response = requests.get(url, allow_redirects=True) #strony internetowe moga przekierowywac
if response.ok == True:
    print("Response ok for url: ", url)
    now = datetime.now()
    dateString = now.strftime("%d.%m.%Y %H.%M.%S")
    print(dateString)
    fileName = "./websites/" + parseUrl.netloc + " " + dateString + ".html"
    fh = open(fileName, "wb")
    fh.write(response.content)
    fh.close()
