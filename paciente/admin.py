from django.contrib import admin
from django import forms
from .models import Paciente
from ubigeo.models import Ubigeo

class PacienteAdminForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'flatpickr'}),
        }

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    form = PacienteAdminForm

    list_display = ['nombres', 'apellidos', 'dni', 'clinica', 'ubigeo', 'activo', 'fecha_registro']
    list_filter = ['clinica', 'activo', 'ubigeo__departamento']
    search_fields = ['nombres', 'apellidos', 'dni']
    list_per_page = 20

    fieldsets = (
        ('Información Personal', {
            'fields': ('clinica', 'nombres', 'apellidos', 'dni', 'fecha_nacimiento')
        }),
        ('Contacto', {
            'fields': ('telefono', 'email', 'direccion', 'ubigeo')
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )

    class Media:
        css = {
            'all': ('https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css',)
        }
        js = ('https://cdn.jsdelivr.net/npm/flatpickr', 'admin/js/paciente_flatpickr.js',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # superusuario ve todo
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

    # 🔹 Filtro dinámico para que ubigeo solo muestre los de la clínica del usuario
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "ubigeo" and not request.user.is_superuser:
            if hasattr(request.user, 'userprofile') and request.user.userprofile.clinica:
                kwargs["queryset"] = Ubigeo.objects.filter(clinica=request.user.userprofile.clinica)
            else:
                kwargs["queryset"] = Ubigeo.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



