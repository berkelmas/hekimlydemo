from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'doktorsitesi/index.html')


def gogusestetigi(request):
    return render(request, 'doktorsitesi/memeestetigi.html')

def burunestetigi(request):
    return render(request, 'doktorsitesi/burunestetigi.html')


def ameliyatsizyuzgerme(request):
    return render(request, 'doktorsitesi/ameliyatsizyuzgerme.html')


def kombineestetik(request):
    return render(request, 'doktorsitesi/kombineestetik.html')

def vucutestetigi(request):
    return render(request, 'doktorsitesi/vucutestetigi.html')

def yuzestetigi(request):
    return render(request, 'doktorsitesi/yuzestetigi.html')


def genitalestetik(request):
    return render(request, 'doktorsitesi/genitalestetik.html')

def elcerrahisi(request):
    return render(request, 'doktorsitesi/elcerrahisi.html')


def botoks(request):
    return render(request, 'doktorsitesi/botoks.html')


def sacekimi(request):
    return render(request, 'doktorsitesi/fuesacekimi.html')


def biyikekimi(request):
    return render(request, 'doktorsitesi/biyikekimi.html')

def kasekimi(request):
    return render(request, 'doktorsitesi/kasekimi.html')

def sakalekimi(request):
    return render(request, 'doktorsitesi/sakalekimi.html')


def doktorhakkimizda(request):
    return render(request, 'doktorsitesi/doktorhakkinda.html')


def yayinlarimiz(request):
    return render(request, 'doktorsitesi/yayinlarimiz.html')


def iletisim(request):
    return render(request, 'doktorsitesi/iletisim.html')

