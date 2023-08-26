from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from time import sleep
import json
import googleapiclient.discovery
from bardapi import Bard
import os
from tempfile import TemporaryFile
from pyudemy import Udemy
from youtubesearchpython import VideosSearch
path= input("What do you want to learn today? ")
steps = []
# Replace XXXX with the values you get from __Secure-1PSID
token = 'aQhxb05fALonGMbKnV-12mEGW0fKoVkt48v7Uk-jzDyAD5U2c7bgaxZdL1w5sPiOy6_-_w.'
bard = Bard(token=token)
# Set your input text
input_text = f'Generate a list to learn {path}. Each list item should start with a number. There should be at more 20 list items. Do not create sub lists under each list item, instead add them to the main list. Each list item should be less than 6 words and should start with the word "how to learn". include the word {path} in each list item. Each step should include a quantative skill that can be developed.Do not mention hours required for each list item'
# Send an API request and get a respons
    
bard_output = bard.get_answer(input_text)['content']
print(str(bard_output))
bard_output = bard_output.replace("*", "")
bard_output = bard_output.replace("Step", "")
bard_output = bard_output.replace("`", "")
fp = TemporaryFile('w+t')
fp.write(str(bard_output))
fp.seek(0)
for lines in fp:
    lines = lines.strip()
    if lines and lines[0].isdigit():
        steps.append(lines)
print(steps)