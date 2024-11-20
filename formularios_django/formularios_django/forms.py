from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='Escriba su nombre',required=True,max_length=100,help_text='100 caracteres máximo.')
    url = forms.URLField(label='Tu sitio web',required=False, initial='http://')
    comment = forms.CharField(label='Comentarios')

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre:',max_length=50,widget=forms.TextInput(attrs={'class':'input'}))
    email = forms.EmailField(label='Email',max_length=50)
    message = forms.CharField(label='Mensaje:')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name != 'Open':
            raise forms.ValidationError('Tan solo el valor "Open" está permitido.')
        else:
            return name