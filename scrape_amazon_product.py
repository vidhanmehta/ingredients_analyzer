import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/Kitchens-India-Daily-Treat-Makhani/dp/B00LJVDWSG/ref=sr_1_8_f3_0o_fs?sr=8-8"




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Scrape product title
    title_element = soup.select_one('#productTitle')
    title = title_element.text.strip() if title_element else "Not found"
    print(f"Product Title: {title}")

    # Scrape product price
    price_element = soup.select_one('span.a-offscreen')
    price = price_element.text.encode('utf-8').decode('utf-8') if price_element else "Not found"
    print(f"Product Price: {price}")

    # Scrape product image
    image_element = soup.select_one('#landingImage')
    image = image_element.attrs.get('src') if image_element else "Not found"
    print(f"Product Image: {image}")

    # Scrape product ingredients
    ingredients_element = soup.find('div', {'id': 'important-information'})
    if ingredients_element and ingredients_element.find('h4', string='Ingredients:'):
        ingredients_text = ingredients_element.find('h4', string='Ingredients:').find_next('p').text.strip()
        ingredients_list = [ingredient.strip() for ingredient in ingredients_text.split(',')]
        print(f"Product Ingredients: {ingredients_list}")
    else:
        print("Product Ingredients: Not available")

else:
    print(str(response.status_code) + ' - Error loading the page')
