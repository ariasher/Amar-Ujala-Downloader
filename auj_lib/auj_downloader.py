import requests 
import os
import sys
from shutil import copyfileobj
from datetime import date, timedelta
from time import sleep


class AUJDownloader():
    '''
    This class is used to download newspaper pages from Amar Ujala.
    '''

    def __init__(self, config:dict):
        '''
        Downloads the newspaper images from the website.

        Required:
            config[Dictionary]:
              A configuration dictionary created by AUJConfig class.
        '''

        self.__session = {}
        self.__config = config

    def __generate_dates(self, start:tuple, end:tuple) -> list:
        '''
        This method is used to generate date objects for the range of dates provided.
        Starting and ending dates are inclusive.

        Required:
            start[Tuple/List]: Starting date. Format: yyyy,mm,dd.
            end[Tuple/List]: Ending date. Format: yyyy,mm,dd.
        
        Returns a list of date objects.
        '''

        s_date = date(*start)
        e_date = date(*end)

        # This will create a list containing all of the dates.
        dates = [s_date + timedelta(days=x) for x in range((e_date - s_date).days + 1)]

        return dates
    
    def __generate_links(self, d_date:date) -> tuple:
        '''
        This method is used to generate links for a particular date.

        Required:
            d_date[Date]: Date object for which the links have to be generated.

        Returns a tuple of two lists of links - Main city pages and My City pages.
        '''

        # Convert the date into string of format yyyy/mm/dd
        dt = d_date.strftime("%Y/%m/%d")
        city = self.__config["city_code"]
        main_city = f"https://epaperwmimg.amarujala.com/{dt}/{city}"
        my_city = f"https://epaperwmimg.amarujala.com/{dt}/my/{city}"

        main_links = [f"{main_city}/{i:02d}/hdimage.jpg" for i in range(1, 41)]
        city_links = [f"{my_city}/{i:02d}/hdimage.jpg" for i in range(1, 11)]

        return main_links, city_links

    def __image_download(self, link:str, path:str, name:str) -> bool:
        '''
        This method downloads individual images.

        Required:
            link[String]: Link of the image file.
            path[String]: Path where to save the image.
            name[String]: Name of the file.

        Returns success status in the form of True/False.
        '''

        # Name of the file with complete path.
        filename = path + name

        # Header configuration for the request.
        header = {
            'User-Agent': r"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
        }

        try:

            # Open the url image, set stream to True, this will return the stream content.
            r = requests.get(link, stream = True, headers=header)

            # Sleep for 10 seconds so the connection is not terminated by the server.
            sleep(10)

            # Check whether the image was downloaded successfully.
            if r.status_code == 200:

                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                r.raw.decode_content = True
                
                # Open a local file with wb (write binary) permission.
                with open(filename,'wb') as f:
                    copyfileobj(r.raw, f)
                    
                return True
            else:
                return False

        except Exception as e:
            sys.stderr.write(f"Error downloading image from: {link} \n")
            sys.stderr.write(f"{str(e)} \n")
            return False

    def download(self, start:tuple, end:tuple=None) -> dict:
        '''
        This method is used to download the newspaper from the website.

        Required: 
            start[Tuple/List]: Start date in integers. Format: yyyy,mm,dd.
            end[Tuple/List]: End date in integers. Format: yyyy,mm,dd. If not specified
                        then start and end dates are considered same.

        Returns a dictionary with Key(date in string format: yyyy-mm-dd) and Value(string path).
        '''

        config = self.__config
        path = config["path"]
        prefix = config["prefix"]

        if not path.endswith("/") and not path.endswith("\\"):
            path += "/"
        
        if end == None:
            end = start

        # Retrieve all the dates for which the newspaper has to be downloaded.
        all_dates = self.__generate_dates(start, end)

        for date in all_dates:
            links = self.__generate_links(date)

            # Directory path.
            folder = f"{path}{prefix}_{date}/"

            # If the directory is not created already.
            if not os.path.exists(folder):
                os.mkdir(folder)

            dt = date.strftime("%d-%m-%Y")
            
            # used for naming the file.
            count = 1

            # Links - Main city and My city.
            for link in links:
                for l in link:
                    filename = f"{count:02d}.jpg"
                    success = self.__image_download(l, folder, filename)
                    if not success:
                        break
                    count += 1

            self.__session[dt] = folder

        return self.__session