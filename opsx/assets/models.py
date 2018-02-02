#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

SERVER_TYPE = (
    (0, u"服务器"),
    (1, u"交换机"),
    (2, u"存储"),
    (3,u"其它"),
)

SERVER_VIRTUAL = (
    (0, u"实体机"),
    (1, u"虚拟机[HYPER-V]"),
    (2, u"虚拟机[KVM]"),
    (3, u"虚拟机[ESXI]"),
    (4, u"虚拟机[OTHER]"),
    (5, u"无"),
)

SERVER_FLAG = ( 
    (0, u"正常"),
    (1, u"故障"),
    (2, u"待用"),
    (3, u"报废"),
)

Product_FLAG = (
    (0, u"运营"),
    (1, u"公开测试"),
    (2, u"内部测试"),
    (3, u"未开放"),
    (4, u"停服"),
    (5, u"停运"), 
)

DEL_STATUS =(
    (0, u"可用"),
    (1, u"删除")
)

PRODUCTTYPE =(
    (0, u"游戏"),
    (1, u"非游戏")
)

# Create your models here.

class Contract(models.Model):
    """合同级品牌配置信息"""
    purchasebatch = models.CharField(max_length=50,verbose_name=u"采购批次")
    name = models.CharField(max_length=50,verbose_name=u"合同抬头")
    provider = models.CharField(max_length=50,verbose_name=u"供应商",blank=True,null=True)
    brand = models.CharField(max_length=50,verbose_name=u"品牌",blank=True,null=True)
    manager = models.CharField(max_length=50,verbose_name=u"负责人",blank=True,null=True)
    list = models.TextField(verbose_name=u"清单",blank=True,null=True)
    
    insertuser = models.ForeignKey(User,verbose_name=u"负责人",blank=True,null=True)
    insertdate = models.DateField(auto_now_add=True,verbose_name=u"添加时间")
    updatedate = models.DateField(auto_now=True,verbose_name=u"更新时间")
    
    def __unicode__(self):
        return self.purchasebatch
    
    class Meta:
        verbose_name = u"合同管理"
        verbose_name_plural = verbose_name
               

class Config(models.Model):
    """服务器配置信息"""
    info = models.CharField(max_length=200,verbose_name=u"设备配置")
    adddate = models.DateField(auto_now_add=True,verbose_name=u"添加时间")
    des = models.TextField(verbose_name=u"详细配置")
    contract = models.ForeignKey(Contract,verbose_name=u"合同编号")
    
    insertuser = models.ForeignKey(User,verbose_name=u"负责人",blank=True,null=True) 
    updatedate = models.DateField(auto_now=True,verbose_name=u"更新时间")
    
    def __unicode__(self):
        return self.info
    
    class Meta:
        verbose_name = u"配置管理"
        verbose_name_plural = verbose_name
        

class Idc(models.Model):
    """机房信息"""
    area = models.CharField(max_length=10,verbose_name=u"机房区域")
    idcname = models.CharField(max_length=30,verbose_name=u"机房名称")
    idcalias= models.CharField(max_length=10,verbose_name=u"别名")
    iprange = models.CharField(max_length=200,verbose_name=u"IP范围")
    mask = models.CharField(max_length=32,verbose_name=u"掩码")
    gateway = models.CharField(max_length=32,verbose_name=u"网关")
    swithip = models.CharField(max_length=32,verbose_name=u"交换机IP")
    contact = models.TextField(max_length=300,verbose_name=u"联系方式")
    totalserver = models.SmallIntegerField(max_length=6,verbose_name=u"服务器总数")
    totalline = models.SmallIntegerField(max_length=6,verbose_name=u"链路数")
    totalrack = models.IntegerField(max_length=6,verbose_name=u"机柜数")
    bandwidth = models.IntegerField(max_length=11,verbose_name=u"带宽")
    
    insertuser = models.ForeignKey(User,verbose_name=u"负责人",blank=True,null=True)
    insertdate = models.DateField(auto_now_add=True,verbose_name=u"添加时间")
    updatedate = models.DateField(auto_now=True,verbose_name=u"更新时间")
    
    def __unicode__(self):
        return self.idcname
    
    class Meta:
        verbose_name = u"IDC"
        verbose_name_plural = verbose_name
    
class Assets(models.Model):
    """设备信息"""
    idcname= models.ForeignKey(Idc,verbose_name=u"机房名称")
    dtype = models.SmallIntegerField(choices=SERVER_TYPE,verbose_name=u"设备类型",default=0) # 0=服务器;1=交换机;2=存储;3=其它;
    virtual = models.SmallIntegerField(choices=SERVER_VIRTUAL,verbose_name=u"主机类型",default=0) # 0=实体机;1=虚拟机
    idcrack = models.CharField(max_length=30,verbose_name=u"idc机柜",blank=True,null=True)
    ip = models.CharField(max_length=15,verbose_name=u"管理IP")
    ips = models.CharField(max_length=300,verbose_name=u"所有IP列表 ",blank=True,null=True)
    ipmi_ip = models.CharField(max_length=300,verbose_name=u"IPMI IP or 宿主机",blank=True,null=True,help_text=u"如果是虚拟机，不用添加，会自动对应宿主机；例如: [192.168.1.1]")
    appmark = models.CharField(max_length=50,verbose_name=u"应用备注",blank=True,null=True)
    xxsn = models.CharField(max_length=50,verbose_name=u"单位编号",blank=True,null=True)
    sn = models.CharField(max_length=50,verbose_name=u"生产编号",blank=True,null=True)
    setting = models.ForeignKey(Config,verbose_name=u"默认配置",blank=True,null=True)
    flag = models.SmallIntegerField(choices=SERVER_FLAG,verbose_name=u"资产状态",default=0) #0=正常;1=故障;2=待用;3=报废
    os = models.CharField(max_length=30,verbose_name=u"操作系统")
    
    virtual_to = models.ForeignKey('self',null=True ,blank=True ,verbose_name=u"实机体IP")  #http://wenku.it168.com/d_000666871.shtml
    settings = models.TextField(verbose_name=u"真实配置",blank=True,null=True) #主要用户工具收集
    
    insertuser = models.ForeignKey(User,verbose_name=u"负责人",blank=True,null=True)
    insertdate = models.DateField(auto_now_add=True,verbose_name=u"添加时间")
    updatedate = models.DateField(auto_now=True,verbose_name=u"更新时间")   
    
    
    def __unicode__(self):
        return self.ip
    
    class Meta:
        verbose_name = u"设备管理"
        verbose_name_plural = verbose_name
        
class Product(models.Model):
    productname = models.CharField(max_length=50,verbose_name=u"产品名称")
    shortname = models.CharField(max_length=50,verbose_name=u"产品简称")
    flag = models.SmallIntegerField(choices=Product_FLAG,verbose_name=u"产品状态") #flag 状态:1运营,2公开测试,3内部测试,4未开放,5停服,6停运
    producttype = models.SmallIntegerField(choices=PRODUCTTYPE,verbose_name=u"类型",blank=True,null=True)
    
    insertuser = models.ForeignKey(User,verbose_name=u"负责人",blank=True,null=True)
    insertdate = models.DateField(auto_now_add=True,verbose_name=u"添加时间")
    updatedate = models.DateField(auto_now=True,verbose_name=u"更新时间") 
   
    def __unicode__(self):
        return self.productname
    
    class Meta:
        verbose_name = u"产品管理"
        verbose_name_plural = verbose_name

class Region(models.Model):
    regionname = models.CharField(max_length=30,verbose_name=u"区名称")
    productid = models.ForeignKey(Product,verbose_name=u"产品名称")
    shortname = models.CharField(max_length=10,verbose_name=u"区简称")
    flag = models.SmallIntegerField(choices=Product_FLAG,verbose_name=u"产品状态") #flag 状态:1运营,2公开测试,3内部测试,4未开放,5停服,6停运
    
    insertuser = models.ForeignKey(User,verbose_name=u"负责人",blank=True,null=True)
    insertdate = models.DateField(auto_now_add=True,verbose_name=u"添加时间")
    updatedate = models.DateField(auto_now=True,verbose_name=u"更新时间")     

    def __unicode__(self):
        return self.regionname
    
    class Meta:
        verbose_name = u"区管理"
        verbose_name_plural = verbose_name

class Group(models.Model):
    idcid = models.ForeignKey(Idc,verbose_name=u"idc机房")
    productid = models.ForeignKey(Product,verbose_name=u"产品")
    regionid = models.ForeignKey(Region,verbose_name=u"游戏区")
    groupname = models.CharField(max_length=20,verbose_name=u"组名称")
    shortname = models.CharField(max_length=10,verbose_name=u"组简称")
    linesum = models.IntegerField(max_length=11,verbose_name=u"线总数")
    flag = models.SmallIntegerField(choices=Product_FLAG,verbose_name=u"产品状态") #flag 状态:1运营,2公开测试,3内部测试,4未开放,5停服,6停运
    
    insertuser = models.ForeignKey(User,verbose_name=u"负责人",blank=True,null=True)
    insertdate = models.DateField(auto_now_add=True,verbose_name=u"添加时间")
    updatedate = models.DateField(auto_now=True,verbose_name=u"更新时间")     

    def __unicode__(self):
        return self.groupname
    
    class Meta:
        verbose_name = u"组管理"
        verbose_name_plural = verbose_name
    

class Apptype(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"应用名称")
    des = models.CharField(max_length=255,verbose_name=u"应用描述")
    productid = models.ForeignKey(Product,verbose_name=u"产品")
    
    db = models.IntegerField(max_length=11,verbose_name=u"DB类型",blank=True,null=True,help_text=u"数据采集的时候使用1-4，如果超过需要修改采集工具")
    
    insertuser = models.ForeignKey(User,verbose_name=u"负责人",blank=True,null=True)
    insertdate = models.DateField(auto_now_add=True,verbose_name=u"添加时间")
    updatedate = models.DateField(auto_now=True,verbose_name=u"更新时间")
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u"应用管理"
        verbose_name_plural = verbose_name

class Appasset(models.Model):
    appid = models.ForeignKey(Apptype,verbose_name=u"应用名称")
    assetsid = models.ForeignKey(Assets,verbose_name=u"资 产ID")
    productid = models.ForeignKey(Product,verbose_name=u"产品")
    regionid = models.ForeignKey(Region,verbose_name=u"游戏区",blank=True,null=True)    
    groupid = models.ForeignKey(Group,verbose_name=u"游戏组",blank=True,null=True)
    status = models.SmallIntegerField(choices=DEL_STATUS,verbose_name=u"状态",default=0) #0;表示可用 1：表示删除
    port = models.IntegerField(max_length=10,verbose_name=u"端口号")
    

    insertuser = models.ForeignKey(User,verbose_name=u"负责人",blank=True,null=True)
    insertdate = models.DateField(auto_now_add=True,verbose_name=u"添加时间")
    updatedate = models.DateField(auto_now=True,verbose_name=u"更新时间")

    def __unicode__(self):
        return "%s - %s - %s - %s" % (self.productid,self.regionid,self.groupid,self.appid)
    
    class Meta:
        verbose_name = u"设备应用管理"
        verbose_name_plural = verbose_name    
    
        