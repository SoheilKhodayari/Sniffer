
from BeautifulSoup import *
from urllib2 import *
import re

class EmailScraper():
    def __init__(self):
        self.emails = []

    def reset(self):
        self.emails = []

    def collectAllEmail(self, soup):

        email_pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
        self.emails = list(set(re.findall(email_pattern, soup)))

    def collectEmail(self, soup):

        email_pattern = re.compile("<a\s+href=\"mailto:([a-zA-Z0-9._@]*)\">", re.IGNORECASE)
        self.emails = re.findall(email_pattern, soup)
    def __str__(self):
        return '{0}'.format(self.emails)

#x=EmailScraper()

#f=open('C:/Users/soheil/Desktop/pdf doros/1.htm')
#soup=BeautifulSoup(urlopen('http://www.python.org').read())
#f=open('me.htm','w+')
#f.write(soup.prettify())

#x.collectAllEmail(f.read())
#x = list(set(x))
#print(x)


