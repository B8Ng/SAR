# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import sys
import gettext
import myico
_ = gettext.gettext

###########################################################################
## Class TopFrame
###########################################################################

class TopFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Landsat遥感图像处理工具"), pos = wx.DefaultPosition, size = wx.Size( 816,660 ), style = wx.DEFAULT_FRAME_STYLE^wx.TAB_TRAVERSAL^wx.RESIZE_BORDER^wx.MAXIMIZE_BOX )

        self.SetIcon(myico.AppIcon.GetIcon())
        self.rootpath = os.getcwd()

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.Menu = wx.MenuBar( 0 )
        self.Menu1 = wx.Menu()
        self.Menu1_1 = wx.MenuItem( self.Menu1, wx.ID_ANY, _(u"打开"), wx.EmptyString, wx.ITEM_NORMAL )
        self.Menu1.Append( self.Menu1_1 )

        self.Menu1_2 = wx.MenuItem( self.Menu1, wx.ID_ANY, _(u"主页"), wx.EmptyString, wx.ITEM_NORMAL )
        self.Menu1.Append( self.Menu1_2 )

        self.Menu1_3 = wx.MenuItem( self.Menu1, wx.ID_ANY, _(u"退出"), wx.EmptyString, wx.ITEM_NORMAL )
        self.Menu1.Append( self.Menu1_3 )

        self.Menu.Append( self.Menu1, _(u"文件") )

        self.Menu2 = wx.Menu()
        self.Menu2_1 = wx.MenuItem( self.Menu2, wx.ID_ANY, _(u"图像合成"), wx.EmptyString, wx.ITEM_NORMAL )
        self.Menu2.Append( self.Menu2_1 )

        self.Menu2_2 = wx.MenuItem( self.Menu2, wx.ID_ANY, _(u"图像裁剪"), wx.EmptyString, wx.ITEM_NORMAL )
        self.Menu2.Append( self.Menu2_2 )

        self.Menu2_3 = wx.MenuItem( self.Menu2, wx.ID_ANY, _(u"图像拼接"), wx.EmptyString, wx.ITEM_NORMAL )
        self.Menu2.Append( self.Menu2_3 )

        self.Menu2_4 = wx.MenuItem( self.Menu2, wx.ID_ANY, _(u"图像压缩"), wx.EmptyString, wx.ITEM_NORMAL )
        self.Menu2.Append( self.Menu2_4 )

        self.Menu2_5 = wx.MenuItem( self.Menu2, wx.ID_ANY, _(u"图像复原"), wx.EmptyString, wx.ITEM_NORMAL )
        self.Menu2.Append( self.Menu2_5 )

        self.Menu2_6 = wx.MenuItem( self.Menu2, wx.ID_ANY, _(u"图像去黑边"), wx.EmptyString, wx.ITEM_NORMAL )
        self.Menu2.Append( self.Menu2_6 )

        self.Menu.Append( self.Menu2, _(u"工具") )

        self.Menu3 = wx.Menu()
        self.Menu3_1 = wx.MenuItem( self.Menu3, wx.ID_ANY, _(u"关于"), wx.EmptyString, wx.ITEM_NORMAL )
        self.Menu3.Append( self.Menu3_1 )

        self.Menu.Append( self.Menu3, _(u"帮助") )

        self.SetMenuBar( self.Menu )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.Menu1_1Function, id = self.Menu1_1.GetId() )
        self.Bind( wx.EVT_MENU, self.Menu1_2Function, id = self.Menu1_2.GetId() )
        self.Bind( wx.EVT_MENU, self.Menu1_3Function, id = self.Menu1_3.GetId() )
        self.Bind( wx.EVT_MENU, self.Menu2_1Function, id = self.Menu2_1.GetId() )
        self.Bind( wx.EVT_MENU, self.Menu2_2Function, id = self.Menu2_2.GetId() )
        self.Bind( wx.EVT_MENU, self.Menu2_3Function, id = self.Menu2_3.GetId() )
        self.Bind( wx.EVT_MENU, self.Menu2_4Function, id = self.Menu2_4.GetId() )
        self.Bind( wx.EVT_MENU, self.Menu2_5Function, id = self.Menu2_5.GetId() )
        self.Bind( wx.EVT_MENU, self.Menu2_6Function, id = self.Menu2_6.GetId() )
        self.Bind( wx.EVT_MENU, self.Menu3_1Function, id = self.Menu3_1.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def Menu1_1Function( self, event ):
        event.Skip()

    def Menu1_2Function( self, event ):
        event.Skip()

    def Menu1_3Function( self, event ):
        event.Skip()

    def Menu2_1Function( self, event ):
        event.Skip()

    def Menu2_2Function( self, event ):
        event.Skip()

    def Menu2_3Function( self, event ):
        event.Skip()

    def Menu2_4Function( self, event ):
        event.Skip()

    def Menu2_5Function( self, event ):
        event.Skip()

    def Menu2_6Function( self, event ):
        event.Skip()

    def Menu3_1Function( self, event ):
        event.Skip()


###########################################################################
## Class MainPanel
###########################################################################

class MainPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.filepath = ''

        MainPanelSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        MainPanelSizer1.SetFlexibleDirection( wx.BOTH )
        MainPanelSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.MainPanelPath = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,500 ), wx.TR_DEFAULT_STYLE|wx.TR_HIDE_ROOT )
        self.root = self.MainPanelPath.AddRoot("Root")
        MainPanelSizer1.Add( self.MainPanelPath, 0, wx.ALL, 5 )

        self.MainPanelPic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 645,500 ), 0 )
        MainPanelSizer1.Add( self.MainPanelPic, 0, wx.ALL, 5 )


        MainPanelSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        MainPanelSizer1_1 = wx.BoxSizer( wx.VERTICAL )

        self.MainPanelSlider = wx.Slider( self, wx.ID_ANY, 0, 0, 180, wx.DefaultPosition, wx.Size( 300,30 ), wx.SL_MIN_MAX_LABELS|wx.SL_TOP )
        self.MainPanelSlider.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

        MainPanelSizer1_1.Add( self.MainPanelSlider, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.SHAPED, 0 )


        MainPanelSizer1.Add( MainPanelSizer1_1, 1, wx.EXPAND, 5 )


        self.SetSizer( MainPanelSizer1 )
        self.Layout()

        self.MainPanelPath.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_tree_select, self.MainPanelPath)
        self.MainPanelSlider.Bind(wx.EVT_SLIDER, self.slider)

    def __del__( self ):
        pass

    def create_tree(self, parent, path):
        # 递归地向树状组件中添加指定目录中的所有文件和子目录
        for item in os.listdir(path):
            fullpath = os.path.join(path, item)
            if os.path.isdir(fullpath):
                node = self.MainPanelPath.AppendItem(parent, item)
                self.create_tree(node, fullpath)
            else:
                ext = os.path.splitext(fullpath)[1].lower()
                if ext in [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tif"]:
                    self.MainPanelPath.AppendItem(parent, item, data=fullpath)

    def on_tree_select(self, event):
        # 处理树状组件的选中事件，更新预览窗格中的图像文件
        print('on_tree_select')
        event.Skip()

    def slider(self, event):
        print('slider')
        event.Skip()

###########################################################################
## Class CompositePanel
###########################################################################

class CompositePanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.SetMaxSize( wx.Size( 800,600 ) )

        CompositePanelSizer1 = wx.WrapSizer( wx.VERTICAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        CompositePanelSizer1_1 = wx.FlexGridSizer( 0, 3, 0, 0 )
        CompositePanelSizer1_1.SetFlexibleDirection( wx.BOTH )
        CompositePanelSizer1_1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.originalpic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 380,380 ), 0 )
        CompositePanelSizer1_1.Add( self.originalpic, 0, wx.ALL, 5 )


        CompositePanelSizer1_1.Add( ( 4, 0), 1, wx.EXPAND, 0 )

        self.compositedpic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 380,380 ), 0 )
        CompositePanelSizer1_1.Add( self.compositedpic, 0, wx.ALL, 5 )


        CompositePanelSizer1.Add( CompositePanelSizer1_1, 1, wx.EXPAND, 5 )

        CompositePanelSizer1_2 = wx.GridBagSizer( 0, 0 )
        CompositePanelSizer1_2.SetFlexibleDirection( wx.BOTH )
        CompositePanelSizer1_2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


        CompositePanelSizer1_2.Add( ( 110, 0 ), wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.CompositeText1 = wx.StaticText( self, wx.ID_ANY, _(u"合成波段前图像"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.CompositeText1.Wrap( -1 )

        self.CompositeText1.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

        CompositePanelSizer1_2.Add( self.CompositeText1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        CompositePanelSizer1_2.Add( ( 240, 0 ), wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        self.CompositeText2 = wx.StaticText( self, wx.ID_ANY, _(u"合成波段后图像"), wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        self.CompositeText2.Wrap( -1 )

        self.CompositeText2.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

        CompositePanelSizer1_2.Add( self.CompositeText2, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        CompositePanelSizer1.Add( CompositePanelSizer1_2, 1, wx.EXPAND, 5 )

        CompositePanelSizer1_3 = wx.FlexGridSizer( 0, 6, 0, 0 )
        CompositePanelSizer1_3.SetFlexibleDirection( wx.BOTH )
        CompositePanelSizer1_3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        CompositePanelSizer1_3_1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        CompositePanelSizer1_3_1.SetFlexibleDirection( wx.BOTH )
        CompositePanelSizer1_3_1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        CompositePanelSizer1_3_1_1 = wx.BoxSizer( wx.VERTICAL )

        CompositePanelSizer1_3_1_1_1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        CompositePanelSizer1_3_1_1_1.SetFlexibleDirection( wx.BOTH )
        CompositePanelSizer1_3_1_1_1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.CompositeText3 = wx.StaticText( self, wx.ID_ANY, _(u"输入目录 :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.CompositeText3.Wrap( -1 )

        CompositePanelSizer1_3_1_1_1.Add( self.CompositeText3, 0, wx.ALL, 5 )

        self.CompositeDirIn = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        CompositePanelSizer1_3_1_1_1.Add( self.CompositeDirIn, 0, wx.ALL, 5 )


        CompositePanelSizer1_3_1_1.Add( CompositePanelSizer1_3_1_1_1, 1, wx.TOP, 5 )

        self.CompositePanelTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 255,80 ), wx.TE_MULTILINE)
        CompositePanelSizer1_3_1_1.Add( self.CompositePanelTextCtrl, 0, wx.ALL, 5 )

        CompositePanelSizer1_3_1.Add( CompositePanelSizer1_3_1_1, 1, wx.EXPAND, 5 )

        CompositePanelSizer1_3_1_2 = wx.FlexGridSizer( 0, 5, 0, 0 )
        CompositePanelSizer1_3_1_2.SetFlexibleDirection( wx.BOTH )
        CompositePanelSizer1_3_1_2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        CompositePanelSizer1_3_1_2_1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"波段选择") ), wx.VERTICAL )

        BandBoxChoices = [ _(u"234（BGR）"), _(u"465（BGR）") ]
        self.BandBox = wx.ComboBox( CompositePanelSizer1_3_1_2_1.GetStaticBox(), wx.ID_ANY, _(u"请选择波段"), wx.DefaultPosition, wx.DefaultSize, BandBoxChoices, wx.CB_READONLY )
        self.BandBox.SetSelection( -1 )
        CompositePanelSizer1_3_1_2_1.Add( self.BandBox, 0, wx.ALL, 5 )


        CompositePanelSizer1_3_1_2.Add( CompositePanelSizer1_3_1_2_1, 1, wx.EXPAND, 5 )

        CompositePanelSizer1_3_1_2_2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"去噪模式") ), wx.VERTICAL )

        self.Mode1_1 = wx.RadioButton( CompositePanelSizer1_3_1_2_2.GetStaticBox(), wx.ID_ANY, _(u"高斯滤波器"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CompositePanelSizer1_3_1_2_2.Add( self.Mode1_1, 0, wx.ALL, 5 )

        self.Mode1_2 = wx.RadioButton( CompositePanelSizer1_3_1_2_2.GetStaticBox(), wx.ID_ANY, _(u"傅里叶滤波器"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CompositePanelSizer1_3_1_2_2.Add( self.Mode1_2, 0, wx.ALL, 5 )

        self.Mode1_3 = wx.RadioButton( CompositePanelSizer1_3_1_2_2.GetStaticBox(), wx.ID_ANY, _(u"中值滤波器"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CompositePanelSizer1_3_1_2_2.Add( self.Mode1_3, 0, wx.ALL, 5 )

        self.Mode1_4 = wx.RadioButton( CompositePanelSizer1_3_1_2_2.GetStaticBox(), wx.ID_ANY, _(u"无"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CompositePanelSizer1_3_1_2_2.Add( self.Mode1_4, 0, wx.ALL, 5 )


        CompositePanelSizer1_3_1_2.Add( CompositePanelSizer1_3_1_2_2, 1, wx.EXPAND, 5 )

        CompositePanelSizer1_3_1_2_3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"增强处理模式") ), wx.VERTICAL )

        self.Mode2_1 = wx.RadioButton( CompositePanelSizer1_3_1_2_3.GetStaticBox(), wx.ID_ANY, _(u"直方图均衡化"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CompositePanelSizer1_3_1_2_3.Add( self.Mode2_1, 0, wx.ALL, 5 )

        self.Mode2_2 = wx.RadioButton( CompositePanelSizer1_3_1_2_3.GetStaticBox(), wx.ID_ANY, _(u"自适应直方图均衡化"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CompositePanelSizer1_3_1_2_3.Add( self.Mode2_2, 0, wx.ALL, 5 )

        self.Mode2_3 = wx.RadioButton( CompositePanelSizer1_3_1_2_3.GetStaticBox(), wx.ID_ANY, _(u"图像锐化"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CompositePanelSizer1_3_1_2_3.Add( self.Mode2_3, 0, wx.ALL, 5 )

        self.Mode2_4 = wx.RadioButton( CompositePanelSizer1_3_1_2_3.GetStaticBox(), wx.ID_ANY, _(u"无"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CompositePanelSizer1_3_1_2_3.Add( self.Mode2_4, 0, wx.ALL, 5 )


        CompositePanelSizer1_3_1_2.Add( CompositePanelSizer1_3_1_2_3, 1, wx.EXPAND, 5 )


        CompositePanelSizer1_3_1_2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

        CompositePanelSizer1_3_1_2_4 = wx.BoxSizer( wx.VERTICAL )

        self.Confirmbtn = wx.Button( self, wx.ID_ANY, _(u"确定"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CompositePanelSizer1_3_1_2_4.Add( self.Confirmbtn, 0, wx.ALL, 5 )

        self.Backbtn = wx.Button( self, wx.ID_ANY, _(u"返回"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CompositePanelSizer1_3_1_2_4.Add( self.Backbtn, 0, wx.ALL, 5 )


        CompositePanelSizer1_3_1_2.Add( CompositePanelSizer1_3_1_2_4, 1, wx.EXPAND, 5 )


        CompositePanelSizer1_3_1.Add( CompositePanelSizer1_3_1_2, 1, wx.EXPAND, 5 )


        CompositePanelSizer1_3.Add( CompositePanelSizer1_3_1, 1, wx.EXPAND, 5 )


        CompositePanelSizer1.Add( CompositePanelSizer1_3, 1, wx.EXPAND, 5 )


        self.SetSizer( CompositePanelSizer1 )
        self.Layout()

        # Connect Events
        self.CompositeDirIn.Bind( wx.EVT_DIRPICKER_CHANGED, self.compositeDirINFunction )
        self.BandBox.Bind( wx.EVT_COMBOBOX, self.BandBoxFunction )
        self.Mode1_1.Bind( wx.EVT_RADIOBUTTON, self.Mode1_1Function )
        self.Mode1_2.Bind( wx.EVT_RADIOBUTTON, self.Mode1_2Function )
        self.Mode1_3.Bind( wx.EVT_RADIOBUTTON, self.Mode1_3Function )
        self.Mode1_4.Bind( wx.EVT_RADIOBUTTON, self.Mode1_4Function )
        self.Mode2_1.Bind( wx.EVT_RADIOBUTTON, self.Mode2_1Function )
        self.Mode2_2.Bind( wx.EVT_RADIOBUTTON, self.Mode2_2Function )
        self.Mode2_3.Bind( wx.EVT_RADIOBUTTON, self.Mode2_3Function )
        self.Mode2_4.Bind( wx.EVT_RADIOBUTTON, self.Mode2_4Function )
        self.Confirmbtn.Bind( wx.EVT_BUTTON, self.ConfirmbtnFunction )
        self.Backbtn.Bind( wx.EVT_BUTTON, self.BackbtnFunction )

        reprint = RedirectTextComposite(self.CompositePanelTextCtrl)
        sys.stdout = reprint

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def compositeDirINFunction( self, event ):
        event.Skip()

    def BandBoxFunction( self, event ):
        event.Skip()

    def Mode1_1Function( self, event ):
        event.Skip()

    def Mode1_2Function( self, event ):
        event.Skip()

    def Mode1_3Function( self, event ):
        event.Skip()

    def Mode1_4Function( self, event ):
        event.Skip()

    def Mode2_1Function( self, event ):
        event.Skip()

    def Mode2_2Function( self, event ):
        event.Skip()

    def Mode2_3Function( self, event ):
        event.Skip()

    def Mode2_4Function( self, event ):
        event.Skip()

    def ConfirmbtnFunction( self, event ):
        event.Skip()

    def BackbtnFunction( self, event ):
        event.Skip()


class RedirectTextComposite(object):
    def __init__(self,aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)

###########################################################################
## Class CropPanel
###########################################################################

class CropPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        CropPanelSizer1 = wx.BoxSizer( wx.VERTICAL )

        CropPanelSizer1_1 = wx.BoxSizer( wx.HORIZONTAL )

        self.originalpic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 380,380 ), 0 )
        CropPanelSizer1_1.Add( self.originalpic, 0, wx.ALL, 5 )


        CropPanelSizer1_1.Add( ( 4, 0), 1, wx.EXPAND, 5 )

        self.cropedpic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 380,380 ), 0 )
        CropPanelSizer1_1.Add( self.cropedpic, 0, wx.ALL, 5 )


        CropPanelSizer1.Add( CropPanelSizer1_1, 1, wx.EXPAND, 5 )

        CropPanelSizer1_2 = wx.BoxSizer( wx.HORIZONTAL )


        CropPanelSizer1_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.CropPanelText1 = wx.StaticText( self, wx.ID_ANY, _(u"裁剪前图像"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.CropPanelText1.Wrap( -1 )

        self.CropPanelText1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        CropPanelSizer1_2.Add( self.CropPanelText1, 0, wx.ALL, 5 )


        CropPanelSizer1_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CropPanelSizer1_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.CropPanelText2 = wx.StaticText( self, wx.ID_ANY, _(u"裁剪后图像"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.CropPanelText2.Wrap( -1 )

        self.CropPanelText2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        CropPanelSizer1_2.Add( self.CropPanelText2, 0, wx.ALL, 5 )


        CropPanelSizer1_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CropPanelSizer1.Add( CropPanelSizer1_2, 1, wx.EXPAND, 5 )

        CropPanelSizer1_3 = wx.BoxSizer( wx.HORIZONTAL )


        CropPanelSizer1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.CropPanelText3 = wx.StaticText( self, wx.ID_ANY, _(u"输入图像:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.CropPanelText3.Wrap( -1 )

        self.CropPanelText3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        CropPanelSizer1_3.Add( self.CropPanelText3, 0, wx.ALL, 5 )

        self.CropPanelFileIn = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.Size( 569,25 ), wx.FLP_DEFAULT_STYLE )
        CropPanelSizer1_3.Add( self.CropPanelFileIn, 0, wx.ALL, 5 )


        CropPanelSizer1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CropPanelSizer1.Add( CropPanelSizer1_3, 1, wx.EXPAND, 5 )

        CropPanelSizer1_4 = wx.BoxSizer( wx.HORIZONTAL )


        CropPanelSizer1_4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CropPanelSizer1_4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.CropPanelTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 440,120 ), wx.TE_MULTILINE)
        CropPanelSizer1_4.Add( self.CropPanelTextCtrl, 0, wx.ALL, 5 )


        CropPanelSizer1_4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        CropPanelSizer1_4_1 = wx.BoxSizer( wx.VERTICAL )


        CropPanelSizer1_4_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.Confirmbtn = wx.Button( self, wx.ID_ANY, _(u"确定"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CropPanelSizer1_4_1.Add( self.Confirmbtn, 0, wx.ALL, 5 )


        CropPanelSizer1_4_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.Backbtn = wx.Button( self, wx.ID_ANY, _(u"返回"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CropPanelSizer1_4_1.Add( self.Backbtn, 0, wx.ALL, 5 )


        CropPanelSizer1_4_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CropPanelSizer1_4.Add( CropPanelSizer1_4_1, 1, wx.EXPAND, 5 )


        CropPanelSizer1_4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CropPanelSizer1_4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CropPanelSizer1.Add( CropPanelSizer1_4, 1, wx.EXPAND, 5 )


        CropPanelSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.SetSizer( CropPanelSizer1 )
        self.Layout()

        # Connect Events
        self.CropPanelFileIn.Bind( wx.EVT_FILEPICKER_CHANGED, self.CropPanelFileInFunction )
        self.Confirmbtn.Bind( wx.EVT_BUTTON, self.ConfirmbtnFunction )
        self.Backbtn.Bind( wx.EVT_BUTTON, self.BackbtnFunction )

        reprint = RedirectTextCrop(self.CropPanelTextCtrl)
        sys.stdout = reprint

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def CropPanelFileInFunction( self, event ):
        event.Skip()

    def ConfirmbtnFunction( self, event ):
        event.Skip()

    def BackbtnFunction( self, event ):
        event.Skip()

class RedirectTextCrop(object):
    def __init__(self,aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)

###########################################################################
## Class MosiacPanel
###########################################################################

class MosiacPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        MosiacPanelSizer1 = wx.BoxSizer( wx.VERTICAL )


        MosiacPanelSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        MosiacPanelSizer1_1 = wx.BoxSizer( wx.HORIZONTAL )


        MosiacPanelSizer1_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.mosiac1pic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,250 ), 0 )
        MosiacPanelSizer1_1.Add( self.mosiac1pic, 0, wx.ALL, 5 )

        self.mosiac2pic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,250 ), 0 )
        MosiacPanelSizer1_1.Add( self.mosiac2pic, 0, wx.ALL, 5 )

        self.mosaicoutpic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,300 ), 0 )
        MosiacPanelSizer1_1.Add( self.mosaicoutpic, 0, wx.ALL, 5 )


        MosiacPanelSizer1_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1.Add( MosiacPanelSizer1_1, 1, wx.EXPAND, 5 )

        MosiacPanelSizer1_2 = wx.BoxSizer( wx.HORIZONTAL )


        MosiacPanelSizer1_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.MosiacPanelText1 = wx.StaticText( self, wx.ID_ANY, _(u"待拼接1"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.MosiacPanelText1.Wrap( -1 )

        self.MosiacPanelText1.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

        MosiacPanelSizer1_2.Add( self.MosiacPanelText1, 0, wx.ALL, 5 )


        MosiacPanelSizer1_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.MosiacPanelText2 = wx.StaticText( self, wx.ID_ANY, _(u"待拼接2"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.MosiacPanelText2.Wrap( -1 )

        self.MosiacPanelText2.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

        MosiacPanelSizer1_2.Add( self.MosiacPanelText2, 0, wx.ALL, 5 )


        MosiacPanelSizer1_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.MosiacPanelText3 = wx.StaticText( self, wx.ID_ANY, _(u"拼接后"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.MosiacPanelText3.Wrap( -1 )

        self.MosiacPanelText3.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

        MosiacPanelSizer1_2.Add( self.MosiacPanelText3, 0, wx.ALL, 5 )


        MosiacPanelSizer1_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1.Add( MosiacPanelSizer1_2, 1, wx.EXPAND, 5 )

        MosiacPanelSizer1_3 = wx.BoxSizer( wx.HORIZONTAL )

        self.MosiacPanelTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,200 ), wx.TE_MULTILINE )
        MosiacPanelSizer1_3.Add( self.MosiacPanelTextCtrl, 0, wx.ALL, 5 )

        MosiacPanelSizer1_3_1 = wx.BoxSizer( wx.VERTICAL )

        MosiacPanelSizer1_3_1_1 = wx.BoxSizer( wx.HORIZONTAL )

        self.MosiacPanelText4 = wx.StaticText( self, wx.ID_ANY, _(u"输入目录1:"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.MosiacPanelText4.Wrap( -1 )

        self.MosiacPanelText4.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        MosiacPanelSizer1_3_1_1.Add( self.MosiacPanelText4, 0, wx.ALL, 5 )

        self.MosiacPanelDirIn1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.Size( 430,-1 ), wx.DIRP_DEFAULT_STYLE )
        MosiacPanelSizer1_3_1_1.Add( self.MosiacPanelDirIn1, 0, wx.ALL, 5 )


        MosiacPanelSizer1_3_1.Add( MosiacPanelSizer1_3_1_1, 1, wx.EXPAND, 5 )

        MosiacPanelSizer1_3_1_2 = wx.BoxSizer( wx.HORIZONTAL )

        self.MosiacPanelText5 = wx.StaticText( self, wx.ID_ANY, _(u"输入目录2:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.MosiacPanelText5.Wrap( -1 )

        self.MosiacPanelText5.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        MosiacPanelSizer1_3_1_2.Add( self.MosiacPanelText5, 0, wx.ALL, 5 )

        self.MosiacPanelDirIn2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.Size( 430,-1 ), wx.DIRP_DEFAULT_STYLE )
        MosiacPanelSizer1_3_1_2.Add( self.MosiacPanelDirIn2, 0, wx.ALL, 5 )


        MosiacPanelSizer1_3_1.Add( MosiacPanelSizer1_3_1_2, 1, wx.EXPAND, 5 )

        MosiacPanelSizer1_3_1_3 = wx.BoxSizer( wx.HORIZONTAL )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.Confirmbtn = wx.Button( self, wx.ID_ANY, _(u"确定"), wx.DefaultPosition, wx.DefaultSize, 0 )
        MosiacPanelSizer1_3_1_3.Add( self.Confirmbtn, 0, wx.ALL, 5 )

        self.Backbtn = wx.Button( self, wx.ID_ANY, _(u"返回"), wx.DefaultPosition, wx.DefaultSize, 0 )
        MosiacPanelSizer1_3_1_3.Add( self.Backbtn, 0, wx.ALL, 5 )


        MosiacPanelSizer1_3_1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3_1.Add( MosiacPanelSizer1_3_1_3, 1, wx.EXPAND, 5 )


        MosiacPanelSizer1_3.Add( MosiacPanelSizer1_3_1, 1, wx.EXPAND, 5 )


        MosiacPanelSizer1.Add( MosiacPanelSizer1_3, 1, wx.EXPAND, 5 )


        MosiacPanelSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.SetSizer( MosiacPanelSizer1 )
        self.Layout()

        # Connect Events
        self.MosiacPanelDirIn1.Bind( wx.EVT_DIRPICKER_CHANGED, self.mosiacDirIn1Function )
        self.MosiacPanelDirIn2.Bind( wx.EVT_DIRPICKER_CHANGED, self.mosiacDirIn2Function )
        self.Confirmbtn.Bind( wx.EVT_BUTTON, self.ConfirmbtnFunction )
        self.Backbtn.Bind( wx.EVT_BUTTON, self.BackbtnFunction )

        reprint = RedirectTextMosiac(self.MosiacPanelTextCtrl)
        sys.stdout = reprint

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def mosiacDirIn1Function( self, event ):
        event.Skip()

    def mosiacDirIn2Function( self, event ):
        event.Skip()

    def ConfirmbtnFunction( self, event ):
        event.Skip()

    def BackbtnFunction( self, event ):
        event.Skip()

class RedirectTextMosiac(object):
    def __init__(self,aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)


###########################################################################
## Class WaveTransformPanel
###########################################################################


class WaveTransformPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        WaveTransformPanelSizer1 = wx.BoxSizer( wx.VERTICAL )

        WaveTransformPanelSizer1_1 = wx.BoxSizer( wx.HORIZONTAL )

        self.originalpic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 400,400 ), 0 )
        WaveTransformPanelSizer1_1.Add( self.originalpic, 0, wx.ALL, 5 )

        self.transformpic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 400,400 ), 0 )
        WaveTransformPanelSizer1_1.Add( self.transformpic, 0, wx.ALL, 5 )


        WaveTransformPanelSizer1.Add( WaveTransformPanelSizer1_1, 1, wx.EXPAND, 5 )

        WaveTransformPanelSizer1_2 = wx.BoxSizer( wx.VERTICAL )

        WaveTransformPanelSizer2_1 = wx.BoxSizer( wx.HORIZONTAL )


        WaveTransformPanelSizer2_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.WaveTransformPanelText1 = wx.StaticText( self, wx.ID_ANY, _(u"小波变换前图像"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.WaveTransformPanelText1.Wrap( -1 )

        self.WaveTransformPanelText1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        WaveTransformPanelSizer2_1.Add( self.WaveTransformPanelText1, 0, wx.ALL, 5 )


        WaveTransformPanelSizer2_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformPanelSizer2_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.WaveTransformPanelText2 = wx.StaticText( self, wx.ID_ANY, _(u"小波变换后图像"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.WaveTransformPanelText2.Wrap( -1 )

        self.WaveTransformPanelText2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        WaveTransformPanelSizer2_1.Add( self.WaveTransformPanelText2, 0, wx.ALL, 5 )


        WaveTransformPanelSizer2_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformPanelSizer1_2.Add( WaveTransformPanelSizer2_1, 1, wx.EXPAND, 5 )

        WaveTransformPanelSizer2_2 = wx.BoxSizer( wx.HORIZONTAL )

        WaveTransformPanelSizer2_2_1 = wx.BoxSizer( wx.HORIZONTAL )

        self.WaveTransformPanelTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,150 ),  style=wx.TE_MULTILINE)
        WaveTransformPanelSizer2_2_1.Add( self.WaveTransformPanelTextCtrl, 0, wx.ALL, 5 )


        WaveTransformPanelSizer2_2.Add( WaveTransformPanelSizer2_2_1, 1, wx.EXPAND, 5 )

        WaveTransformPanelSizer2_2_2 = wx.BoxSizer( wx.VERTICAL )

        WaveTransformPanelSizer2_2_2_1 = wx.BoxSizer( wx.HORIZONTAL )

        WaveTransformPanelSizer2_2_2_1_1 = wx.BoxSizer( wx.VERTICAL )


        WaveTransformPanelSizer2_2_2_1.Add( WaveTransformPanelSizer2_2_2_1_1, 1, wx.EXPAND, 5 )

        self.WaveTransformPanelText3 = wx.StaticText( self, wx.ID_ANY, _(u"输入图像:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.WaveTransformPanelText3.Wrap( -1 )

        self.WaveTransformPanelText3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        WaveTransformPanelSizer2_2_2_1.Add( self.WaveTransformPanelText3, 0, wx.ALL, 5 )

        self.WaveTransformPanelFileIn = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.Size( 480,25 ), wx.FLP_DEFAULT_STYLE )
        WaveTransformPanelSizer2_2_2_1.Add( self.WaveTransformPanelFileIn, 0, wx.ALL, 5 )


        WaveTransformPanelSizer2_2_2.Add( WaveTransformPanelSizer2_2_2_1, 1, wx.EXPAND, 5 )

        WaveTransformPanelSizer2_2_2_2 = wx.BoxSizer( wx.HORIZONTAL )


        WaveTransformPanelSizer2_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformPanelSizer2_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformPanelSizer2_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformPanelSizer2_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformPanelSizer2_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformPanelSizer2_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        WaveTransformPanelSizer2_2_2_2_1 = wx.BoxSizer( wx.VERTICAL )

        self.Confirmbtn = wx.Button( self, wx.ID_ANY, _(u"确定"), wx.DefaultPosition, wx.DefaultSize, 0 )
        WaveTransformPanelSizer2_2_2_2_1.Add( self.Confirmbtn, 0, wx.ALL, 5 )

        self.Backbtn = wx.Button( self, wx.ID_ANY, _(u"返回"), wx.DefaultPosition, wx.DefaultSize, 0 )
        WaveTransformPanelSizer2_2_2_2_1.Add( self.Backbtn, 0, wx.ALL, 5 )


        WaveTransformPanelSizer2_2_2_2.Add( WaveTransformPanelSizer2_2_2_2_1, 1, wx.EXPAND, 5 )


        WaveTransformPanelSizer2_2_2.Add( WaveTransformPanelSizer2_2_2_2, 1, wx.EXPAND, 5 )


        WaveTransformPanelSizer2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformPanelSizer2_2.Add( WaveTransformPanelSizer2_2_2, 1, wx.EXPAND, 5 )


        WaveTransformPanelSizer1_2.Add( WaveTransformPanelSizer2_2, 1, wx.EXPAND, 5 )


        WaveTransformPanelSizer1.Add( WaveTransformPanelSizer1_2, 1, wx.EXPAND, 5 )


        self.SetSizer( WaveTransformPanelSizer1 )
        self.Layout()

        # Connect Events
        self.WaveTransformPanelFileIn.Bind( wx.EVT_FILEPICKER_CHANGED, self.WaveTransformPanelFileInFunction )
        self.Confirmbtn.Bind( wx.EVT_BUTTON, self.ConfirmbtnFunction )
        self.Backbtn.Bind( wx.EVT_BUTTON, self.BackbtnFunction )

        reprint = RedirectTextWaveTransform(self.WaveTransformPanelTextCtrl)
        sys.stdout = reprint


    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def WaveTransformPanelFileInFunction( self, event ):
        event.Skip()

    def ConfirmbtnFunction( self, event ):
        event.Skip()

    def BackbtnFunction( self, event ):
        event.Skip()

class RedirectTextWaveTransform(object):
    def __init__(self,aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)



###########################################################################
## Class CorrectionPanel
###########################################################################

"""
class WaveTransformBackPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        WaveTransformBackPanelSizer1 = wx.BoxSizer( wx.VERTICAL )

        WaveTransformBackPanelSizer1_1 = wx.BoxSizer( wx.HORIZONTAL )


        WaveTransformBackPanelSizer1_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.transformpic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 400,400 ), 0 )
        WaveTransformBackPanelSizer1_1.Add( self.transformpic, 0, wx.ALL, 5 )


        WaveTransformBackPanelSizer1_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1.Add( WaveTransformBackPanelSizer1_1, 1, wx.EXPAND, 5 )

        WaveTransformBackPanelSizer1_2 = wx.BoxSizer( wx.VERTICAL )

        WaveTransformBackPanelSizer2_1 = wx.BoxSizer( wx.HORIZONTAL )


        WaveTransformBackPanelSizer2_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.WaveTransformBackPanelText1 = wx.StaticText( self, wx.ID_ANY, _(u"小波变换复原图像"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.WaveTransformBackPanelText1.Wrap( -1 )

        self.WaveTransformBackPanelText1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        WaveTransformBackPanelSizer2_1.Add( self.WaveTransformBackPanelText1, 0, wx.ALL, 5 )


        WaveTransformBackPanelSizer2_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2.Add( WaveTransformBackPanelSizer2_1, 1, wx.EXPAND, 5 )

        WaveTransformBackPanelSizer2_2 = wx.BoxSizer( wx.HORIZONTAL )


        WaveTransformBackPanelSizer2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.WaveTransformBackPanelText2 = wx.StaticText( self, wx.ID_ANY, _(u"输入npz文件:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.WaveTransformBackPanelText2.Wrap( -1 )

        self.WaveTransformBackPanelText2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        WaveTransformBackPanelSizer2_2.Add( self.WaveTransformBackPanelText2, 0, wx.ALL, 5 )

        self.WaveTransformBackPanelFileIn = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        WaveTransformBackPanelSizer2_2.Add( self.WaveTransformBackPanelFileIn, 0, wx.ALL, 5 )


        WaveTransformBackPanelSizer2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2.Add( WaveTransformBackPanelSizer2_2, 1, wx.EXPAND, 5 )

        WaveTransformBackPanelSizer2_3 = wx.BoxSizer( wx.HORIZONTAL )


        WaveTransformBackPanelSizer2_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.Confirmbtn = wx.Button( self, wx.ID_ANY, _(u"确定"), wx.DefaultPosition, wx.DefaultSize, 0 )
        WaveTransformBackPanelSizer2_3.Add( self.Confirmbtn, 0, wx.ALL, 5 )


        WaveTransformBackPanelSizer2_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2.Add( WaveTransformBackPanelSizer2_3, 1, wx.EXPAND, 5 )

        WaveTransformBackPanelSizer2_4 = wx.BoxSizer( wx.HORIZONTAL )


        WaveTransformBackPanelSizer2_4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.Backbtn = wx.Button( self, wx.ID_ANY, _(u"返回"), wx.DefaultPosition, wx.DefaultSize, 0 )
        WaveTransformBackPanelSizer2_4.Add( self.Backbtn, 0, wx.ALL, 5 )


        WaveTransformBackPanelSizer2_4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2.Add( WaveTransformBackPanelSizer2_4, 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1.Add( WaveTransformBackPanelSizer1_2, 1, wx.EXPAND, 5 )


        self.SetSizer( WaveTransformBackPanelSizer1 )
        self.Layout()

        # Connect Events
        self.WaveTransformBackPanelFileIn.Bind( wx.EVT_FILEPICKER_CHANGED, self.WaveTransformBackPanelFileInFunction )
        self.Confirmbtn.Bind( wx.EVT_BUTTON, self.ConfirmbtnFunction )
        self.Backbtn.Bind( wx.EVT_BUTTON, self.BackbtnFunction )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def WaveTransformBackPanelFileInFunction( self, event ):
        event.Skip()

    def ConfirmbtnFunction( self, event ):
        event.Skip()

    def BackbtnFunction( self, event ):
        event.Skip()

"""
class WaveTransformBackPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        WaveTransformBackPanelSizer1 = wx.BoxSizer( wx.VERTICAL )

        WaveTransformBackPanelSizer1_1 = wx.BoxSizer( wx.HORIZONTAL )


        WaveTransformBackPanelSizer1_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.transformpic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 400,400 ), 0 )
        WaveTransformBackPanelSizer1_1.Add( self.transformpic, 0, wx.ALL, 5 )


        WaveTransformBackPanelSizer1_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1.Add( WaveTransformBackPanelSizer1_1, 1, wx.EXPAND, 5 )

        WaveTransformBackPanelSizer1_2 = wx.BoxSizer( wx.VERTICAL )

        WaveTransformBackPanelSizer1_2_1 = wx.BoxSizer( wx.HORIZONTAL )


        WaveTransformBackPanelSizer1_2_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.WaveTransformBackPanelText1 = wx.StaticText( self, wx.ID_ANY, _(u"小波变换复原图像"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.WaveTransformBackPanelText1.Wrap( -1 )

        self.WaveTransformBackPanelText1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        WaveTransformBackPanelSizer1_2_1.Add( self.WaveTransformBackPanelText1, 0, wx.ALL, 5 )


        WaveTransformBackPanelSizer1_2_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2.Add( WaveTransformBackPanelSizer1_2_1, 1, wx.EXPAND, 5 )

        WaveTransformBackPanelSizer1_2_2 = wx.BoxSizer( wx.HORIZONTAL )

        WaveTransformBackPanelSizer1_2_2_1 = wx.BoxSizer( wx.HORIZONTAL )

        self.WaveTransformBackPanelTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,150 ), style=wx.TE_MULTILINE )
        WaveTransformBackPanelSizer1_2_2_1.Add( self.WaveTransformBackPanelTextCtrl, 0, wx.ALL, 5 )


        WaveTransformBackPanelSizer1_2_2.Add( WaveTransformBackPanelSizer1_2_2_1, 1, wx.EXPAND, 5 )

        WaveTransformBackPanelSizer1_2_2_2 = wx.BoxSizer( wx.VERTICAL )

        WaveTransformBackPanelSizer1_2_2_2_1 = wx.BoxSizer( wx.HORIZONTAL )

        WaveTransformBackPanelSizer1_2_2_2_1_1 = wx.BoxSizer( wx.VERTICAL )


        WaveTransformBackPanelSizer1_2_2_2_1.Add( WaveTransformBackPanelSizer1_2_2_2_1_1, 1, wx.EXPAND, 5 )

        self.WaveTransformBackPanelText3 = wx.StaticText( self, wx.ID_ANY, _(u"输入图像:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.WaveTransformBackPanelText3.Wrap( -1 )

        self.WaveTransformBackPanelText3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        WaveTransformBackPanelSizer1_2_2_2_1.Add( self.WaveTransformBackPanelText3, 0, wx.ALL, 5 )

        self.WaveTransformBackPanelFileIn = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.Size( 480,25 ), wx.FLP_DEFAULT_STYLE )
        WaveTransformBackPanelSizer1_2_2_2_1.Add( self.WaveTransformBackPanelFileIn, 0, wx.ALL, 5 )


        WaveTransformBackPanelSizer1_2_2_2.Add( WaveTransformBackPanelSizer1_2_2_2_1, 1, wx.EXPAND, 5 )

        WaveTransformBackPanelSizer1_2_2_2_2 = wx.BoxSizer( wx.HORIZONTAL )


        WaveTransformBackPanelSizer1_2_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        WaveTransformBackPanelSizer1_2_2_2_2_1 = wx.BoxSizer( wx.VERTICAL )

        self.Confirmbtn = wx.Button( self, wx.ID_ANY, _(u"确定"), wx.DefaultPosition, wx.DefaultSize, 0 )
        WaveTransformBackPanelSizer1_2_2_2_2_1.Add( self.Confirmbtn, 0, wx.ALL, 5 )

        self.Backbtn = wx.Button( self, wx.ID_ANY, _(u"返回"), wx.DefaultPosition, wx.DefaultSize, 0 )
        WaveTransformBackPanelSizer1_2_2_2_2_1.Add( self.Backbtn, 0, wx.ALL, 5 )


        WaveTransformBackPanelSizer1_2_2_2_2.Add( WaveTransformBackPanelSizer1_2_2_2_2_1, 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2_2_2.Add( WaveTransformBackPanelSizer1_2_2_2_2, 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2_2_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2_2.Add( WaveTransformBackPanelSizer1_2_2_2, 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1_2.Add( WaveTransformBackPanelSizer1_2_2, 1, wx.EXPAND, 5 )


        WaveTransformBackPanelSizer1.Add( WaveTransformBackPanelSizer1_2, 1, wx.EXPAND, 5 )


        self.SetSizer( WaveTransformBackPanelSizer1 )
        self.Layout()

        # Connect Events
        self.WaveTransformBackPanelFileIn.Bind( wx.EVT_FILEPICKER_CHANGED, self.WaveTransformBackPanelFileInFunction )
        self.Confirmbtn.Bind( wx.EVT_BUTTON, self.ConfirmbtnFunction )
        self.Backbtn.Bind( wx.EVT_BUTTON, self.BackbtnFunction )

        reprint = RedirectTextWaveTransform(self.WaveTransformBackPanelTextCtrl)
        sys.stdout = reprint

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def WaveTransformBackPanelFileInFunction( self, event ):
        event.Skip()

    def ConfirmbtnFunction( self, event ):
        event.Skip()

    def BackbtnFunction( self, event ):
        event.Skip()


class RedirectTextWaveTransformBack(object):
    def __init__(self,aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)

###########################################################################
## Class CorrectionPanel
###########################################################################

class CorrectionPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        CorrectionPanelSizer1 = wx.BoxSizer( wx.VERTICAL )

        CorrectionPanelSizer1_1 = wx.BoxSizer( wx.HORIZONTAL )

        self.orignalpic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 400,400 ), 0 )
        CorrectionPanelSizer1_1.Add( self.orignalpic, 0, wx.ALL, 5 )

        self.correctedpic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 400,400 ), 0 )
        CorrectionPanelSizer1_1.Add( self.correctedpic, 0, wx.ALL, 5 )


        CorrectionPanelSizer1.Add( CorrectionPanelSizer1_1, 1, wx.EXPAND, 5 )

        CorrectionPanelSizer1_2 = wx.BoxSizer( wx.HORIZONTAL )


        CorrectionPanelSizer1_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.CorrectionPanelText1 = wx.StaticText( self, wx.ID_ANY, _(u"图像去黑边"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.CorrectionPanelText1.Wrap( -1 )

        self.CorrectionPanelText1.SetFont( wx.Font( 22, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "幼圆" ) )

        CorrectionPanelSizer1_2.Add( self.CorrectionPanelText1, 0, wx.ALL, 5 )


        CorrectionPanelSizer1_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CorrectionPanelSizer1.Add( CorrectionPanelSizer1_2, 1, wx.EXPAND, 5 )

        CorrectionPanelSizer1_3 = wx.BoxSizer( wx.VERTICAL )

        CorrectionPanelSizer1_3_1 = wx.BoxSizer( wx.HORIZONTAL )


        CorrectionPanelSizer1_3_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.CorrectionPanelText2 = wx.StaticText( self, wx.ID_ANY, _(u"输入文件:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.CorrectionPanelText2.Wrap( -1 )

        self.CorrectionPanelText2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )

        CorrectionPanelSizer1_3_1.Add( self.CorrectionPanelText2, 0, wx.ALL, 5 )

        self.CorrectionPanelFileIn = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.Size( 500,-1 ), wx.FLP_DEFAULT_STYLE )
        CorrectionPanelSizer1_3_1.Add( self.CorrectionPanelFileIn, 0, wx.ALL, 5 )


        CorrectionPanelSizer1_3_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CorrectionPanelSizer1_3.Add( CorrectionPanelSizer1_3_1, 1, wx.EXPAND, 5 )

        CorrectionPanelSizer1_3_2 = wx.BoxSizer( wx.HORIZONTAL )


        CorrectionPanelSizer1_3_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CorrectionPanelSizer1_3_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.CorrectionPanelTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,100 ), wx.TE_MULTILINE)
        CorrectionPanelSizer1_3_2.Add( self.CorrectionPanelTextCtrl, 0, wx.ALL, 5 )


        CorrectionPanelSizer1_3_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CorrectionPanelSizer1_3_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CorrectionPanelSizer1_3_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        CorrectionPanelSizer1_3_2_1 = wx.BoxSizer( wx.VERTICAL )


        CorrectionPanelSizer1_3_2_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.Confirmbtn = wx.Button( self, wx.ID_ANY, _(u"确定"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CorrectionPanelSizer1_3_2_1.Add( self.Confirmbtn, 0, wx.ALL, 5 )


        CorrectionPanelSizer1_3_2_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.Backbtn = wx.Button( self, wx.ID_ANY, _(u"返回"), wx.DefaultPosition, wx.DefaultSize, 0 )
        CorrectionPanelSizer1_3_2_1.Add( self.Backbtn, 0, wx.ALL, 5 )


        CorrectionPanelSizer1_3_2_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CorrectionPanelSizer1_3_2.Add( CorrectionPanelSizer1_3_2_1, 1, wx.EXPAND, 5 )


        CorrectionPanelSizer1_3_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CorrectionPanelSizer1_3_2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CorrectionPanelSizer1_3.Add( CorrectionPanelSizer1_3_2, 1, wx.EXPAND, 5 )


        CorrectionPanelSizer1_3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        CorrectionPanelSizer1.Add( CorrectionPanelSizer1_3, 1, wx.EXPAND, 5 )


        self.SetSizer( CorrectionPanelSizer1 )
        self.Layout()

        # Connect Events
        self.CorrectionPanelFileIn.Bind( wx.EVT_FILEPICKER_CHANGED, self.CorrectionPanelFileInFunction )
        self.Confirmbtn.Bind( wx.EVT_BUTTON, self.ConfirmbtnFunction )
        self.Backbtn.Bind( wx.EVT_BUTTON, self.BackbtnFunction )

        reprint = RedirectTextCorrection(self.CorrectionPanelTextCtrl)
        sys.stdout = reprint

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def CorrectionPanelFileInFunction( self, event ):
        event.Skip()

    def ConfirmbtnFunction( self, event ):
        event.Skip()

    def BackbtnFunction( self, event ):
        event.Skip()



class RedirectTextCorrection(object):
    def __init__(self,aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)



###########################################################################
## Class Info
###########################################################################

class Info ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"关于"), pos = wx.DefaultPosition, size = wx.Size( 300,200 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        InfoSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.InfoText = wx.StaticText( self, wx.ID_ANY, _(u"   基于Python的Landsat遥感图像处理工具v1.3\n\n            本工具尚未开发完毕，待续......\n\n                                    作者：罗杰华、邱振邦\n"), wx.DefaultPosition, wx.Size( 300,100 ), 0 )
        self.InfoText.Wrap( -1 )

        InfoSizer1.Add( self.InfoText, 0, wx.ALL, 5 )

        InfoSizer1_1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        InfoSizer1_1.SetFlexibleDirection( wx.BOTH )
        InfoSizer1_1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


        InfoSizer1_1.Add( ( 110, 0), 1, wx.EXPAND, 5 )

        self.Exitbtn = wx.Button( self, wx.ID_ANY, _(u"关闭"), wx.DefaultPosition, wx.Size( 80,23 ), 0 )
        InfoSizer1_1.Add( self.Exitbtn, 0, wx.ALL, 0 )


        InfoSizer1.Add( InfoSizer1_1, 1, wx.SHAPED, 0 )


        self.SetSizer( InfoSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Exitbtn.Bind( wx.EVT_BUTTON, self.ExitbtnFunction )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def ExitbtnFunction( self, event ):
        event.Skip()


