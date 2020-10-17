# solver-society-job-analysis
Bagian dari program solver society oleh Iykra.

Melakukan analisis data lowongan pekerjaan dari Jobstreet dan Glints.

## Catatan penting :exclamation::exclamation:
1. Pastikan path/lokasi pada seluruh data sudah sesuai ketika akan load data.
2. Pada lexicon dan ngram path di notebook 2_3_3 dan 2_3_4, pastikan sesuai.
```
lexicon_path = "[path-to-file]/Lexicon.trn"
ngram_path = "[path-to-file]/Ngram.trn"
```
3. Pada file <code>tagger.py</code>, pastikan path inlex dan cattable sudah sesuai.
```
inlex_url = "[path-to-file]/inlex.txt"
cattable_url = "[path-to-file]/cattable.txt"                
```

## Credit
Part-of-Speech tagging Bahasa Indonesia.
[INACL journal](http://inacl.id/journal/index.php/jlk/article/view/20)
> A. F. Wicaksono and P. Ayu, “HMM Based Part-of-Speech Tagger for Bahasa Indonesia,” in Prooceedings of 4th International MALINDO (Malay and Indonesian Language) Workshop, 2010, no. August, pp. 1–7.
