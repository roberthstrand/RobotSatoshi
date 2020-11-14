import os
import discord
import blockchain
import logging

client = discord.Client()
# List of currency available
availableCurrency = [
    "USD",
    "EUR",
    "SEK",
    "JPY",
    "ISK",
    "AUD",
    "CAD",
    "NZD",
    "GBP",
    "KRW",
]


@client.event
async def on_ready():
    logging.info("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    # Safegaurd, make sure that the bot doesn't respond to itself
    if message.author == client.user:
        return

    # Show available currency
    if message.content.startswith("!currency"):
        await message.channel.send("The following currencies are available:")
        await message.channel.send(", ".join(str(c) for c in availableCurrency))

    # Show current BTC price, based on what currency the user wants
    if message.content.startswith("!price"):
        # Split the incoming message, and set the currency as the second result
        # If the command is run with no currency, set currency to false
        splitMessage = message.content.split(" ")
        try:
            currency = splitMessage[1].upper()
        except IndexError:
            currency = False
        # check if the currency is one of the available
        # if it is present, check the price from blockchain.info
        if currency == False:
            await message.channel.send(
                "No currency chosen. Please use the !price <currency> format."
            )
        elif currency not in availableCurrency and not False:
            await message.channel.send(
                "The currency you've chosen is not valid. You can check what is available by using the !currency command"
            )
        else:
            await message.channel.send(blockchain.buy(currency=currency))

    # Displays link that will add bot to a server that the user has access to
    if message.content.startswith("!link"):
        await message.author.send(
            "Want to add me to your server? No problem! :sweat_smile: Follow this link, but remember that you have to be an admin to add me to servers - http://str.onl/RobotSatoshi"
        )


# Run the client
token = os.environ.get("RobotSatoshiToken")
client.run(token)