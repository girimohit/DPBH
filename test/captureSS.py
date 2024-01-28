import time
from selenium import webdriver
from PIL import Image
from PIL import ImageDraw
from io import BytesIO
import pytesseract
# import tesseract

# Set the path for Tesseract OCR
amazon_url = "https://www.amazon.in/boAt-Launched-Airdopes-141-ANC/dp/B0C7QS9M38/ref=sr_1_4?_encoding=UTF8&content-id=amzn1.sym.e08c6279-844d-49c6-8e7c-3fcd4b905908&pd_rd_r=e967339c-148c-469f-ac3f-9d0522b2f7d4&pd_rd_w=i81cd&pd_rd_wg=16OSk&pf_rd_p=e08c6279-844d-49c6-8e7c-3fcd4b905908&pf_rd_r=DS6WC1JXDT2AACYZ7PZZ&qid=1706385721&sr=8-4"


def capture_screenshot_with_message(url, message):
    # Set up the web driver (assuming Chrome here)
    driver = webdriver.Chrome()

    # Navigate to the Amazon product page
    driver.get(url)

    # Wait for some time for the page to load (you might need to adjust this)
    time.sleep(3)

    # Add a message at the top of the page
    driver.execute_script(
        "var element = document.createElement('div'); element.style.position = 'fixed'; element.style.top = '0'; element.style.left = '0'; element.style.background = 'white'; element.style.padding = '10px'; element.innerText = arguments[0]; document.body.appendChild(element);",
        message,
    )

    # Wait for the message to be added
    time.sleep(2)

    # Capture screenshot
    screenshot = driver.get_screenshot_as_png()

    # Close the browser window
    driver.quit()

    return screenshot


def extract_text_from_screenshot(screenshot):
    # Open the screenshot using PIL
    image = Image.open(BytesIO(screenshot))

    # Perform OCR
    text = pytesseract.image_to_string(image)
    return text.strip()


# Example usage with an Amazon product URL
# amazon_product_url = input("Enter a URL: ")
screenshot = capture_screenshot_with_message(amazon_url, "Customised Message")
text = extract_text_from_screenshot(screenshot)
print(f"Detected text: {text}")
