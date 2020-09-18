from subprocess import call
import re
import sys
import webbrowser

print("""\

  ___  _____ _____    _____                     _     
 / _ \|_   _|  _  |  /  ___|                   | |    
/ /_\ \ | | | | | |  \ `--.  ___  __ _ _ __ ___| |__  
|  _  | | | | | | |   `--. \/ _ \/ _` | '__/ __| '_ \ 
| | | |_| |_\ \_/ /  /\__/ /  __/ (_| | | | (__| | | |
\_| |_/\___/ \___/   \____/ \___|\__,_|_|  \___|_| |_|
                                                     
                    """)

links = []

filename = 'C:\\Users\\TestoW\\Documents\\Coding\\definition-search\\searches.txt'

def aiosearch():
    searchtype = input(
        '[1] Regular Search\n[2] Definition\n[3] Google Maps\n[4] Youtube\n[5] Github\n[6] StackOverflow\nWhat type of search is this for? (example: 3): ')
    try:
        with open(filename) as linkListFile:
            for line in linkListFile:
                link = line.strip()
                if link != '':
                    if re.match('http://.+|https://.+|ftp://.+|file://.+', link.lower()):
                        links.append(link)
                    elif searchtype == "1":
                        links.append('https://www.google.com/search?q=' + link)
                    elif searchtype == "2":
                        subject = input("What subject/class is this for? ")
                        links.append('https://www.google.com/search?q=' + link + ' ' + subject + ' definition')
                    elif searchtype == "3":
                        links.append('http://maps.google.com/?q=' + link)
                    elif searchtype == "4":
                        links.append('https://www.youtube.com/results?search_query=' + link)
                    elif searchtype == "5":
                        links.append('https://github.com/search?q=' + link)
                    elif searchtype == "6":
                        links.append('https://stackoverflow.com/search?q=' + link)
                    else:
                        print(
                            "Something went wrong, make sure you filled the searches.txt file, and gave the program the correct path. inside")
    except IOError:
        print('Failed to open the file "%s".\nExiting.')
        sys.exit()
    print(links)
    for lnk in links:
        webbrowser.open_new_tab(lnk)

aiosearch()
