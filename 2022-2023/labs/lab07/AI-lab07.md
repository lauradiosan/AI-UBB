# Lab07 - Rezolvarea unor probleme de regresie prin metode de învățare automată  <img src="images/regression.png" width="200">



## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. Probleme de tip regresie rezolvate cu metoda gradientului descrescator. Evaluareaa performanței acestor metode.

## :book:  Aspecte teoretice

Metoda gradientului descrescător pentru rezolvarea problemelor de regresie.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță. 



## :bulb: Probleme

**Ce îi poate face pe oameni fericiți?** 
Se consideră problema predicției gradului de fericire a populației globului folosind informații despre diferite caracteristici a bunăstării respectivei populații precum Produsul intern brut al țării în care locuiesc (gross domestic product – GBP), gradul de fericire, etc. 

Folsind datele aferente anului 2017 [link](https://www.kaggle.com/unsdsn/world-happiness#2017.csv), să se realizeze o predicție a gradului de fericire în funcție:
-	doar de Produsul intern brut
-	de Produsul intern brut si de gradul de libertate. 




## :memo:  Cerinte 

Specificaţi, proiectaţi, implementaţi si testati cate un algoritm de predicție bazat pe:
- metoda gradientului descrescator stocastic (demo) - please check the [notebook](SGD/AI-lab08-linRegressionSGD.ipynb)
- metoda gradientului descrescator bazat pe batch-uri, cu tool/API si/sau cod propriu (tema).

Se vor normaliza datele de antrenament si validare - please check the [notebook](dataNormalisation/AI-lab07-dataNormalisation.ipynb). 
 


🏵️ Cerinte opționale

Rezolvarea unei probleme de regresie prin:
- implementare regresie multi-target (cu mai multe output-uri) – sugestii:
    -	outputurile sa fie independente (de ex pe setul de date din sklearn.datasets pot folosi datele psyho din linnerud)
    - outputurile sa fie dependente (aici s-ar putea folosi un regressor gata antrenat – gen yolo (https://pjreddie.com/darknet/yolo/) – pentru a prezice coordonatele bounding box-urilor care încadrează obiectele recunoscute în imagini; trebuie studiat cum se evaluează dacă acele BBs sunt bune sau nu; focusul este de fapt pe interpretarea outputului dat de regressor, nu pe modul în care se antrenează regressorul)


## :hourglass: Termen de predare 

Laborator 8

## :moneybag: Evaluarea

Punctajele acordate:

- Rezolvarea problemei cu tool – 50 puncte

- Rezolvarea problemei cu cod propriu, cazul regresiei univariate – 100 puncte

- Rezolvarea problemei cu cod propriu, cazul regresiei multi-variate – 50 puncte

- Normalizarea datelor – cod propriu 100 puncte

- Rezolvarea cerințelor opționale – maxim 200 puncte

Notă: 

- punctajul maxim acumulat pentru acest laborator este 500 puncte.

- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  






