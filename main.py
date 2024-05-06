import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape Amazon product details
def scrape_amazon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Scrape product title
        title_element = soup.select_one('#productTitle')
        title = title_element.text.strip()

        # Scrape product rating
        rating_element = soup.select_one('#acrPopover')
        rating_text = rating_element.attrs.get('title')
        rating = rating_text.replace('out of 5 stars', '')

        # Scrape product price
        price_element = soup.select_one('span.a-offscreen')
        price = price_element.text.encode('utf-8').decode('utf-8')

        # Scrape product image
        image_element = soup.select_one('#landingImage')
        image = image_element.attrs.get('src')

        # Scrape product description
        description_element = soup.select_one('#productDescription')
        description = description_element.text.strip()

        # Additional details (example: number of reviews)
        reviews_element = soup.select_one('#acrCustomerReviewText')
        if reviews_element:
            reviews = reviews_element.text
        else:
            reviews = "Not available"

        return {
            "title": title,
            "rating": rating,
            "price": price,
            "image": image,
            "description": description,
            "reviews": reviews
        }
    else:
        return None

# Function to analyze ingredients using Gemini API
def analyze_ingredients(ingredients):
    # Use Gemini API to analyze ingredients and identify harmful ones
    # Replace this with Gemini API call

    # Dummy response for demonstration
    return {"harmful_ingredients": ["Artificial flavorings", "High-fructose corn syrup"]}

# Main Streamlit app
def main():
    st.title("Ingredient Analyzer")

    # Get user input (Amazon URL)
    amazon_url = st.text_input("Enter Amazon URL of the product:")

    if st.button("Analyze Ingredients"):
        # Scrape Amazon product details
        product_details = scrape_amazon(amazon_url)

        if product_details:
            st.subheader("Product Details")
            st.write("Title:", product_details["title"])
            st.write("Rating:", product_details["rating"])
            st.write("Price:", product_details["price"])
            st.image(product_details["image"])
            st.write("Description:", product_details["description"])
            st.write("Number of Reviews:", product_details["reviews"])

            # Analyze ingredients using Gemini API
            ingredients = []  # Extract ingredients from product details
            analysis_result = analyze_ingredients(ingredients)

            st.subheader("Ingredient Analysis")
            if analysis_result:
                harmful_ingredients = analysis_result.get("harmful_ingredients", [])
                if harmful_ingredients:
                    st.write("Harmful Ingredients Found:")
                    for ingredient in harmful_ingredients:
                        st.write("- ", ingredient)
                    st.warning("This product contains harmful ingredients.")

                    # Recommend alternative products
                    st.subheader("Recommendations")
                    # Implement recommendation logic based on harmful ingredients
                else:
                    st.success("No harmful ingredients found.")
            else:
                st.error("Failed to analyze ingredients.")
        else:
            st.error("Failed to fetch product details from Amazon.")

if __name__ == "__main__":
    main()
