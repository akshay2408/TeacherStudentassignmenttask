from django import forms
# from django.forms import formset_factory

# class StudentForm(forms.Form):
#     firstname = forms.CharField()
#     lastname = forms.CharField()
    

# ArticleFormSet = formset_factory(StudentForm)    
# formset = ArticleFormSet()
# for form in formset:
#     print(form.as_table())
    
# ArticleFormSet = formset_factory(ArticleForm, extra=2)    
class StudentForm(forms.Form):
    student_field = forms.BooleanField( )