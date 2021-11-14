import selenium, requests, time, sys, json, os.path
from selenium import webdriver

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/config.json"

if not os.path.exists(FILE_PATH):
    WEBSITE_URL = input("enter the website to target\n")
    WEBHOOK_URL = input("enter the discord webhook url\n")

    end = False
    while not end:
        WAIT_BEFORE_SCREENSHOT = input("enter the time to wait before taking a screenshot\n")
        try:
            WAIT_BEFORE_SCREENSHOT = int(WAIT_BEFORE_SCREENSHOT)
            end = True
        except:
            print("specify a number")
            end = False

    with open(FILE_PATH, "w") as f:
        json.dump({"WEBSITE_URL": WEBSITE_URL, "WEBHOOK_URL": WEBHOOK_URL, "WAIT_BEFORE_SCREENSHOT": WAIT_BEFORE_SCREENSHOT}, f, indent=4)

with open(FILE_PATH, "r") as f:
    config = json.load(f)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920,1080")

print("[DRIVER] Starting driver...")
try:
    driver = webdriver.Chrome(options=chrome_options)
except selenium.common.exceptions.WebDriverException:
    print("\nchromedriver isn't installed!\nhttps://chromedriver.chromium.org/downloads\n(you can use sudo apt install chromium-chromedriver on ubuntu/debian))")
    exit()

print("[DRIVER] Getting webpage...")
driver.get(config['WEBSITE_URL'])
print("[DRIVER] Rendering...")
time.sleep(config['WAIT_BEFORE_SCREENSHOT'])
screenshot = driver.get_screenshot_as_png()
driver.quit()
print("[DRIVER] Done!")

print("[DISCORD] Sending Discord webhook...")
r = requests.post(config['WEBHOOK_URL'], files={'file': ('screenhook.png',screenshot)})
print(f"[DISCORD] Webhook sent with statuscode {r.status_code}")

