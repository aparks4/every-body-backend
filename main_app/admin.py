from django.contrib import admin
from .models import TeamMember, Retreat, ResourceCategory, Resource

class RetreatAdmin(admin.ModelAdmin):
    list_display = ('name', 'dates')  # Fields to display in the list view
    list_filter = ('name', 'dates')  # Fields to use for filtering in the right sidebar
    search_fields = ('name', 'dates')  # Fields to search for using the search bar

# Register your models here.
admin.site.register(TeamMember)
admin.site.register(Retreat, RetreatAdmin)
admin.site.register(ResourceCategory)
admin.site.register(Resource)