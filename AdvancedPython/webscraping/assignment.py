import bs4
import requests

response = requests.get("http://quotes.toscrape.com/")

soup = bs4.BeautifulSoup(response.text, 'lxml')

authors = []
quotes = []
unique_authors = []
authors_array = soup.select('.author')
for author in authors_array:
    authors.append(author.text)
# print(authors)

quotes_array = soup.select(".text")
for quote in quotes_array:
    quotes.append(quote.text)
# print(quotes)

tags_box = soup.select(".col-md-4.tags-box .tag-item .tag")

# for tag in tags_box:
#     print(tag.text)

base_url = "https://quotes.toscrape.com/page/"
authors = set()
page = 1
page_valid = True
while page_valid:
    scrape_url = base_url + str(page)
    print(scrape_url)
    resp = requests.get(scrape_url)
    if "No quotes found!" in resp.text:
        page_valid = False
    else:
        sup = bs4.BeautifulSoup(resp.text, 'lxml')
        for author in sup.select('.author'):
            if author.text:
                authors.add(author.text)
    page  = int(page) + 1

print(authors)

# for i in range(1, 11):
#     scrape_url = base_url.format(i)
#     resp = requests.get(scrape_url)

#     sup = bs4.BeautifulSoup(resp.text, 'lxml')
#     auth = sup.select('.author')
#     for author in auth:
#         if author not in unique_authors:
#             unique_authors.append(author.text)

# print(set(unique_authors))

# resp = requests.get("https://quotes.toscrape.com/page/13/")
# sup = bs4.BeautifulSoup(resp.text, 'lxml')
# auth = sup.select('.author')
# print(auth)




