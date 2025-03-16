from selenium import webdriver
import Fetcher

def redirect(link):

    final_url = []
    urls = Fetcher.fetch(link)

    # Use headless mode to run in the background
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)

    for url in urls:
        # Open the URL
        driver.get(url)

        # Get the final redirected URL
        final_url.append(driver.current_url)


    # Close the driver
    driver.quit()
    return(final_url)