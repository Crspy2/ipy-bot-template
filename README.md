# Interactions.py Bot Tempalte
<h3 align=center>Python template for the interactions.py Discord API wrapper</h3>
<hr>

# Overview
> `main.py:`
- Utilizes the logging library and implements an easy to use custom logger and formatter. All you need to do is call `initLogger("script_name")` in a module, and log configuration is taken care of for you.
- Alongside the custom logging utility, a custom client class is used for the discord application. This allows you to add custom variables to your client class while retaining typesafety and autocomplete. This feature is lost when "monkey patching" variables onto the class.

> `handlers/commandHandler.py`
- A custom, dynamic command loader is present. Write a cog following the `ping.py` in `/commands/`, place it in the `/commands/` directory, and it will automatically be loaded when the bot boots.

> `handlers/eventHandler.py`
- A custom, dynamic event loader is present. Write an event following the `ready.py` in `/events/`, place it in the `/events/` directory, and it will automatically be loaded when the bot boots.


> `logutil.py:`
- Functions here exist to aid the user in simplifying `logging` configuration. Here, all log messages go to standard output.
- A custom formatter also applies based on what level logging you desire, whereas DEBUG produces verbose output and is tailored to aid in debugging, showing which module the message is originating from and, in most cases, which line number. Loggging levels are categorized by color.

# Installation
> 1. Clone this repository. To switch to a different version, `cd` into this cloned repository and run `git checkout [branch name/version here]`
> 2. It's generally advised to work in a Python virtual environment. Here are steps to create one *(the `interactions.py` library requires Python 3.10.0 or later)*:
> Instructions for MacOS / Linux:
> ```
> $ python3 -m venv venv
> $ source venv/bin/activate
> ```
>
> Instructions for Windows (Command Prompt):
> ```
> $ python3 -m venv venv
> $ venv\Scripts\activate.bat
> ```
>
> Instructions for Windows (Powershell):
> ```
> $ python3 -m venv venv
> $ venv\Scripts\activate.ps1
> ```
> Note: If you receive an error stating that the execution of scripts is disabled on your system, you may need to change the execution policy for PowerShell. You can do this by running PowerShell as an administrator and executing the following command:
> ```
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
> ```
> 3. Create a Discord bot token from [here](https://discord.com/developers/applications/)  
> **Register it for slash commands:**
> - Under *OAuth2 > General*, set the Authorization Method to "In-app Authorization"
> - Tick `bot` and `applications.commands`
> - Go to *OAuth2 > URL Generator*, tick `bot` and `applications.commands`
> - Copy the generated URL at the bottom of the page to invite it to desired servers
> 4. Make a new file called `.env` inside the repo folder and paste the below code block in the file
> ```
> TOKEN="[paste Discord bot token here]"
> DEV_GUILD=[paste your bot testing server ID here]
> ```
> 5. Run `pip install -r requirements.txt` to install packages.
> 6. Once that's done, run the bot by executing `python main.py` in the terminal
>
> <hr />
> 
> *If you aren't sure how to obtain your server ID, check out [this article](https://www.alphr.com/discord-find-server-id/)*
> 
> *If you get errors related to missing token environment variables, run `source .env`*

### README heavily inspired from https://github.com/interactions-py/boilerplate
