from selenium import webdriver
import requests
from time import sleep

WEBHOOK_URL = "https://discord.com/api/webhooks/908746324537671720/t05u7iuaHqGEWCACSsgkxtlhB2ej-UWuCKrUHjskW37uPLLl54nIPbPhdGLFXTJK4-_p"

if not WEBHOOK_URL:
    print("Please insert the webhook url")
    exit()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920,1080")

print("[DRIVER] Starting driver...")
driver = webdriver.Chrome(options=chrome_options)
print("[DRIVER] Getting webpage...")
driver.get('https://map.infinit7even.xyz')
print("[DRIVER] Rendering...")
sleep(1)
screenshot = driver.get_screenshot_as_png()
driver.quit()
print("[DRIVER] Done!")

print("[DISCORD] Sending Discord webhook...")
r = requests.post(WEBHOOK_URL,files={'file':('dynmap.png',screenshot)})
print(f"[DISCORD] Webhook sent with statuscode {r.status_code}")

