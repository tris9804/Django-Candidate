from django.contrib import admin
from .models import Candidate, Votepool, Department, Choice


admin.site.register(Votepool)
admin.site.register(Department)
admin.site.register(Choice)

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 
    )








