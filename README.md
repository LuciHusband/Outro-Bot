# Outro Bot

This is a goofy Discord bot that plays an epic outro song for a specified user, waits for beat to drop, removes the user from the channel and then disconnects. This is the ultimate way to end the party!
## Usage

To use the bot, you will need to provide a Discord bot token in the `TOKEN` variable in `the run_discord_bot()` function. You can create a bot and get a token by following [these instructions](https://discordpy.readthedocs.io/en/latest/discord.html).

Once you have a token, replace `<Your token here>` with your token and then run the script with `python3 bot.py`.

You can then use the command `.outro @username` in your Discord server, where `@username` is the mention of the user you want to play the audio file for. The bot will join the voice channel of the mentioned user and play the "outro.mp3" file. After 15 seconds, the bot will move the user out of the channel and disconnect from the channel.
## Requirements

This bot requires the following python packages:

    discord.py
    asyncio
    ffmpeg

Make sure to install these packages before running the bot by running `pip install -r requirements.txt`
## Note

To run this bot, you will need to have FFmpeg installed on your system. You can download a pre-built version from the official website https://ffmpeg.org/download.html, then add it to your system's PATH environment variable so that the code can find it.

On Windows:

1. Open the Start menu and search for "Environment Variables".
2. Click "Edit the system environment variables".
3. Under "System Variables", find the "Path" variable and click the "Edit" button.
4. Click the "New" button and enter the path to the FFmpeg executable (e.g. C:\ffmpeg\bin).
5. Click "OK" to close all open dialogs.

On Linux and MacOS:

1. Open the terminal and use the export command to add FFmpeg path into PATH variable by running `export PATH=$PATH:/path/to/ffmpeg`.
2. Put this command in your shell profile file (such as `~/.bash_profile` or `~/.bashrc`) to make it persistent across reboots.

Please make sure to add the path to the environment variables before running the bot.
Additionally, in order for the bot to join and speak in voice channels, you will need to enable Privileged Gateway Intents for your bot in the Discord Developer Portal, [here is a guide](https://discordpy.readthedocs.io/en/stable/intents.html#privileged-intents).
## Troubleshooting

If the bot is not working as expected, make sure that the file "outro.mp3" is located in the same directory as the bot script. Also, check that the bot has the necessary permissions to join and speak in the voice channel.
