from subprocess import call
import re
import sys

links = []

filename = '/Users/ianhildebrand/Desktop/Coding/Freshman Python/Tools/Personal/Auto Search/Searches3.txt'

try:
    with open(filename) as linkListFile:
        for line in linkListFile:
            link = line.strip()
            if link != '':
                if re.match('http://.+|https://.+|ftp://.+|file://.+', link.lower()):
                    links.append(link)
                else:
                    links.append('https://www.google.com/search?q=' + link)
                    #https://www.google.com/search?q=
                    #https://www.dictionary.com/browse/
                    #http://maps.google.com/?q=
except IOError:
    print ('Failed to open the file "%s".\nExiting.')
    sys.exit()

print (links)
call(["open"]+links)


