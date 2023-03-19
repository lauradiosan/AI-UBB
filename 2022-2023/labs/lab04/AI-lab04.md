# Lab04 - Algoritmi evolutivi  <img src="evolComp.gif" width="100">



## :microscope: Obiective 

Formularea problemelor ca probleme de căutare şi identificarea modalităţilor de rezolvare a lor bazate pe algoritmi evolutivi. Specificarea, proiectarea şi implementarea metodelor de căutare bazate pe algoritmi evolutivi.

## :book:  Aspecte teoretice

- Rezolvarea problemelor ca proces de optimizare
- Tipuri de probleme de optimizare.
- Modalităţi de rezolvare a problemelor de căutare -> Identificarea soluţiei potenţiale optime:
    - Stabilirea componentelor problemei 
        - Condiţii (constrângeri) pe care trebuie să le satisfacă (parţial sau total) soluţia  
        - Funcţie de evaluare a unei soluţii potenţiale -> identificareaa optimului
    - Definirea spaţiul de căutare 
    - Stabilirea strategiei de identificare a soluţiei optime în spaţiul de căutare 

## :bulb: Problema celui mai scurt drum

In contextul problemei de la laboratoarele 2 si 3, se doreste propagarea unui mesaj in retea intre doua noduri pe drumul cel mai bun posibil (e.g. drumul cel mai scurt, drumul cel mai ieftin, drumul cel mai putin periculos, etc.).



## :memo:  Cerinte 

Să se identifice cel mai scurt drum care pleacă dintr-un nod, vizitează toate nodurile (fiecare nod este vizitat o singură dată) și revine în locația de start folosind un algoritm evolutiv. Se vor folosi:
- informatii din lucrarea Gonen, B., & Louis, S. J. (2006). Genetic Algorithm finding the shortest path in Networks. Reno: University of Nevada [link](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.712.8445&rep=rep1&type=pdf)
- reteaua sociala dezvoltata semestrul trecut la MAP (cu construirea in prealabil a grafului corespunzator ei)
- exemplele din arhiva TSP.zip

Aplicaţia (specificata, proiectata si implementata) trebuie să permită:
-	Încărcarea datelor problemei 
-	Alegerea şi parametrizarea metodei de rezolvare a problemei
-	Afişarea soluţiei identificate
-	Precizarea performanţelor metodei de rezolvare alese

Aplicația trebuie să respecte specificațiile privind datele de intrare și datele de ieșire.

Aplicația va fi testată folosind date de difcultăți diferite (fiecare test validat având asociat un anumit punctaj).

Datele de intrare sunt reprezentate de:
-	graful retelei
-	parametrii algoritmului

Datele de iesire sunt reprezentate de:
-	ordinea in care trebuie vizitate nodurile pentru a obtine cel mai bun drum

## 🏵️Cerinte optionale

1. In cazul existentei mai multor solutii, precizati toate solutiile. Analizati diversitatea populatiei de potentiale solutii.

2. Cum impacteaza metoda de rezolvare si solutia/solutiile identificate modificarea cerintei astfel: *Să se identifice cel mai scurt drum care pleacă dintr-un nod și revine în locația de start folosind un algoritm evolutiv.*


## :hourglass: Termen de predare 
Laborator 5

## :moneybag: Evaluarea

Punctajele acordate (in funcție de seturile de date folosite) sunt:
- date de dificultate redusa - 50 puncte
- date de dificultate medie - 100 puncte
- date de dificultate mare - 150 puncte
- cerinte optionale - 2 * 100 puncte


Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  




