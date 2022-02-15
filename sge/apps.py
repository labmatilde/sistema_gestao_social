from django.apps import AppConfig

# utilizado para fazer o registro na settings principal do projeto para mapear as urls
class SgeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sge'
