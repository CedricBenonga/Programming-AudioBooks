import requests
from bs4 import BeautifulSoup


URL = "https://www.audible.com/search?keywords=programming+books&ref-override=a_search_t1_header_search&k=" \
      "programming+books&crid=28KL4V4FRMBSC&sprefix=programming+books%2Cna-audible-us%2C316&i=na-audible-us&url=" \
      "search-alias%3Dna-audible-us&ref=nb_sb_noss_2"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# titles & links
all_books = soup.select(selector="li h3 a")
titles = []
links = []
for book in all_books:
    # titles
    title = book.getText()
    titles.append(title)
    # links
    link = f'https://www.audible.com/{book.get("href")}'
    links.append(link)

# authors
all_authors = soup.find_all(name="a", class_="bc-link bc-color-link")
mix_list = []
for a in all_authors:
    mix_list.append(a.getText())

authors = [mix_list[3], mix_list[7], mix_list[11], mix_list[15], mix_list[19], mix_list[23], mix_list[27], mix_list[32],
           mix_list[38], mix_list[42], mix_list[47], mix_list[51], mix_list[55], mix_list[59], mix_list[63],
           mix_list[67], mix_list[72], mix_list[77], mix_list[81], mix_list[87]]

# prices
all_prices = soup.find_all(name="span", class_="bc-text bc-size-base bc-color-base")
prices = []
for price in all_prices:
    book_price = price.getText()
    if "$" in book_price:
        prices.append(book_price.replace("\n", "").replace(" ", ""))

# saving data on a csv file
with open("programming_audiobooks.txt", mode="w") as file:
    n = -1
    for _ in range(len(titles) + 1):
        if n == -1:
            # headings
            file.write('row nbr, title, author, price, link\n')
        else:
            # data
            file.write(f'{n + 1}, {titles[n]}, {authors[n]}, {prices[n]}, {links[n]}\n')
        n += 1
