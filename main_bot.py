from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import file_token  # файл, содержащий токет телеграм-бота. Закоментировать после внесения токена своего бота
import view
# from controller import run
import model


async def help(update: Update, context: ContextTypes) -> None:  # Вызов справки
    await update.message.reply_text(f'Что сделать со справочником?\n {view.show_menu()}')

async def show_all(update: Update, context: ContextTypes) -> None: # Показ всех записей
    res = model.csv_data_open()
    for i, row in enumerate(res):
        await update.message.reply_text(f"{i}. {' '.join(row)}")

async def add(update, context) -> None: # Добавление записи
    msg = update.message.text
    in_info = msg.split()
    print(msg)
    model.add_info(in_info)

async def delete(update, context) -> None:  # Удаление записи
    msg = update.message.text
    in_info = msg.split()
    model.del_info(int(in_info[1]))

async def find(update, context) -> None:  # Поиск записи по фамилии
    msg = update.message.text
    in_info = msg.split()
    await update.message.reply_text(model.find_last_name(in_info[1]))

async def import_txt(update: Update, context: ContextTypes) -> None: # Импорт справочника в txt-формат
    model.import_into_csv()

    
app = ApplicationBuilder().token(file_token.token()).build()  # Вместо "file_token.token()" необходимо вставить токен телегам-бота


app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("show_all", show_all))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("delete", delete))
app.add_handler(CommandHandler("find", find))
app.add_handler(CommandHandler("import_txt", import_txt))

print('server start')

app.run_polling()