import os
import qrcode
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8709875871:AAEEtKxo36F51dQgQ-evStw2yfWsOwrJ1bQ"

# papkalar yaratish
os.makedirs("images", exist_ok=True)
os.makedirs("qr", exist_ok=True)

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    
    file = await context.bot.get_file(photo.file_id)
    
    image_path = f"images/{photo.file_id}.jpg"
    await file.download_to_drive(image_path)
    
    # bu yerda link o‘rniga file nomini ishlatyapmiz
    data = f"Rasm ID: {photo.file_id}"
    
    qr = qrcode.make(data)
    
    qr_path = f"qr/{photo.file_id}.png"
    qr.save(qr_path)
    
    await update.message.reply_photo(photo=open(qr_path, "rb"))

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

print("Bot ishga tushdi...")
app.run_polling()