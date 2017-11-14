import random
import re
import math
acts=[["^"],["*","/"],["+"]]
def CountSome(ts,v1,v2):
    val=0
    vf1=float(v1)
    vf2 = float(v2)
    if ts=="^":
        val = vf1 ** vf2
    if ts=="*":
        val =  vf1 * vf2
    if ts=="/":
        val =  vf1 / vf2
    if ts=="+":
        val =  vf1 + vf2
    if ts=="sin":
        val = math.sin(vf1)
    if ts=="cos":
        val = math.cos(vf1)
    if ts=="tg":
        c=math.cos(vf1)
        if c <= 0.1 and c>=-0.1:
            c=0
        val = math.sin(vf1)/c
    if ts=="ctg":
        s=math.sin(vf1)
        if s <= 0.1 and s>=-0.1:
            s=0
        val = math.cos(vf1)/s
    if ts=="arcsin":
        val = math.asin(vf1)
    if ts=="arccos":
        val = math.acos(vf1)
    if ts=="arctg":
        val = math.atan(vf1)
    if ts=="arcctg":
        val = math.pi/2-math.atan(vf1)
    if ts=="log":
        val = math.log(vf1,vf2)
    if ts=="lg":
        val = math.log10(vf1)
    if ts=="ln":
        val = math.log(vf1,math.e)
    return round(val,2)
def Solving(mytask,j=0):
    curtask=mytask
    convdegr = re.findall(r"\d-+", curtask)
    if curtask[0]=="-" and curtask[1]=="-":
        curtask = curtask.replace("--", "")
    else:
        curtask = curtask.replace("--", "+")
    for d in range(len(convdegr)):
        curtask = curtask.replace(convdegr[d], convdegr[d].replace("-", "+-"))
    for i in range(len((curtask))):
        for k in range(len(acts[j])):
            if i < len(curtask):
                if curtask[i] == acts[j][k]:
                    av = ""
                    bv = ""
                    n = i - 1
                    while re.match(r"[0-9\.-]", curtask[n]):
                        av += curtask[n]
                        if n > 0:
                            n -= 1
                        else:
                            break
                    n = i + 1
                    while re.match(r"[0-9\.-]", curtask[n]):
                        bv += curtask[n]
                        if n < len(curtask) - 1:
                            n += 1
                        else:
                            break
                    curtask = curtask.replace((av[::-1] + acts[j][k] + bv),str(CountSome(acts[j][k], float(av[::-1]), float(bv))))
                    return (Solving(curtask, 0))
    if j < len(acts)-1:
        return (Solving(curtask,j+1))
    else:
        return (curtask.replace("+",""))
def SolvDop(mytask):
    pat=r"[a-z]+-*[0-9\.]+"
    if re.search("log",mytask):
        pat = r"[a-z]+-*[0-9\.]+(,-*[0-9\.]+)*"
    if re.search(pat,mytask):
        curt=(re.search(pat,mytask)).group(0)
        curtfin=curt.split(",")
        if len(curtfin)>1:
            mytask = mytask.replace(curt,str(CountSome(re.search(r"[a-z]+",curtfin[0]).group(0),float(curtfin[1]),float(re.search(r"[0-9\.-]+",curtfin[0]).group(0)))))
        else:
            mytask = mytask.replace(curt,str(CountSome(re.search(r"[a-z]+",curtfin[0]).group(0),float(re.search(r"[0-9\.-]+",curtfin[0]).group(0)),0)))
        return SolvDop(mytask)
    else:
        return Solving(mytask)
def Calculating(mytask):
    fintask=mytask.replace("Pi",str(math.pi))
    fintask="("+fintask+")"
    modulspattern=r"\|[\)\(\w\.,\*\+\^/-]*[\)\w\.]+\|"
    while len(re.findall(modulspattern,fintask))>0:
        curmods=re.findall(modulspattern,fintask)
        for curmodul in curmods:
            stv=curmodul
            curmodul = curmodul.replace("|","")
            fintask = fintask.replace(stv,str(math.fabs(float(Calculating(curmodul)))))
    curactpattern=r"\([\d\*\+\^\./-]+\)"
    while len(re.findall(curactpattern,fintask))>0:
        curactions=re.findall(curactpattern,fintask)
        for i in range(len(curactions)):
            stv=curactions[i]
            curactions[i] = curactions[i].replace("(", "")
            curactions[i] = curactions[i].replace(")", "")
            fintask = fintask.replace(stv,Solving(curactions[i]))
    doppattern = r"\([\w\*\+\^\.,/-]+\)"
    while len(re.findall(doppattern,fintask))>0:
        dopsolvings = re.findall(doppattern, fintask)
        for i in range(len(dopsolvings)):
            stv = dopsolvings[i]
            dopsolvings[i] = dopsolvings[i].replace("(", "")
            dopsolvings[i] = dopsolvings[i].replace(")", "")
            fintask = fintask.replace(stv, SolvDop(dopsolvings[i]))
    return fintask
def Showgraf(mytask,val):
    fintask = mytask
    fintask = fintask.replace("x", str(val))
    rez=0
    er=0
    try:
        rez = float(Calculating(fintask))
    except:
        er=1
    return rez,er
def CalcIntegral(mytask, solvmet, a, b, n,fmin=0,fmax=0,n2=0,dopinf="None"):
    rndpoints = []
    result = 0
    try:
        h = 0
        if solvmet != "3":
            h = (b - a) / n
        for i in range(n):
            if solvmet == "0":
                if dopinf=="0":
                    result += Showgraf(mytask, a + h * i)[0]
                if dopinf=="1":
                    result += Showgraf(mytask, a + h * (1+i))[0]
                if dopinf=="2":
                    result += Showgraf(mytask, a + h * (i+0.5))[0]
            if solvmet == "1":
                if i > 0 and i < n:
                    result += Showgraf(mytask, a + h * i)[0]
            if solvmet == "2":
               if i>0 and i<n:
                    result += (2 + 2 * (i % 2)) * Showgraf(mytask, a + h * i)[0]
        if solvmet == "1":
            result += ((Showgraf(mytask, a)[0]) + Showgraf(mytask, a + h * n)[0])/2
        if solvmet == "2":
            result+=(Showgraf(mytask, a)[0]) + Showgraf(mytask, a + h * n)[0]
            result /= 3
        if solvmet == "3":
            constvariables = [[[1, 1], [-0.577350269, 0.577350269]],
                              [[0.555555556, 0.888888889, 0.555555556], [-0.774596669, 0, 0.774596669]],
                              [[0.347854845,0.652145155,0.652145155,0.347854845],[-0.861136312,-0.339981044,0.339981044,0.861136312]],
                              [[0.236926885,0.47862867,0.568888889,0.47862867,0.236926885],[-0.906179846,-0.53846931,0,0.53846931,0.906179846]],
                              [[0.171324492, 0.360761573, 0.467913935, 0.467913935, 0.360761573, 0.171324492],[-0.932469514, -0.661209386, -0.238619186, 0.238619186, 0.661209386, 0.932469514]]]
            sumfunc = 0
            for i in range(len(constvariables[n-2][0])):
                sumfunc += constvariables[n-2][0][i] * Showgraf(mytask, ((b + a) / 2 + ((b - a) / 2) * constvariables[n-2][1][i]))[0]
            result = ((b - a) / 2) * sumfunc
        if solvmet == "4":
            for j in range(n2):
                integpoints = []
                rndpoints = []
                for i in range(n):
                    rndpoints.append(i)
                    rndpoints[i] = [random.uniform(a, b), random.uniform(fmin, fmax)]
                    if (rndpoints[i][1] < Showgraf(mytask, rndpoints[i][0])[0] and rndpoints[i][1] >= 0) or (rndpoints[i][1] > Showgraf(mytask, rndpoints[i][0])[0] and rndpoints[i][1] < 0):
                        integpoints.append(i)
                        integpoints[len(integpoints) - 1] = rndpoints[i]
                pluspoints=[]
                minuspoints=[]
                for i in range(len(integpoints)):
                    if integpoints[i][1]>0:
                        pluspoints.append(integpoints[i][1])
                    else:
                        minuspoints.append(integpoints[i][1])
                result += (fmax - fmin) * (b - a) * ((len(pluspoints)-len(minuspoints))/len(rndpoints))
            result = result / n2
        if solvmet == "5":
            sumfunc=0
            for i in range(n):
                sumfunc+=Showgraf(mytask,a+i*((b-a)/(n-1)))[0]
            result = ((b-a)/n)*sumfunc
        if solvmet != "3" and solvmet!="4" and solvmet!="5":
            result *= h
    except:
        print("Error")
    return result,rndpoints

