# screenhook: screenshot from the web for webhooks

screenhook is a script that captures an image of a web page by sending it through the webhook system
In the configuration file you can in fact configure the following things:
- The website link to be captured
- The webhook link
- The loading time of the web page before capture
- How often to send the capture image
![Banner](https://github.com/ToastEnergy/screenhook/blob/master/banner.png)
### installation
```
sudo apt update && sudo apt upgrade
sudo apt install chromium-chromedriver
curl -fsSl https://raw.githubusercontent.com/ToastEnergy/screenhook/master/install.sh | sh
```
