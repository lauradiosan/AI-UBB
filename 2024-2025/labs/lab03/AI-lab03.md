# Lab03 - Optical Character Recognition <img src="ocr.png" width="100">


## :microscope: Obiective 

Recunoașterea optică a caracterelor (OCR) este o tehnologie care permite computerelor să citească text din imagini. Instrumentele OCR au devenit din ce în ce mai populare datorită capacității lor de a automatiza introducerea datelor și de a extrage informații din documentele scanate. Scopul acestui laborator este familiarizarea cu algoritmii de AI capabili sa recunoasca in mod automat texte scrise, plecand de la date de intrare de tip imagine.

## :book:  Aspecte teoretice 

OCR 
- specificarea problemei
- evaluarea performantei unui algoritm de AI in rezolvarea problemei 
    - diferite rate de eroare (Character error rate (CER), Word Error Rate (WER))
    - diferite metrici de distanta (distanta Hamming, distanta Jaro-Winkler, distanta Levenshtein, Longest common subsequence, etc.)

Biblioteci utile:
- Azure AI Vision [link](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- Tesseract [link](https://github.com/tesseract-ocr/tesseract)

A se consulta exemplul de [aici](https://github.com/lauradiosan/AI-UBB/blob/main/2023-2024/labs/lab03/AIlab03-OCR.ipynb)


## :bulb: Probleme 

Sa se identifice textul scris [de mana] intr-o imagine:
- locatia textului
- textul propriu-zis



## :memo:  Cerinte 

Specificaţi, implementaţi și testați subalgoritmi pentru problema enuntata.
Sa se determine:
1. calitatea procesului de recunoastere a textului, atat la nivel de caracter, cat si la nivel de cuvant 
- a. prin folosirea unei metrici de distanta sau
- b. prin folosirea mai multor metrici de distanta.
2. calitatea localizarii corecte a textului in imagine
3. posibilitati de imbunatatire a recunoasterii textului


Pentru a folosi rezursele Azure [more details](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/client-library?tabs=windows%2Cvisual-studio&pivots=programming-language-python):
- creare subscriptie (in calitate de student UBB exista acces gratis)
- creare resursa AI Vision (si salvare keys & endpoint)
- instalare pachete necesare
- autentificare credentiale si creare client (pt a accesa resursele Azure)
- prelucrare imagine in mod automat si identificare text
- stabilire calitate pentru procesul de recunoastere




## :hourglass: Termen de predare 

Laborator 4

## :moneybag: Evaluarea

- Cerinta 1 a - 100 puncte
- Cerinta 1 b - 100 puncte 
- Cerinta 2 - 100 puncte
- Cerinta3 - 200 puncte