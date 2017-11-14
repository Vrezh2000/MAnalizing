import math
from django.shortcuts import render

from Analiz.analizator import Showgraf,CalcIntegral
from Analiz.forms import NameForm

def get_name(request):
    funcval = ""
    randpoints=[]
    scalings = 5
    integralrez = 0
    xmas = []
    ymas = []
    integxmas = []
    integymas = []
    er = []
    acur=1
    experims=10
    methchanged="0"
    resttypes="0"
    roundLimit=2
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        try:
            # create a form instance and populate it with data from the request:
            form = NameForm(request.POST,auto_id=True)
            # check whether it's valid:
            if form.is_valid():
                roundLimit = form.cleaned_data['roundLim']
                mytask = form.cleaned_data['mainTask']
                minval = form.cleaned_data['minrange']
                maxval = form.cleaned_data['maxrange']
                integminval = minval
                integmaxval = maxval
                acur = form.cleaned_data['acuracy']
                experims = form.cleaned_data['experiments']
                scalings = form.cleaned_data['scalings']
                methchanged=form.cleaned_data['solvmethod']
                resttypes = form.cleaned_data['resttypes']
                funcval = minval
                while funcval <= maxval:
                    xmas.append(funcval)
                    ymas.append(Showgraf(mytask,funcval)[0])
                    er.append(Showgraf(mytask, funcval)[1])
                    funcval += 0.1
                    funcval = round(funcval,1)
                if er[0]==1:
                    for i in range(len(er)):
                        if er[i]==0:
                            integminval = xmas[i]
                            break
                if er[len(er)-1]==1:
                    for i in range(len(er)):
                        if er[len(er)-1-i]==0:
                            integmaxval = xmas[len(er)-1-i]
                            break
                funcval2 = integminval
                if methchanged=="0":
                    integralrez = CalcIntegral(mytask,methchanged,integminval,integmaxval,acur,0,0,0,resttypes)[0]
                else:
                    if methchanged=="4":
                        integcounting=CalcIntegral(mytask, methchanged, integminval, integmaxval, acur,min(ymas),max(ymas),experims)
                        integralrez = integcounting[0]
                        randpoints = integcounting[1]
                    else:
                        integralrez = CalcIntegral(mytask, methchanged, integminval, integmaxval, acur)[0]
                if methchanged=="4":
                    integxmas=[integminval,integmaxval]
                    integymas=[min(ymas),max(ymas)]
                else:
                    intervals=acur
                    if methchanged == "0":
                        if resttypes=="2":
                            intervals = intervals*2
                    if methchanged == "3":
                        intervals=intervals+1
                    if methchanged == "5":
                        intervals=intervals-1

                    for i in range(intervals+1):
                        integxmas.append(funcval2)
                        integymas.append(Showgraf(mytask, funcval2)[0])
                        funcval2 += (integmaxval - integminval) / intervals
                        funcval2 = round(funcval2, 4)
                return render(request, 'Analiz/index.html', {'fr':0,'form': form,'xmas':xmas,'ymas':ymas,"integxmas":integxmas,"integymas":integymas,'cancscale':700,'er':er,'scalings':scalings,'integralrez':integralrez,'methchanged':methchanged,'resttypes':resttypes,'acur':acur,'roundLim':roundLimit,'randpoints':randpoints})
        except:
            return render(request, 'Analiz/index.html',
                          {'fr': 1, 'form': NameForm(auto_id=True), 'xmas': xmas, 'ymas': ymas, "integxmas": integxmas,
                           "integymas": integymas, 'cancscale': 700, 'er': er, 'scalings': scalings,
                           'integralrez': integralrez, 'methchanged': methchanged, 'resttypes': resttypes, 'acur': acur,
                           'roundLim': roundLimit, 'randpoints': randpoints})
    else:
        form = NameForm(auto_id=True)
    return render(request, 'Analiz/index.html', {'fr':1,'form': form,'xmas':xmas,'ymas':ymas,"integxmas":integxmas,"integymas":integymas,'cancscale':700,'er':er,'scalings':scalings,'integralrez':integralrez,'methchanged':methchanged,'resttypes':resttypes,'acur':acur,'roundLim':roundLimit,'randpoints':randpoints})