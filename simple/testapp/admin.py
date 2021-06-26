from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Rubric, Article

# admin.site.register(Rubric, DraggableMPTTAdmin)
admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
admin.site.register(Article)
