from django import forms
from django.contrib import admin

from stephanie.main import models


class SizeInput(forms.widgets.TextInput):

    def render(self, name, value, attrs=None):
        if value:
            value = ' x '.join(str(x) for x in value)
            value += ' cm'
        return super(SizeInput, self).render(name, value, attrs=attrs)


class ArtworkAdminForm(forms.ModelForm):

    class Meta:
        model = models.Artwork
        widgets = {
            'size': SizeInput,
        }


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'modified')
    form = ArtworkAdminForm
    exclude = ('added', 'modified')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ArtGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    exclude = ('modified',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent', 'date')
    exclude = ('modified',)

    def date(self, obj):
        return obj.modified


admin.site.register(models.Artwork, ArtworkAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.ArtGroup, ArtGroupAdmin)
admin.site.register(models.Contact, ContactAdmin)
