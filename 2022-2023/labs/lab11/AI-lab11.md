# Lab11 - Recunoastere emotii in imagini



## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. 

## :book:  Aspecte teoretice

Tehnici de pre-procesare a imaginilor.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță. 




## :bulb: Probleme

Job-ul de la Facebook se consolideaza. Utilizatorii sunt foarte incantati de noul algoritm de detectie a filtrelor in poze si a emotilor in texte, asadar poti sa te ocupi de o noua functionalitate care ar face platforma si mai atractiva.

Echipa de analisti ar dori sa evalueze starea emotionala a utilizatorilor si pe baza imaginilor (daca ei au poze de profil sau posteaza imagini vesele sau triste). De aceea, noul tau task este sa implementezi un algoritm de clasificare a pozelor care care sa indice daca o poza este vesela sau trista. 

Team leaderul echipei de ML iti propune un plan de lucru in 3 iteratii:
- Iteratia 1: clasificarea emotiilor in imagini continand emoticoane (de exemplu Happy faces   versus Sad faces ). Pentru aceasta va trebui:
    - creata o baza cu imagini cu emoticoane si etichetele corespunzatoare (please check this one[link](https://github.com/iamcal/emoji-data))
    - antrenarea unui clasificator de emotii in imagini cu emoticoane
    - testarea clasificatorului
- Iteratia 2: clasificarea emotiilor in imagini cu fete reale folosind un clasificator pre-antrenat. Pentru aceasta va trebui:
    - Preluarea unei baze cu imagini faciale (de ex [FER](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/overview))
    - Preluarea unui clasificator (model) de emotii in imagini pre-antrenat (de ex [EmoPy](https://github.com/thoughtworksarts/EmoPy))
    - Testarea clasificatorului 
- Iteratia 3: clasificarea emotiilor in imagini cu fete reale folosind un clasificator antrenat de la 0. Pentru aceasta se vor efectua urmatorii pasi:
    - Preluarea unei baze cu imagini faciale (de ex [FER](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/overview))
    - Antrenarea unui clasificator (model) de emotii in imagini folosind caracteristici ale imaginilor extrase
        - manual - descriptori precum [Haar](https://www.merl.com/publications/docs/TR2004-043.pdf), [HOG](https://hal.inria.fr/file/index/docid/548512/filename/hog_cvpr2005.pdf), etc. Se pot folosi descriptorii implementati in biblioteci specifice de Computer Vision precum [OpenCV](https://opencv.org/), [SciKit-Image](https://scikit-image.org/).
        - automat - modele de extragere preantrenate (precum Facenet) sau antrenate de la 0.
    - Testarea clasificatorului 

Clasificarea imaginilor poate fi:
- Multi-class – fiecare imagine apartine unei anumite emotii
- Multi-label – o imagine poate avea associate mai multe emotii  (de ex baza cu imagini [EmoReact](https://www.behnaznojavan.com/emoreact) descrie imaginile prin mai multe etichete emotionale)


## :memo:  Cerinte 

Specificaţi, proiectaţi, implementaţi si testati algoritmi de Machine Learning pentru problema de mai sus.

🏵️ Cerinte opționale

Feel free to add!


## :hourglass: Termen de predare 
Laborator 12

## :moneybag: Evaluarea

Punctajele acordate 

- Clasificare emoticoane – 100 puncte
- Clasificare imagini faciale folosind model pre-antrenat – 200 puncte
- Clasificare imagini faciale folosind model antrenat (from scratch) si 
    - Caracteristici „extrase manual”  – 200 puncte
    - Caracteristici „extrase automat” – 300 puncte
- Clasificarea multi-label a imaginilor – 200 puncte (bonus)
 


Notă: 
- punctajul maxim acumulat pentru acest laborator este 1000 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  







