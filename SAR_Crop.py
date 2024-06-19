import os
from PIL import Image, ImageTk
import tkinter as tk
import datetime

class ImageCropper:
    """
    图像的裁剪
    """
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.crop_coordinates = None
        self.closed = False  # 标志窗口是否被关闭

        self.screen_width = 1980  # 屏幕宽度
        self.screen_height = 1080  # 屏幕高度
        self.margin = 100  # 保持一定的边距

        self.scale_factor = min((self.screen_width - self.margin) / self.image.width,
                                (self.screen_height - self.margin) / self.image.height)
        self.scaled_width = int(self.image.width * self.scale_factor)
        self.scaled_height = int(self.image.height * self.scale_factor)

        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.on_window_close)  # 捕捉窗口关闭事件
        self.canvas = tk.Canvas(self.root, width=self.scaled_width, height=self.scaled_height)
        self.canvas.pack()
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

        self.photo = ImageTk.PhotoImage(self.image.resize((self.scaled_width, self.scaled_height)))  # 调整图片大小以适应画布
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.root.mainloop()

    def on_window_close(self):
        """
        捕捉关闭事件
        """
        self.closed = True
        self.root.quit()
        self.root.destroy()

    def on_mouse_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_mouse_drag(self, event):
        self.canvas.delete("crop_rectangle")
        self.current_x = event.x
        self.current_y = event.y
        self.canvas.create_rectangle(self.start_x, self.start_y, self.current_x, self.current_y, outline="red", tags="crop_rectangle")

    def on_mouse_release(self, event):
        if not self.closed:  # 检查窗口是否被关闭
            self.canvas.delete("crop_rectangle")
            self.end_x = event.x
            self.end_y = event.y
            self.crop_coordinates = (min(self.start_x, self.end_x) / self.scale_factor,
                                     min(self.start_y, self.end_y) / self.scale_factor,
                                     max(self.start_x, self.end_x) / self.scale_factor,
                                     max(self.start_y, self.end_y) / self.scale_factor)
        self.root.quit()
        self.root.destroy()

def Crop(image_path):
    # 创建ImageCropper实例并获取裁剪区域坐标
    print("请滑动选择区域进行裁剪……")
    cropper = ImageCropper(image_path)
    if cropper.closed:
        print("裁剪取消，未保存图像。")
        return
    crop_coordinates = cropper.crop_coordinates  # 获取裁剪区域坐标
    print("裁剪区域坐标:", crop_coordinates)
    # 使用PIL库裁剪图像
    img = Image.open(image_path)
    cropped = img.crop(crop_coordinates)
    # 将图像转换为RGB模式
    cropped = cropped.convert("RGB")
    # 创建输出文件夹
    output_dir = "Output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # 创建缓存文件夹
    buffer_dir = "Buffer"
    if not os.path.exists(buffer_dir):
        os.makedirs(buffer_dir)
    # 保存裁剪后的图像,并输出保存的地址
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = os.path.join(output_dir, f"pil_cut_{current_time}.jpg")
    buffer_path = os.path.join(buffer_dir, f"buffer.png")
    cropped.save(save_path)
    cropped.save(buffer_path)
    print("裁剪后的图像已保存至:", save_path)


