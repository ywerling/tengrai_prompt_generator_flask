from flask import Blueprint, render_template, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Webscrapping of the Adobe stock photos page
# Provides the description of the pictures corresponding to the search query
# limited to the first result page
# the displayed lines can be used as prompts for generating AI image

# Create a blueprint for the Adobe functionality
adobe_bp = Blueprint('adobe', __name__, url_prefix='/scrape')

# Define constants
ADOBE_STOCK_IMAGES_URL = "https://stock.adobe.com/"
WEBSCRAPPER_SLEEP_INTERVAL = 1


# Function to initialize the Selenium WebDriver
def init_webdriver():
    # Setting up the Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run headless Chrome for better performance
    driver = webdriver.Chrome(options=options)
    return driver


# Function to scrape Adobe Stock Images using Selenium
def scrape_adobe_images(query):
    print(f"Query: {query}")
    driver = init_webdriver()
    try:
        driver.get(ADOBE_STOCK_IMAGES_URL)
        time.sleep(WEBSCRAPPER_SLEEP_INTERVAL)

        # Example search functionality on Adobe Stock
        search_box = driver.find_element(By.NAME, "keyword")
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        time.sleep(WEBSCRAPPER_SLEEP_INTERVAL)

        # Example of extracting image data
        # images = driver.find_elements(By.CLASS_NAME, "image-class")  # Replace with actual class name
        # image_urls = [image.get_attribute('src') for image in images]

        images = driver.find_elements(By.XPATH, "//img[@alt]")
        # for image in images:
        #     print(f'{image.get_attribute("alt")}{image.get_attribute("name")}\n')

        return images

    finally:
        # driver.quit()
        time.sleep(WEBSCRAPPER_SLEEP_INTERVAL)


# Route to handle Adobe scraping
@adobe_bp.route("/scrape", methods=["GET", "POST"])
def scrape():
    images = []
    search_term = ""
    print("scrape called")
    if request.method == "POST":
        print("scrape post")
        search_term = request.form.get("topic")
        images = scrape_adobe_images(search_term)
        # for image in images:
        #     print(f'{image.get_attribute("alt")}{image.get_attribute("name")}\n')
        return render_template('adobe.html',
                               images=images,
                               topic=search_term)

    return render_template('adobe.html',
                           images=None,
                           topic=search_term)
