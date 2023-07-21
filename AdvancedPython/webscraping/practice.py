import re
import requests
import bs4

# result = requests.get("http://www.example.com")
# print(type(result))
# print(result.text)

# soup = bs4.BeautifulSoup(result.text, "lxml")
# print(soup)
# print(soup.select("title")[0].getText())

# site_paragraphs = soup.select("p")
# print(type(site_paragraphs[0]))

# res = requests.get("https://en.wikipedia.org/wiki/Ratan_Tata")

# soup = bs4.BeautifulSoup(res.text, 'lxml')

# first_item = soup.select(".vector-toc-text > .vector-toc-numb")[0]
# print(first_item.text)
# for item in soup.select(".vector-toc-text > .vector-toc-numb"):
#     print(item.getText())

# print(soup.select('.image'))

# tata = soup.select(".thumbimage")[0]
# print(tata['src'])

# image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/1/11/Ratan_Tata.jpg")

# with open("my_image.jpg", "wb") as f_image:
#     f_image.write(image_link.content)


base_url = "https://books.toscrape.com/catalogue/page-{}.html"

two_start_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    print(scrape_url)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')
    # print(books)

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_start_titles.append(book_title)

print(two_start_titles)