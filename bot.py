from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '5025802926:AAF7k0z6kzLxf6APR-ClCcBDkbWc-kQ8sxM'

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! I am your bot.')

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text('This is a help message.')

def main():
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
