# Lab04 - Object detection <img src="images\objectDetection.png" width="200">


## :microscope: Obiective 

Clasificarea imaginilor si localizarea cat mai precisa a obiectelor in imagini. 
Scopul acestui laborator este familiarizarea cu algoritmii de AI capabili sa clasifice imagini si sa detecteze diferite elemente (obiecte) in aceste imagini.

## :book:  Aspecte teoretice 

Clasificarea imaginilor si recunoasterea obiectelor in imagini
- specificarea problemei
- evaluarea performantei unui algoritm de AI in rezolvarea problemei 
    - numarul imaginilor corect clasificate
    - numarul obiectelor corect detectate
    - calitatea detectiei 

Biblioteci utile:
- Azure AI Vision [link](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)


A se consulta exemplul de [aici](https://github.com/lauradiosan/AI-UBB/blob/main/2023-2024/labs/lab04/AIlab04-detection.ipynb)


## :bulb: Probleme 

Se dau mai multe imagini (in folderul lab04\images) care pot contine biciclete. Se doreste sa se identifice care dintre imagini contin bicilete si unde se situeaza ele in aceste imagini. 



## :memo:  Cerinte 

Specificaţi, implementaţi și testați subalgoritmi pentru problema enuntata.

1. Sa se foloseasca un algoritm de clasificare a imaginilor (etapa de inferenta/testare) si sa se stabileasca performanta acestui algoritm de clasificare binara (imagini cu biciclete vs. imagini fara biciclete).

2. Pentru imaginile care contin biciclete:

    a. sa se localizeze automat bicicletele in aceste imagini si sa se evidentieze chenarele care incadreaza bicicletele 

    b. sa se eticheteze (fara ajutorul algoritmilor de AI) aceste imagini cu chenare care sa incadreze cat mai exact bicicletele. Care task dureaza mai mult (cel de la punctul a sau cel de la punctul b)?

    c. sa se determine performanta algoritmului de la punctul a avand in vedere etichetarile realizate la punctul b (se vor folosi cel putin 2 metrici).


Pentru a folosi rezursele Azure [more details](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/client-library?tabs=windows%2Cvisual-studio&pivots=programming-language-python):
- creare subscriptie (in calitate de student UBB exista acces gratis)
- creare resursa AI Vision (si salvare keys & endpoint)
- instalare pachete necesare
- autentificare credentiale si creare client (pt a accesa resursele Azure)
- prelucrare imagini in mod automat 

## :hourglass: Termen de predare 

Laborator 5

## :moneybag: Evaluarea

- Cerinta 1 - 100 puncte
- Cerinta 2 a - 100 puncte 
- Cerinta 2 b - 100 puncte
- Cerinta 2 c - 100 puncte
