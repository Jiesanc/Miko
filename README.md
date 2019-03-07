## Django-Miko,一个可定制操作的组件

>Miko组件,能够快速实现对N张表的增删改查以及对表的定制化操作-- 批量执行,分页,关键字搜索,组合搜索等功能

## 该项目的成因和原理简介

项目中增删改查作为最基本和繁琐的操作,需要有一套适用于Django所有项目的组件
本组件参考Django-admin自带的后台管理系统,实现自身的可定制化操作

## 使用说明

### 设置

- 本组件基于Django1.11开发
- 在setting.py中注册当前app --> miko
- 在路由系统中
  from miko.service.miko import site
  urlpatterns = [
    url(r'^miko/', site.urls),
  ]
- 在每个app下生成1个miko.py文件
- 在miko.py文件内注册Models
  from miko.service.miko import site,MikoConfig
  
  class PublishConfig(MikoConfig):
    pass
    
  site.register(类名, PublishConfig)
  
  
  
  




