import logging
import you
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater, MessageHandler, Filters
import video_converter_pb2 as pb2
import video_converter_pb2_grpc as pb2_grpc
import grpc
import math

BOT_TOKEN = ""
GRPC_PORT = 5051


logging.basicConfig(format='%(asctime)s|%(levelname)s|%(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

SAVE_BASE_PATH = "/tmp/"

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}! Please send the video you want to convert.')


async def download_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = update.message.document or or update.message.video
    file_id = file.file_id
    file_ext = file.file_extension
    
    if file and file_ext in ["mp4", "av1", "webm", "mov", "avi", "wmv", "flv", ]:
        file_name = file.file_name or f"{file.file_id}.{file.file_extension}"

        file_info = pb2.VideoInfo(file_name=file_name, file_encoding=file_ext, video_id=file_id)
        
        file_path = os.path.join(SAVE_BASE_PATH, file_id)

        
        
        buf = file.get_file().download_as_bytearray()

        try:         
            reponse_chunks = stub.ConvertVideo((pb2.VideoToConvert(video_info=file_info, chunk_index=idx, last_chuck=) 
                for idx, chunk in enumerate(range(0, len(buf), 1024 * 4), 1))
            for chunk in response_chunks:
                pass
        
        except as e:
            logger.log(logging.ERROR, f"Can't convert file {file_id}: {e}")
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Something wrong hasa happened! ")            
            
                   
                      
                
        
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"File '{file_name}' saved to '{SAVE_DIR}'.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't receive a file.")

def main():
    with grpc.insecure_channel(f"localhost:{GRPC_PORT}") as channel:
        global stub = pb2_grpc.VideoConverterStub(channel)
 
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    file_handler = MessageHandler(Filters.document | Filters.video, download_file)

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHBOT_TOKENpolling()
