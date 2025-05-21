# Lab10 - Algoritmi evolutivi  <img src="evolComp.gif" width="100">



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

2. Problema identificării comunităților într-o rețea complexă. A se consulta descrierea din AI-lab10-GAs.ipynb - Tema
- cateva info utile despre comunitati [link](https://youtu.be/sI8TK2mETrk?feature=shared), [link](https://youtu.be/RfgjHoVCZwU?feature=shared), [link](https://www.youtube.com/watch?v=KXi4ha79o3s)

## :memo:  Cerinte 

Se cere identificarea comunităților existente într-o rețea folosind:
- un algoritm predefinit intr-o biblioteca specializata (e.g. networkx, gephi, altele);
- un algoritm evolutiv. 

Se vor folosi 
-	informații privind reprezentarea cromozomilor și operatorii genetici din lucrarea: Pizzuti, Clara. "Evolutionary computation for community detection in networks: a review." IEEE Transactions on Evolutionary Computation 22.3 (2017): 464-483. [link](https://github.com/lauradiosan/AI-UBB/blob/main\2023-2024\labs\lab10\communityDetection\communityDetection.pdf) 
<!-- (http://staff.icar.cnr.it/pizzuti/pubblicazioni/IEEETEC2017.pdf) -->
-	cele 4 rețele / seturi de date din folderul asociat laboratorului current (in format GML – more details [here](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/rutter/abschlussarbeiten/ba-goetz.pdf))
-	rețele / seturi de date identificate de student (maxim 6 retele)


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
Laborator 13 

## :moneybag: Evaluarea

Punctajele acordate (in funcție de seturile de date folosite) sunt:
- 20 puncte / retea in cazul folosirii functiilor prdefinite din biblioteci
- 50 puncte / retea  in cazul folosirii algoritmului genetic dezvoltat de catre student
Astfel se pot obtine pentru:
- Seturi de date indicate in documentatie (sunt 4 retele in arhiva real-networks.zip) - maxim 280 puncte   
- Seturi de date identificate de student / profesor (maxim 6 retele diferite de cele din arhiva real-networks.zip)

Bonus:
- functii de fitnes pt algoritmul genetic diferite de cea bazata pe modularitate (maxim 2 functii) - 50 puncte / functie


Notă: 
- punctajul maxim acumulat pentru acest laborator este 800 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 200 puncte.  



