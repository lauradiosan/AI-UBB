# Lab10 - Rezolvarea unor probleme de clustering prin metode de învățare automată 


## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. Probleme de tip clustering din domeniul text-mining
rezolvate cu ajutorul algoritmilor de tip k-means. Evaluareaa performanței acestor metode.


## :book:  Aspecte teoretice

Algoritmul k-means. Tehnici de pre-procesare a textelor.

Proiectarea sistemelor care învaţă singure.

Evaluarea sistemelor care învaţă singure. Metrici de performanță.

 



## :bulb: Probleme

1. **Ce fel de mesaje primesti in Inbox?**
Se doreste clusterizarea unor mesaje in doua categorii (spam si ham). Pentru fiecare mesaj se cunoaste textul aferent lui. Să se rezolve problema, implementându-se rutine pentru clusterizare cu k-means a mesajelor.

2. **Retea sociala: ce fel de mesaje ai postat?**
Mai tii minte ca tocmai ti-ai inceput munca ca si software developer la Facebook si ca faci parte din echipa care se ocupa cu partea de continut a platformei? 
Utilizatorii sunt foarte incantati de noul algoritm de detectie a filtrelor in poze, asadar poti sa te ocupi de o noua functionalitate care ar face platforma mai atractiva. Utilizatorii posteaza o gama larga de mesaje, iar in feed-urile lor apar de multe ori prea multe mesaje negative si prea putine pozitive. Facebook incearca o noua functionalitate prin care sa detecteze sentimentele dintr-un mesaj si sa filtreze feed-urile utilizatorilor. 
Task-ul tau este sa implementezi un algoritm care poate recunoaste sentimentele dintr-un text (pozitiv, negativ, ura, rasism, etc.). 
Team leaderul echipei de ML iti propune urmatorul plan de lucru 
- devoltarea, antrenarea si testarea unui algoritm de tip k-means folosind data de tip numeric (de ex datele cu irisi) 
- devoltarea, antrenarea si testarea unui algoritm de tip k-means folosind data de tip text
    - Considerarea unei baze cu texte etichetate cu emotii (de ex. textele din data/review_mixed.csv sau https://github.com/sarnthil/unify-emotion-datasets/tree/master/datasets)
    - Extragerea de caracteristici din texte folosind diferite reprezentari precum:
        - Bag of Words
        - TF-IDF
        - Word2Vec
        - N-grams, etc.
    - pe baza caracteristicilor extrase, clasificarea textelor si etichetarea lor cu emotii folosind
        - un algoritm de invatare supervizat (folosind etichetele pt emotiile asociate fiecarui text)
        - un algoritm de invatare nesupervizat bazat pe k-means (fara a folosi etichetele pt emotiile asociate fiecarui text)
        - un algoritm hibrid care combina tehncile de invare cu reguli ajutatoare, de ex prin folosirea unor reguli care verifica/numara aparitiile unor cuvinte - polarized words - (e.g. negative words such as bad, worst, ugly, etc and positive words such as good, best, beautiful, etc.)


## :memo:  Cerinte 

Specificaţi, proiectaţi, implementaţi si testati cate un algoritm de clasificare nesupervizata bazat pe k-means.


🏵️ Cerinte opționale

Feel free to add!


## :hourglass: Termen de predare 
Laborator 11

## :moneybag: Evaluarea

Punctajele acordate
- Implementare kMeans pt clusterizare – 100 puncte
- Extragere caracteristici din texte –
    - Bag of Words / TF-IDF / Wrd2Vec - 50 puncte
    - Alte caracteristici – 100 puncte
- Etichetare emotii
    - supervizat – 50 puncte
    - nesupervizat  – 100 puncte
    - hibrid – 100 puncte


Notă: 
- punctajul maxim acumulat pentru acest laborator este 500 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  




