from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus import  DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


from .models import (
    Photographers,
    Images,
    Payment
    
)

STATE_CHOICES = (
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
    ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
)

APP_CHOICES = (
    ('PS', 'PhotoShop'), ('LR', 'LightRoom')
)

USER_CHOICES = (
    ('Admin', 'Admin'), ('User', 'User')
)


class PhotographersForm(UserCreationForm):
     def __init__(self, *args, **kwargs):
         super(PhotographersForm, self).__init__(*args, **kwargs)
         self.fields["name"].label = "Nome"
         self.fields["lastname"].label = "Sobrenome"
         self.fields["birthday"].label = "Nascimento"
         self.fields["phone"].label = "Celular"
         self.fields["address"].label = "Endereço"
         self.fields["number"].label = "Número"
         self.fields["district"].label = "Bairro"
         self.fields["zip_code"].label = "CEP"
         self.fields["city"].label = "Cidade"
         self.fields["state"].label = "Estado"
         self.fields["password1"].label = "Senha"
         self.fields["password2"].label = "Repita a senha"
         self.fields["picture"].label = "Foto"
         self.fields["type_user"].label = "Tido de Usúario"
       
       
       # pode fazer isso com todos os campos
    
     name = forms.CharField( 
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Nome'}))
     
     lastname = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Sobrenome'}))
     email = forms.EmailField(
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Email Válido', 'id': 'email'}))
     picture = forms.FileField(required = False,
            widget=forms.ClearableFileInput(attrs={'multiple': 'False'}))

     phone = forms.CharField(
            widget=forms.TextInput(
                                    attrs={
                                           'placeholder': '(00)0000-0000', 'class': 'phone_with_ddd'}))
      
     cpf = forms.CharField(required = False,
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': '000.000.000-00', 'class': 'cpf', 'id': 'cpf'}))
     cnpj = forms.CharField(required = False,
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'xx.xxx.xxx/xxxx-xx', 'class': 'cnpj'}))

     birthday = forms.CharField(required = False,
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': '00/00/000', 'class': 'data', }))                                       

     address = forms.CharField(required = False,
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Rua, Av, Estrada'}))

     number = forms.CharField(required = False,
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'numero', 'class': 'numero'}))

     district = forms.CharField(required = False,
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'seu bairro'}))
     zip_code = forms.CharField(required = False,
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': '00000-000', 'class': 'cep'}))
     city = forms.CharField(required = False,
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Sua cidade'}))

     state = forms.ChoiceField(required = False, choices=STATE_CHOICES,  initial='RS')

     type_user = forms.ChoiceField(required = True, choices=USER_CHOICES,  initial='User')

     password1 = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                            'placeholder': 'Mínimo 8 digitos', 'id': 'password1'}))

     password2 = forms.CharField(widget=forms.PasswordInput(
                                    attrs={
                                            'placeholder': 'Mínimo 8 digitos', 'id': 'password2', 'label': 'Repita a senha'}))




     class Meta:
        model = User
        fields = ('username', 'name', 'lastname', 'email', 'picture', 'phone',  'cpf',
                  'cnpj', 'birthday', 'address', 'number', 'district',   'zip_code', 'city',
                  'state', 'type_user', 'password1', 'password2')

#name queryset que filtra só os photografhers cadastrado no sistema
class ImagesForm(forms.ModelForm):
            
       client = forms.CharField( 
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Cliente'}))

       number = forms.CharField(required = True, label='Código',
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'numero', 'class': 'numero'}))

       pictures = forms.CharField(required = True, label='Quantidade de Imagens',
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Quantidades de fotos', 'class': 'numero'}))

       checkin = forms.DateField(required=True, label='Recebidas', widget=DatePickerInput(format='%d/%m/%Y'))

       checkout = forms.DateField(required=False, label='Entregues', widget=DatePickerInput(format='%d/%m/%Y'))

       deadline = forms.DateField(required=False, label='Prazo', widget=DatePickerInput(format='%d/%m/%Y'))

       app  = forms.ChoiceField(required = True, label='Tratamentos', choices=APP_CHOICES,  initial='PS')

       price = forms.DecimalField(required = True, label='Valor',
            widget=forms.NumberInput(
                                    attrs={
                                            'placeholder': 'numero'}))

       Link = forms.CharField(required = False, label='Link',
            widget=forms.TextInput(
                                    attrs={
                                            'placeholder': 'Link'}))

       
       info = forms.CharField(required = False, label='Observações',
            widget=forms.Textarea(
                                    attrs={
                                            'width': "100%", 'cols': "80", 'rows': "4", 'placeholder': 'Observações de tratamento', 'id': 'textareaChars', 'maxlength': "255"}))

       
       class Meta:
              model = Images
              fields = '__all__'


class PaymentForm(forms.ModelForm):
            


       value = forms.DecimalField(required = True, label='Valor',
            widget=forms.NumberInput(
                                    attrs={
                                            'placeholder': 'numero'}))
    

       date = forms.DateField(required=True, label='Recebidas', widget=DatePickerInput(format='%d/%m/%Y'))

       
       
       class Meta:
              model = Payment
              fields = '__all__'

      
       