from django import forms
from django.forms.widgets import RadioSelect
class NameForm(forms.Form):
    methodslist=(
        (0, 'Rectangles'),
        (1, 'Trapezoids'),
        (2, 'Parabolas'),
        (3, 'Gauss'),
        (4, 'Geometric Monte Carlos'),
        (5, 'Simple Monte Carlos'),
    )
    resttypeslist=(
        (0, 'Left'),
        (1, 'Right'),
        (2, 'Middle')
    )
    roundLim = forms.IntegerField(initial=2)
    mainTask = forms.CharField(max_length="1000",initial="x")
    solvmethod = forms.ChoiceField(choices=(methodslist))
    resttypes = forms.ChoiceField(choices=(resttypeslist))
    acuracy = forms.IntegerField(initial=10)
    experiments = forms.IntegerField(initial=10)
    minrange = forms.FloatField(initial=-10)
    maxrange = forms.FloatField(initial=10)
    scalings = forms.IntegerField(max_value=100,min_value=1,initial=10)






