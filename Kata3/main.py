from telegram.text import Updater, CommandHandler

def main():
    #Instanciamos el updater
    updater = Updater(token=open("./bot_token").read(), use_context=True)

    #Añadimos un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    #Añadimos un manejador al comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    #Añadimos un manejador al comando /suma
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    #Pedimos notificaciones a Telegram
    updater.start_polling()

    #Capturamos señales de parada
    updater.idle()

    def start(update, context):
        update.message.reply_text("Hola, soy un bot")
        
    def repite(update, context):
        update.message.reply_text(update.message.text)

    def suma(update, context):
        resultado = int(context.args[0]) + int(context.args[1])
        resultado = str(resultado)
        update.message.reply_text("El resultado es " + resultado)

    main()