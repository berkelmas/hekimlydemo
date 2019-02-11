from django.urls import path
from .views import index, gogusestetigi, \
    burunestetigi, ameliyatsizyuzgerme, kombineestetik, vucutestetigi, \
    yuzestetigi, genitalestetik, elcerrahisi, botoks, sacekimi, biyikekimi, kasekimi, \
    sakalekimi, doktorhakkimizda, iletisim, yayinlarimiz

urlpatterns = [
    path('', index, name="index"),
    path('gogus-estetigi/', gogusestetigi, name="gogusestetigi"),
    path('burun-estetigi/', burunestetigi, name="burunestetigi"),
    path('ameliyatsiz-yuz-germe/', ameliyatsizyuzgerme, name="ameliyatsizyuzgerme"),
    path('kombine-estetik/', kombineestetik, name="kombineestetik"),
    path('vucut-estetigi/', vucutestetigi, name="vucutestetigi"),
    path('yuz-estetigi/', yuzestetigi, name="yuzestetigi"),
    path('genital-estetik/', genitalestetik, name="genitalestetik"),
    path('el-cerrahisi/', elcerrahisi, name="elcerrahisi"),
    path('botoks/', botoks, name="botoks"),
    path('sac-ekimi/', sacekimi, name="sacekimi"),
    path('biyik-ekimi/', biyikekimi, name="biyikekimi"),
    path('kas-ekimi/', kasekimi, name="kasekimi"),
    path('sakal-ekimi/', sakalekimi, name="sakalekimi"),
    path('doktor-hakkinda/', doktorhakkimizda, name="doktorhakkimizda"),
    path('iletisim/', iletisim, name="iletisim"),
    path('bilimsel-yayinlarimiz/', yayinlarimiz, name="bilimselyayinlarimiz"),

]