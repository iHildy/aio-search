from subprocess import call
import re
import sys
import win32com.client

print("""\

  ___  _____ _____   _____                     _     
 / _ \|_   _|  _  | /  ___|                   | |    
/ /_\ \ | | | | | | \ `--.  ___  __ _ _ __ ___| |__  
|  _  | | | | | | |  `--. \/ _ \/ _` | '__/ __| '_ \ 
| | | |_| |_\ \_/ / /\__/ /  __/ (_| | | | (__| | | |
\_| |_/\___/ \___/  \____/ \___|\__,_|_|  \___|_| |_|
                                                     
                    """)


links = []

filename = 'C:\\Users\\TestoW\\Documents\\Coding\\definition-search\\searches.txt'

#https://github.com/search?q=
#https://www.google.com/search?q=
#https://www.vocabulary.com/dictionary/
#https://www.dictionary.com/browse/
#http://maps.google.com/?q=
#https://www.youtube.com/results?search_query=
#https://stackoverflow.com/search?q=

def aiosearch():
    searchtype = input(
    '[1] Regular Search\n[2] Definition\n[3] Google Maps\n[4] Youtube\n[5] Github\n[6] StackOverflow\nWhat type of search is this for? (example: 3): ')
    if searchtype == "1":
        try:
            with open(filename) as linkListFile:
                for line in linkListFile:
                    link = line.strip()
                    if link != '':
                        if re.match('http://.+|https://.+|ftp://.+|file://.+', link.lower()):
                            links.append(link)
                        else:
                            links.append('https://www.google.com/search?q=' + link)
        except IOError:
            print ('Failed to open the file "%s".\nExiting.')
            sys.exit()
        print (links)
        sh = win32com.client.Dispatch('WScript.Shell')
        for lnk in links:
            sh.run(lnk)
    elif searchtype == "2":
        subject = input("What subject/class is this for? ")
        try:
            with open(filename) as linkListFile:
                for line in linkListFile:
                    link = line.strip()
                    if link != '':
                        if re.match('http://.+|https://.+|ftp://.+|file://.+', link.lower()):
                            links.append(link)
                        else:
                            links.append(
                                'https://www.google.com/search?q=' + link + ' ' + subject + ' definition')
        except IOError:
            print('Failed to open the file "%s".\nExiting.')
            sys.exit()
        print(links)
        sh = win32com.client.Dispatch('WScript.Shell')
        for lnk in links:
            sh.run(lnk)
    elif searchtype == "3":
        try:
            with open(filename) as linkListFile:
                for line in linkListFile:
                    link = line.strip()
                    if link != '':
                        if re.match('http://.+|https://.+|ftp://.+|file://.+', link.lower()):
                            links.append(link)
                        else:
                            links.append('http://maps.google.com/?q=' + link)
        except IOError:
            print('Failed to open the file "%s".\nExiting.')
            sys.exit()
        print(links)
        sh = win32com.client.Dispatch('WScript.Shell')
        for lnk in links:
            sh.run(lnk)
    elif searchtype == "4":
        try:
            with open(filename) as linkListFile:
                for line in linkListFile:
                    link = line.strip()
                    if link != '':
                        if re.match('http://.+|https://.+|ftp://.+|file://.+', link.lower()):
                            links.append(link)
                        else:
                            links.append('https://www.youtube.com/results?search_query=' + link)
        except IOError:
            print('Failed to open the file "%s".\nExiting.')
            sys.exit()
        print(links)
        sh = win32com.client.Dispatch('WScript.Shell')
        for lnk in links:
            sh.run(lnk)
    elif searchtype == "5":
        try:
            with open(filename) as linkListFile:
                for line in linkListFile:
                    link = line.strip()
                    if link != '':
                        if re.match('http://.+|https://.+|ftp://.+|file://.+', link.lower()):
                            links.append(link)
                        else:
                            links.append(
                                'https://github.com/search?q=' + link)
        except IOError:
            print('Failed to open the file "%s".\nExiting.')
            sys.exit()
        print(links)
        sh = win32com.client.Dispatch('WScript.Shell')
        for lnk in links:
            sh.run(lnk)
    elif searchtype == "6":
        try:
            with open(filename) as linkListFile:
                for line in linkListFile:
                    link = line.strip()
                    if link != '':
                        if re.match('http://.+|https://.+|ftp://.+|file://.+', link.lower()):
                            links.append(link)
                        else:
                            links.append(
                                'https://stackoverflow.com/search?q=' + link)
        except IOError:
            print('Failed to open the file "%s".\nExiting.')
            sys.exit()
        print(links)
        sh = win32com.client.Dispatch('WScript.Shell')
        for lnk in links:
            sh.run(lnk)
    else:
        print('Something went wrong, make sure you filled the searches.txt file')

aiosearch()
