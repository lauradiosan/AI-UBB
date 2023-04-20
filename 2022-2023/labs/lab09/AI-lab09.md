# Lab09 - Rezolvarea unor probleme de clasificare prin metode de învățare automată  <img src="images/ann.jpeg" width="150">



## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. Probleme de tip clasificare rezolvate cu ajutorul rețeleleor neuronale artificiale (Artificial Neural Networks - ANN). Evaluareaa performanței acestor metode.

## :book:  Aspecte teoretice

Rețele neuronale artificiale pentru rezolvarea problemelor de clasificare.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță. 
 



## :bulb: Probleme

1. **Ce fel de floare preferi?** 
Se consideră problema clasificării florilor de iris în diferite specii precum: setosa, versicolor și virginica. Pentru fiecare floare se cunosc caracteristici precum: lungimea și lățimea sepalei, lungimea și lățimea petalei. Mai multe detalii despre acest set se pot găsi [aici](https://archive.ics.uci.edu/ml/datasets/Iris). Folosindu-se aceste informații, să se decidă din ce specie aparține o anumită floare. 

2. **Ce cifră am scris?**
Se consideră un set de imagini care conțin cifre scrise de mână. Sa se decida ce cifra apare intr-o imagine.

3. **Retea sociala: ce fel de poze ai postat?**
Tocmai ti-ai inceput prima ta zi de munca ca si software developer la Facebook in echipa care se ocupa cu partea de continut a platformei. 
Echipa de analisti a observat ca foarte multe persoane folosesc filtre peste pozele lor, asadar in speranta de a promova continut mai putin editat, si poze cat mai reale, doresc sa implementeze o noua functionalite in care sa arate utilizatorilor daca o poza a fost sau nu editata. Pentru a testa aceasta idee, si pentru a vedea daca utlizatorilor li s-ar parea folositoare o astfel de functionalitate, au decis sa testeze ideea pe pozele care au filtre sepia. 
Primul task al tau este sa implementezi un algoritm de clasificare a pozelor care sa ne spuna daca o poza are sau nu adaugat filtru sepia. 
Team leaderul echipei de ML iti propune urmatorul plan de lucru 
- devoltarea, antrenarea si testarea unui clasificator bazat pe retele neuronale folosind date mai simple, de tip caracteristici numerice - de ex datele cu irisi) 
- devoltarea, antrenarea si testarea unui clasificator bazat pe retele neuronale folosind date mai complexe, de tip imagine - de ex baza de date cu cifre, pentru fiecare exmplu considerandu-se matricea de pixeli) 
- crearea unei baze cu imagini (cu si fara filtru sepia) si etichetele corespunzatoare 
- antrenarea si testarea clasificatorului (bazat pe retele neuronale artificiale – tool sau ANN-ul dezvoltat la pasul 2) pentru clasificarea imaginilor cu si fara filtru



## :memo:  Cerinte 

Specificaţi, proiectaţi, implementaţi si testati cate un algoritm de clasificare bazat pe retele neuronale artificiale (ANN). 


🏵️ Cerinte opționale

Specificaţi, proiectaţi, implementaţi si testati cate un algoritm de clasificare bazat pe retele neuronale artificiale convolutive (CNN). 


## :hourglass: Termen de predare 
Laborator 10

## :moneybag: Evaluarea

Punctajele acordate:
- Implementare ANN pt clasificare (cod propriu):
    - antrenare si testare pt datele cu irisi - 200 puncte
    - antrenare si testare pt imagini (de ex cifre) - 300 puncte
- Clasificare (antrenare si testare) imagini cu si fara filtru cu o ANN (cod propriu sau tool) – 250 puncte
- Clasificare (antrenare si testare) imagini cu si fara filtru cu o CNN (cod propriu sau tool) – 250 puncte


Notă: 
- punctajul maxim acumulat pentru acest laborator este 1000 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  







