# Lab02 - Explorarea datelor <img src="EDA.png" width="100">


## :microscope: Obiective 

Explorarea și analiza datelor se află în centrul științei datelor. "Data scientists"-ii au nevoie de abilități în limbaje de programare pentru a explora, vizualiza și manipula datele. Folosirea unor instrumente/pachete pentru analiza datelor.

## :book:  Aspecte teoretice 

Elemente de baza de matematica si statistica. Biblioteci utile:
- [NumPy](https://numpy.org/) - biblioteca Python care ofera numeroase functii matematice
- [Pandas](https://pandas.pydata.org/) - biblioteca Python care ofera functii de prelucrare a datelor tabulare
- [NLTK](https://www.nltk.org/) - biblioteca Python care ofera functii de prelucrare a textelor
- [PIL](https://pypi.org/project/pillow/) - biblioteca Python care ofera functii de prelucrare a iamginilor
- [Matplotlib](https://matplotlib.org/) - biblioteca Python care ofera functii de vizualizare a datelor. 

A se parcurge si informatiile de [aici](https://learn.microsoft.com/en-us/training/modules/explore-analyze-data-with-python/)

Un scurt exemplu pentru setul de date "data/employee.csv" [aici](emplyeeExample.ipynb)

Normalizarea datelor - please check the [notebook](dataNormalisation/AI-lab02-dataNormalisation.ipynb). 

## :bulb: Probleme 

1.	S-a efectuat un studiu despre starea domeniului Data Science, iar datele colectate sunt salvate in fisierul "data/surveyDataScience.csv". 
    
    1.a. Sa se stabileasca:
    - numarul de respondenti (de la care s-au colectate informatiile)
    - numar si tipul informatiilor (atributelor, proprietatilor) detinute pentru un respondent
    - numarul de respondenti pentru care se detin date complete
    - durata medie a anilor de studii superioare pentru acesti respondenti (cea efectiva sau cea estimata), durata medie a anilor de studii pentru respondentii din Romania si durata medie a anilor de studii pentru respondentii din Romania care sunt femei. Comparati rezultatele obtinute pentru cele trei grupuri de respondenti. Se presupune ca studiile de licenta dureaza 3 ani, cele de master 2 ani si cele de doctorat 3 ani.
    - numarul de respondenti femei din Romania pentru care se detin date complete
    - numarul de femei din Romania care programeaza in Python, precum si intervalul de varsta cu cele mai multe femei care programeaza in Python? Dar in C++? Comparati rezultatele obtinute pentru cele doua limbaje de programare.    
    - domeniul de valori posibile si valorile extreme pentru fiecare atribut/proprietate (feature). In cazul proprietatilor nenumerice, cate valori posibile are fiecare astfel de proprietate
    - transformati informatiile despre vechimea in programare in numar de ani (folositi in locul intervalului, mijlocul acestuia) si apoi calculati momentele de ordin 1 si 2 pentru aceasta variabila (minim, maxim, media, deviatia standard, mediana). Ce se poate spune despre aceasta variabila?

    1.b. Sa se vizualizeze:
    - distributia respondentilor care programeaza in Python pe categorii de varsta
    - distributia respondentilor din Romania care programeaza in Python pe categorii de varsta 
    - distributia respondentilor femei din Romania care programeaza in Python pe categorii de varsta 
    - respondentii care pot fi considerati "outlieri" din punct de vedere al vechimii in programare (puteti folositi un boxplot pentru a identifica aceste valori)

2. Se dau mai multe imagini (salvate in folder-ul "data/images"). Se cere:
    - sa se vizualizeze una din imagini
    - daca imaginile nu aceeasi dimensiune, sa se redimensioneze toate la 128 x 128 pixeli si sa se vizualizeze imaginile intr-un cadru tabelar.
    - sa se transforme imaginile in format gray-levels si sa se vizualizeze
    - sa se blureze o imagine si sa se afiseze in format "before-after"
    - sa se identifice muchiile intr-o imagine si sa se afiseze in format "before-after"

3. Se da un fisier care contine un text (format din mai multe propozitii) in limba romana - a se vedea fisierul ”data/texts.txt”. Se cere sa se determine si sa se vizualizeze:
    - numarul de propozitii din text;
    - numarul de cuvinte din text
    - numarul de cuvinte diferite din text
    - cel mai scurt si cel mai lung cuvant (cuvinte)
    - textul fara diacritice
    - sinonimele celui mai lung cuvant din text

4. Sa se normalizeze informatiile de la problema 1 si 2 folosind diferite metode de normalizare astfel:
    - problema 1 - durata anilor de studii universitare, vechimea in programare
    - problema 2 - valorile pixelilor din imagini
    - problema 3 - numarul de aparitii a cuvintelor la nivelul unei propozitii.






## :memo:  Cerinte 

Specificaţi, implementaţi și testați subalgoritmi pentru problemele enuntate. 

## :hourglass: Termen de predare 

- Laborator 2 - problema 1 
- Laborator 3 - problema 2, 3, 4

## :moneybag: Evaluarea
- Problema 1 - 50 puncte
- Problema 2 - 50 puncte
- Problema 3 - 50 puncte
- Problema 4 - 150 puncte

Notă: 
- punctajul maxim acumulat pentru acest laborator este 300 puncte.
- punctajul minim pentru ca tema predată sa fie validă este 100 puncte.  

