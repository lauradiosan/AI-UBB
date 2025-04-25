# Lab09 - Procesarea textelor cu ajutorul LLMs 


## :microscope: Obiective 

Dezvoltarea sistemelor care învaţă singure. Probleme de tip clasificare din domeniul text-mining rezolvate cu ajutorul algoritmilor de tip LLM. Evaluareaa performanței acestor metode.

## :book:  Aspecte teoretice

1.	Data
    - https://huggingface.co/datasets/biglam/gutenberg-poetry-corpus
    - https://github.com/tnhaider/english-gutenberg-poetry
    - https://www.shakespeares-sonnets.com/all.php
2.	BLUE
    - https://machinelearninginterview.com/topics/natural-language-processing/bleu-score/
    - https://machinelearningmastery.com/calculate-bleu-score-for-text-python/
    - https://aclanthology.org/P02-1040/ 

 



## :bulb: Probleme

In urma unor inundatii, o parte din versurile unor poezii  s-au degradat. Folositi un LLM pentru a completa versurile lipsa (avand in vedere ca primul vers din fiecare strofa s-a pastrat intact)

a. folositi un LLM pre-antrenat (pe texte generale) si analizati influenta parametrilor (inclusiv a tokenizer-ului) asupra calitatii textului generat
b. folositi un LLM pre-antrenat si adaptat la un corpus de poezii si analizati influenta parametrilor (inclusiv a tokenizer-ului) asupra calitatii textului generat
c. Incercati sa raspundeti la urmatoarele intrebari: 
- c.1 care sunt diferentele de calitate intre textele generate cu cele doua tipuri de LLM-uri?
- c.2 ce se intampla daca versurile din prompt sunt in limba engleza?
- c.3 ce se intampla daca versurile din prompt sunt in limba romana?
- c.4 ce se intampla daca versurile din prompt sunt in limba romana si corpusul de antrenare este in limba engleza?
- c.5 cum se poate "personaliza" LLM pentru a genera versuri in stil de pastel (cu accent pe frumusetea naturii)?


2. Salvați poezia care vi se pare cea mai reușită si trimiteti-o unui prieten.

## :memo:  Cerinte 

Specificați, implementați și testați subalgoritmii necesari rezolvarii problemelor.

## :hourglass: Termen de predare 
Laborator 11

## :moneybag: Evaluarea

Punctajele acordate:
- Cerinte a - 100p
- Cerinta b - 200p
- cerinta c - 250p

Notă: 
- punctajul maxim acumulat pentru acest laborator este 550 puncte.
- punctajul minim pentru ca o tema predata sa fie valida este 100 puncte.  


