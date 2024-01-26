from django.contrib import admin
from .models import Patient
from .models import Medecin
from .models import RendezVous
from .models import Dossier
from .models import Diagnostic
from .models import Ordonnance
from .models import Medicament
from .models import Salle


admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(RendezVous)
admin.site.register(Dossier)
admin.site.register(Diagnostic)
admin.site.register(Ordonnance)
admin.site.register(Medicament)
admin.site.register(Salle)

