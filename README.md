# Site Uptime
A site uptime checker to see how often my internet breaks

## Requirements:
You'll need Python and pip installed.
You need to install the requests module by running `pip install requests`.

Then you'll want to schedule this to run every minute (or however often you want) in the crontab.

You can edit the root user crontab with `sudo crontab -e`. You can have a crontab for each user but I like to keep everything in the root crontab.
Add the following to your crontab file.

    */1 * * * * python ~/site_uptime/ping.py
    
Then ping.py should run every minute and check if the site is up.
