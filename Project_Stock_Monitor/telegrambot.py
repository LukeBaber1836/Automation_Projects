import logging
import stock_crypto_fetcher as fetchc
from uuid import uuid4
from hidden_items import stock_monitor1
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, InlineQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = [
        InlineQueryResultArticle(
            # Gets current price of coin from CoinGecko API
            id=str(uuid4()),
            title='Coin Price in USD',
            input_message_content=InputTextMessageContent(fetchc.get_coin_price(coin_name=query, currency='USD'))
        ),
        InlineQueryResultArticle(
            # Sends back the abbreviated name of the coin
            id=str(uuid4()),
            title='Abbreviated Name',
            input_message_content=InputTextMessageContent(fetchc.get_coin_symbol(coin_name=query))
        ),
        InlineQueryResultArticle(
            # Sends back the abbreviated name of the coin
            id=str(uuid4()),
            title='Coin Sentiment',
            input_message_content=InputTextMessageContent(fetchc.get_coin_symbol(coin_name=query))
        )
    ]
    await context.bot.answer_inline_query(update.inline_query.id, results)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':
    application = ApplicationBuilder().token(stock_monitor1.telegram_API_key).build()

    start_handler = CommandHandler('start', start)
    caps_handler = CommandHandler('caps', caps)
    inline_handler = InlineQueryHandler(inline_query)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(caps_handler)
    application.add_handler(inline_handler)
    application.add_handler(unknown_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)