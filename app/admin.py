from django.contrib import admin
import app.models as models

# Register your models here.
admin.site.register(models.Section)
admin.site.register(models.Supermarket)
admin.site.register(models.Employee)
admin.site.register(models.Product)
admin.site.register(models.Warehouse)
admin.site.register(models.Distributor)
admin.site.register(models.WareHStock)