from decouple import config
import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import (filters,
                          MessageHandler,
                          ApplicationBuilder,
                          CommandHandler,
                          ContextTypes, InlineQueryHandler)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {update.effective_chat.username},\n"
                                                                          f"I'm doctor ")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = [InlineQueryResultArticle(
        id=query.upper(),
        title='Caps',
        input_message_content=InputTextMessageContent(query.upper())
    )]
    await context.bot.answer_inline_query(update.inline_query.id, results)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.\n"
                                                                          "I believe you will find the below helpful\n"
                                                                          "/start\n"
                                                                          "/get_exam_result")


async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    split_message = message.split('\n')
    print(split_message)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=split_message[1] + split_message[2] if len(split_message) == 3 else
                                   split_message[0] + split_message[1])


if __name__ == '__main__':
    application = ApplicationBuilder().token(config('TOKEN')).build()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    inline_caps_handler = InlineQueryHandler(inline_caps)
    application.add_handler(inline_caps_handler)

    unknown_handler = MessageHandler(filters.TEXT, unknown)
    application.add_handler(unknown_handler)

    application.run_polling()
