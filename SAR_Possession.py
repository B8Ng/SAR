import numpy as np
import cv2
from osgeo import gdal
import os
import datetime

# 启用GDAL异常处理
gdal.UseExceptions()

"""
遥感卫星图像处理类
"""


class landsat8_Possesing:
    def __init__(self, path):
        self.path = path  # 处理路径
        file_list = self.finded_all_band()  # 波段的数组
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
        self.outfile = os.path.join(self.output_dir, f"output_{current_time}.png")
        self.buffer_outfile = os.path.join(self.buffer_dir, 'buffer.png')

        #print(os.getcwd())
        print(f"文件将保存在: {self.output_dir}")

    def get_tif_file(self, filetype='.TIF'):
        """
       Search for files whose filetype extension does not include subdirectories
        """
        L = []
        if type(filetype) == str:
            if len([filetype]) == 1:
                filelist = os.listdir(self.path)
                for file in filelist:
                    if os.path.splitext(file)[1] == filetype:
                        L.append(os.path.join(self.path, file))
        if type(filetype) != str:
            if len(filetype) > 1:
                for i in range(len(filetype)):
                    filelist = os.listdir(self.path)
                    for file in filelist:
                        if os.path.splitext(file)[1] == type[i]:
                            L.append(os.path.join(self.path, file))
        print(f"已读取文件: {L}")
        return L

    def finded_all_band(self):
        '''
        所有波段文件
        :return:波段文件的数组
        '''
        Allfilelist = self.get_tif_file()
        B2file, B3file, B4file, B5file, B6file = None, None, None, None, None
        for file in Allfilelist:
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
        print("波段文件已读取")
        # print(B4file)
        return [B2file, B3file, B4file, B5file, B6file]

    def read_tif_NaturalTrueColor(self):
        """
        opencv里面为BGR的顺序
        自然真彩波段：234
        """
        print("开始读取波段4、波段3、波段2...")
        ds1 = gdal.Open(self.band2file)
        blue = ds1.ReadAsArray()

        ds2 = gdal.Open(self.band3file)
        green = ds2.ReadAsArray()

        ds3 = gdal.Open(self.band4file)
        red = ds3.ReadAsArray()

        x, y = blue.shape
        new_arr = np.zeros(shape=[x, y, 4])
        new_arr[:, :, 0] = linear_stretch(blue)
        new_arr[:, :, 1] = linear_stretch(green)
        new_arr[:, :, 2] = linear_stretch(red)

        new_arr[:, :, 3][blue != 0] = 255  # 透明度
        print("波段读取完成")
        return new_arr

    def read_tif_Coastal_Detection(self):
        """
        opencv里面为BGR的顺序
        海岸识别波段：465
        """
        print("开始读取波段5、波段6、波段4...")
        ds1 = gdal.Open(self.band4file)
        blue = ds1.ReadAsArray()

        ds2 = gdal.Open(self.band6file)
        green = ds2.ReadAsArray()

        ds3 = gdal.Open(self.band5file)
        red = ds3.ReadAsArray()

        x, y = blue.shape
        new_arr = np.zeros(shape=[x, y, 4])
        new_arr[:, :, 0] = linear_stretch(blue)
        new_arr[:, :, 1] = linear_stretch(green)
        new_arr[:, :, 2] = linear_stretch(red)

        new_arr[:, :, 3][blue != 0] = 255  # 透明度.
        print("波段读取完成")
        return new_arr

    def save_png_by_opencv(self, new_arr, minification=5):
        """
        将处理完的数组保存为png格式的图像
        :param new_arr: 处理后的数组
        :param minification: 缩放系数 1-5
        :return:
        """
        print("开始保存PNG图像...")
        new_arr = (new_arr - new_arr.min()) / (new_arr.max() - new_arr.min()) * 255  # 归一化
        new_arr = new_arr.astype(np.uint8)

        # The size of the output picture
        new_x = int(new_arr.shape[0] / minification)
        new_y = int(new_arr.shape[1] / minification)

        # Zoom out
        gray_im = cv2.resize(new_arr, (new_x, new_y), interpolation=cv2.INTER_AREA)

        # Save to Output directory
        cv2.imwrite(self.outfile, gray_im)
        print(f"图像已保存至: {self.outfile}")

        # Save to Buffer directory
        cv2.imwrite(self.buffer_outfile, gray_im)
        #print(f"Image saved to: {self.buffer_outfile}")

    def OutputNaturalTrueColorByPng(self, minification=5):
        """
        输出234卫星png格式图像
        :param minification: 1-5
        :return:
        """
        data = self.read_tif_NaturalTrueColor()
        # data = self.read_tif_Coastal_Detection()
        self.save_png_by_opencv(data, minification)

    def OutputCoastalColorByPng(self, minification=5):
        """
        输出465卫星png结果
        :param minification: 缩放系数, 你喜欢多大就多大, 一般 1-5
        :return:
        """
        data = self.read_tif_Coastal_Detection()
        self.save_png_by_opencv(data, minification)

    def GaussianResult(self, Mode='NaturalTrueColor'):
        """
        高斯滤波
        :param Mode: NaturalTrueColor / CoastalTrueColor (真彩用于正常观测, 海岸用于海岸线检测)
        :return:滤波后的数组
        """
        print(f"开始高斯滤波处理:{Mode}")
        if Mode == 'NaturalTrueColor':
            data = self.read_tif_NaturalTrueColor()
        elif Mode == 'CoastalTrueColor':
            data = self.read_tif_Coastal_Detection()
        gaussian_data = cv2.GaussianBlur(data, (5, 5), 0)
        print(f"高斯滤波处理完成")
        return gaussian_data

    def FourierFilter(self, Mode='NaturalTrueColor', cutoff_frequency=30):
        """
        快速傅里叶变换滤波
        :param Mode: NaturalTrueColor / CoastalTrueColor (真彩用于正常观测, 海岸用于海岸线检测)
        :param cutoff_frequency: 高通滤波的截止频率
        :return: 滤波后的数组
        """
        print(f"开始傅里叶变换滤波处理: {Mode} 模式, 截止频率: {cutoff_frequency}")
        if Mode == 'NaturalTrueColor':
            data = self.read_tif_NaturalTrueColor()
        elif Mode == 'CoastalTrueColor':
            data = self.read_tif_Coastal_Detection()
        # 对每个波段进行快速傅里叶变换和滤波
        filtered_data = np.zeros_like(data)
        for i in range(data.shape[2]):
            # 进行快速傅里叶变换
            fft_data = np.fft.fft2(data[:, :, i])
            # 创建高通滤波器
            rows, cols = data[:, :, i].shape
            crow, ccol = rows // 2, cols // 2
            mask = np.ones((rows, cols), dtype=np.uint8)
            mask[crow - cutoff_frequency:crow + cutoff_frequency, ccol - cutoff_frequency:ccol + cutoff_frequency] = 0
            # 应用滤波器
            filtered_fft = fft_data * mask
            # 逆快速傅里叶变换得到滤波后的数据
            filtered_data[:, :, i] = np.abs(np.fft.ifft2(filtered_fft))
        print("傅里叶变换滤波处理完成")
        return filtered_data

    def MedianFilter(self, Mode='NaturalTrueColor', kernel_size=5):
        print(f"开始中值滤波处理: {Mode} 模式, 滤波核大小: {kernel_size}")
        if Mode == "NaturalTrueColor":
            data = self.read_tif_NaturalTrueColor()
        elif Mode == 'CoastalTrueColor':
            data = self.read_tif_Coastal_Detection()
        else:
            raise ValueError("Invalid Mode. Choose either 'NaturalTrueColor' or 'Coastal'")
        if data is None or data.size == 0:
            raise ValueError("Failed to read data. Check if the TIFF files are loaded correctly.")
        # Debug print to ensure data is correctly read
        #print(f"Data shape: {data.shape}, min value: {data.min()}, max value: {data.max()}")
        # Normalize data to the 0-255 range
        data_normalized = ((data - data.min()) / (data.max() - data.min()) * 255).astype(np.uint8)
        # Apply median filter
        median_filtered_data = cv2.medianBlur(data_normalized, kernel_size)
        print(f"中值滤波完成")
        return median_filtered_data

    def OutputGaussianResultByPng(self, minification=5, Mode='NaturalTrueColor'):
        """
        输出高斯处理后的png结果
        :param minification: 缩放系数, 你喜欢多大就多大, 一般 1-5
        :param Mode: NaturalTrueColor or Coastal
        :return:
        """
        data = self.GaussianResult(Mode)
        self.save_png_by_opencv(data, minification)

    def OutputFourierResultByPng(self, minification=5, Mode='NaturalTrueColor'):
        """
        输出傅里叶变换处理后的png结果
        :param minification: 缩放系数, 你喜欢多大就多大, 一般 1-5
        :param Mode: NaturalTrueColor or CoastalTrueColor
        :return:
        """
        data = self.FourierFilter(Mode)
        self.save_png_by_opencv(data, minification)

    def OutputMedianFilterByPng(self, minification=5, Mode="NaturalTrueColor"):
        """
        输出中值滤波处理后的png结果
        :param minification: 缩放系数, 你喜欢多大就多大, 一般 1-5
        :param Mode: NaturalTrueColor or Coastal
        :return:
        """
        data = self.MedianFilter(Mode)
        self.save_png_by_opencv(data, minification)

    def Equalized(self, minification=5, Mode='NaturalTrueColor', Filter="Gaussian"):
        """
        直方图均衡化(缺点：色彩失真)并输出png图像
        :param minification: 1-5
        :param Mode: NaturalTrueColor or Coastal
        :param Filter: Gaussian or Fourier or Median
        :return:
        """
        print(f"开始直方图均衡化处理……")
        if Filter == "Gaussian":
            data = self.GaussianResult(Mode)
        elif Filter == "Fourier":
            data = self.FourierFilter(Mode)
        elif Filter == "Median":
            data = self.MedianFilter(Mode)
        elif Filter == "None":
            if Mode == "NaturalTrueColor":
                data = self.read_tif_NaturalTrueColor()
            elif Mode == "CoastalTrueColor":
                data = self.read_tif_Coastal_Detection()

        # 对4通道的RGBA图像的每个通道分别进行直方图均衡化
        equalized_data = data.copy()
        for i in range(data.shape[2]):
            equalized_data[:, :, i] = cv2.equalizeHist(data[:, :, i].astype(np.uint8))
        print("直方图均衡化处理完成")
        self.save_png_by_opencv(equalized_data, minification)

    def EnhanceImage(self, minification=5, Mode='NaturalTrueColor', Filter="Gaussian"):
        """
        使用自适应直方图均衡化增强并输出png图像
        :param minification: 1-5
        :param Mode: NaturalTrueColor or Coastal
        :param Filter: Gaussian or Fourier or Median or None
        :return:
        """
        print("开始自适应直方图均衡化处理……")
        if Filter == "Gaussian":
            data = self.GaussianResult(Mode)
        elif Filter == "Fourier":
            data = self.FourierFilter(Mode)
        elif Filter == "Median":
            data = self.MedianFilter(Mode)
        elif Filter == "None":
            if Mode == "NaturalTrueColor":
                data = self.read_tif_NaturalTrueColor()
            elif Mode == "CoastalTrueColor":
                data = self.read_tif_Coastal_Detection()
        # 创建CLAHE对象
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        # 对4通道的RGB图像的每个通道分别进行自适应直方图均衡化
        enhanced_data = data.copy()
        for i in range(data.shape[2]):
            enhanced_data[:, :, i] = clahe.apply(data[:, :, i].astype(np.uint8))
        print("自适应直方图均衡化处理完成")
        self.save_png_by_opencv(enhanced_data, minification)

    def Sharpen(self, minification=5, Mode='NaturalTrueColor', Filter="Gaussian"):
        """
        锐化图像并输出png图像
        :param minification: 1-5
        :param Mode: NaturalTrueColor or CoastalTrueColor
        :param Filter: Gaussian or Fourier or Median or None
        :return:
        """
        print("开始锐化处理……")
        if Mode == 'NaturalTrueColor':
            data = self.read_tif_NaturalTrueColor()
        elif Mode == 'CoastalTrueColor':
            data = self.read_tif_Coastal_Detection()

        # 平滑处理
        if Filter == "Gaussian":
            smoothed_data = cv2.GaussianBlur(data, (0, 0), 1.5)
        elif Filter == "Fourier":
            smoothed_data = self.FourierFilter(Mode, 50)
        elif Filter == "Median":
            smoothed_data = self.MedianFilter(Mode, 5)
        elif Filter == "None":
            smoothed_data = data
        # 归一化数据
        smoothed_data = (smoothed_data - smoothed_data.min()) / (smoothed_data.max() - smoothed_data.min()) * 255
        smoothed_data = smoothed_data.astype(np.uint8)
        # 拉普拉斯滤波器
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        # 应用滤波器
        sharpened_data = cv2.filter2D(smoothed_data, -1, kernel)
        # 再次归一化
        sharpened_data = (sharpened_data - sharpened_data.min()) / (sharpened_data.max() - sharpened_data.min()) * 255
        sharpened_data = sharpened_data.astype(np.uint8)
        print("锐化完成")
        self.save_png_by_opencv(sharpened_data, minification)


def linear_stretch(data, num=1):
    """
    线性拉伸(单波段)
    @param data: 被拉伸图像矩阵
    @param num: 拉伸系数, 1-5
    @return: 拉伸后的图像矩阵
    """
    #x, y = np.shape(data)
    data_8bit = data
    data_8bit[data_8bit == -9999] = 0
    # Convert nan in the data to a specific value, for example
    d2 = np.percentile(data_8bit, num)
    u98 = np.percentile(data_8bit, 100 - num)
    maxout = 255
    minout = 0
    data_8bit_new = minout + ((data_8bit - d2) / (u98 - d2)) * (maxout - minout)
    data_8bit_new[data_8bit_new < minout] = minout
    data_8bit_new[data_8bit_new > maxout] = maxout
    data_8bit_new = data_8bit_new.astype(np.int32)
    return data_8bit_new


if __name__ == '__main__':
    path = r'Data/LC81250632021360LGN00'
    path1 = r'Data/LC81190432021350LGN00'
    path2 = r'Data/LC81190442021350LGN00'

    landsat8_Possesing(path).Sharpen(5, "Coastal", 'Median')
    # landsat8_Possesing(path).EnhanceImage(5, 'Coastal')
    # landsat8_Possesing(path='Test/LC82290442021350LGN00').EnhanceImage(5)
    # landsat8_Possesing(path).EnhanceImage(5, 'Coastal')
    # landsat8_Possesing(path2).EnhanceImage(5, 'Coastal')
    print("done")
