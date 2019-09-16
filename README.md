# Hands-on IoT Update Demo

The purpose of this directory is to provide you with a boilerplate codebase for controlling the lights on your Pimoroni Blinkt.

In order to execute this code, the Blinkt library must be installed.

Documentation for Blinkt can be found here: https://github.com/pimoroni/blinkt

SSH into your Raspberry Pi and run the following command to install it:

`curl https://get.pimoroni.com/blinkt | bash`

Note that this installation can take some time. The Raspberry Pi Zero is not a powerful board! But that's okay, because most IoT devices aren't. :)

## Included Scripts

In `app.py`, a number of scripts are imported for your use. These are your starting points; feel free to add more! Your RPi will execute whichever script is set as the current value of the variable `effect`.

### Rainbow

The rainbow script simply lights the LEDs is in a rainbow pattern, on a loop.

### Pulse

The pulse script lights the LEDs in a pulsing pattern of a single color, currently set to cyan.

### Twitter

This script requires a little more setup. It flashes the lights whenever someone posts a tweet containing a hashtag you want to watch. In order for this script to work, you must have a Twitter account and provide the script with several keys.

To get a Twitter developer account, go to https://developer.twitter.com/ and select "Other." On the next page, make sure you are signing up for an individual account, not a team account, and a fill out the required fields. There will be a lot of questions about what you're planning to do; don't worry, the applications are usually approved within a few minutes.

Once you have an account, create a new application for it. Once that's done, go to the "Keys and Tokens" tab. You will need to generate the access tokens.

### Weather

This script lights the LEDs based on the projected temperature for today. Requires an API key from https://openweathermap.org/

Once you have your API key, paste it into weather.py as the value of the `API_KEY` variable. The value of `CITY_KEY` should be the name of the city you want to monitor the weather for.

## On API Keys and Environment Variables

Usually, it's a bad idea to store API keys or access tokens in a place where they're publicly accessible. How do we get them into the code, then?

The answer is environment variables. There are several ways to get them into your RPi's environment, but in this case we're just going to paste them into your `.bashrc` file so that they're exported every time the device starts. Use the following format:

`export WEATHER_API_KEY='YOUR KEY OR TOKEN HERE'`
`export TWITTER_API_KEY='YOUR KEY OR TOKEN HERE'`
`export TWITTER_CONSUMER_KEY='YOUR KEY OR TOKEN HERE'`
`export TWITTER_CONSUMER_SECRET='YOUR KEY OR TOKEN HERE'`
`export TWITTER_ACCESS_KEY='YOUR KEY OR TOKEN HERE'`
`export TWITTER_ACCESS_SECRET='YOUR KEY OR TOKEN HERE'`

The file we are looking for is in the root directory, and it's a hidden file. To get to it, do the following:

`cd ~ && ls -a`

You will be able to see a bunch of files that were hidden before. They are indicated by a leading dot in the filename.

Edit `.bashrc` by entering `sudo nano .bashrc` (or your editor of choice, but nano is installed by default). Add your environment variables according to the template above, save the file, and reload your bash profile by typing `source ~/.bashrc`

## CI/CD

The RPi Zero is not powerful enough to run Docker reliably and I only have two hours for this workshop, so we're going to build the quick-and-dirty version of a CI/CD pipeline: a simple Flask app exposed to the public internet via ngrok, and a webhook on your GitHub repository.

Every time you push new code to your GitHub repo, the webhook will be triggered and it will send a POST request to a route on your Flask app with some information about the commit. Your Flask app will then pull down the new code, kill the currently-running copy of the script controlling your lights, and restart it with the new code.

Note that this kind of setup obviously doesn't scale well. The "easy" options for a proper CI/CD pipeline are very difficult or outright impossible to set up on a device this small. The "correct" ways to do it are complicated and require additional supporting infrastructure.

### The Flask App

Your Flask app only needs one route, and it just needs to wait for a POST request (the webhook from GitHub), then pull down from GitHub, kill the currently-running version of your Python script, and restart it with the new version.

In the JFrog ecosystem, we could easily be pulling modules via Artifactory and using Pipelines to trigger this instead; however, in the interest of time (and making it more accessible for y'all to mess around with this at home in your spare time), I've left those two tools out. They would be important in a production environment.
