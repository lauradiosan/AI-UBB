# Lab05 - Invatare automata - metode de evaluare  :+1: or :-1:



## :microscope: Obiective 

Introducere în dezvoltarea sistemelor care învaţă singure. Tipuri de probleme rezolvabile cu metode de învățare automată (regresie și clasificare). Măsuri de evaluare a performanței acestor metode.

## :book:  Aspecte teoretice

Clasificarea problemelor care necesită metode de învățare automată.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță:
- Eroare
- Acuratețe, Precizie, Rapel,
- Funcție de cost 


## :bulb: Probleme

**Problema de regresie**: predictia bunastarii sociale pe baza PIB-ului si a altor factori economici: Se consideră problema predicției gradului de fericire a populației globului folosind informații despre diferite caracteristici a bunăstării respectivei populații precum Produsul intern brut al țării în care locuiesc (gross domestic product – GBP), gradul de fericire, etc. 

**Problema de clasificare**: clasificarea emailurilor (spam si ham) sau a unor persoane (infectate sau sanatoase) sau a unor imagini cu fructe si alte obiecte (fruit vs. non-fruit) sau a unor imagini cu fructe (apple vs. pear vs grappes). 



## :memo:  Cerinte 

Specificaţi, proiectaţi şi implementaţi rutine de evaluare a performanței unui algoritm de ML:
- performanța predicției în cazul unei probleme de regresie
- performanța clasificării (acuratețe, precizie, rapel) în cazul unei probleme de clasificare


Demo:
- **demo1**: performanța predicției în cazul unei probleme de regresie (cu un singur output)
- **demo2**: performanța clasificării (acuratețe, precizie, rapel) în cazul unei clasificări binare (cu output-uri de tip etichetă) - cazul unui set de date echilibrat si cazul unui set de date ne-echilibrat
- **demo3**: performanța clasificării (acuratețe, precizie, rapel) în cazul unei clasificări binare (cu output-uri de tip probabilități - matrice cu $noSamples \times noClasses$ elemente)

Temă:
- sa se specifice procedura de evaluare a unui algoritm de ML care a rezolvat o problema de regresie multi-target si sa se determine eroarea de predictie: pe baza unor date de intrare (precum numarul de ridicari, sarituri, etc.) se doreste predicatia greutatii, taliei si pulsului persoanei care a realizat exrcitiile. Un algoritm de ML a prezis aceste valori. Se doreste calcularea calitatii acestor predictii. A se consulta datele din fisierul "sport.csv".

- sa se specifice procedura de evaluare a unui algoritm de ML care a rezolvat o problema de clasificare multi-clasa si sa se determine acuratetea, precizia, rapelul: pe baza unor masuratori ale petalelor si sepalelor, se doreste predictia tipului de floare intr-un din clasele Daisy, Tulip, Rose. Se doreste calcularea calitatii acestor predictii. A se consulta datele din fisierul "flowers.csv". 

🏵️ Cerinte opționale
- Determinarea loss-ului (funcție de cost) în cazul problemelor de regresie 
- Determinarea loss-ului (funcție de cost) în cazul problemelor de clasificare binară (outputul clasificatorului este reprezentat ca o matrice cu noSamples x 2 valori reale subunitare, fiecare linie având suma 1)
- Determinarea loss-ului (funcție de cost) în cazul problemelor de clasificare multi-clasă (outputul clasificatorului este reprezentat ca o matrice cu noSamples x noClasses valori reale)
- Determinarea loss-ului (funcție de cost) în cazul problemelor de clasificare multi-label (outputul clasificatorului este reprezentat ca o matrice cu noSamples x noClasses valori reale) 


## :hourglass: Termen de predare 
Laborator 6

## :moneybag: Evaluarea

Punctajele acordate:
•	Determinarea erorii de predictie - regresie multi-target – 150 puncte
•	Determinarea acurateții, preciziei, rapelului - clasificare multi-class – 150 puncte
•	Determinarea loss-ului - probleme de regresie și clasificare multi-class și multi-label – 200 puncte 



Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  









