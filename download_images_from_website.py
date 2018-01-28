import requests
import os
import uuid
from bs4 import BeautifulSoup
import imghdr

def check_image_format(image):
    return imghdr.what(image)

def open_file(target_folder, file_name):
    try:
        f = open(os.path.join(target_folder, file_name), 'wb')
    except:
        print("Could not download as: " + file_name)
        tf = str(uuid.uuid4())+'.jpg'
        f = open(os.path.join(target_folder, tf), 'wb')
    return f


def download_file(url, target_folder):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    if len(r.content) > 1000:
        print("Downloading {} ---> {}".format(url, local_filename))
        f = open_file(target_folder, local_filename)
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
# 
# def Download_Image_from_Web(url, target_folder ='images', downloaded_images_counter=0):
#     source_code = requests.get(url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text, "html.parser")
#     for link in soup.findAll('img'):
#         try:
#             image_links = link.get('src')
#             print(image_links)
#             if not image_links.startswith('http'):
#                 image_links = url + '/' + image_links
#             download_file(image_links, target_folder)
#             downloaded_images_counter += 1
#         except(AttributeError):
#             pass
#     print(downloaded_images_counter.__str__() + " has beed downloaded")

def GetImagesLinks(src, url):
    soup = BeautifulSoup(src, "lxml")
    images_to_download = []
    for link in soup.findAll('img'):
        try:
            image_link = link.get('src')
            if not image_link.startswith('http'):
                image_link = url + '/' + image_link
            images_to_download.append(image_link)
        except(AttributeError):
            pass
    print("found %s images to download" % images_to_download.__len__().__str__())
    return images_to_download
