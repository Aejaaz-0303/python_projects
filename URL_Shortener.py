import pyshorteners

url=input("Enter the url you want to short: ")
def shorturl(url):
    urlobj=pyshorteners.Shortener()
    print(urlobj.tinyurl.short(url))
shorturl(url)
