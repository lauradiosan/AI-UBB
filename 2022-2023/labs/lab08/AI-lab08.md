# Lab08 - Rezolvarea unor probleme de clasificare prin metode de învățare automată  <img src="images/binClassification.png" width="150">



## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. Probleme de tip clasificare rezolvate cu metoda regresiei logistice. Evaluareaa performanței acestor metode.

## :book:  Aspecte teoretice

Metoda gradientului descrescător pentru rezolvarea problemelor de clasificare.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță. 



## :bulb: Probleme

1. **Clasificarea țesuturilor cancerigene** 
Se consideră informații despre cancerul de sân la femei, informații extrase din ecografii mamare (detalii [aici](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))) precum:
    -	Tipul malformației identificate (țesut benign sau țesut malign)
    -	Caracteristici numerice ale nucleului celulelor din aceste țesuturi:
        - raza (media distanțelor între centru si punctele de pe contur)
        - textura (măsurată prin deviația standard a nivelelor de gri din imaginea asociată țesutului analizat)
Folosindu-se aceste date, să se decidă dacă țesutul dintr-o nouă ecografie (pentru care se cunosc cele 2 caracteristici numerice – raza și textura –) va fi etichetat ca fiind malign sau benign. 


2. **Ce fel de floare preferi?** 
Se consideră problema clasificării florilor de iris în diferite specii precum: setosa, versicolor și virginica. Pentru fiecare floare se cunosc caracteristici precum: lungimea și lățimea sepalei, lungimea și lățimea petalei. Mai multe detalii despre acest set se pot găsi [aici](https://archive.ics.uci.edu/ml/datasets/Iris). Folosindu-se aceste informații, să se decidă din ce specie aparține o anumită floare. 




## :memo:  Cerinte 

Specificaţi, proiectaţi, implementaţi si testati cate un algoritm de clasificare bazat pe metoda regresiei logistice. 


🏵️ Cerinte opționale

- folosirea batch-urilor în procesul de antrenament și validarea încrucișată 
- investigarea diferitelor funcții de loss 
- ce se întîmplă în cazul clasificarii binare daca se modifică pragul de decizie din 0.5 în alte valori. Cum se poate aprecia calitatea clasificatorului pentru diferite valori ale pragului?


## :hourglass: Termen de predare 
Laborator 9

## :moneybag: Evaluarea

Punctajele acordate:
- Rezolvarea problemei cu tool – 100 puncte
- Rezolvarea problemei cu cod propriu – 150 puncte + 50 puncte (daca acuratetea clasificarii > 90%)
- Rezolvarea cerințelor opționale – 200 puncte 



Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  





