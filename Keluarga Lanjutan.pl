
menikah(david, amy).
menikah(jack, karen).
menikah(john, susan).


orangTua(david, john).
orangTua(amy, john).
orangTua(jack, ray).
orangTua(karen, ray).
orangTua(john, liza).
orangTua(susan, liza).
orangTua(john, peter).
orangTua(susan, peter).
orangTua(john, mary).
orangTua(susan, mary).


lakiLaki(david).
lakiLaki(jack).
lakiLaki(john).
lakiLaki(ray).
lakiLaki(peter).

perempuan(amy).
perempuan(karen).
perempuan(susan).
perempuan(liza).
perempuan(mary).


ayah(X, Y) :- orangTua(X, Y), lakiLaki(X).
ibu(X, Y) :- orangTua(X, Y), perempuan(X).
saudara(X, Y) :- orangTua(Z, X), orangTua(Z, Y), X \= Y.
kakek(X, Y) :- ayah(X, Z), orangTua(Z, Y).
nenek(X, Y) :- ibu(X, Z), orangTua(Z, Y).
