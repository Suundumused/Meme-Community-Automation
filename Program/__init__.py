import sys
import time
import pyperclip
import argparse

from Tools.Argparse_customs import tuple_type
from Tools.Logger import *
from Tools.Exception_arg_message import arg_message


def capture_from_area():
    previous_content = ""

    while True:
        current_content = pyperclip.paste()
        
        if current_content != previous_content:
            previous_content = current_content
            writeLine_to_file(current_content)
        time.sleep(0.25)
    
    
def capture_thread():    
    try:
        capture_from_area()
            
    except (KeyboardInterrupt, SystemExit):
        pass
    
    except Exception as ex:
        logger.error(f"KeyReader - {bcolors.FAIL}{arg_message(ex)}{bcolors.ORIGINAL}")
        sys.exit(1)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='FuNAutomation')
    
    try:
        parser.add_argument("-capture", "--capture_from_clippaste", action="store_true")
        parser.add_argument("-discord", "--post_discord", type=tuple_type, default=(None, 'https://discord.com/api/v9/channels/your_channel_id_room/messages')) #auth_key, channel_url/chat
        #parser.add_argument("-reels", "--download_reels", action="store_true")

        
        args = parser.parse_args()
        
    except Exception as ex:
        logger.error(f"Program - {bcolors.FAIL}{arg_message(ex)}{bcolors.ORIGINAL}")
        sys.exit(1)
    
    if args.capture_from_clippaste:
        from Manager import writeLine_to_file
        capture_thread()
        
    '''if args.download_reels:
        from Scrapers.Reels import download
        download()'''
        
    if args.post_discord[0] and args.post_discord[1]:
        from Bots.Discord_bot import send_string_message
        send_string_message(auth_key=args.post_discord[0], url=args.post_discord[1])
        
    logger.info(F"{bcolors.WARNING}Program terminated.{bcolors.ORIGINAL}")
        
        
        
    