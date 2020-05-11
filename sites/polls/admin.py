from django.contrib import admin
from .models import Global_Indices
from .models import MAS_BSE
from .models import MAS_NSE
from .models import FD_CASH
from .models import FD_FII
from .models import FD_FandO
from .models import FD_MF_SEBI


# Register your models here.
admin.site.register(Global_Indices)
admin.site.register(MAS_BSE)
admin.site.register(MAS_NSE)
admin.site.register(FD_CASH)
admin.site.register(FD_FII)
admin.site.register(FD_FandO)
admin.site.register(FD_MF_SEBI)