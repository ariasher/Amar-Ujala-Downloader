import requests 
import shutil 
import os
from datetime import date, timedelta
from time import sleep

class AUJDownloader():
    '''
    A class to create a downloader and download newspaper pages from amar ujala
    '''

    def __init__(self):
        self.__session = {}

    def __generate_dates(self, start, end):
        s_date = date(*start)
        e_date = date(*end)

        # this will give you a list containing all of the dates
        dates = [s_date + timedelta(days=x) for x in range((e_date - s_date).days + 1)]

        return dates
    
    def __generate_links(self, date):
        dt = date.strftime("%Y/%m/%d")
        main_city = f"https://epaperwmimg.amarujala.com/{dt}/lc"
        my_city = f"https://epaperwmimg.amarujala.com/{dt}/my/lc"

        main_links = [f"{main_city}/{i:02d}/hdimage.jpg" for i in range(1, 41)]
        city_links = [f"{my_city}/{i:02d}/hdimage.jpg" for i in range(1, 11)]

        return main_links, city_links

    def __image_download(self, link, path, name):
        filename = path + name
        header = {
            'User-Agent': r"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
        }
        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(link, stream = True, headers=header)
        sleep(10)
        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            
            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            return True
        else:
            return False

    def download(self, start:tuple, end:tuple=None, output_dir=None):
        
        path = output_dir if output_dir is not None else os.getcwd()
        if not path.endswith("/"):
            path += "/"
        
        if end == None:
            end = start
              
        all_dates = self.__generate_dates(start, end)

        for date in all_dates:
            links = self.__generate_links(date)
            folder = f"{path}auj_{date}/"
            os.mkdir(folder)
            dt = date.strftime("%d-%m-%Y")
            
            count = 1

            for link in links:
                for l in link:
                    filename = f"{count:02d}.jpg"
                    success = self.__image_download(l, folder, filename)
                    if not success:
                        break
                    count += 1

            self.__session[dt] = folder

        return self.__session