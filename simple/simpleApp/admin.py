from django.contrib import admin
from .models import Post, Author
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class PostAdminForm(forms.Form):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'desc', 'name')

admin.site.register(Post)
admin.site.register(Author)
