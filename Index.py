import re
from dateutil.parser import parser
from telegram.ext import CommandHandler, Updater
from telegram.ext import MessageHandler, Filters
import content

def main():
    def echo(update, context):
        print(update.message.text)
    def is_allowed(update):
        return update.message.from_user.id in allowed_users

    def start(update, context):
        if is_allowed(update):
            context.bot.send_message(chat_id=update.effective_chat.id, text="дарова педики")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="К сожалению, у вас нет доступа к этому боту.")

    def delete_message(update, context):
        if is_allowed(update):
            context.bot.delete_message(chat_id=update.effective_chat.id,
                                       message_id=update.message.reply_to_message.message_id)
            context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="К сожалению, у вас нет доступа к этому боту.")

    def mute_user(update, context):
        if is_allowed(update):
            try:
                time = int(context.args[0])
                user_id = update.message.reply_to_message.from_user.id
                context.bot.restrict_chat_member(chat_id=update.effective_chat.id, user_id=user_id, until_date=time)
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=f"Пользователь {user_id} замучен на {time} секунд.")
            except (IndexError, ValueError):
                context.bot.send_message(chat_id=update.effective_chat.id, text="Использование: /mute <время>")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="К сожалению, у вас нет доступа к этому боту.")

    def ban_user(update, context):
        if is_allowed(update):
            try:
                user = update.message.reply_to_message.from_user
                chat_id = update.message.chat_id
                time_string = context.args[0]
                time = parser.parse(time_string).minute
                context.bot.restrict_chat_member(chat_id, user.id, until_date=time * 60)
                update.message.reply_text(f"{user.name} был забанен на {time_string}.")
            except (IndexError, ValueError):
                update.message.reply_text("Использование: /ban <время>")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="К сожалению, у вас нет доступа к этому боту.")

    def delete_message_with_phrase(update, context):

        try:
                message = update.message
                text = message.text.lower()
                if forbidden_pattern.search(text):

                    message.delete()
                    context.bot.send_message(chat_id=update.effective_chat.id, text="Я ща тебя забаню нахуй")
                if forbidden_pattern2.search(text):
                    print("попался")
                    message.delete()
        except Exception as E:
                    print(E)

    allowed_users = content.allowed_users
    TOKEN = content.TOKEN
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start666", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, delete_message_with_phrase))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dp.add_handler(CommandHandler("sms", delete_message))
    dp.add_handler(CommandHandler("mut", mute_user))
    dp.add_handler(CommandHandler("bon", ban_user))
    updater.start_polling()
    updater.idle()

forbidden_words = content.forbidden_words
forbidden_pattern = re.compile('|'.join(forbidden_words), re.IGNORECASE)
forbidden_words2 = content.forbidden_words2
forbidden_pattern2 = re.compile('|'.join(forbidden_words2), re.IGNORECASE)
print("ready")
main()
