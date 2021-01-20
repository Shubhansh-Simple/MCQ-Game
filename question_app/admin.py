from django.contrib import admin
from .models        import Question, Numbering, Attempt

admin.site.register( Question )
admin.site.register( Numbering )
admin.site.register( Attempt )

