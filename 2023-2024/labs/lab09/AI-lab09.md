# Lab09 - Rezolvarea unor probleme de clustering prin metode de învățare automată 


## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. Probleme de tip clustering din domeniul text-mining rezolvate cu ajutorul algoritmilor de tip k-means. Evaluareaa performanței acestor metode.


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
- folosirea unui model de ML gata antrenat precum cel din Azure
- antrenarea si testarea unui algoritm de tip k-means folosind data de tip text
    - Considerarea unei baze cu texte etichetate cu emotii (de ex. textele din data/review_mixed.csv sau https://github.com/sarnthil/unify-emotion-datasets/tree/master/datasets)
    - Extragerea de caracteristici din texte folosind diferite reprezentari precum: Bag of Words, TF-IDF, Word2Vec, altele.
    - pe baza caracteristicilor extrase, antrenarea nesupervizata a unui clasificator de texte cu scopul etichetarii lor cu emotii folosind un algoritm de invatare nesupervizata bazat pe k-means (fara a folosi etichetele pt emotiile asociate fiecarui text)


## :memo:  Cerinte 

Stabiliti care este sentimentul transmis prin mesajul **By choosing a bike over a car, I’m reducing my environmental footprint. Cycling promotes eco-friendly transportation, and I’m proud to be part of that movement.**. 

Folositi: 
- clasificatorul bazat pe k-means antrenat de voi (folosind o biblioteca care implementeaza algoritmul k-means)
- clientul AZURE (se poate consulta exemplu din notebook).

Care este mai performant?


🏵️ Cerinte opționale

1. Implementati algoritmul de clusterizare k-Means
2. Ce alternative exista la algoritmul k-means? Au ele o performanta mai buna pentru problema data?


## :hourglass: Termen de predare 
Laborator 10

## :moneybag: Evaluarea

Punctajele acordate
- Extragere caracteristici din texte 
    - Bag of Words / TF-IDF / Word2Vec - 50 puncte
    - Alte caracteristici – 100 puncte
- Etichetarea textelor cu emotii folosind kMeans (tool) - 100 puncte
- Implementare (cod propriu) kMeans pt clusterizare – 100 puncte
- alternative la k-means si analiza performanta - 100 puncte


Notă: 
- punctajul maxim acumulat pentru acest laborator este 450 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 120 puncte.  




