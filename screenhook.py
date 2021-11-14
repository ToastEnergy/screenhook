from selenium import webdriver
import requests, time, sys

if len(sys.argv) < 3:
    print("Usage: python3 main.py <website url> <webhook url>")
    exit()

URL = sys.argv[1]
WEBHOOK_URL = sys.argv[2]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920,1080")

print("[DRIVER] Starting driver...")
driver = webdriver.Chrome(options=chrome_options)
print("[DRIVER] Getting webpage...")
driver.get(URL)
print("[DRIVER] Rendering...")
time.sleep(1)
screenshot = driver.get_screenshot_as_png()
driver.quit()
print("[DRIVER] Done!")

print("[DISCORD] Sending Discord webhook...")
r = requests.post(WEBHOOK_URL,files={'file':('dynmap.png',screenshot)})
print(f"[DISCORD] Webhook sent with statuscode {r.status_code}")

