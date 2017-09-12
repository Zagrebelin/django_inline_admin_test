from django import forms
from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from .models import Person, Departament, Company


class DepartamentInlineAdmin(admin.TabularInline):
    model = Departament
    readonly_fields = ['get_departament_names']

    # https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields
    def get_departament_names(self, instance):
        return format_html_join(mark_safe('<br/>'),
                                '{}',
                                (line for line in instance.person_set.values_list('name')),
                                )

    get_departament_names.short_description = "List of dep members"


class PersonInlineAdmin(admin.TabularInline):
    model = Person


admin.site.register(Company, inlines=[DepartamentInlineAdmin])
admin.site.register(Departament, inlines=[PersonInlineAdmin])
admin.site.register(Person)
