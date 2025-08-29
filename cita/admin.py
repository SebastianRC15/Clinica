from django.contrib import admin
from .models import Cita
from paciente.models import Paciente

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'fecha_hora', 'clinica', 'estado', 'fecha_creacion']
    list_filter = ['clinica', 'estado', 'fecha_hora']
    search_fields = ['paciente__nombres', 'paciente__apellidos', 'motivo']
    list_per_page = 20
    date_hierarchy = 'fecha_hora'
    
    fieldsets = (
        ('Información de la Cita', {
            'fields': ('clinica', 'paciente', 'fecha_hora', 'motivo')
        }),
        ('Estado', {
            'fields': ('estado', 'observaciones')
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'userprofile') and request.user.userprofile.clinica:
            return qs.filter(clinica=request.user.userprofile.clinica)
        return qs.none()

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser and hasattr(request.user, 'userprofile'):
            obj.clinica = request.user.userprofile.clinica
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        readonly = list(getattr(self, 'readonly_fields', []) or [])
        if not request.user.is_superuser:
            readonly.append('clinica')
        return readonly

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "paciente" and not request.user.is_superuser:
            if hasattr(request.user, 'userprofile') and request.user.userprofile.clinica:
                kwargs["queryset"] = Paciente.objects.filter(clinica=request.user.userprofile.clinica)
            else:
                kwargs["queryset"] = Paciente.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
