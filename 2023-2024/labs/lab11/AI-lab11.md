# Lab11 - Generative AI - for codebases  <img src="genAIcode.png" width="100">



## :microscope: Obiective 

Folosirea modelelor de tip Generative AI pentru imbunatatirea codurilor sursa

## :book:  Aspecte teoretice

- Cum genereaza modelelor de limbaj textele?
- Cum se pot folosi modelele de GenerativeAI pentru imbunatatirea codurilor sursa?

## :bulb: Probleme


O echipa de programatori are nevoie de ajutor in mai multe task-uri precum refresh la un cod "preluat" de la altii prin adaugarea de specificatii (comentarii) la fiecare (sub-algoritm) si dezvoltarea rapida de noi functionalitati plecand de la cerintele clientilor.

## :memo:  Cerinte 
Sa se foloseasca modele inteligente pentru:
1. a stabili rolul (scopul) unui (sub)algoritm plecand de la codul sau - maparea/proiectia codului sursa intr-un spatiu latent (embedding), urmata de clasificarea acestuia;
2. a genera specificatii (comentarii) care sa elucideze ce face un anumit algoritm - se va folosi un model care va primi codul sursa aferent unui algoritm si va genera textul aferent comentariilor
3. a genera cod sursa plecand de la descrierea in limbaj natural a functionalitaii pe care a enuntat-o clientul - se va folosi un model care va primi enuntul in limbaj natural si va genera codul

Se pot folosi modele pre-antrenate sau modele personalizate (antrenate "from scratch" sau "fine-tuned") pentru codurile proprii.
Ca baza de testare (show case) se vor folosi cerintele si subalgoritmii dezvoltati la laboratorul 1.

Info utile:
- Embedding-uri de cod de tipul celor calculate de [Code2Vec](https://code2vec.org/)
- model pentru Python [PyCodeGPT](https://github.com/microsoft/PyCodeGPT/blob/main/README.md)
- modele similare pentru limbajul Java [link](https://github.com/agemagician/CodeTrans/blob/main/prediction/single%20task/code%20comment%20generation/base_model.ipynb)
- modele de generare de text [HugginFaceZoo](https://huggingface.co/models?pipeline_tag=text-generation&sort=trending)

## :hourglass: Termen de predare 
Laborator 14 

## :moneybag: Evaluarea

Punctajele acordate
- Cerinta 1 - 100p (model pre-trained) sau 200p (model personalizat)
- Cerinta 2 - 100p (model pre-trained) sau 200p (model personalizat)
- Cerinta 3 - 100p (model pre-trained) sau 200p (model personalizat)


Notă: 
- punctajul maxim acumulat pentru acest laborator este 600 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  



