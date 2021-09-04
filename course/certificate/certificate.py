#!/usr/bin/env/ python3

from PIL import Image, ImageDraw,ImageFont
import pandas as pd
import os
from random import randint
class ImageMan():
    def __init__(self):
        path='certificate.jpg'
        self.original_cert = Image.open(path)
        self.name_font = ImageFont.truetype('fonts/prata.ttf',100)
        self.date_font = ImageFont.truetype("fonts/play-fair-display.ttf",36)
        self.course_font = ImageFont.truetype('fonts/play-fair-display.ttf',27)
        self.course_creator_font = ImageFont.truetype('fonts/play-fair-display.ttf',30)

    def change_values(self,name,date,course_name,course_creator_name):
        blue = (40, 50, 194)
        black = (3, 4, 15)
        editible_cert = ImageDraw.Draw(self.original_cert)
        editible_cert.text((902,600),name,blue,font=self.name_font)
        editible_cert.text((925,460),date,black,font=self.date_font)
        editible_cert.text((905,827),course_name,black,font=self.course_font)
        editible_cert.text((490,1066),course_creator_name,blue,font=self.course_creator_font)
        rand = randint(100,999)
        self.original_cert.save(f'output/{name}_{rand}.jpg')
        return f'output/{name}_{rand}.jpg'

newobj = ImageMan()
path = newobj.change_values("Ashwot","2021-9-4","Intro to Hacking","Adhit Upaydhyay") # name, date, course_name,course_creator
print(path)
