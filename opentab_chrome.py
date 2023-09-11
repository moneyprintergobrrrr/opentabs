from selenium import webdriver

# List of URLs to open
urls_to_open = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.github.com",
]

# Set the path to your ChromeDriver executable
chrome_driver_path = "path_to_chromedriver.exe"

# Create a new Chrome browser instance
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximize the browser window
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

try:
    # Open each URL in the list
    for url in urls_to_open:
        driver.get(url)
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    # Close the browser when done
    driver.quit()
