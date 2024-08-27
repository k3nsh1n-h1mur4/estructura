from django.contrib import admin


from estructurasApp.models import basep1

class basep1Admin(admin.ModelAdmin):
    #fields = ["field1","MATRICULA","NOMBRECOMPLETO"]
    search_fields = ["MATRICULA"]


admin.site.register(basep1, basep1Admin)
