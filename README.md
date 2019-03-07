## Django-Miko,一个可定制操作的组件

>Miko组件,能够快速实现对N张表的增删改查以及对表的定制化操作-- 批量执行,分页,关键字搜索,组合搜索等功能

## 该项目的成因和原理简介

项目中增删改查作为最基本和繁琐的操作,需要有一套适用于Django所有项目的组件
本组件参考Django-admin自带的后台管理系统,实现自身的可定制化操作

## 使用说明

### 设置

- 本组件基于Django1.11开发
- 在setting.py中注册当前app --> miko
- 注册路由系统
  ```python
  from miko.service.miko import site
  urlpatterns = [
    url(r'^miko/', site.urls),
  ]
  ```
- 需要在每个app下生成1个miko.py文件
- 在每个miko.py文件内注册Models
```python
  from miko.service.miko import site,MikoConfig
  
  class PublishConfig(MikoConfig):
    pass
    
  site.register(类名, PublishConfig)
 ```
  
### 对每个Model定制化功能

- C 默认具有这项功能
```python
def get_add_btn(self):
    return None
```

- R
```python
def get_list_display(self):
    return  [MikoConfig.display_checkbox, '需要展示的字段',StarkConfig.display_edit(编辑功能),StarkConfig.display_del(删除功能)]
```

- 批量执行

```python
   def multi_init(self, request):
        """
        初始化
        :param request:
        :return:
        """
        pass

    multi_init.text = "初始化"
```

- 关键字搜索

```python
静态字段
search_list = ['当前类的字段名','tel','user__title']
```

- 组合搜索

```python
   from miko.service.miko import Option
   
   list_filter = [
        Option('数据库的字段名', is_choice=是否是choice, 
				  is_multi=是否支持多选,condition=筛选条件,text_func=前端筛选文本, value_func=前端文本所对应的url)
        Option('level', is_choice=True, text_func=lambda x: x[1]),
        Option('title', is_multi=True),
        Option('pub', is_multi=True, text_func=lambda x:x.name)
        ]
  
```

### 后记

当前组件预留了一些钩子函数

- 定制ModelForm
```python
def get_model_form_class(self):

    return DepartModelForm

```

- 增加URL
```python
def extra_url(self):
  data = [
    url(r'^xxxxxxx/$', self.xxxxxx),
    ]
  return data
```









