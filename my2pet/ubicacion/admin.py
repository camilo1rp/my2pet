from django.contrib import admin
from .models import *
# Register your models here.
modelos= [ 
	Pais,
	Departamento,
	Ciudad,
]

admin.site.register(modelos)