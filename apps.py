from django.apps import AppConfig


class MikoConfig(AppConfig):
    name = 'miko'

    def ready(self):
        from django.utils.module_loading import autodiscover_modules
        # 当程序启动时，去每个app目录下找stark.py并加载。
        autodiscover_modules('miko')
