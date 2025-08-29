from django import forms
from .models import Paciente
from ubigeo.models import Ubigeo
from clinica.models import Clinica

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombres', 'apellidos', 'dni', 'fecha_nacimiento', 
                 'telefono', 'email', 'direccion', 'ubigeo']
        widgets = {
            'fecha_nacimiento': forms.TextInput(attrs={
                'class': 'datepicker',  # clase que usará Flatpickr
                'autocomplete': 'off'
            }),
            'direccion': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        clinica_id = kwargs.pop('clinica_id', None)
        super().__init__(*args, **kwargs)
        
        # Filtrar ubigeos solo de la clínica actual
        if clinica_id:
            self.fields['ubigeo'].queryset = Ubigeo.get_for_clinica(clinica_id)
            self.fields['ubigeo'].empty_label = "Seleccione una ubicación"
        else:
            self.fields['ubigeo'].queryset = Ubigeo.objects.none()
    
    def save(self, commit=True):
        paciente = super().save(commit=False)
        if commit:
            paciente.save()
        return paciente
