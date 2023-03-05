# Lab03 - Algoritmi evolutivi  <img src="evolComp.gif" width="100">



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

## :bulb: Probleme

1. Identificarea punctului de optim a unei functii reale - Demo1


2. Problema identificării comunităților într-o rețea complexă. A se consulta descrierea de la laboratorul 2 - Tema


## :memo:  Cerinte 

Se cere identificarea comunităților existente într-o rețea folosind un algoritm evolutiv. Se vor folosi 
-	informații privind reprezentarea cromozomilor și operatorii genetici din lucrarea: Pizzuti, Clara. "Evolutionary computation for community detection in networks: a review." IEEE Transactions on Evolutionary Computation 22.3 (2017): 464-483. [link](http://staff.icar.cnr.it/pizzuti/pubblicazioni/IEEETEC2017.pdf)
- reteaua sociala dezvoltata semestrul trecut la MAP (cu construirea in prealabil a grafului corespunzator ei)
-	cele 4 rețele / seturi de date din folderul asociat laboratorului current (in format GML – more details [here](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/rutter/abschlussarbeiten/ba-goetz.pdf))
-	rețele / seturi de date identificate de student 

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
-	numarul de comunitati identificate in graf
-	apartenenta la o anumita comunitate pentru fiecare nod al grafului/retelei


## :hourglass: Termen de predare 
Laborator 4 

## :moneybag: Evaluarea

Punctajele acordate (in funcție de seturile de date folosite) sunt:
-	Seturi de date indicate in documentatie - maxim 200 puncte (50 puncte / retea – sunt 4 retele in arhiva real-networks.zip) 
-	Seturi de date identificate de student – maxim 200 puncte (50 puncte / retea)
- functii de fitnes diferite de modularitate - maxim 100 puncte (50 puncte / functie)


Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  



