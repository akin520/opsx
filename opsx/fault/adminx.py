#coding:utf-8
import xadmin
from xadmin import views
from models import Type,Report,Better

from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction

from xadmin import site


class TypeAdmin(object):
    list_display = ('type','flag')
    list_display_line = ('type',) 
    list_per_page = 15

    list_filter = ['type','flag'] 
    search_fields = ['type',]  
    
    reversion_enable = True
    
xadmin.site.register(Type,TypeAdmin)

class ReportAdmin(object):
    list_display = ('title','isloss','handleStatus','type','discovertime','theprincipal',)
    list_display_line = ('title',) 
    list_per_page = 15

    list_filter = ['title','isloss'] 
    search_fields = ['title','isloss','type']  
    
    reversion_enable = True

xadmin.site.register(Report,ReportAdmin)


class BetterAdmin(object):
    list_display = ('fault','status','bettercontent','schedule','staff')
    list_display_line = ('fault',) 
    list_per_page = 15

    list_filter = ['fault','status'] 
    search_fields = ['fault',]  
    
    reversion_enable = True

xadmin.site.register(Better,BetterAdmin)



