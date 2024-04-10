# Lab08 - Generative AI - generare texte



## :microscope: Obiective 

Înțelegerea problemei de generare de text (date de intrare, date de ieșire, preprocesări, aspect probabilistic).

## :book:  Aspecte teoretice

1.	Data
    - https://huggingface.co/datasets/biglam/gutenberg-poetry-corpus
    - https://github.com/tnhaider/english-gutenberg-poetry
    - https://www.shakespeares-sonnets.com/all.php
2.	Markov
    - https://github.com/jsvine/markovify
    - https://www.stat.auckland.ac.nz/~fewster/325/notes/ch8.pdf
3.	Embeddings
    - https://radimrehurek.com/gensim/models/word2vec.html
    - https://radimrehurek.com/gensim/models/fasttext.html#gensim.models.fasttext.FastText
    - https://aws.amazon.com/what-is/embeddings-in-machine-learning/
    - https://www.cloudflare.com/en-gb/learning/ai/what-are-embeddings/
    - https://towardsdatascience.com/what-is-embedding-and-what-can-you-do-with-it-61ba7c05efd8  
4.	BLUE
    - https://machinelearninginterview.com/topics/natural-language-processing/bleu-score/
    - https://machinelearningmastery.com/calculate-bleu-score-for-text-python/
    - https://aclanthology.org/P02-1040/ 

 



## :bulb: Probleme
1.	Generare în limba română: Implementați un sistem care transformă un text (corpus) într-un lanț Markov și folosiți-l pentru a generare un proverb sau o poezie în limba română (folosiți fișierele proverbRo.txt sau poezieRo.txt)
    - Varianta 1 – Implementați un lanț Markov cu o singură stare sau
    - Varianta 2 – Implementați un lanț Markov cu n-stări

*(stare = numărul de cuvinte pe baza cărora se realizează predicția)

2.	Generare în limba engleză: 

a.	Folosiți biblioteca markovify (sau implementarea voastră de la problema 1) pentru a genera o strofă de poezie în limba engleză folosind unul din următoarele corpus-uri (sau orice altă sursă găsiți voi):
- https://huggingface.co/datasets/biglam/gutenberg-poetry-corpus
- https://github.com/tnhaider/english-gutenberg-poetry
- https://www.shakespeares-sonnets.com/all.php

b.	Calculați emoția textului generat, puteți folosi una din următoarele resurse:
- Natural Language Toolkit (nltk) SentimentIntensityAnalyzer
- TextBlob sentiment

c.	Pentru a adresa limitările de creativitate în poezia generată înlocuiți aleator cuvinte cu sinonime. Se cere ca sinonimele să fie obținute folosind embedding-uri. (i.e. Cuvântul ales e transformat în forma sa embedded și se alege embedding-ul cel mai apropiat care este convertit la string)

d.	Salvați poezia care vi se pare cea mai reușită si trimiteti-o unui prieten.

e.	Calculați metrica BLEU (Bilingual Evaluation Understudy Score) pentru poezia aleasă

## :memo:  Cerinte 

Specificați, implementați și testați fucțiile, respectiv algortimii de la problemele 1 și 2.

## :hourglass: Termen de predare 
Laborator 9

## :moneybag: Evaluarea

Punctajele acordate:
- Problema 1. a – 50 puncte
- Problema 1. b – 150 puncte
- Problema 2. a – 50 puncte
- Problema 2. b – 50 puncte
- Problema 2. c – 50 puncte
- Problema 2. e – 50 puncte  



Notă: 
- punctajul maxim acumulat pentru acest laborator este 400 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  







