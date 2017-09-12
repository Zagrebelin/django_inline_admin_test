from django import forms
from django.contrib import admin

from .models import Person, Departament, Company


# code stolen here: https://stackoverflow.com/a/19556353
class DepartamentAdminForm(forms.ModelForm):
    class Meta:
        model = Departament
        fields = ['title', 'boss']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['boss'].queryset = Person.objects.filter(departament=self.instance)


class DepartamentInlineAdmin(admin.TabularInline):
    form = DepartamentAdminForm
    model = Departament


class PersonInlineAdmin(admin.TabularInline):
    model = Person


admin.site.register(Company, inlines=[DepartamentInlineAdmin])
admin.site.register(Departament, inlines=[PersonInlineAdmin], form=DepartamentAdminForm)
admin.site.register(Person)
