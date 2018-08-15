from django.contrib import admin
from accounts.models import UserProfile, LeadPage, CultPage, ProfPage, EntrePage, GamePage, NatPage

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(LeadPage)
admin.site.register(CultPage)
admin.site.register(ProfPage)
admin.site.register(EntrePage)
admin.site.register(GamePage)
admin.site.register(NatPage)
