from django.contrib import admin
from .model.student import Student
from .model.branch import Branch

admin.site.register(Student)
admin.site.register(Branch)
