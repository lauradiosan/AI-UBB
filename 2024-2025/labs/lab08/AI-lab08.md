# Lab08 - text mining



## :microscope: Obiective 

Înțelegerea problemei de clasificare a textelor (date de intrare, date de ieșire, preprocesări, aspect probabilistic) cu aplicatii diverse, precum:
- analiza sentimentelor exprimate de recenzii, comentarii sau ale mesaje din media online
- identificarea comentarilor toxice in social media sau recenzilor/stirilor false
- determinarea daca un user va da click pe un mesaj publicitar, etc.

## :book:  Aspecte teoretice

Chiar daca procesul prelucrarii datelor este similar celui din cazul imaginilor, in cazul textelor se adauga o serie de pasi de pre-procesare, adesea vitali, si de reprezentare a textelor.

Metode de pre-procesare:
- stemming & lemmatisation - aducerea cuvintelor la forma canonica 
- curatarea textului de caractere speciale si semne de punctuatie
- eliminarea cifrelor/numerelor din cadrul textului 
- corectarea greselilor de scriere (ex. "teh" -> "the")
- expansiunea contractiilor (ex. "it's" -> "it is", "can't" -> "can not")

Metode de reprezentare:
- Bag of Words (BoW) - fiecare cuvant este reprezentat printr-un vector binar de dimensiune egala cu numarul de cuvinte din vocabularul corpus-ului
- Term Frequency-Inverse Document Frequency (TF-IDF) - fiecare cuvant este reprezentat printr-un vector de dimensiune egala cu numarul de cuvinte din vocabularul corpus-ului, dar fiecare cuvant este ponderat in functie de frecventa sa in corpus
- Word2Vec features (embeddings) - fiecare cuvant este reprezentat printr-un vector (cu valori reale) de dimensiune fixa (ex. 100, 200, 300) care contine informatii despre semantica sa


## :bulb: Probleme

**Retea sociala: ce fel de mesaje ai postat?**
Mai tii minte ca tocmai ti-ai inceput munca ca si software developer la Facebook si ca faci parte din echipa care se ocupa cu partea de continut a platformei? 
Utilizatorii sunt foarte incantati de noul algoritm de detectie a filtrelor in poze, asadar poti sa te ocupi de o noua functionalitate care ar face platforma mai atractiva. Utilizatorii posteaza o gama larga de mesaje, iar in feed-urile lor apar de multe ori prea multe mesaje negative si prea putine pozitive. Facebook incearca o noua functionalitate prin care sa detecteze sentimentele dintr-un mesaj si sa filtreze feed-urile utilizatorilor. 
Task-ul tau este sa implementezi un algoritm care poate recunoaste sentimentele dintr-un text (pozitiv, negativ, ura, rasism, etc.). 
Team leaderul echipei de ML iti propune urmatorul plan de lucru 
- folosirea unui model de ML gata antrenat precum cel din Azure
- antrenarea si testarea unui algoritm bazat pe retele neuronale artificiale folosind data de tip text
    - Considerarea unei baze cu texte etichetate cu emotii (de ex. textele din data/review_mixed.csv sau https://github.com/sarnthil/unify-emotion-datasets/tree/master/datasets)
    - preprocesarea textului
    - Extragerea de caracteristici din texte folosind diferite reprezentari precum: Bag of Words, TF-IDF, Word2Vec, altele.
    - pe baza caracteristicilor extrase, antrenarea a unui clasificator de texte cu scopul etichetarii lor cu emotii folosind un algoritm de invatare bazat pe retele neuronale artificiale

## :memo:  Cerinte 

Stabiliti care este sentimentul transmis prin mesajul **By choosing a bike over a car, I’m reducing my environmental footprint. Cycling promotes eco-friendly transportation, and I’m proud to be part of that movement.**. 

Folositi: 
- clasificatorul din clientul AZURE (se poate consulta exemplul din notebook).
- clasificatorul bazat pe retele neuronale artificiale antrenat de voi (folosind o biblioteca care implementeaza ANNs)

Care clasificator este mai performant?


🏵️ Cerinte opționale

Rezolvati cerinta de mai sus folosind un clasificator bazat pe retele neuronale artificiale antrenat de voi (folosind o cod propriu pentru dezvoltarea ANN-ului).


## :hourglass: Termen de predare 
Laborator 9

## :moneybag: Evaluarea

Punctajele acordate
- stabilirea sentimentului mesajului folosinf Azure - 50 puncte
- Extragere caracteristici din texte 
    - Bag of Words / TF-IDF / Word2Vec - 50 puncte
    - Alte caracteristici – 100 puncte
- Antrenarea unui clasificator bazat pe ANN (ANN cu tool) si stabilirea sentimentului mesajului - 100 puncte
- Antrenarea unui clasificator bazat pe ANN (cod propriu) si stabilirea sentimentului mesajului - 300 puncte



Notă: 
- punctajul maxim acumulat pentru acest laborator este 600 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 150 puncte.  





