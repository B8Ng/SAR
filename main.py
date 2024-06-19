import UI
import wx
import math
import SAR_Crop
import SAR_Possession
import SAR_Mosaic
import SAR_Wave_Transform
import SAR_Correction
import threading

class MainFrame(UI.TopFrame):
    def __init__(self, parent):
        UI.TopFrame.__init__(self, parent)

        #初始化面板
        self.PanelDefault()

        ####关闭窗口跳转#####
        self.Bind(wx.EVT_CLOSE, self.on_close)

    '''
    初始化函数
    '''
    def PanelDefault(self):
        self.Panel = None
        self.PanelFlag = 0
    def BackPanel(self):
        if self.Panel:
            self.Panel.Destroy()
        self.Panel = MainPanel(self)
        self.PanelFlag = 1

    def on_close(self, event):
        app.Destroy()
        wx.Exit()

    '''
    菜单按钮事件
    '''

    def Menu1_1Function( self, event ):
        if self.PanelFlag == 1:
            dialog = wx.DirDialog(self, "Select a folder")
            if dialog.ShowModal() == wx.ID_OK:
                self.Panel.MainPanelPath.DeleteChildren(self.Panel.root)
                self.Panel.create_tree(self.Panel.root, dialog.GetPath())
            dialog.Destroy()

    def Menu1_2Function( self, event ):
        if self.PanelFlag == 0:
            if self.Panel:
                self.Panel.Destroy()
            self.Panel = MainPanel(self)
            self.PanelFlag = 1

    def Menu1_3Function( self, event ):
        app.Destroy()
        wx.Exit()

    def Menu2_1Function( self, event ):
        if self.Panel:
            self.Panel.Destroy()
        self.Panel = CompositePanel(self)
        self.PanelFlag = 0

    def Menu2_2Function( self, event ):
        if self.Panel:
            self.Panel.Destroy()
        self.Panel = CropPanel(self)
        self.PanelFlag = 0

    def Menu2_3Function( self, event ):
        if self.Panel:
            self.Panel.Destroy()
        self.Panel = MosiacPanel(self)
        self.PanelFlag = 0

    def Menu2_4Function( self, event ):
        if self.Panel:
            self.Panel.Destroy()
        self.Panel = WaveTransformPanel(self)
        self.PanelFlag = 0

    def Menu2_5Function( self, event ):
        if self.Panel:
            self.Panel.Destroy()
        self.Panel = WaveTransformBackPanel(self)
        self.PanelFlag = 0

    def Menu2_6Function( self, event ):
        if self.Panel:
            self.Panel.Destroy()
        self.Panel = CorrectionPanel(self)
        self.PanelFlag = 0

    def Menu3_1Function( self, event ):
        info.Show()

class MainPanel(UI.MainPanel):
    def __init__(self, parent):
        UI.MainPanel.__init__(self, parent)

    def on_tree_select(self, event):
        # 处理树状组件的选中事件，更新预览窗格中的图像文件
             item = event.GetItem()
             if item and self.MainPanelPath:
                 self.filepath = self.MainPanelPath.GetItemData(item)
                 if self.filepath:
                     orgimage = wx.Image(self.filepath, wx.BITMAP_TYPE_ANY).Rescale(500, 500)
                     self.MainPanelPic.SetBitmap(orgimage)
                     self.MainPanelPic.Update()
                     self.MainPanelPic.Refresh()

    def slider(self, event):
        self.value = event.GetEventObject()
        self.x = self.value.GetValue()
        if self.filepath != '':
            threading.Thread(target=self.run_task).start()

    def run_task(self):
        rotimage = wx.Image(self.filepath, wx.BITMAP_TYPE_ANY).Rotate(self.x * 2 * math.pi / 360, (250, 250))
        wx.Image.Rescale(rotimage, 500, 500)
        self.MainPanelPic.SetBitmap(rotimage)
        self.MainPanelPic.Update()
        self.MainPanelPic.Refresh()

class CompositePanel(UI.CompositePanel):
    def __init__(self, parent):
        UI.CompositePanel.__init__(self, parent)

        ###模式状态初始化###
        self.BandChoice = 0
        self.QUZAOMode = 0
        self.CHULIMode = 0
        self.InDir = 0

    def compositeDirINFunction( self, event ):
        self.InDir = self.CompositeDirIn.GetPath()
        imglist =SAR_Possession.landsat8_Possesing(self.InDir).finded_all_band()
        img = wx.Image(imglist[0])
        wx.Image.Rescale(img, 380, 380)
        self.originalpic.SetBitmap(img)
        self.originalpic.Update()
        self.originalpic.Refresh()

    def BandBoxFunction( self, event ):
        self.BandChoice = event.GetString()

    def Mode1_1Function( self, event ):
        QUZAOMode = event.GetEventObject()
        self.QUZAOMode = QUZAOMode.GetLabel()

    def Mode1_2Function( self, event ):
        QUZAOMode = event.GetEventObject()
        self.QUZAOMode = QUZAOMode.GetLabel()

    def Mode1_3Function( self, event ):
        QUZAOMode = event.GetEventObject()
        self.QUZAOMode = QUZAOMode.GetLabel()

    def Mode1_4Function(self, event):
        QUZAOMode = event.GetEventObject()
        self.QUZAOMode = QUZAOMode.GetLabel()

    def Mode2_1Function( self, event ):
        CHULIMode = event.GetEventObject()
        self.CHULIMode = CHULIMode.GetLabel()

    def Mode2_2Function( self, event ):
        CHULIMode = event.GetEventObject()
        self.CHULIMode = CHULIMode.GetLabel()

    def Mode2_3Function( self, event ):
        CHULIMode = event.GetEventObject()
        self.CHULIMode = CHULIMode.GetLabel()

    def Mode2_4Function( self, event ):
        CHULIMode = event.GetEventObject()
        self.CHULIMode = CHULIMode.GetLabel()

    def ConfirmbtnFunction( self, event ):
            threading.Thread(target=self.run_task).start()

    def run_task(self):
        if self.InDir == 0 or self.BandChoice == 0 or self.QUZAOMode == 0 or self.CHULIMode == 0:
            toastone = wx.MessageDialog(None, "选项不能为空!", "错误信息提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框
        else:
                #波段234选项（16种）
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "无" and self.CHULIMode == "无":
                SAR_Possession.landsat8_Possesing(self.InDir).OutputNaturalTrueColorByPng(minification=5)
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "无" and self.CHULIMode == "图像锐化":
                SAR_Possession.landsat8_Possesing(self.InDir).Sharpen(minification=5, Mode='NaturalTrueColor', Filter='None')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "无" and self.CHULIMode == "自适应直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).EnhanceImage(minification=5, Mode='NaturalTrueColor', Filter='None')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "无" and self.CHULIMode == "直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).Equalized(minification=5, Mode='NaturalTrueColor', Filter='None')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "中值滤波器" and self.CHULIMode == "无":
                SAR_Possession.landsat8_Possesing(self.InDir).OutputMedianFilterByPng(minification=5, Mode='NaturalTrueColor')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "中值滤波器" and self.CHULIMode == "图像锐化":
                SAR_Possession.landsat8_Possesing(self.InDir).Sharpen(minification=5, Mode='NaturalTrueColor', Filter='Median')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "中值滤波器" and self.CHULIMode == "自适应直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).EnhanceImage(minification=5, Mode='NaturalTrueColor', Filter='Median')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "中值滤波器" and self.CHULIMode == "直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).Equalized(minification=5, Mode='NaturalTrueColor', Filter='Median')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "傅里叶滤波器" and self.CHULIMode == "无":
                SAR_Possession.landsat8_Possesing(self.InDir).OutputFourierResultByPng(minification=5, Mode='NaturalTrueColor')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "傅里叶滤波器" and self.CHULIMode == "图像锐化":
                SAR_Possession.landsat8_Possesing(self.InDir).Sharpen(minification=5, Mode='NaturalTrueColor', Filter='Fourier')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "傅里叶滤波器" and self.CHULIMode == "自适应直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).EnhanceImage(minification=5, Mode='NaturalTrueColor', Filter='Fourier')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "傅里叶滤波器" and self.CHULIMode == "直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).Equalized(minification=5, Mode='NaturalTrueColor', Filter='Fourier')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "高斯滤波器" and self.CHULIMode == "无":
                SAR_Possession.landsat8_Possesing(self.InDir).OutputGaussianResultByPng(minification=5, Mode='NaturalTrueColor')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "高斯滤波器" and self.CHULIMode == "图像锐化":
                SAR_Possession.landsat8_Possesing(self.InDir).Sharpen(minification=5, Mode='NaturalTrueColor', Filter='Gaussian')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "高斯滤波器" and self.CHULIMode == "自适应直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).EnhanceImage(minification=5, Mode='NaturalTrueColor', Filter='Gaussian')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "234（BGR）" and self.QUZAOMode == "高斯滤波器" and self.CHULIMode == "直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).Equalized(minification=5, Mode='NaturalTrueColor', Filter='Gaussian')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            # 波段234选项（16种）
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "无" and self.CHULIMode == "无":
                SAR_Possession.landsat8_Possesing(self.InDir).OutputNaturalTrueColorByPng(minification=5)
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "无" and self.CHULIMode == "图像锐化":
                SAR_Possession.landsat8_Possesing(self.InDir).Sharpen(minification=5, Mode='CoastalTrueColor',
                                                                      Filter='None')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "无" and self.CHULIMode == "自适应直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).EnhanceImage(minification=5, Mode='CoastalTrueColor',
                                                                           Filter='None')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "无" and self.CHULIMode == "直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).Equalized(minification=5, Mode='CoastalTrueColor',
                                                                        Filter='None')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "中值滤波器" and self.CHULIMode == "无":
                SAR_Possession.landsat8_Possesing(self.InDir).OutputMedianFilterByPng(minification=5,
                                                                                      Mode='CoastalTrueColor')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "中值滤波器" and self.CHULIMode == "图像锐化":
                SAR_Possession.landsat8_Possesing(self.InDir).Sharpen(minification=5, Mode='CoastalTrueColor',
                                                                      Filter='Median')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "中值滤波器" and self.CHULIMode == "自适应直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).EnhanceImage(minification=5, Mode='CoastalTrueColor',
                                                                           Filter='Median')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "中值滤波器" and self.CHULIMode == "直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).Equalized(minification=5, Mode='CoastalTrueColor',
                                                                        Filter='Median')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "傅里叶滤波器" and self.CHULIMode == "无":
                SAR_Possession.landsat8_Possesing(self.InDir).OutputFourierResultByPng(minification=5,
                                                                                       Mode='CoastalTrueColor')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "傅里叶滤波器" and self.CHULIMode == "图像锐化":
                SAR_Possession.landsat8_Possesing(self.InDir).Sharpen(minification=5, Mode='CoastalTrueColor',
                                                                      Filter='Fourier')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "傅里叶滤波器" and self.CHULIMode == "自适应直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).EnhanceImage(minification=5, Mode='CoastalTrueColor',
                                                                           Filter='Fourier')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "傅里叶滤波器" and self.CHULIMode == "直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).Equalized(minification=5, Mode='CoastalTrueColor',
                                                                        Filter='Fourier')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "高斯滤波器" and self.CHULIMode == "无":
                SAR_Possession.landsat8_Possesing(self.InDir).OutputGaussianResultByPng(minification=5,
                                                                                        Mode='CoastalTrueColor')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "高斯滤波器" and self.CHULIMode == "图像锐化":
                SAR_Possession.landsat8_Possesing(self.InDir).Sharpen(minification=5, Mode='CoastalTrueColor',
                                                                      Filter='Gaussian')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "高斯滤波器" and self.CHULIMode == "自适应直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).EnhanceImage(minification=5, Mode='CoastalTrueColor',
                                                                           Filter='Gaussian')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()
            if self.BandChoice == "465（BGR）" and self.QUZAOMode == "高斯滤波器" and self.CHULIMode == "直方图均衡化":
                SAR_Possession.landsat8_Possesing(self.InDir).Equalized(minification=5, Mode='CoastalTrueColor',
        
                                                                        Filter='Gaussian')
                img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(380, 380)
                self.compositedpic.SetBitmap(img)
                self.compositedpic.Update()
                self.compositedpic.Refresh()


    def BackbtnFunction( self, event ):
        frame.BackPanel()

class CropPanel(UI.CropPanel):
    def __init__(self, parent):
        UI.CropPanel.__init__(self, parent)
        self.InPath = 0

    def CropPanelFileInFunction( self, event ):
        self.InPath = self.CropPanelFileIn.GetPath()
        img = wx.Image(self.InPath)
        wx.Image.Rescale(img, 380, 380)
        self.originalpic.SetBitmap(img)
        self.originalpic.Update()
        self.originalpic.Refresh()

    def ConfirmbtnFunction( self, event ):
        threading.Thread(target=self.run_task).start()

    def run_task(self):
        if self.InPath == 0 :
            toastone = wx.MessageDialog(None, "请选择裁剪文件!", "错误信息提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框
        else:
            SAR_Crop.Crop(self.InPath)
            img = wx.Image(frame.rootpath + r"\Buffer\buffer.png", wx.BITMAP_TYPE_ANY)
            Cropimg = wx.Image.Rescale(img, 380, 380)
            self.cropedpic.SetBitmap(Cropimg)
            self.cropedpic.Update()
            self.cropedpic.Refresh()

    def BackbtnFunction( self, event ):
        frame.BackPanel()

class MosiacPanel(UI.MosiacPanel):
    def __init__(self, parent):
        UI.MosiacPanel.__init__(self, parent)
        self.InPath1 = 0
        self.InPath2 = 0

    def mosiacDirIn1Function( self, event ):
        self.InPath1 = self.MosiacPanelDirIn1.GetPath()
        imglist =SAR_Mosaic.Landsat8ProcessingForMosaic(self.InPath1).find_all_bands()
        img = wx.Image(imglist[0])
        wx.Image.Rescale(img, 250, 250)
        self.mosiac1pic.SetBitmap(img)
        self.mosiac1pic.Update()
        self.mosiac1pic.Refresh()

    def mosiacDirIn2Function( self, event ):
        self.InPath2 = self.MosiacPanelDirIn2.GetPath()
        imglist =SAR_Mosaic.Landsat8ProcessingForMosaic(self.InPath2).find_all_bands()
        img = wx.Image(imglist[0])
        wx.Image.Rescale(img, 250, 250)
        self.mosiac2pic.SetBitmap(img)
        self.mosiac2pic.Update()
        self.mosiac2pic.Refresh()

    def ConfirmbtnFunction( self, event ):
        threading.Thread(target=self.run_task).start()

    def run_task(self):
        if self.InPath1 == 0 or self.InPath2 == 0:
            toastone = wx.MessageDialog(None, "请选择正确的路径!", "错误信息提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框
        else:
            SAR_Mosaic.Mosaic_png(self.InPath1,self.InPath2)
            img = wx.Image(frame.rootpath + r"\Buffer\buffer.png", wx.BITMAP_TYPE_ANY)
            Mosiacimg = wx.Image.Rescale(img, 250, 300)
            self.mosaicoutpic.SetBitmap(Mosiacimg)
            self.mosaicoutpic.Update()
            self.mosaicoutpic.Refresh()

    def BackbtnFunction( self, event ):
        frame.BackPanel()

class WaveTransformPanel(UI.WaveTransformPanel):
    def __init__(self, parent):
        UI.WaveTransformPanel.__init__(self, parent)
        self.InPath = 0

    def WaveTransformPanelFileInFunction( self, event ):
        self.InPath = self.WaveTransformPanelFileIn.GetPath()
        img = wx.Image(self.InPath, wx.BITMAP_TYPE_ANY)
        WaveTransimg = wx.Image.Rescale(img, 400, 400)
        self.originalpic.SetBitmap(WaveTransimg)
        self.originalpic.Update()
        self.originalpic.Refresh()

    def ConfirmbtnFunction( self, event ):
        threading.Thread(target=self.run_task).start()

    def run_task(self):
        if self.InPath == 0:
            toastone = wx.MessageDialog(None, "请选择需要压缩的图像!", "错误信息提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框
        else:
            SAR_Wave_Transform.Wave_Transform(self.InPath)
            img = wx.Image(frame.rootpath + r"\Buffer\buffer.png", wx.BITMAP_TYPE_ANY)
            WaveTransimg = wx.Image.Rescale(img, 400, 400)
            self.transformpic.SetBitmap(WaveTransimg)
            self.transformpic.Update()
            self.transformpic.Refresh()

    def BackbtnFunction( self, event ):
        frame.BackPanel()

class WaveTransformBackPanel(UI.WaveTransformBackPanel):
    def __init__(self, parent):
        UI.WaveTransformBackPanel.__init__(self, parent)
        self.InPath = 0

    def WaveTransformBackPanelFileInFunction( self, event ):
        self.InPath = self.WaveTransformBackPanelFileIn.GetPath()

    def ConfirmbtnFunction( self, event ):

        threading.Thread(target=self.run_task).start()

    def run_task(self):
        if self.InPath == 0:
            toastone = wx.MessageDialog(None, "请选择正确的npz格式文件!", "错误信息提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框
        else:
            SAR_Wave_Transform.Wave_Reconstructed(self.InPath)
            img = wx.Image(frame.rootpath + r"\Buffer\buffer.png", wx.BITMAP_TYPE_ANY)
            WaveBackimg = wx.Image.Rescale(img, 400, 400)
            self.transformpic.SetBitmap(WaveBackimg)
            self.transformpic.Update()
            self.transformpic.Refresh()

    def BackbtnFunction( self, event ):
        frame.BackPanel()

class CorrectionPanel(UI.CorrectionPanel):
    def __init__(self, parent):
        UI.CorrectionPanel.__init__(self, parent)
        self.InFile = 0

    def CorrectionPanelFileInFunction( self, event ):
        self.InFile = self.CorrectionPanelFileIn.GetPath()
        img = wx.Image(self.InFile).Rescale(400, 400)
        self.orignalpic.SetBitmap(img)
        self.orignalpic.Update()
        self.orignalpic.Refresh()

    def ConfirmbtnFunction( self, event ):
        threading.Thread(target=self.run_task).start()

    def run_task(self):
        if self.InFile == 0:
            toastone = wx.MessageDialog(None, "请选择需要去黑边的图像!", "错误信息提示", wx.YES_DEFAULT | wx.ICON_QUESTION)
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()  # 则关闭提示框
        else:
            SAR_Correction.Correction(self.InFile)
            img = wx.Image(frame.rootpath + r"\Buffer\buffer.png").Rescale(400, 400)
            self.correctedpic.SetBitmap(img)
            self.correctedpic.Update()
            self.correctedpic.Refresh()

    def BackbtnFunction( self, event ):
        frame.BackPanel()

class Info(UI.Info):
    def __init__(self, parent):
        UI.Info.__init__(self, parent)

    def ExitbtnFunction(self, event):
        self.Hide()


app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
info = Info(None)
# start the applications
app.MainLoop()