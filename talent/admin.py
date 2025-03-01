from django.contrib import admin
from .models import Talent, TalentImage

# Register your models here.
class TalentImageInline(admin.TabularInline):  # ✅ Allows adding multiple images inside Talent Admin
    model = TalentImage
    extra = 3  # Number of empty image fields to show

class TalentAdmin(admin.ModelAdmin):
    inlines = [TalentImageInline]  # ✅ Adds multiple image upload inside Talent

admin.site.register(Talent, TalentAdmin)
admin.site.register(TalentImage)  # ✅ Keep this if you still want to add images separately