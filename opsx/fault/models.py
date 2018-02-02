#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

import assets


TYPE_FLAG = (
    (0, u"停用"),
    (1, u"启用"), 
)

ISLOSS = (
    (0, u"未损失"),
    (1, u"损失"), 
)

HS = (
    (0, u"处理中"),
    (1, u"处理完成"), 
)

IS = (
    (0, u"未改进"),
    (1, u"已改进"), 
)

IC = (
    (0, u"不可控"),
    (1, u"可控"), 
)

SS = (
    (0, u"未完成"),
    (1, u"已完成"), 
)

class Type(models.Model):
    """故障类型"""
    type = models.CharField(max_length=32,verbose_name=u"故障类型")
    flag = models.SmallIntegerField(choices=TYPE_FLAG,verbose_name=u"是否可用",default=1)
    
    def __unicode__(self):
        return self.type
    
    class Meta:
        verbose_name = u"故障类型管理"
        verbose_name_plural = verbose_name
        
 
class Report(models.Model):
    """故障报告"""
    title = models.CharField(max_length=50,verbose_name=u"标题")
    isloss = models.SmallIntegerField(choices=ISLOSS,verbose_name=u"是否损失",default=0)
    handleStatus = models.SmallIntegerField(choices=HS,verbose_name=u"处理状态",default=0)
    isbetter = models.SmallIntegerField(choices=IS,verbose_name=u"是否有改进措施",default=0)
    writetime = models.DateTimeField(verbose_name="填写时间")
    type = models.ForeignKey(Type,verbose_name="故障类型",help_text=u"如果是硬件故障时，选择一下资产ID,如果硬件故障，请选择一下应用")
    #assets = models.CharField(max_length=50,verbose_name="资产ID",blank=True,null=True)
    
    iscontrol = models.SmallIntegerField(choices=IC,verbose_name=u"是否可控",default=1)
    discovertime = models.DateTimeField(verbose_name=u"发现时间")
    recovertime = models.DateTimeField(verbose_name=u"恢复时间",blank=True,null=True)
    submitstaff = models.ForeignKey(User,verbose_name=u"提交人")
    theprincipal = models.CharField(max_length=30,verbose_name=u"负责人",blank=True,null=True)
    #idc = models.CharField(max_length=50,verbose_name=u"IDC")
    idc = models.ForeignKey(assets.models.Idc,verbose_name=u"IDC",blank=True,null=True)
    application = models.ForeignKey(assets.models.Apptype,verbose_name=u"应用",blank=True,null=True)
    assets = models.ForeignKey(assets.models.Assets,verbose_name="资产ID",blank=True,null=True)
    faultdesc = models.TextField(verbose_name=u"故障描述",blank=True,null=True)
    lossdesc = models.TextField(verbose_name=u"损失描述",blank=True,null=True)
    faultreason = models.TextField(verbose_name=u"故障原因",blank=True,null=True)
    solution = models.TextField(verbose_name=u"解决方案",blank=True,null=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"故障报告管理"
        verbose_name_plural = verbose_name
    
class  Better(models.Model):
    """故障改进措施管理"""
    fault = models.ForeignKey(Report,verbose_name=u"故障ID")
    status = models.SmallIntegerField(choices=SS,verbose_name=u"完成状态")
    bettercontent = models.TextField(verbose_name=u"改进内容",blank=True,null=True)
    schedule = models.TextField(verbose_name=u"当前进度说明 ",blank=True,null=True)
    donetime = models.DateTimeField(verbose_name=u"改进完成日期")
    staff = models.CharField(max_length=50,verbose_name=u"改进实施人")
    
    def __unicode__(self):
        return "%s - %s" %(self.fault,self.status)
    
    class Meta:
        verbose_name = u"故障改进措施管理"
        verbose_name_plural = verbose_name    
 
 
 
 
 
        