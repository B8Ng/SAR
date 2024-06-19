import SAR_Possession
import numpy as np
import cv2
from osgeo import gdal
import os
from collections import defaultdict
import datetime

# 启用GDAL异常处理
gdal.UseExceptions()

"""
处理拼接图像遥感数据类
"""


class Landsat8ProcessingForMosaic:

    def __init__(self, path):
        self.path = path
        file_list = self.find_all_bands()
        self.band2file = file_list[0]
        self.band3file = file_list[1]
        self.band4file = file_list[2]
        self.band5file = file_list[3]
        self.band6file = file_list[4]

        self.output_dir = os.path.join(os.getcwd(), 'Output')
        os.makedirs(self.output_dir, exist_ok=True)
        self.buffer_dir = os.path.join(os.getcwd(), 'Buffer')
        os.makedirs(self.buffer_dir, exist_ok=True)
        current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.outfile = os.path.join(self.output_dir, f"mosaic_{current_time}.png")
        self.buffer_file = os.path.join(self.buffer_dir, "buffer.png")

    def get_tif_files(self, filetype='.TIF'):
        """
        搜索路径中指定扩展名的文件
        """
        L = []
        filelist = os.listdir(self.path)
        for file in filelist:
            if os.path.splitext(file)[1].upper() == filetype.upper():
                L.append(os.path.join(self.path, file))
        return L

    def find_all_bands(self):
        """
        找到所有波段文件
        :return: 波段文件的数组
        """
        all_files = self.get_tif_files()
        B2file, B3file, B4file, B5file, B6file = None, None, None, None, None
        for file in all_files:
            if 'B2.TIF' in file:
                B2file = file
            elif 'B3.TIF' in file:
                B3file = file
            elif 'B4.TIF' in file:
                B4file = file
            elif 'B5.TIF' in file:
                B5file = file
            elif 'B6.TIF' in file:
                B6file = file
        return [B2file, B3file, B4file, B5file, B6file]

    def read_band(self, band_file):
        """
        读取单个波段
        """
        if band_file:
            ds = gdal.Open(band_file)
            return ds.ReadAsArray()
        else:
            raise ValueError("波段文件不存在")

    def read_tif_NaturalTrueColor(self):
        """
        读取自然真彩波段：234
        """
        blue = self.read_band(self.band2file)
        green = self.read_band(self.band3file)
        red = self.read_band(self.band4file)

        #print("Blue band min:", blue.min(), "max:", blue.max())
        #print("Green band min:", green.min(), "max:", green.max())
        #print("Red band min:", red.min(), "max:", red.max())

        blue_stretched = linear_stretch(blue)
        green_stretched = linear_stretch(green)
        red_stretched = linear_stretch(red)

        x, y = blue.shape
        new_arr = np.zeros((x, y, 4), dtype=np.uint8)
        new_arr[:, :, 0] = blue_stretched
        new_arr[:, :, 1] = green_stretched
        new_arr[:, :, 2] = red_stretched
        new_arr[:, :, 3] = (blue != 0) * 255  # 透明度

        #print("Stretched Blue band min:", blue_stretched.min(), "max:", blue_stretched.max())
        #print("Stretched Green band min:", green_stretched.min(), "max:", green_stretched.max())
        #print("Stretched Red band min:", red_stretched.min(), "max:", red_stretched.max())

        return new_arr

    def save_png(self, new_arr, output_path, buffer_path, minification=5):
        """
        保存为png格式图像
        """
        new_x = int(new_arr.shape[0] / minification)
        new_y = int(new_arr.shape[1] / minification)

        resized_img = cv2.resize(new_arr, (new_y, new_x), interpolation=cv2.INTER_AREA)
        cv2.imwrite(output_path, resized_img)
        cv2.imwrite(buffer_path, resized_img)
        print(f"图像保存至: {output_path}")

    def output_png(self, minification=5):
        data = self.read_tif_NaturalTrueColor()
        print("处理完成, 正在保存……")
        self.save_png(data, self.outfile, self.buffer_file, minification)


def linear_stretch(data, num=1):
    """
    线性拉伸(单波段)
    """
    d2 = np.percentile(data, num)
    u98 = np.percentile(data, 100 - num)
    maxout = 255
    minout = 0
    data_8bit = np.clip((data - d2) * (maxout - minout) / (u98 - d2) + minout, minout, maxout)
    return data_8bit.astype(np.uint8)

def Mosaic_GDAL(path_image1, path_image2, path_out):
    """
    拼接图像
    :param path_image1: 需要拼接的影像
    :param path_image2: 需要拼接的影像
    :param path_out: 拼接后输出的影像路径
    :return: None
    """
    image1 = gdal.Open(path_image1, gdal.GA_ReadOnly)  # 第一幅影像
    input_proj = image1.GetProjection()
    image2 = gdal.Open(path_image2, gdal.GA_ReadOnly)  # 第二幅影像
    options = gdal.WarpOptions(srcSRS=input_proj, dstSRS=input_proj, format='GTiff', dstNodata=0, srcNodata=0,
                               resampleAlg=gdal.GRA_Cubic)
    # 输入投影，输出投影，输出格式，重采样方法
    gdal.Warp(path_out, [image1, image2], options=options)
    # 创建金字塔
    del image1, image2


def Mosaic_png(path1, path2):
    """
    两张卫星图像拼接并合成
    :param path1:需要合成的图像1路径
    :param path2:需要合成的图像2路径
    :return:None
    """
    Outpath = "Output"
    image1 = SAR_Possession.landsat8_Possesing(path1)
    image2 = SAR_Possession.landsat8_Possesing(path2)
    input1 = image1.finded_all_band()
    input1.extend(image2.finded_all_band())  # 数组: 存两个需要合成的图像的地址
    # 创建一个字典，用于将文件按照波段进行分组
    file_groups = defaultdict(list)
    for file_path in input1:
        file_name = file_path.split('_')[-1]  # 获取文件名后缀，如'B2.TIF'
        key = file_name.split('.')[0]  # 取'B2'、'B3'等作为字典中的键
        file_groups[key].append(file_path)

    for key, files in file_groups.items():  # 键值为波段, value为地址, 输出地址为Outpath, 输出文件为地址一的文件名字+_Bx.TIF
        output_file = os.path.join(Outpath,
                                   os.path.basename(path1).split('.')[0] + '_' + key + '.TIF')  # 是TIF!不是tif!比亚迪!

        Mosaic_GDAL(files[0], files[1], output_file)
    print("正在对拼接图像处理……")
    Landsat8ProcessingForMosaic(Outpath).output_png(5)

