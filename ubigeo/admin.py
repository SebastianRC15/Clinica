from django.contrib import admin
from .models import Ubigeo

@admin.register(Ubigeo)
class UbigeoAdmin(admin.ModelAdmin):
    list_display = ['departamento', 'provincia', 'distrito', 'clinica', 'activo', 'fecha_creacion']
    list_filter = ['clinica', 'activo', 'departamento']
    search_fields = ['departamento', 'provincia', 'distrito']
    list_per_page = 20

    fieldsets = (
        ('Información de Ubicación', {
            'fields': ('clinica', 'departamento', 'provincia', 'distrito', 'codigo_postal')
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )

    # 🔹 Filtrar registros según la clínica del usuario
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # superuser ve todo
            return qs
        if hasattr(request.user, 'userprofile') and request.user.userprofile.clinica:
            return qs.filter(clinica=request.user.userprofile.clinica)
        return qs.none()

    # 🔹 Asignar automáticamente la clínica al crear un registro
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser and hasattr(request.user, 'userprofile'):
            obj.clinica = request.user.userprofile.clinica
        super().save_model(request, obj, form, change)

    # 🔹 Ocultar el campo 'clinica' para usuarios normales
    def get_readonly_fields(self, request, obj=None):
        readonly = list(getattr(self, 'readonly_fields', []) or [])
        if not request.user.is_superuser:
            readonly.append('clinica')
        return readonly

