# Screenhook: screenshot from the web for discord webhooks
Screenhook is a script that captures an image of a web page and send it to a discord webhook.

Screenhook has a guided configuration system, after installing the necessary files with the [script](https://github.com/ToastEnergy/screenhook/blob/master/install.sh) run the [python file](https://github.com/ToastEnergy/screenhook/blob/master/screenhook.py) and follow the instructions!

You can change the settings of the config that will be created at any time.
- The website link to be captured
- The loading time of the web page before capture (if the site is heavy)
- The webhook link where to send the image
![Banner](https://github.com/ToastEnergy/screenhook/blob/master/banner.png)
## Getting started
### installation and configuration
```
sudo apt update && sudo apt upgrade
sudo apt install chromium-chromedriver
curl -fsSl https://raw.githubusercontent.com/ToastEnergy/screenhook/master/install.sh | sh
cd screenhook
python3 screenhook.py
```
## Automatic execution
### crontab installation and settings
```
sudo apt-get update
sudo apt-get install cron
crontab -e
```
Now go to the end of the crontab file and paste `@weekly /bin/python3 /home/user/screenhook/screenhook.py`
| Other examples                                                    | Description                         |
| -------------------------------------------------------------- | ----------------------------------- |
| 0 * * * * /bin/python3 /home/user/screenhook/screenhook.py | Run the command every hour |
| @daily /bin/python3 /home/user/screenhook/screenhook.py | Run the command every day |
| 00 14 * * sat /bin/python3 /home/user/screenhook/screenhook.py | Run the command every Saturday at 14:00 |
| @reboot /bin/python3 /home/user/screenhook/screenhook.py | Run the command every reboot |

You can find more examples on [crontab guru](https://crontab.guru/)
