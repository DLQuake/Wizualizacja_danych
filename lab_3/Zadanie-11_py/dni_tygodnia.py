import datetime
import locale

def dzien_tygodnia_dla_dowolnej_daty(data):
    locale.setlocale(locale.LC_ALL, 'pl_PL')
    return data.strftime("%A")

def dzien_tygodnia_na_podstawie_numeru_dnia_tygodnia(nr_tygodnia):
    lista=['poniedzialek','wtorek','sroda','czwartek','piatek','sobota','niedziela']
    return lista[nr_tygodnia-1]

def skrocone_nazwy_dni_tygodnia(nazwa):
    if nazwa=='poniedziałek':
        return 'pon'
    elif nazwa=='wtorek':
        return 'wt'
    elif nazwa=='środa':
        return 'śr'
    elif nazwa=='czwartek':
        return 'czw'
    elif nazwa=='piątek':
        return 'pt'
    elif nazwa=='sobota':
        return 'sob'
    elif nazwa=='niedziela':
        return 'niedz'