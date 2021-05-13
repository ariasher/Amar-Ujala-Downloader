from PIL import Image
import os
import sys

class AUJCombiner():

    def __init__(self, data:dict):
        self.data = data

    def generate_pdfs(self):
        dates = list(self.data.keys())

        try:
            for date in dates:
                d = self.data[date]
                files = os.listdir(d)
                first_file_name = files[0]
                first_file = Image.open(d + first_file_name)

                im_list = [Image.open(f"{d}{f}") for f in files if f != first_file_name]
                pdf_name = f"auj_{date}.pdf"

                first_file.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=im_list)
        except Exception as e:
            sys.stderr.write("ERROR: ")
            sys.stderr.writelines(str(e))
