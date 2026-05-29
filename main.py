import qbittorrentapi
import asyncio
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
import logging
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("PirateJarvis")

#Login to Telegram
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level = logging.INFO
)

#Start qbittorrent session
conn_info = dict(
        host = "localhost",
        port = 8080,
        )
qbt_client = qbittorrentapi.Client(**conn_info)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text="Ahoy."
            )

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    magnet_link = ' '.join(context.args)
    print(magnet_link)
    with qbittorrentapi.Client(**conn_info) as qbt_client:
            qbt_client.torrents_add(urls=magnet_link)

    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Downloading..."
            )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    download_handler = CommandHandler('download', download)


    application.add_handler(start_handler)
    application.add_handler(download_handler)

    application.run_polling()
