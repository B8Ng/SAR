import cv2 as cv
import numpy as np
from pywt import wavedec2, waverec2
import os
import time


def Wave_Transform(path):
    """
    图像小波变换:输入TIF、jpg或者png都可以
    :param path: 需要变换的图像地址
    :return: 变换后的图像数据: .npz
    """
    # 创建Output文件夹，如果不存在
    print("开始小波压缩……")
    output_dir = os.path.join(os.getcwd() , "Output")
    os.makedirs(output_dir, exist_ok=True)
    buffer_dir = os.path.join(os.getcwd() , "Buffer")
    os.makedirs(buffer_dir, exist_ok=True)
    im = cv.imread(path)
    if im.shape[1] > 500:
        (h, w) = im.shape[:2]
        width = 500
        height = int(h * (width / float(w)))
        im = cv.resize(im, (width, height), interpolation=cv.INTER_AREA)

    # 对每个通道进行二级小波分解
    coeffs_channels = []
    for i in range(3):
        coeffs = wavedec2(im[:, :, i], 'haar', level=2)
        coeffs_channels.append(coeffs)

    # 生成唯一的文件名
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(output_dir , f'wavelet_transform_{timestamp}.npz')
    # 保存二级小波变换结果到文件
    np.savez(filename,
             cA2_r=coeffs_channels[0][0], cH2_r=coeffs_channels[0][1][0], cV2_r=coeffs_channels[0][1][1],
             cD2_r=coeffs_channels[0][1][2],
             cH1_r=coeffs_channels[0][2][0], cV1_r=coeffs_channels[0][2][1], cD1_r=coeffs_channels[0][2][2],
             cA2_g=coeffs_channels[1][0], cH2_g=coeffs_channels[1][1][0], cV2_g=coeffs_channels[1][1][1],
             cD2_g=coeffs_channels[1][1][2],
             cH1_g=coeffs_channels[1][2][0], cV1_g=coeffs_channels[1][2][1], cD1_g=coeffs_channels[1][2][2],
             cA2_b=coeffs_channels[2][0], cH2_b=coeffs_channels[2][1][0], cV2_b=coeffs_channels[2][1][1],
             cD2_b=coeffs_channels[2][1][2],
             cH1_b=coeffs_channels[2][2][0], cV1_b=coeffs_channels[2][2][1], cD1_b=coeffs_channels[2][2][2])
    print(f"文件已保存至：{filename}")
    # 将红色通道的二级分解结果拼接显示
    cA2, (cH2, cV2, cD2) = coeffs_channels[0][:2]
    AH2 = np.concatenate([cA2, cH2 + 255], axis=1)
    VD2 = np.concatenate([cV2 + 255, cD2 + 255], axis=1)
    res2 = np.vstack([AH2, VD2])

    #cv.imshow('2D_DWT_2level', cv.convertScaleAbs(res2, alpha=(255.0 / res2.max())))
    # 保存显示的图像到缓存文件夹
    buffer_path = os.path.join(buffer_dir, f"buffer.png")
    print("小波压缩完成")
    cv.imwrite(buffer_path, cv.convertScaleAbs(res2, alpha=(255.0 / res2.max())))
    cv.waitKey(0)
    cv.destroyAllWindows()


def Wave_Reconstructed(path):
    """
    小波逆变换:输入.npz文件回复成原来的图像(彩色图像)
    :param path: 需要小波逆变换的.npz文件
    :return: 小波逆变换后的png图像
    """
    print("开始恢复图像……")
    filename = path
    # 加载小波变换结果
    data = np.load(filename)

    # 读取红色通道的小波变换系数
    cA2_r = data['cA2_r']
    cH2_r = data['cH2_r']
    cV2_r = data['cV2_r']
    cD2_r = data['cD2_r']
    cH1_r = data['cH1_r']
    cV1_r = data['cV1_r']
    cD1_r = data['cD1_r']

    # 读取绿色通道的小波变换系数
    cA2_g = data['cA2_g']
    cH2_g = data['cH2_g']
    cV2_g = data['cV2_g']
    cD2_g = data['cD2_g']
    cH1_g = data['cH1_g']
    cV1_g = data['cV1_g']
    cD1_g = data['cD1_g']

    # 读取蓝色通道的小波变换系数
    cA2_b = data['cA2_b']
    cH2_b = data['cH2_b']
    cV2_b = data['cV2_b']
    cD2_b = data['cD2_b']
    cH1_b = data['cH1_b']
    cV1_b = data['cV1_b']
    cD1_b = data['cD1_b']

    # 进行二级小波逆变换
    rec_img_r = waverec2((cA2_r, (cH2_r, cV2_r, cD2_r), (cH1_r, cV1_r, cD1_r)), 'haar')
    rec_img_g = waverec2((cA2_g, (cH2_g, cV2_g, cD2_g), (cH1_g, cV1_g, cD1_g)), 'haar')
    rec_img_b = waverec2((cA2_b, (cH2_b, cV2_b, cD2_b), (cH1_b, cV1_b, cD1_b)), 'haar')

    # 合并通道
    rec_img2 = cv.merge([rec_img_r, rec_img_g, rec_img_b])

    # 保存重建结果
    output_dir = os.path.join(os.getcwd() , "Output")
    os.makedirs(output_dir, exist_ok=True)
    buffer_dir = os.path.join(os.getcwd() , "Buffer")
    os.makedirs(buffer_dir, exist_ok=True)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    rec_filename2 = os.path.join(output_dir, f'reconstructed_image_2_level_{timestamp}.png')
    cv.imwrite(rec_filename2, rec_img2)
    print(f"文件已保存至：{rec_filename2}")
    # 显示结果
    #cv.imshow('2 level reconstruction', cv.convertScaleAbs(rec_img2, alpha=(255.0 / rec_img2.max())))
    if not os.path.exists(buffer_dir):
        os.makedirs(buffer_dir)
    # 保存显示的图像到缓存文件夹
    buffer_path = os.path.join(buffer_dir , f"buffer.png")
    cv.imwrite(buffer_path, rec_img2)
    print("恢复完成")
    cv.waitKey(0)
    cv.destroyAllWindows()


