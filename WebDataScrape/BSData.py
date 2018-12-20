

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

myURL = "http://pna.fi/tty"


open_url = uReq(myURL)
page_data = open_url.read()
open_url.close()

parsed = soup(page_data, "html.parser")

restaurants = parsed.findAll("ul", {"class":"food"})
num_of_restaurants = len(restaurants)
print("Found ", num_of_restaurants, " open restaurants from TUT.", sep="")


# Parse the segments of the page
left = parsed.findAll("div", {"class":"left"})
middle = parsed.findAll("div", {"class":"middle"})
right = parsed.findAll("div", {"class":"right"})


# Left side of pge
left_lists = left[0].findAll("ul")
Newton = left_lists[0].findAll("li")
Konehuone = left_lists[1].findAll("li")


# Middle part of page
middle_lists = middle[0].findAll("ul")
Reaktori = middle_lists[0].findAll("li")
Fusari  = middle_lists[1].findAll("li")


# Right side of page
right_lists = right[0].findAll("ul")
Hertsi =  right_lists[0].findAll("li")

Kaikki = [Newton, Konehuone, Reaktori, Fusari, Hertsi]
nimet = ["Newton", "Konehuone", "Reaktori", "Fusari", "Hertsi"]

for i in range(len(Kaikki)):
    print("\n", nimet[i], ":\n")
    for ruoka in Kaikki[i]:
        ruoka = str(ruoka)
        siistitty = ruoka[ruoka.index(">")+1:]
        siistitty2 = siistitty[:siistitty.index("<")]
        print(siistitty2)
input("\n\nPress Enter to close.")