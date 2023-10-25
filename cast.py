import re
import json
from util import preprocess_text, load_dataset, load_to_json


dataset = load_dataset()


tweets = [tweet['tweet_text'] for tweet in dataset.values() if 'tweet_text' in tweet and tweet.get('tweet_text') is not None]

def match_cast_member ():
    richard_mofedamijo = [re.compile(r'richard', re.IGNORECASE ), re.compile(r'mofe', re.IGNORECASE ), re.compile(r'damijo', re.IGNORECASE ), re.compile(r'mofedamijo', re.IGNORECASE ), re.compile(r'rmd', re.IGNORECASE )]
    ade_laoye = [re.compile(r'ade', re.IGNORECASE ), re.compile(r'laoye', re.IGNORECASE ), re.compile(r'adalaoye', re.IGNORECASE )]
    alex_usifo = [re.compile(r'alex', re.IGNORECASE ), re.compile(r'usifo', re.IGNORECASE ), re.compile(r'alexusifo', re.IGNORECASE )]
    olumide_oworu = [re.compile(r'olumide', re.IGNORECASE ), re.compile(r'oworu', re.IGNORECASE ), re.compile(r'olumideoworu', re.IGNORECASE )]
    shaffy_bello = [re.compile(r'shaffy', re.IGNORECASE ), re.compile(r'bello', re.IGNORECASE ), re.compile(r'shaffybello', re.IGNORECASE )]
    ireti_doyle = [re.compile(r'ireti', re.IGNORECASE ), re.compile(r'doyle', re.IGNORECASE ), re.compile(r'iretidoyle', re.IGNORECASE )]
    sam_dede= [re.compile(r'sam', re.IGNORECASE ), re.compile(r'dede', re.IGNORECASE ), re.compile(r'samdede', re.IGNORECASE )]
    kelechi_udegbe = [re.compile(r'kelechi', re.IGNORECASE ), re.compile(r'udegbe', re.IGNORECASE ), re.compile(r'kelechiudegbe', re.IGNORECASE )]
    bimbo_akintola = [ re.compile(r'akintola', re.IGNORECASE ), re.compile(r'bimboakintola', re.IGNORECASE )]
    femi_branch = [re.compile(r'femi', re.IGNORECASE ), re.compile(r'branch', re.IGNORECASE ), re.compile(r'femibranch', re.IGNORECASE )]
    joseph_momodu = [re.compile(r'joseph', re.IGNORECASE ), re.compile(r'momodu', re.IGNORECASE ), re.compile(r'josephmomodu', re.IGNORECASE )]
    denola_grey = [re.compile(r'denola', re.IGNORECASE ), re.compile(r'grey', re.IGNORECASE ), re.compile(r'denolagrey', re.IGNORECASE )]
    ikechukwu_onunaku = [re.compile(r'ikechukwu', re.IGNORECASE ), re.compile(r'onunaku', re.IGNORECASE ), re.compile(r'ikechukwuonunaku', re.IGNORECASE )]
    bimbo_manuel= [ re.compile(r'manuel', re.IGNORECASE ), re.compile(r'bimbomanuel', re.IGNORECASE )]
    funky_mallam = [re.compile(r'funky', re.IGNORECASE ), re.compile(r'mallam', re.IGNORECASE ), re.compile(r'funkymallam', re.IGNORECASE )]
    asabe_madaki = [re.compile(r'asabe', re.IGNORECASE ), re.compile(r'madaki', re.IGNORECASE ), re.compile(r'asabemadaki', re.IGNORECASE )]
    patrick_doyle= [re.compile(r'patrick', re.IGNORECASE ), re.compile(r'doyle', re.IGNORECASE ), re.compile(r'patrickdoyle', re.IGNORECASE )]
    nobert_young = [re.compile(r'nobert', re.IGNORECASE ), re.compile(r'young', re.IGNORECASE ), re.compile(r'nobertyoung', re.IGNORECASE )]
    boki_ofodile = [re.compile(r'boki', re.IGNORECASE ), re.compile(r'ofodile', re.IGNORECASE ), re.compile(r'bokiofodile', re.IGNORECASE )]
    taiwo_ajayilycett = [re.compile(r'taiwo', re.IGNORECASE ), re.compile(r'ajayi', re.IGNORECASE ), re.compile(r'lycett', re.IGNORECASE ), re.compile(r'ajayilycett', re.IGNORECASE )]

    cast_appearance = {
        'richard': 0,
         'ade':0,
         'alex':0,
         'olumide':0,
         'shaffy':0,
         'ireti':0,
         'sam': 0,
         'kelechi':0,
         'akintola':0,
         'femi':0,
         'joseph':0,
         'denola':0,
         'ikechukwu':0,
         'manuel':0,
         'funky':0,
         'asabe':0,
         'taiwo':0,
         'patrick':0,
         'nobert':0,
         'boki':0,
    }
    cast_names = []

    for tweet in tweets:
        print ('matching tweet ' + tweet)
        if any(pattern.search(tweet) for pattern in richard_mofedamijo):
            cast_appearance['richard'] = cast_appearance['richard'] + 1
            cast_names.append('Richard Mofedamijo RMD')
        if any(pattern.search(tweet) for pattern in ade_laoye):
            cast_appearance['ade'] = cast_appearance['ade'] + 1
            cast_names.append('Ade Laoye')
        if any(pattern.search(tweet) for pattern in olumide_oworu):
            cast_appearance['olumide'] = cast_appearance['olumide'] + 1
            cast_names.append('Olumide Oworu')
        if any(pattern.search(tweet) for pattern in shaffy_bello):
            cast_appearance['shaffy'] = cast_appearance['shaffy'] + 1
            cast_names.append('Shaffy Bello')
        if any(pattern.search(tweet) for pattern in ireti_doyle):
            cast_appearance['ireti'] = cast_appearance['ireti'] + 1
            cast_names.append('Ireti Doyle')
        if any(pattern.search(tweet) for pattern in sam_dede):
            cast_appearance['sam'] = cast_appearance['sam'] + 1
            cast_names.append('Sam Dede')
        if any(pattern.search(tweet) for pattern in kelechi_udegbe):
            cast_appearance['kelechi'] = cast_appearance['kelechi'] + 1
            cast_names.append('Kelechi Udegbe')
        if any(pattern.search(tweet) for pattern in bimbo_akintola):
            cast_appearance['akintola'] = cast_appearance['akintola'] + 1
            cast_names.append('Bimbo Akintola')
        if any(pattern.search(tweet) for pattern in femi_branch):
            cast_appearance['femi'] = cast_appearance['femi'] + 1
            cast_names.append('Femi Branch')
        if any(pattern.search(tweet) for pattern in joseph_momodu):
            cast_appearance['joseph'] = cast_appearance['joseph'] + 1
            cast_names.append('Joseph Momodu')
        if any(pattern.search(tweet) for pattern in denola_grey):
            cast_appearance['denola'] = cast_appearance['denola'] + 1
            cast_names.append('Denola Grey')
        if any(pattern.search(tweet) for pattern in ikechukwu_onunaku):
            cast_appearance['ikechukwu'] = cast_appearance['ikechukwu'] + 1
            cast_names.append('Ikechukwu Onunaku')
        if any(pattern.search(tweet) for pattern in bimbo_manuel):
            cast_appearance['manuel'] = cast_appearance['manuel'] + 1
            cast_names.append('Bimbo Manuel')
        if any(pattern.search(tweet) for pattern in funky_mallam):
            cast_appearance['funky'] = cast_appearance['funky'] + 1
            cast_names.append('Funky Mallam')
        if any(pattern.search(tweet) for pattern in asabe_madaki):
            cast_appearance['asabe'] = cast_appearance['asabe'] + 1
            cast_names.append('Asabe Madaki')
        if any(pattern.search(tweet) for pattern in patrick_doyle):
            cast_appearance['patrick'] = cast_appearance['patrick'] + 1
            cast_names.append('Patrick Doyle')
        if any(pattern.search(tweet) for pattern in nobert_young):
            cast_appearance['nobert'] = cast_appearance['nobert'] + 1
            cast_names.append('Nobert Young')
        if any(pattern.search(tweet) for pattern in boki_ofodile):
            cast_appearance['boki'] = cast_appearance['boki'] + 1
            cast_names.append('Boki Ofodile')
        if any(pattern.search(tweet) for pattern in taiwo_ajayilycett):
            cast_appearance['taiwo'] = cast_appearance['taiwo'] + 1
            cast_names.append('Taiwo Ajayilycett')
    return cast_names

print(match_cast_member)

load_to_json (match_cast_member(), 'cast_appearance')
load_to_json (match_cast_member(), 'cast_names')


            
            