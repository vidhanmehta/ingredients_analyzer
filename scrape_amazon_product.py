import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/RIGHT4PAWS-10-8kg-Dog-Food-Biologically/dp/B0B15BC1CW/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.-7rZEa80_UMWRKLIgWl2fGq0HW61iL8oJqCEFjmBxRaBG7cEhxZ85p3BsRnJE2cux5i8RAQv0nc57zcWY9KzK6oJlW9iTmqLnigD_PE6shArL0rGk94OQJPwDbYhlrK3A2XG_1Ap4h1t9uSoI5556O9p5S7XhTjUf_YkTURXSxCJVi2t8mXhEO25nfDj8CHqtCx_CCoatR5XF1-GUVHotquwwVhc1-BKnGcchDUOrJ2jT_yVRMJpK5294YqCej6SYdm7oajlRh37yupc6oercpc3q7dGhRqMwXOqLxPuIHw.d7-01kcajRonFgTB1o48of9tzQ0-Xveg8QlQBytjAx0&dib_tag=se&keywords=food&qid=1714984445&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Scrape product title
    title_element = soup.select_one('#productTitle')
    title = title_element.text.strip()
    print(f"Product Title: {title}")

    # Scrape product rating
    rating_element = soup.select_one('#acrPopover')
    rating_text = rating_element.attrs.get('title')
    rating = rating_text.replace('out of 5 stars', '')
    print(f"Product Rating: {rating}")

    # Scrape product price
    price_element = soup.select_one('span.a-offscreen')
    price = price_element.text.encode('utf-8').decode('utf-8')
    print(f"Product Price: {price}")

    # Scrape product image
    image_element = soup.select_one('#landingImage')
    image = image_element.attrs.get('src')
    print(f"Product Image: {image}")

    # Scrape product description
    description_element = soup.select_one('#productDescription')
    description = description_element.text.strip()
    print(f"Product Description: {description}")

    # Additional details (example: number of reviews)
    reviews_element = soup.select_one('#acrCustomerReviewText')
    if reviews_element:
        reviews = reviews_element.text
        print(f"Number of Reviews: {reviews}")
    else:
        print("Number of Reviews: Not available")

else:
    print(str(response.status_code) + ' - Error loading the page')