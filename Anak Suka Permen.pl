anakIbu(andi).
anakIbu(budi).
anakIbu(cika).
anakIbu(dani).
anakIbu(emil).
not(anakIbu(fadil)).

sukaPermen(andi).
sukaPermen(budi).
sukaPermen(cika).
not(sukaPermen(dani)).
not(sukaPermen(emil)).


mendapatPermen(X) :- anakIbu(X), sukaPermen(X).
mendapatUang(X) :- anakIbu(X), not(sukaPermen(X)).

anak_ibu_siapa(X) :- anakIbu(X).
mendapat_permen_siapa(X) :- mendapatPermen(X).
mendapat_uang_siapa(X) :- mendapatUang(X).
cika_mendapat_uang :- mendapatUang(cika).
fadil :- not(mendapatPermen(fadil)), not(mendapatUang(fadil)).
