from django import forms


class RegistroForm(forms.Form):
    field1 = forms.CharField(label="Field1", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    Marcatemporal = forms.CharField(label="MarcaTemporal", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    MATRICULA = forms.CharField(label="Matrícula", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    NOMBRECOMPLETO = forms.CharField(label="Nombre Completo", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    FOTODELTRABAJADOR = forms.CharField(label="Foto Trabajador", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    FOTODELAFIRMA = forms.CharField(label="Foto Firma", max_length=250,  widget=forms.TextInput({'class': 'form-control'}))
    FECHADENACIMIENTO = forms.CharField(label="Fecha de Nacimiento", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    CATEGORIA = forms.CharField(label="Categoría", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    CENTRODETRABAJOACTUAL = forms.CharField(label="Adscripción Actual", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    ADSCRIPCIONESANTERIORES = forms.CharField(label="Adscripción Anterior", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    TURNO = forms.CharField(label="Turno", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    DOMICILIOPARTICULAR = forms.CharField(label="Domicilio", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    COLONIA = forms.CharField(label="Colonia", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    MUNICIPIO = forms.CharField(label="Municipio", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    SECCIONAL= forms.CharField(label="Seccional", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    NUMERODECELULAR= forms.CharField(label="# Célular", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    CORREO= forms.EmailField(label="Email", max_length=250, widget=forms.EmailInput({'class': 'form-control'}))
    ENCARGADODEESTRUCTURA= forms.CharField(label="Encargado Estructura", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    RESPONSABLEDE100= forms.CharField(label="Responsable de 100", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    RESPONSABLEDE10= forms.CharField(label="Responsable de 10", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    PARTICIPACIONESDELTRABAJADOR = forms.CharField(label="Participaciones Trabajador", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    INFORMACIONADICIONAL= forms.CharField(label="Información Adicional", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    DESCANSOS= forms.CharField(label="Descansos", max_length=250, widget=forms.TextInput({'class': 'form-control'}))  
    VACACIONESPROGRAMADAS= forms.CharField(label="Vacaciones Programadas", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    SERVICIO= forms.CharField(label="Servicio", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    PROMOCION= forms.CharField(label="Promoción", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    MOVILIZACION= forms.CharField(label="Movilización", max_length=250, widget=forms.TextInput({'class': 'form-control'}))
    MIRESPONSABLE= forms.CharField(label="Mi Responsable", max_length=250, widget=forms.TextInput({'class': 'form-control'}))


class SearchForm(forms.Form):
    q = forms.CharField(label='Natrícula:', max_length=10, widget=forms.TextInput({'class': 'form-control'}))
