from subprocess import call
import re
import sys
import webbrowser
from dhooks import Webhook, Embed


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
hook = Webhook('')
if hook == '':
    hook = input("What's the webhook? ")
else:
    print("Webhook detected")


def successhook():

    embed = Embed(
        title='AIO Search Executed Successfully',
        description="AIO Search Program was able to open you're defined searches",
        color=0x00ff1e,
        timestamp='now'  # sets the timestamp to current time
    )

    image1 = 'https://avatars2.githubusercontent.com/u/25069719?s=460&u=0758922d6a85a09f971fbf778bb720788a2f2e5b&v=4'

    embed.set_footer(text='AIO Search | Made by iHildy#3839', icon_url=image1)

    hook.send(embed=embed)

def badhook():
    embed = Embed(
        title='AIO Search Failed',
        description="AIO Search Program was un-able to open you're defined searches",
        color=0xff0000,
        timestamp='now'  # sets the timestamp to current time
    )
 
    image1 = 'https://avatars2.githubusercontent.com/u/25069719?s=460&u=0758922d6a85a09f971fbf778bb720788a2f2e5b&v=4'

    embed.add_field(name='Test Field', value='Value of the field :open_mouth:')
    embed.add_field(name='Another Field', value='1234 :smile:')
    embed.set_footer(text='AIO Search | Made by iHildy#3839', icon_url=image1)

    hook.send(embed=embed)

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
                        successhook()
                    elif searchtype == "1":
                        links.append('https://www.google.com/search?q=' + link)
                        successhook()
                    elif searchtype == "2":
                        subject = input("What subject/class is this for? ")
                        links.append('https://www.google.com/search?q=' + link + ' ' + subject + ' definition')
                        successhook()
                    elif searchtype == "3":
                        links.append('http://maps.google.com/?q=' + link)
                        successhook()
                    elif searchtype == "4":
                        links.append('https://www.youtube.com/results?search_query=' + link)
                        successhook()
                    elif searchtype == "5":
                        links.append('https://github.com/search?q=' + link)
                        successhook()
                    elif searchtype == "6":
                        links.append('https://stackoverflow.com/search?q=' + link)
                        successhook()
                    else:
                        print(
                            "Something went wrong, you might not have typed the number in right.")
                        badhook()

    except IOError:
        print('Something went wrong, make sure you filled the searches.txt file correctly, and gave the program the correct path inside')
        sys.exit()
    print(links)
    for lnk in links:
        webbrowser.open_new_tab(lnk)




aiosearch()
