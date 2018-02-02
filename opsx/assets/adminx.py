#coding:utf-8
import xadmin
from xadmin import views
from models import Contract,Config,Idc,Assets,Product,Region,Group,Apptype,Appasset

from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction

from xadmin import site


class ContractAdmin(object):
    list_display = ('purchasebatch','name','provider','brand','updatedate')
    list_display_line = ('purchasebatch',) 
    list_per_page = 15

    list_filter = ['purchasebatch','name','brand'] 
    search_fields = ['name',]
 
    def save_models(self):
        obj = self.new_obj
        obj.insertuser = self.request.user
        obj.save()  
    
    reversion_enable = True
    
xadmin.site.register(Contract,ContractAdmin)


class ConfigAdmin(object):
    list_display = ('info','des','updatedate')
    list_display_line = ('info',) 
    list_per_page = 15

    list_filter = ['info','des'] 
    search_fields = ['info',]

    def save_models(self):
        obj = self.new_obj
        obj.insertuser = self.request.user
        obj.save()  
     
    reversion_enable = True
       
xadmin.site.register(Config,ConfigAdmin)

class IdcAdmin(object):
    list_display = ('area','idcname','idcalias','iprange','mask','gateway','swithip','updatedate')
    list_display_line = ('idcname',) 
    list_per_page = 15

    list_filter = ['area','idcname','gateway','swithip'] 
    search_fields = ['idcname',]

    def save_models(self):
        obj = self.new_obj
        obj.insertuser = self.request.user
        obj.save()  
    
    reversion_enable = True
    
xadmin.site.register(Idc,IdcAdmin)


class AssetsAdmin(object):
    list_display = ('idcname','idcrack','dtype','xxsn','virtual','sn','flag','os','ip','ipmi_ip','ips','appmark')
    list_display_line = ('ip',) 
    list_per_page = 15

    list_filter = ['idcname','idcrack','ip','os','appmark','xxsn','sn','ipmi_ip'] 
    search_fields = ['ip',]

    def save_models(self):
        obj = self.new_obj
        obj.insertuser = self.request.user
        if obj.virtual in (1,2,3,4):
            obj.idcrack = "["+obj.virtual_to.idcrack+"]"
            obj.xxsn = "["+obj.virtual_to.xxsn+"]"
            obj.sn = "["+obj.virtual_to.sn+"]"
            obj.ipmi_ip = "["+obj.virtual_to.ip+"]"
        obj.save()  
    
    reversion_enable = True
    
xadmin.site.register(Assets,AssetsAdmin)


class ProductAdmin(object):
    list_display = ('productname','flag','shortname')
    list_display_line = ('productname',)

    list_filter = ['productname','shortname','flag']
    search_fields = ['productname',]

    def save_models(self):
        obj = self.new_obj
        obj.insertuser = self.request.user
        obj.save()  
    
    reversion_enable = True
    
xadmin.site.register(Product,ProductAdmin)


class RegionAdmin(object):
    list_display = ('regionname','flag','productid','shortname')
    list_display_line = ('regionname','productid')

    list_filter = ['regionname','productid','flag']
    search_fields = ['regionname',]    

    def save_models(self):
        obj = self.new_obj
        obj.insertuser = self.request.user
        obj.save()  
    
    reversion_enable = True
    
xadmin.site.register(Region,RegionAdmin)


class GroupAdmin(object):
    list_display = ('groupname','flag','regionid','shortname','idcid','productid')
    list_display_line = ('groupname',)

    list_filter = ['groupname','productid','flag']
    search_fields = ['groupname',]    

    def save_models(self):
        obj = self.new_obj
        obj.insertuser = self.request.user
        obj.save()  
    
    reversion_enable = True
    
xadmin.site.register(Group,GroupAdmin)   


class ApptypeAdmin(object):
    list_display = ('name','des','productid')
    list_display_line = ('name',)

    list_filter = ['name','des',]
    search_fields = ['name',]        

    def save_models(self):
        obj = self.new_obj
        obj.insertuser = self.request.user
        obj.save()  
    
    reversion_enable = True
    
xadmin.site.register(Apptype,ApptypeAdmin)    


class AppassetAdmin(object):
    list_display = ('productid','regionid','groupid','appid','assetsid','port','status')
    list_display_line = ('productid','appid',)

    list_filter = ['productid','appid','groupid','regionid']
    search_fields = ['productid',]
    
    #fieldsets = [('负责人', {'fields': ['insertuser'], 'classes': ['collapse']}),]
    
    def save_models(self):
        obj = self.new_obj
        obj.insertuser = self.request.user
        obj.save()    
    
    reversion_enable = True
    
xadmin.site.register(Appasset,AppassetAdmin)    














