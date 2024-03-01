import io
import time
import requests
import re

from requests_html import HTMLSession
from Manager import get_current_directory

def download():
    headers = {
    'user-agent':'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
      
    with io.open(get_current_directory(args=("Data", "values.txt")), encoding="utf-8", mode="r") as text_file:
        for index, row in enumerate(text_file):
            url = row.replace("\r\n", "").replace("\n", "")
            params = get_current_directory(args=("Data", "Reels", f"reel_{index}.mp4"))
            
            #under development