from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "8921530434:AAFAq2jXi2X8Kqoc0QCfi1t9AFa3JIJecwI"

def start(update, context):
    update.message.reply_text("🤖 CRM مطب فعال شد")

def echo(update, context):
    update.message.reply_text("📩 " + update.message.text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
