import xml.etree.ElementTree as ET
import os

from PIL import Image

tree = ET.parse('IMG_20200325_134213.xml')
root = tree.getroot()

class Record():
    def __init__(self, name, xmin, xmax, ymin, ymax):
        self.name = name
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def __str__(self):
        return "Name: " + self.name

records = []

name = ""
ymin = ""
ymax = ""
xmin = ""
xmax = ""
for childRoot in root:
    if(childRoot.tag == "object"):
        for subChild in childRoot:
            if(subChild.tag == "name"):
                name = subChild.text
            if(subChild.tag == "bndbox"):
                for coords in subChild:
                    if(coords.tag == "xmin"):
                        xmin = coords.text
                    if(coords.tag == "xmax"):
                        xmax = coords.text
                    if(coords.tag == "ymin"):
                        ymin = coords.text
                    if(coords.tag == "ymax"):
                        ymax = coords.text
        records.append(
            Record(
                name,
                xmin,
                xmax,
                ymin,
                ymax
            )
        )

img = Image.open('IMG_20200325_134213.jpg')
id = 0
for record in records:
    name = record.name

    if(os.path.isdir('data/' + str(name) + '/') == False):
        os.mkdir('data/' + str(name) + '/')

    cropped_img = img.crop(
        (
            float(record.xmin), float(record.ymin),
            float(record.xmax), float(record.ymax)
        )
    )

    cropped_img = cropped_img.resize(
        (100, 100),
        Image.NEAREST
    )

    cropped_img.save('data/' + name + '/' + str(id) + '.jpg')
    id += 1










# from PIL import Image
# im = Image.open("IMG_20200325_134213.jpg")
#
# crop_rectangle = (50, 50, 200, 200)
# cropped_im = im.crop(crop_rectangle)
