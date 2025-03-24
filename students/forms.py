from django import forms

from students.models import Student

class StudentForm(forms.ModelForm):
    # Наследуемся от специального класса форм, который предоставляет
    # весь необходимый функционал, который нужно настроить
    class Meta:
        model = Student # Обязательно указываем модель
        #fields = '__all__' # и перечисляем поля для отображения
        fields = ('first_name', 'last_name', 'avatar', 'email', )

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']

        if 'mail.ru' not in cleaned_data:
            raise forms.ValidationError('Почта должна быть на домене mail.ru')

        return cleaned_data
