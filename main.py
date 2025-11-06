import telebot

TOKEN = "8545017830:AAHWeRLNftHSlWXA721iMVjpdSyPBEx6yIw"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بيك! 🌟 أنا بوتك الجديد بلغة بايثون 💬")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "قائمة الأوامر:\n/start - بدء\n/help - مساعدة")

print("✅ البوت شغال دلوقتي...")

bot.polling()
