# Lab04-optional - Algoritmi inspirati de furnici  <img src="ants.jpg" width="100">



## :microscope: Obiective 

Formularea problemelor ca probleme de căutare şi identificarea modalităţilor de rezolvare a lor bazate pe algoritmi inspirati de furnici. Specificarea, proiectarea şi implementarea metodelor de căutare bazate pe algoritmi inspirati de furnici.

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

A se consulta descrierea de la laboratorul 4.



## :memo:  Cerinte 

Să se identifice cel mai scurt drum care pleacă dintr-un nod, vizitează toate nodurile (fiecare nod este vizitat o singură dată) și revine în locația de start folosind un algoritm inspirat de furnici. 


Materiale utile:
- Articolele lui Marco Dorigo [link](https://scholar.google.com/citations?user=PwYT6EMAAAAJ&hl=en), precum
    - M. Dorigo, C. Blum, Ant colony optimization theory: A survey, Theoretical computer science 344 (2-3), 243-278 [link](http://www.mat.uab.cat/~alseda/MasterOpt/DorBlu2005tcs.pdf)
    - M Dorigo, M Birattari, T Stützle, Ant Colony Optimization - Artificial Ants as a Computational Intelligence Technique, IEEE Computational Intelligence Magazine 1 (4), 28-39  [link](https://courses.cs.ut.ee/all/MTAT.03.238/2011K/uploads/Main/04129846.pdf)
    - M. Dorigo, T. Ztutzle, Ant Colony Optimisation, MIT Press [link](http://www.mat.uab.cat/~alseda/MasterOpt/DorBlu2005tcs.pdf)
- Articolele lui C. Blum [link](https://scholar.google.com/citations?user=4e-ykx0AAAAJ&hl=en&oi=sra)
    - Blum, Christian. "Ant colony optimization: Introduction and recent trends." Physics of Life reviews 2, no. 4 (2005): 353-373. 
- Articole pentru grafe dinamice 
    - Chowdhury, Sudipta, Mohammad Marufuzzaman, Huseyin Tunc, Linkan Bian, and William Bullington. "A modified ant colony optimization algorithm to solve a dynamic traveling salesman problem: a case study with drones for wildlife surveillance." Journal of Computational Design and Engineering 6, no. 3 (2019): 368-386. [link](https://academic.oup.com/jcde/article/6/3/368/5732351)
    - Articolele amintite in lucrarea precedenta (in finalul sectiunii Introduction)

Seturi de date utile pot fi gasite [aici](http://www.math.uwaterloo.ca/tsp/data/index.html)
Pentru grafe dinamice se pot folosi:
-	grafurile statice asupra carora se aplica diferite perturbari random
-	grafuri dinamice precum cele de [aici](http://networkrepository.com/dynamic.php)


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


## :hourglass: Termen de predare 
Laborator 6

## :moneybag: Evaluarea

Punctajele acordate (în funcție de seturile de date folosite) sunt:
-	Seturi de date cu grafe statice 300 puncte
-	Seturi de date cu grafe dinamice 200 puncte 



Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  






