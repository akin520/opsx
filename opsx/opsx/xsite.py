#coding:utf-8
from xadmin import Settings

from assets.models import *

class Base(Settings):
    enable_themes = True
    use_bootswatch = True

class Comm(Settings):
    menu_style = 'accordion'    #只有两种模式
    site_title = (u"OPSX运维管理系统")          #设置站名，这个是全局，也可以在Admin里面设置
    