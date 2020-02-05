import csv
import os
from os import listdir
from os import path
import base64

class Database():
    def __init__(self):
        self.platform_csv_path = "../../data/platform.csv"
        self.platform_list = self.init_get_platform_table()
        self.document_csv_path = "../../data/document.csv"
        self.document_list = self.init_get_document_table()
        self.video_csv_path = "../../data/youtube.csv"
        self.video_list = self.init_get_video_table()
        self.partner_csv_path = "../../data/partners.csv"
        self.partner_list = self.init_get_partners_data()

    def get_platform_table(self):
        return self.platform_list
    
    def init_get_platform_table(self):
        data_list = []
        with open(self.platform_csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #if(row['Image_path']):
                #    with open("./static/" + row['Image_path'], "rb") as image_file:
                        #encoded_image_string = base64.b64encode(image_file.read())
                data_list.append({"Switch_Vendor":row['Switch Vendor'], \
                    "Switch_SKU":row['Switch_SKU'], \
                    "ASIC_Vendor":row['ASIC_Vendor'], \
                    "Switch_ASIC":row['Switch_ASIC'], \
                    "Port_Configuration":row['Port_Configuration'], \
                    "Bandwith":row['Bandwith'], \
                    "image":row['Image_path']
                    })
        return data_list

    def get_document_table(self):
        return self.document_list

    def init_get_document_table(self):
        data_list = []
        with open(self.document_csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append({"sort":row["sort"], \
                "sub_sort":row["sub_sort"], \
                "title":row["title"], \
                "filename":row["filename"], \
                "path":row["path"]})
        return data_list

    def get_video_table(self):
        return self.video_list

    def init_get_video_table(self):
        data_list=[]
        with open(self.video_csv_path,'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader :
                data_list.append({"TMS_title":row["TMS_title"], \
                    "video_link":row["video_link"], \
                    "png":row["png_path"], \
                    "bandwidth":row["bandwidth"], \
                    "type":row["type"], \
                        })
        return data_list
    
    def get_partners_data(self):
        return self.partner_list

    def init_get_partners_data(self):
        data_list = []
        with open (self.partner_csv_path,'r') as csvfile:
            reader = csv.DictReader(csvfile)
            img_path = 'images/partners/'
            for row in reader:
                data_list.append({"sort":row["sort"], \
                    "country":row["country"], \
                    "type":row["partner_type"], \
                    "company":row["company"], \
                    "address":row["address"], \
                    "telephone":row["telephone"], \
                    "fax":row["fax"], \
                    "img_path":img_path + row["img_filename"], \
                    "company_link":row["company_link"]})
        return data_list
            