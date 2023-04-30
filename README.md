# ModBot

This is a moderation bot I wrote for use on Discord.

## Dependencies

You will need to install
[`discord.py`](https://discordpy.readthedocs.io/en/stable/index.html).

## Configuration

All configuration goes in the `config/` directory.

The bot token goes in `config/bot_token.conf`, just by itself on the first line
with no other characters.

The bot will need a test guild, which is the guild all commands are synced to
before they will be manually synced globally (as there is a ratelimit on adding
new global commands). The ID of the test guild is provided in the `test_guild`
key inside `config/config.json`, as an integer.

## Running

To run the bot, simply do `python main.py`.

## License

This repository is licensed under MIT.
