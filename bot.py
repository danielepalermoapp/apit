from telegram.ext import Application, CommandHandler
import os

async def get_photos(update, context):
    user = update.message.from_user
    photos = await context.bot.get_user_profile_photos(user.id)
    
    if photos.total_count > 0:
        await update.message.reply_text(f"Hai {photos.total_count} foto profilo")
        # Invia la foto più recente
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photos.photos[0][0].file_id
        )
    else:
        await update.message.reply_text("Nessuna foto profilo trovata")

def main():
    app = Application.builder().token('7576122464:AAF8YMAWuQFwigzOyKxV5pso6bsDrR6v4ZI').build()
    app.add_handler(CommandHandler("photos", get_photos))
    app.run_polling()

if __name__ == '__main__':
    main()