import os
import cv2
import numpy as np
import datetime
def Correction(path1):
    """
    对图像进行黑边裁剪(默认输出到Output文件夹)
    :param path1: 输入图像地址
    :return:
    """
    print("正在进行图像裁剪")
    img = cv2.imread(path1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 使用Canny边缘检测算法检测图像中的边缘
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    # 使用霍夫变换检测图像中的直线
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    # 获取检测到的直线中最长的一条
    longest_line = None
    max_length = 0
    for line in lines:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            length = np.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
            if length > max_length:
                max_length = length
                longest_line = line
    # 获取直线的端点坐标
    for rho, theta in longest_line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
    # 计算直线的角度
    angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
    # 获取最小外接矩形
    h, w = img.shape[:2]
    rect = cv2.minAreaRect(np.array([(x, y) for x in range(w) for y in range(h) if edges[y, x] > 0]))
    box = cv2.boxPoints(rect)
    box = np.intp(box)
    # 旋转原始图像以校正矩形
    width = int(rect[1][0])
    height = int(rect[1][1])
    src_pts = box.astype("float32")
    dst_pts = np.array([[0, height - 1],
                        [0, 0],
                        [width - 1, 0],
                        [width - 1, height - 1]], dtype="float32")
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warped = cv2.warpPerspective(img, M, (width, height))
    # 裁剪并保存结果图像
    output = warped[0:height, 0:width]
    # 创建唯一的文件名
    # 创建输出文件夹
    output_dir = os.getcwd() + r"\Output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # 创建缓存文件夹
    buffer_dir = os.getcwd() + r"\Buffer"
    if not os.path.exists(buffer_dir):
        os.makedirs(buffer_dir)
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"correction_{current_time}.png")
    buffer_path = os.path.join(buffer_dir, f"buffer.png")
    cv2.imwrite(buffer_path, output)
    cv2.imwrite(output_path, output)
    print("图像裁剪完成")
    print(f"图像保存至: {output_path}")

