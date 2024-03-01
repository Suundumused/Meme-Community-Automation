import io
import time
import requests

from Manager import get_current_directory
from Tools.Logger import *
from Tools.Exception_arg_message import arg_message


def send_string_message(auth_key:str=None, url:str=None):
    if auth_key and url:
        index:int
        
        try:
            with io.open(get_current_directory(args=("Data", "values.txt")), encoding="utf-8", mode="r") as text_file:
                for index, row in enumerate(text_file):
                    rex = requests.post(url, data={'content':row.replace("\r\n", "").replace("\n", "")}, headers={'authorization':auth_key})
                    
                    if rex.status_code <= 302:
                        logger.info(f"{index} - {bcolors.OKBLUE}Discord{bcolors.ORIGINAL}: returned with status code: {bcolors.WARNING}{rex.status_code}{bcolors.ORIGINAL}")
                        time.sleep(1)
                    else:
                        raise requests.exceptions.ConnectionError
                    
        except (KeyboardInterrupt, SystemExit):
            logger.info(f"{index} - {bcolors.OKBLUE}Discord{bcolors.ORIGINAL}: {bcolors.WARNING}terminated by user.{bcolors.ORIGINAL}")
            
        except requests.exceptions.ConnectionError:
            logger.error(f"{bcolors.OKBLUE}Discord{bcolors.ORIGINAL} - {bcolors.FAIL}returned with status code: {rex.status_code}{bcolors.ORIGINAL}")
            
        except Exception as ex:
            logger.error(f"{bcolors.OKBLUE}Discord{bcolors.ORIGINAL} - {bcolors.FAIL}{arg_message(ex)}{bcolors.ORIGINAL}")
    