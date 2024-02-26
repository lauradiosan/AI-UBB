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

Normalizarea datelor - please check the [notebook](dataNormalisation/AI-lab02-dataNormalisation.ipynb). 

## :bulb: Probleme 

1.	Se cunosc date despre angajatii unei companii, date salvate in fisierul "data/employees.csv". 
    
    1.a. Sa se stabileasca:
    - numarul de angajati 
    - numar si tipul informatiilor (proprietatilor) detinute pentru un angajat
    - numarul de angajati pentru care se detin date complete
    - valorile minime, maxime, medii pentru fiecare proprietate
    - in cazul proprietatilor nenumerice, cate valori posibile are fiecare astfel de proprietate
    - daca sunt valori lipsa si cum se poate rezolva aceasta problema

    1.b. Sa se vizualizeze:
    - distributia salariilor acestor angajati pe categorii de salar 
    - distributia salariilor acestor angajati pe categorii de salar si echipa din care fac parte
    - angajatii care pot fi considerati "outlieri"

2. Se dau mai multe imagini (salvate in folder-ul "data/images"). Se cere:
    - sa se vizualizeze una din imagini
    - daca imaginile nu aceeasi dimensiune, sa se redimensioneze toate la 128 x 128 pixeli si sa se vizualizeze imaginile intr-un cadru tabelar.
    - sa se transforme imaginile in format gray-levels si sa se vizualizeze
    - sa se blureze o imagine si sa se afiseze in format "before-after"
    - sa se identifice muchiile ontr-o imagine si sa se afiseze in format "before-after"

3. Se da un fisier care contine un text (format din mai multe propozitii) in limba romana - a se vedea fisierul ”data/texts.txt”. Se cere sa se determine si sa se vizualizeze:
    - numarul de propozitii din text;
    - numarul de cuvinte din text
    - numarul de cuvinte diferite din text
    - cel mai scurt si cel mai lung cuvant (cuvinte)
    - textul fara diacritice
    - sinonimele celui mai lung cuvant din text

4. Sa se normalizeze informatiile de la problema 1 si 2 folosind diferite metode de normalizare astfel:
    - problema 1 - salariul, bonusul, echipa
    - problema 2 - valorile pixelilor din imagini
    - problema 3 - numarul de aparitii a cuvintelor la nivelul unei propozitii.






## :memo:  Cerinte 

Specificaţi, implementaţi și testați subalgoritmi pentru problemele enuntate. 

## :hourglass: Termen de predare 

Laborator 3

## :moneybag: Evaluarea
- Problema 1 - 50 puncte

- Problema 2 - 50 puncte

- Problema 3 - 50 puncte

- Problema 4 - 150 puncte

Notă: 
- punctajul maxim acumulat pentru acest laborator este 300 puncte.
- punctajul minim pentru ca tema predată sa fie validă este 100 puncte.  

