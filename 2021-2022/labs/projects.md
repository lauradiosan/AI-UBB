
# Proiecte AI 2021-2022

1. [Project *Speech to text*](#speech-to-text)
2. [Project *Sentiment analysis in voice*](#markdown-header-sentiment-analysis-in-voice)
3. [Project *Sentiment analysis in text*](#markdown-header-sentiment-analysis-in-text)
4. [Project *Image processing for dental data*](#markdown-header-image-processing-for-dental-data)
5. [Project *Image processing for prostate cancer**](#markdown-header-image-processing-for-prostate-cancer)
6. [Project *Image processing for bladder cancer*](#markdown-header-image-processing-for-bladder-cancer)
7. [Project *3D reconstruction*](#markdown-header-3D-reconstructiona)
8. [Project *Image classification of batteries*](#markdown-header-image-classification-of-batteries)
[Project *Image processing for dental data*](#markdown-header-image-processing-for-dental-data)

## Speech to text

### Scop
- transformarea vocii in text pentru limba romana

### Ideea de baza

- transformarea unor inregistrari vocale in text poate fi utila persoanelor cu dizabilitati, reporterilor, medicilor (care analizeaza situatia pacientilor sau doresc sa realizeze fisa pacientului in timp ce mainile lor sunt ocupate cu salvarea pacientului), scriitorilor, cadrelor didactice (care doresc sa ofere notite aferente lectiilor explicate).

### TODOlist
1. Iteratia1
- analiza seturi de date (voce, transcriere) pentru limba engleza si pentru limba romana
- parsarea vocii in text prin folosirea de modele inteligente (pre-trained) (de ex [link0](https://deepspeech.readthedocs.io/en/v0.8.2/?badge=latest), [link1](https://realpython.com/python-speech-recognition/#how-speech-recognition-works-an-overview), [link2](https://pypi.org/project/SpeechRecognition/))
- evaluarea performantei transformarii


2. Iteratia2
- dezvoltarea de modele inteligente pt SpeechToText (si antrenarea lor)  [link0](https://deepspeech.readthedocs.io/en/v0.7.4/TRAINING.html)
- evaluarea a performantei transformarii
- compararea modelelor pre-trained (iteratia 1) cu cele trained (iteratia 2)

### Data
- [LibriSpeech](http://www.openslr.org/12)
- [TIMIT](https://catalog.ldc.upenn.edu/LDC93S1)


### Bibliografie
- Hannun, A., Case, C., Casper, J., Catanzaro, B., Diamos, G., Elsen, E., ... & Ng, A. Y. (2014). Deep speech: Scaling up end-to-end speech recognition. arXiv preprint arXiv:1412.5567
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., & Polosukhin, I. (2017). Attention is all you need. Advances in neural information processing systems, 30.
- https://github.com/flashlight/flashlight/tree/main/flashlight/app/asr 


### Coordonator
- ???


## Sentiment analysis in voice

### Scop
- Recunoasterea emotiilor in semnale audio.

### Ideea de baza

- identificarea emotilor in semnalele vocale/audio poate fi de real folos in marketing, psihologie, sistemul de educatie, etc. 


### TODOlist
1. Iteratia1
- analiza datelor
- extragerea de caracteristici acustice din semnalele audio (by a tool - e.g. [Librosa](https://librosa.org/doc/latest/index.html) - or by implementing the feature extractor) 
- clasificarea semnalelor audio pe categorii de emotii folosind un model de clasificare (bazat pe SVM, ANN, etc.)
- evaluarea procesului de recunoastere a emotilor

2. Iteratia2
- extragerea de caracteristici spectrale din semnalele audio (format2D)
- clasificarea semnalelor audio pe categorii de emotii folosind un model de clasificare bazat pe CNN
- evaluarea procesului de recunoastere a emotilor
- compararea aboradrii din iteratia 1 cu abordarea din iteratia 2


### Data
- emotions [RAVDESS](https://zenodo.org/record/1188976#.YjjY5epBy5e)
- polarity [CMU-Moisei](http://multicomp.cs.cmu.edu/resources/cmu-mosei-dataset/)


### Bibliografie
- [Papers with code](https://paperswithcode.com/task/speech-emotion-recognition)
- Stolar, M., Lech, M., Bolia, R. S., & Skinner, M. (2018, December). Acoustic characteristics of emotional speech using spectrogram image classification. In 2018 12th International Conference on Signal Processing and Communication Systems (ICSPCS) (pp. 1-5). IEEE.
- Verbitskiy, Sergey, Vladimir Berikov, and Viacheslav Vyshegorodtsev. ”Eranns: Efficient residual audio neural networks for audio pattern recognition.” arXiv preprint arXiv:2106.01621 (2021).
- Lassalle, Amandine, et al. "The EU-Emotion Voice Database." Behavior research methods 51.2 (2019): 493-506.
- Matsuda, Yuki, et al. "Emotour: Estimating emotion and satisfaction of users based on behavioral cues and audiovisual data." Sensors 18.11 (2018): 3978.
- Issa, D., Demirci, M. F., & Yazici, A. (2020). Speech emotion recognition with deep convolutional neural networks. Biomedical Signal Processing and Control, 59, 101894.

### Coordonator
- ???


## Sentiment analysis in text

### Scop
- Recunoasterea emotiilor in texte.


### Ideea de baza
- analizarea limbajului uman prin extragerea de opinii, idei si ganduri prin atribuirea de polaritati (negative, pzotive sau neutre) sau emotii mai granulare (fericire, tristete, furie, etc.) incearca sa contribuie la mai buna dezvoltarea a retelelor sociale, sistemelor de marketing sau de sanatate, in educatie.

### TODOlist
1. Iteratia1
- analiza datelor
- recunoasterea emotilor in texte folosind modele gata antrenate (e.g. [GoogleAPI](https://cloud.google.com/natural-language/docs/basics#sentiment-analysis-values), [MicrosoftAPI](https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/sentiment-opinion-mining/quickstart?pivots=programming-language-python))
- evaluarea procesului de recunoastere a emotilor

2. Iteratia2
- recunoasterea emotilor in texte folosind modele de invatare bazate pe caracteristici extrase cu ajutorul algoritmilor de ML (de ex. BERT sau transformers [link](https://github.com/huggingface/transformers))
- evaluarea procesului de recunoastere a emotilor
- compararea abordarii din iteratia 1 cu abordarea din iteratia 2


### Data
- [Rotten Tomatoes](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/data)
- [Twitter US Airline](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)
= [SemEval2018](https://alt.qcri.org/semeval2018/index.php?id=tasks)

### Bibliografie
- Nandwani, P., & Verma, R. (2021). A review on sentiment analysis and emotion detection from text. Social Network Analysis and Mining, 11(1), 1-19.
- Ribeiro, F. N., Araújo, M., Gonçalves, P., Gonçalves, M. A., & Benevenuto, F. (2016). Sentibench-a benchmark comparison of state-of-the-practice sentiment analysis methods. EPJ Data Science, 5(1), 1-29.
- Dang, N. C., Moreno-García, M. N., & De la Prieta, F. (2020). Sentiment analysis based on deep learning: A comparative study. Electronics, 9(3), 483.
- Adoma, A. F., Henry, N. M., & Chen, W. (2020, December). Comparative analyses of bert, roberta, distilbert, and xlnet for text-based emotion recognition. In 2020 17th International Computer Conference on Wavelet Active Media Technology and Information Processing (ICCWAMTIP) (pp. 117-121). IEEE.
- [Papers with code](https://paperswithcode.com/task/sentiment-analysis)

### Coordonator
- ???


## Image processing for dental data


### Scop

Identificarea dintilor si leziunilor in imagini dentare

### Ideea de baza

- procesarea automata a imaginilor medicale dentare poate fi foarte utila atat medicilor, cat si pacientilor. Identificarea dintilor si a leziunilro in aceste imagini reprezinta baza dezvoltarii unor aplicatii de screening automat a starii de sanatate a dintilor.


### TODOlist

1. Iteratia 1
- analiza datelor
- segmentarea zonelor de interes (mandibula, dinti) cu ajutorul unor modele preantrenate [DeepMedic](https://github.com/deepmedic/deepmedic), [U2net](https://github.com/xuebinqin/U-2-Net), [DeepLab](https://github.com/tensorflow/models/tree/master/research/deeplab)
- evaluarea segmentarilor

2. Iteratia 2
- antrenarea unor modele de segmentare bazate pe CNN si grafe [link](Lu, Y., Chen, Y., Zhao, D., Liu, B., Lai, Z., & Chen, J. (2020). CNN-G: Convolutional neural network combined with graph for image segmentation with theoretical analysis. IEEE Transactions on Cognitive and Developmental Systems, 13(3), 631-644.) a zonelor de interes specifice datelor medicale stomatologice [exemplu](https://github.com/SerdarHelli/Segmentation-of-Teeth-in-Panoramic-X-ray-Image-Using-U-Net) si studiul diferitelor functii de loss [link](https://github.com/JunMa11/SegLoss)
- evaluarea segmentarilor
- compararea abordarii din iteratia 1 cu abordarea din iteratia 2


### Data
- images with segmented [mandible](https://data.mendeley.com/datasets/hxt48yk462/1) and [tooth](https://github.com/SerdarHelli/Segmentation-of-Teeth-in-Panoramic-X-ray-Image-Using-U-Net)
- spectral images and their masks [here](https://sites.uef.fi/spectral/odsi-db/)

### Bibliografie
- Jader, G., Fontineli, J., Ruiz, M., Abdalla, K., Pithon, M., & Oliveira, L. (2018, October). Deep instance segmentation of teeth in panoramic X-ray images. In 2018 31st SIBGRAPI Conference on Graphics, Patterns and Images (SIBGRAPI) (pp. 400-407). IEEE.
- Leite, A. F., Gerven, A. V., Willems, H., Beznik, T., Lahoud, P., Gaêta-Araujo, H., ... & Jacobs, R. (2021). Artificial intelligence-driven novel tool for tooth detection and segmentation on panoramic radiographs. Clinical oral investigations, 25(4), 2257-2267.
- Lu, Y., Chen, Y., Zhao, D., Liu, B., Lai, Z., & Chen, J. (2020). CNN-G: Convolutional neural network combined with graph for image segmentation with theoretical analysis. IEEE Transactions on Cognitive and Developmental Systems, 13(3), 631-644.
- T. Wu et al, Leveraging graph-based hierarchical medical entity embedding for healthcare applications, Scientific reports, 11(1):pp. 1-13 (2021)

### Coordonator

- ???



## Image processing for prostate cancer

### Scop

- identificarea si clasificarea tumorilor in imagini medicale ale prostatei

### Ideea de baza

- detectarea tesuturilor cancerigene in prostata (prin metode automate non-invazive) contribuie la stabilirea unui tratament personalizat si recuperarea mai buna a pacientului. 

### TODOlist

1. Iteratia 1
- analiza datelor
- extragerea de hand-crafted radiomics features (cu ajutorul instrumentelor existente - ex. PyRadiomics) si clasificarea leziunilor cu un algoritm evolutiv (de ex [Multi Expression Programming](http://mepx.org/))
- evaluarea performantelor clasificarii

2. Iteratia 2
- antrenarea unor modele de extragere a caracteristicilor bazate pe deep learning si clasificarea leziunilor cu un algoritm evolutiv (de ex [Multi Expression Programming](http://mepx.org/))
- evaluarea performantei
- compararea abordarii din iteratia 1 cu abordarea din iteratia 2


### Data
- 26 MR datasets - https://wiki.cancerimagingarchive.net/display/Public/PROSTATE-MRI#327726088352fbd47ff4147b574d72f5b596e4a
- https://promise12.grand-challenge.org/ - great challenge, one can check methods, articles
- https://zenodo.org/record/16396#.X57-1IgzaM9 - 3 patients MR and ultrasound
- https://prostatemrimagedatabase.com/ - 230 datasets - I have no info about quality


### Bibliografie
- Oltean, M. (2022). Multi Expression Programming for solving classification problems [link](https://www.researchgate.net/publication/359261779_Multi_Expression_Programming_for_solving_classification_problems)
- Afshar, P., Mohammadi, A., Plataniotis, K. N., Oikonomou, A., & Benali, H. (2019). From handcrafted to deep-learning-based cancer radiomics: challenges and opportunities. IEEE Signal Processing Magazine, 36(4), 132-160.
- L. Jing, Y. Tian, Self-supervised visual feature learning with deep neural networks: A survey, IEEE Transactions on pattern analysis and machine intelligence (2020)
- theory -> prostate imaging
    - https://www.slideshare.net/abd_ellah_nazeer/presentation1-mri-imaging-of-the-prostate
    - https://www.slideshare.net/abd_ellah_nazeer/presentation1pptx-radiological-imaging-of-prostatic-diseases - sl48/49
    - Kato Zoltan - linear registration of medical data - http://www.inf.u-szeged.hu/rgvc/demos.php?did=affbinregdemo
    - 3D - http://www.inf.u-szeged.hu/rgvc/demos.php?did=affbin3dregdemo


### Coordonator
- ???


## Image processing for bladder cancer 

#£# Scop

- stadializarea tumorilor in imagini medicale ale vezicii

### Ideea de baza

- identificarea tumorilor in vezica si gradul lor de infiltrare in peretele vezicii cu ajutorul tehnicilor automate (prin metode non-invazive) se poate dovedi a fi un real sprijin in stadializarea cancerului de vezica 

### TODOlist

1. Iteratia 1
- analiza datelor
- segmentarea zonelor de interes (perete, interior, tumora, background) cu ajutorul unor modele bazate pe CNN [DeepMedic](https://github.com/deepmedic/deepmedic), [U2net](https://github.com/xuebinqin/U-2-Net), [DeepLab](https://github.com/tensorflow/models/tree/master/research/deeplab)
- evaluarea segmentarilor

2. Iteratia 2
- clasificarea leziunilor anterior segmentate in functie de gradul lor de penetrare a peretelui vezicii
- evaluarea performantei



### Data
- 19 MRI - mouse, xenograft model - 2019 - https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=52757379120
- human participants - multimodal imaging - https://wiki.cancerimagingarchive.net/display/Public/TCGA-BLCA#1605636778b0bc3193ac47e9a70f2dcc3b72b99e


### Bibliografie
- M. I. Metwally et al, The validity, reliability, and reviewer acceptance of VI-RADS in assessing muscle invasion by bladder cancer: a multicenter prospective study. European Radiology, 1-13 (2021)
- S. H. Kim, Validation of vesical imaging reporting and data system for assessing muscle invasion in bladder tumor. Abdominal Radiology, 45(2):491-498 (2020)
- Tian, Z., Li, X., Zheng, Y., Chen, Z., Shi, Z., Liu, L., & Fei, B. (2020). Graph‐convolutional‐network‐based interactive prostate segmentation in MR images. Medical physics, 47(9), 4164-4176.
- X. Dolz et al., Multiregion segmentation of bladder cancer structures in MRI with progressive dilated convolutional networks, Med. Phys. 45 (12):5482–5493 (2018)
- K. Hammouda et al., A deep learning-based approach for accurate segmentation of bladder wall using mr images, 2019 IEEE International Conference on Imaging, pp. 1-6 (2019)

### Coordonator
- ?



##  3D reconstruction


### Scop

- dezvoltarea dispozitivelor de imobilizare și materialelor compensatoare personalizate pentru radioterapie prin procesarea imaginilor și imprimare 3D

### Ideea de baza

- in terapia radiologica a diverselor boli este nevoie de construirea unor masti de protectie a anumitor parti ale corpului (de ex. protejarea fetei). Daca aceste masti respecta cat mai mult fizionomia unui pacient, ele se transforma in aliati siguri ai pacientului, dar si ai medicului in combaterea bolilor si cresterea gradului de securitate a organelor care nu trebuie iradiate. Constructia unei masti se poate adapta specificului unui pacient, respectand trasaturile fetei. In acest context se doreste dezvoltarea unei aplicatii care pe baza imaginii fetei unei persoane sa poata extrage caracteristicile faciale si sa frunizeze un model 3D a acestora.

### TODOlist

1. Iteratia 1
- generarea unui mesh plecand de la o imagine faciala/a corpului folosind un generator pre-antrenat (e.g. [Neural Body](https://zju3dv.github.io/neuralbody/), [3DDFA](https://github.com/cleardusk/3DDFA_V2), [MediaPipe](https://google.github.io/mediapipe/solutions/face_mesh.html), [DECA](https://github.com/YadiraF/DECA))
- compararea mastilor generate cu masti fizice si stabilirea erorii

2. Iteratia 2
- generarea unui mesh plecand de la o imagine faciala/a corpului folosind un generator antrenat pe un set de date oferit de client 
- compararea mastilor generate cu masti fizice si stabilirea erorii
- compararea rezultatelor obtinute cu in cele 2 iteratii


### Data
- [ZJU-Mocap](https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset)
- [AFLW2000-3D](http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm)


### Bibliografie
- 
- Michael K. Three-dimensional printing in radiation oncology: A systematic review of the literature 2020
- Jiang, L., Zhang, J., Deng, B., Li, H., & Liu, L. (2018). 3D face reconstruction with geometry details from a single image. IEEE Transactions on Image Processing, 27(10), 4756-4770.
- Guo, J., Zhu, X., Yang, Y., Yang, F., Lei, Z., & Li, S. Z. (2020, August). Towards fast, accurate and stable 3d dense face alignment. In European Conference on Computer Vision (pp. 152-168). Springer, Cham.
- [Papers with code](https://paperswithcode.com/paper/pix2vox-context-aware-3d-reconstruction-from)


### Coordonator
- Zoltan Balint


##  Image classification of batteries


### Scop
- recunoasterea defectelor de fabricatie la bateriile de masina

### Ideea de baza

- identificarea defectelor de fabricate la diferite produse, precum bateriile, poate ajuta la eficientizarea liniilor de productie.


### TODOlist

1. Iteratia 1
- analiza datelor
- clasificarea imaginilor cu baterii folosind un model bazat pe CNN (pre-trained or transfer learning or trained from scratch)
- evaluarea performantei clasificarii

2. Iteratia 2
- clasificarea imaginilor cu baterii folosind un model bazat pe CNN de tip federated learning [link](https://federated.withgoogle.com/), [link](https://github.com/tensorflow/federated)
- evaluarea performantei clasificarii
- compararea abordarii din iteratia 1 cu cea din iteratia 2


### Data
- [ImageNet](https://image-net.org/)
- [Products](https://products-10k.github.io/)

### Bibliografie
- Dandage, H. K., Lin, K. M., Lin, H. H., Chen, Y. J., & Tseng, K. S. (2021). Surface defect detection of cylindrical lithium-ion battery by multiscale image augmentation and classification. International Journal of Modern Physics B, 35(14n16), 2140011.
- Dandage, H. K., Lin, K. M., Lin, H. H., Chen, Y. J., & Tseng, K. S. (2021). Surface defect detection of cylindrical lithium-ion battery by multiscale image augmentation and classification. International Journal of Modern Physics B, 35(14n16), 2140011.
- Sheller, M. J., Edwards, B., Reina, G. A., Martin, J., Pati, S., Kotrotsou, A., ... & Bakas, S. (2020). Federated learning in medicine: facilitating multi-institutional collaborations without sharing patient data. Scientific reports, 10(1), 1-12.


### Coordonator
- ???


