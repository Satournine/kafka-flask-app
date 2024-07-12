import requests
from bs4 import BeautifulSoup


def web_scraper():
    URL = "https://scrapeme.live/shop/"
    try:
        response = requests.get(URL)
    except requests.RequestException as e:
        print(f'main page fetch: {e}')
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    products = []
    product_list = soup.select("ul.products li.product")
    for product in product_list:
        product_link = product.select_one("a")['href']
        product_details = scrape_product_details(product_link)
        products.append(product_details)

    return products


def scrape_product_details(link):
    try:
        response = requests.get(link)
    except requests.RequestException as e:
        print(f'details page fetch: {e}')
        return None
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.select_one(".product_title.entry-title").text
    price = soup.select_one(".price .woocommerce-Price-amount").text
    description = soup.select_one(".woocommerce-product-details__short-description p").text.strip()
    stock = soup.select_one(".stock").text.strip()

    return {
        "name": title,
        "price": price,
        "description": description,
        "stock": stock
    }
