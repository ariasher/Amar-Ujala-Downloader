from PIL import Image
from os import listdir
import sys


class AUJCombiner():
    '''
    This class is used to combine all the downloaded images into one.
    '''

    def __init__(self, data:dict, config:dict):
        '''
        Combines downloaded images into one.

        Required:
            data[Dictionary]:
              Key - String: Date in dd-mm-yyyy format.
              Value - String: Path of the images for that date. Path ends with '/'.

            config[Dictionary]:
              Contains configuration settings created by AUJConfig class.
        '''
        
        self.__data = data
        self.__config = config

    def generate_pdfs(self) -> None:
        '''
        This method is used to combine all the images into a single pdf.
        The name of the pdf will be {prefix}_{date}.pdf
        '''
        
        dates = list(self.__data.keys())
        config = self.__config
        prefix = config["prefix"]

        try:
            for date in dates:
                path = self.data[date]
                pdf_name = f"{path}../{prefix}_{date}.pdf"

                # List all the images in that folder.
                files = listdir(path)

                # Select first image file and its name.
                first_file_name = files[0]
                first_file = Image.open(path + first_file_name)

                # Open all images.
                im_list = [Image.open(f"{path}{f}") for f in files if f != first_file_name]
                
                # Combine all images into one single pdf file.
                first_file.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=im_list)
        
        except Exception as e:
            sys.stderr.write("ERROR: \n")
            sys.stderr.writelines(f"{str(e)} \n")
