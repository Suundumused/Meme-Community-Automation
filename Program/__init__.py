import gc
import io
import sys
import time
import pyperclip
import argparse
import keyboard

from Manager import get_current_directory
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
   
        
class WithPaste(object):
    def __init__(self) -> None:
        self.text_file = [line for line in io.open(get_current_directory(args=("Data", "values.txt")), encoding="utf-8", mode="r")]
        self.index = 1
        self.last_index = len(self.text_file)-1
    
    
    def paste_from_file(self, _):
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('v'):
            time.sleep(0.33)
    
            if self.index <= self.last_index:
                text = self.text_file[self.index].replace("\n", "").replace("\r\n", "")
                pyperclip.copy(text)
                
                logger.info(f"{bcolors.WARNING}Listener: {self.index}{bcolors.ORIGINAL} - {bcolors.WARNING}{text} {bcolors.ORIGINAL}copied.")
                self.index+=1
            else:
                logger.info(f"{bcolors.WARNING}Listener{bcolors.ORIGINAL} Terminated. Press ctrl + c in the terminal to skip.")
               
                
        elif  keyboard.is_pressed('alt') and keyboard.is_pressed('r'):
            if self.index > 0:        
                self.index-=1
                
                text = self.text_file[self.index-1].replace("\n", "").replace("\r\n", "")
                pyperclip.copy(text)
                
                logger.info(f"{bcolors.WARNING}Listener: {self.index-1}{bcolors.ORIGINAL} - {bcolors.WARNING}{text} {bcolors.ORIGINAL}copied (Back).")
                                
                        
    def paste_thread(self):
        try:
            text = self.text_file[0].replace("\n", "").replace("\r\n", "")
            pyperclip.copy(text)
            logger.info(f"{bcolors.WARNING}Listener: 0{bcolors.ORIGINAL} - {bcolors.WARNING}{text}{bcolors.ORIGINAL} copied.")
        
            keyboard.hook(self.paste_from_file)
            keyboard.wait()
        
        except (KeyboardInterrupt, SystemExit):
            logger.info(f"{bcolors.WARNING}Listener{bcolors.ORIGINAL} Terminated.")
            
        self.text_file.clear()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='FuNAutomation')
    
    try:
        parser.add_argument("-capture", "--capture_from_clippaste", action="store_true")
        parser.add_argument("-paste", "--paste_to_clippaste", action="store_true")
        parser.add_argument("-discord", "--post_discord", type=tuple_type, default=(None, 'https://discord.com/api/v9/channels/your_channel_id_room/messages')) #auth_key, channel_url/chat
        #parser.add_argument("-reels", "--download_reels", action="store_true")
        
        args = parser.parse_args()
        
    except Exception as ex:
        logger.error(f"Program - {bcolors.FAIL}{arg_message(ex)}{bcolors.ORIGINAL}")
        sys.exit(1)
    
    gc.enable()
    
    if args.capture_from_clippaste:
        from Manager import writeLine_to_file
        capture_thread()
        
    if args.paste_to_clippaste:
        OnPaste = WithPaste()
        OnPaste.paste_thread()
        del OnPaste

    '''if args.download_reels:
        from Scrapers.Reels import download
        download()'''
        
    if args.post_discord[0] and args.post_discord[1]:
        from Bots.Discord_bot import send_string_message
        send_string_message(auth_key=args.post_discord[0], url=args.post_discord[1])
        
    logger.info(F"{bcolors.WARNING}Program terminated.{bcolors.ORIGINAL}")
        
        
        
    