from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("سلام چخبر دوستان . اسمم برینکسیه")

app = ApplicationBuilder().token("8415423178:AAFr9yxpr5rWAD_Gq2UR_i5IAGn75r5a_eA").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
