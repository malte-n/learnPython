#! python3
# searchpypi.py  - Opens several search results.

import requests, sys, webbrowser, bs4

print("Searching...")  # display text while downloading the search result page
res = requests.get("https://pypi.org/search/?q=" + " ".join(sys.argv[1]))
res_2 = requests.get("https://pypi.org/search/?q=" + " ".join(sys.argv[2]))
res.raise_for_status()
print(res.status_code)
# TODO: Retrieve top search result links.
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")
# Open a browser tab for each result.
linkElems = soup.find_all("a", attrs={"class": "package-snippet"})

# TODO: Open a browser tab for each result.
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = "https://pypi.org/" + linkElems[i].get("href")
    print("Opening", urlToOpen)
    webbrowser.open(urlToOpen)
