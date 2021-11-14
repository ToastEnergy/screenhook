# screenhook
## screenshot from the web for discord webhooks
screenhook is a script that captures an image of a web page and send it to a discord webhook.
![Banner](https://github.com/ToastEnergy/screenhook/blob/master/banner.png)
## Getting started
### installation
```
sudo apt update && sudo apt upgrade
sudo apt install chromium-chromedriver
curl -fsSl https://raw.githubusercontent.com/ToastEnergy/screenhook/master/install.sh | sh
cd screenhook
python3 screenhook.py
```
### configuration
when you run the script for the first time you will be prompted to enter some configuration.
later you will be able to edit the configuration file (`config.json`) that has been created with the following options:
- `WEBSITE_URL`: the website to target (include http protocol)


- `WEBHOOK_URL`: the discord webhook url that will look something like this: `https://discordapp.com/api/webhooks/0123456789/abcdefghijklmnopqrstuvwxyz`

- `WAIT_BEFORE_SCREENSHOT`: the amount of time to wait before taking the screenshot (in seconds)

```json
{
    "WEBSITE_URL": "https://google.com",
    "WEBHOOK_URL": "https://discordapp.com/api/webhooks/0123456789/abcdefghijklmnopqrstuvwxyz",
    "WAIT_BEFORE_SCREENSHOT": 5
}
```
## automatic execution
### crontab installation and settings
```
sudo apt update
sudo apt install cron
crontab -e
```
now go to the end of the crontab file and paste `@weekly /bin/python3 /home/user/screenhook/screenhook.py`
| Other examples                                                    | Description                         |
| -------------------------------------------------------------- | ----------------------------------- |
| 0 * * * * /bin/python3 /home/user/screenhook/screenhook.py | run the command every hour |
| @daily /bin/python3 /home/user/screenhook/screenhook.py | run the command every day |
| 00 14 * * sat /bin/python3 /home/user/screenhook/screenhook.py | run the command every Saturday at 14:00 |
| @reboot /bin/python3 /home/user/screenhook/screenhook.py | run the command every reboot |

You can find more examples on [crontab guru](https://crontab.guru/)
