# UBB-AI 2025-2026 projects

## Metodologie de lucru

<details>

- Proiectele se pot realiza in echipa de maxim 4 persoane
- O echipa poate lucra la o singura tema de proiect. Un proiect poate fi ales de maxim 5 echipe, dar fiecare echipa va lucra independent.
- Echipele si temele vor fi comunicate cadrelor didactice care coordoneaza activitatea de laborator pana cel tarziu in **30 aprilie  2025**.
- Proiectele se vor incarca in acest [git](https://classroom.github.com/a/LESHiTyK). Fiecare proiect trebuie sa contina:
    - codul si explicatiile aferente (de ex. un notebook in care celulele de cod sa alterneze cu cele de explicatii) - organizate cat mai frumos 
    - un folder cu datele folosite 
    - o pagina de garda (readme) care sa contina informatii despre: 
        - echipa care a lucrat la proiect, 
        - problema abordata si 
        - un desen/schema care sa sugereze cat mai bine solutia propusa
    - cel putin cate 2 pull-request-uri (unul pentru fiecare etapa de predare) din partea fiecarui membru al echipei
- In saptamana 12 se vor prezenta, in cadrul orelor de laborator primele 2 etape (Definirea problemei si analiza datelor de intrare) si de vor incarca pe git materialele aferente
- In saptamana 14 se vor prezenta, in cadrul orelor de laborator, ultimele 2 etape (Dezvoltarea modelului si Imbunatatiri) si se vor incarca pe git materialele aferente
- In saptamana 14 (2 - 6 iunie) se vor incarca pe git filmulete scurte de prezentare a proiectelor realizate (doar de catre echipele care au obtinut cel putin 300p pana acum).
- Evaluare:
    - definirea problemei si analiza datelor de intrare - 200p
    - dezvoltarea unui model de AI si evaluarea performantei - 300p
    - imbunatatiri - 300p
    - teaser de prezentare a solutiei dezvoltate - 200p
        - ce problema rezolva proiectul (inputs, outputs)
        - ce tip de AI s-a folosit
        - ce performanta s-a obtinut
        - care sunt [SGD](https://unstats.un.org/wiki/display/SDGeHandbook/Home)-urile impactate de un astfel de proiect (motivati alegerea unuia sau mai multor obiective)
</details>

## Teme de proiect

Pentru oricare tema de proiect se va dezvolta un sistem inteligent bazat pe un agent AI care poate rezolva autonom problema descrisă, prin interpretarea instrucțiunilor în limbaj natural, planificarea pașilor necesari și utilizarea instrumentelor software pentru generarea unui rezultat final corect și relevant. Fiecare echipă va livra un prototip funcțional care demonstrează capacitatea agentului de a executa autonom un flux de lucru complex, folosind:
- modele ML/LLM studiate
- lanțuri de prompting
- un agent capabil să apeleze instrumente (tool use)
- tehnici de evaluare și testare

Proiectul trebuie să includă atât partea de inteligență artificială, cât și un modul minimal de interacțiune (CLI, API, UI simplă sau notebook interactiv).


<details>
    <summary> 1. CV Parsing and HR Assistant
    </summary>

#### Scop
Proiectarea și implementarea unui agent AI capabil să analizeze automat CV‑uri și descrieri de post, să extragă și să compare competențe relevante, să calculeze scoruri de potrivire și să furnizeze explicații și recomandări care sprijină reducerea timpului de recrutare și a influenței biasului în procesele de selecție. Proiectul nu are scopul de a automatiza complet deciziile de angajare, ci de a oferi suport decizional explicabil pentru utilizatorii umani.

#### Ideea de baza
În procesele de recrutare, personalul de HR se confruntă cu provocări semnificative în ceea ce privește trierea eficientă a CV-urilor și evaluarea candidaților pe baza calificărilor și experienței acestora. Volumul mare de aplicații primite pentru fiecare poziție este adesea copleșitor, ceea ce îngreunează identificarea celor mai potriviți candidați. Acest lucru duce la cicluri de angajare prelungite, posibila trecere cu vederea a unor candidați calificați și o încărcare suplimentară pentru personalul HR. În plus, procesul de revizuire manuală este predispus la bias și inconsistențe, ceea ce poate afecta calitatea generală a angajărilor și diversitatea bazei de candidați.

#### TODOlist
Dezvoltarea unui instrument de triere a CV-urilor bazat pe AI/ML care automatizează și standardizează evaluarea candidaților pentru a accelera angajările, a îmbunătăți calitatea potrivirii și a reduce biasul.

Caracteristici cheie și beneficii:
- Scor de potrivire a competențelor: Generează un scor procentual care compară fiecare CV cu descrierea postului, permițând HR-ului să prioritizeze rapid candidații cu potrivirea cea mai bună.
- Număr de entități/competențe: Extrage și contabilizează competențele și entitățile relevante pentru a oferi o imagine clară a calificărilor candidatului și pentru a identifica abilități comune sau unice în pool-ul de talente.
- Recomandări: Oferă sugestii pentru următorii pași (întrebări personalizate pentru interviu, semnale de alarmă, evaluări recomandate) pentru a eficientiza și standardiza deciziile de selecție.
- Analiza frazelor și a cuvintelor cheie: Detectează terminologia specifică industriei și expresiile relevante pentru a îmbunătăți acuratețea trierei și pentru a evita omiterea candidaților calificați.
- Reducerea biasului: Utilizează algoritmi obiectivi și standardizați pentru a minimiza biasul inconștient, sprijinind procese de angajare mai corecte și mai diverse.
- Dashboard ușor de utilizat: Vizualizează metrici (candidați triați, scoruri medii, top candidați) pentru decizii rapide și bazate pe date.
- Învățare continuă: Modelele ML se îmbunătățesc în timp folosind feedback și rezultate, menținând recomandările aliniate cu nevoile de angajare în evoluție.

#### Bibliografie

Devlin, J., Chang, M.‑W., Lee, K., & Toutanova, K. (2019). BERT: Pre‑training of deep bidirectional transformers for language understanding. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL‑HLT), 4171–4186. [link](https://doi.org/10.18653/v1/N19-1423)

Jurafsky, D., & Martin, J. H. (2023). Speech and language processing (3rd ed., draft). [link](https://web.stanford.edu/~jurafsky/slp3/)

Manning, C. D., Raghavan, P., & Schütze, H. (2008). Introduction to information retrieval. Cambridge University Press.

Reimers, N., & Gurevych, I. (2019). Sentence‑BERT: Sentence embeddings using Siamese BERT‑networks. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing. [link](https://arxiv.org/abs/1908.10084)

</details>


<details>
    <summary> 2. Text to AI Video Animation Tool for product teams and educational content
    </summary>

#### Scop
Dezvoltarea unui sistem inteligent bazat pe modele de limbaj de mari dimensiuni (LLM) care transformă descrieri textuale structurate ale unor produse sau conținut educațional în videoclipuri animate scurte, prin conversie automată text‑în‑script, împărțire logică pe scene, generare de narațiune audio și sincronizare vizuală, cu scopul de a sprijini comunicarea eficientă a ideilor și facilitarea proceselor de învățare. Accentul proiectului este pe proiectarea și integrarea unui pipeline inteligent, nu pe producția de animații complexe sau modele video generative

#### Ideea de baza
Dezvoltarea unui sistem inteligent care permite introducerea unui rezumat text al obiectivelor produsului, personelor și funcționalităților într-un sistem de animații video bazat pe inteligență artificială. Instrumentul ar genera un scurt videoclip animat care explică obiectivul general și propunerea de valoare a produsului. Acest lucru ar permite echipelor de business să socializeze ideile și să obțină acordul părților interesate mai devreme în ciclul de dezvoltare. De asemenea, se aliniază cu abordările agile de design thinking aplicate în dezvoltarea de produse. 
Există valoare suplimentară în utilizarea acestui instrument pentru crearea de conținut educațional și de învățare, transformând instrucțiunile bazate pe text în videoclipuri ușor de înțeles de 2–3 minute. 
Soluția ar putea extinde capabilitățile de tip AI chat cu un serviciu de generare și adnotare video (similar ca concept cu instrumente de povestire vizuală precum Pictionary). Aplicația ar putea fi comparabilă cu platforme precum pictory.ai, fliki.ai, animaker.com sau veed.io.

#### TODOlist

Funcționalități cheie
1. Conversie Text‑în‑Script cu împărțire pe scene de bază- Instrumentul va prelua un input text structurat (de ex., descrierea unui produs sau pași educaționali) și va realiza automat:
- Rezumarea conținutului
- Împărțirea acestuia în 5–8 scene logice
- Generarea unui scurt script de narațiune pentru fiecare scenă

2. Generare de animații pe baza unor șabloane - În loc de animații complet dinamice, sistemul va folosi șabloane video predefinite (ex.: stil whiteboard, prezentare tip slide, animație simplă cu iconițe).
Instrumentul va:
- Asocia fiecare scenă generată cu un slide dintr-un șablon
- Insera suprapuneri de text
- Adăuga iconițe/imagini stock de bază relevante pentru cuvintele cheie
- Aplica tranziții simple

3. Narațiune Text‑to‑Speech + Subtitrări - Sistemul va:
- Converti scriptul generat în audio folosind o API de tip text‑to‑speech
- Genera automat subtitrări (fișier SRT) 
- Sincroniza durata narațiunii cu durata fiecărei scene


#### Bibliografie
Devlin, J., Chang, M.‑W., Lee, K., & Toutanova, K. (2019). BERT: Pre‑training of deep bidirectional transformers for language understanding. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL‑HLT), 4171–4186. https://doi.org/10.18653/v1/N19-1423

Jurafsky, D., & Martin, J. H. (2023). Speech and language processing (3rd ed., draft). Stanford University. https://web.stanford.edu/~jurafsky/slp3/

Liu, Y., et al. (2019). Text summarization with pretrained encoders. Proceedings of EMNLP‑IJCNLP 2019, 3730–3740. https://arxiv.org/abs/1908.08345

Radford, A., et al. (2019). Language models are unsupervised multitask learners. OpenAI Technical Report. https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

Reimers, N., & Gurevych, I. (2019). Sentence‑BERT: Sentence embeddings using Siamese BERT‑networks. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing. https://arxiv.org/abs/1908.10084

</details>



<details>
    <summary> 3. AI Interviewer Assistant Tool  
    </summary>

#### Scop
Dezvoltarea unui sistem inteligent bazat pe tehnici de procesare a limbajului natural și modele de limbaj de mari dimensiuni (LLM) care să analizeze descrieri de post și CV‑uri, să identifice și să compare seturi de competențe relevante și să genereze automat întrebări de interviu structurate, cu scopul de a sprijini evaluarea consecventă, eficientă și explicabilă a candidaților. Instrumentul oferă suport decizional pentru pregătirea interviurilor și nu trebuie utilizat ca sistem automat de luare a deciziilor de angajare.

#### Ideea de baza
Asistentul AI pentru Interviuri are ca scop eficientizarea procesului de pregătire a interviurilor prin oferirea unei abordări structurate pentru evaluarea candidaților în raport cu cerințele postului. Prin automatizarea identificării seturilor de competențe și a generării întrebărilor pentru interviu, instrumentul îmbunătățește atât eficiența, cât și calitatea procesului de intervievare.

Asistentul AI pentru Interviuri va accepta următoarele inputuri:
- Descrierea Postului (JD): O descriere detaliată a rolului, incluzând competențele și calificările necesare.
- CV-ul candidatului, care evidențiază competențele, experiența și calificările sale.
- Numărul de întrebări per competență: Numărul dorit de întrebări de interviu generate pentru fiecare set de competențe identificat.


Procesare
- Identificarea Seturilor de Competențe - Analizează Descrierea Postului pentru a extrage seturile de competențe necesare.
Categorizează competențele în două grupuri:
    - Must Have: Competențe esențiale pentru rol.
    - Good to Have: Competențe suplimentare, utile dar nu obligatorii.

- Analiza CV-ului - Evaluează CV-ul candidatului pentru a determina potrivirea acestuia cu seturile de competențe identificate. Stabilește dacă fiecare competență este demonstrată de candidat și marchează drept „Da” sau „Nu”.

Outputuri
- Un tabel care afișează potrivirea competențelor candidatului cu cerințele descrierii postului, evidențiind competențele „Must Have” și „Good to Have” și indicând dacă fiecare competență este prezentă în CV-ul candidatului.

#### TODOlist

Instrumentul trebuie să poată parsa și analiza descrierile de post și CV-urile în diferite formate (ex.: PDF, DOCX, TXT).

Instrumentul trebuie să categorizeze corect seturile de competențe conform unor criterii predefinite.

Instrumentul trebuie să genereze întrebări relevante pentru interviu, aliniate seturilor de competențe identificate.

Instrumentul trebuie să permită utilizatorilor să specifice numărul de întrebări per set de competențe.


#### Bibliografie
evlin, J., Chang, M.‑W., Lee, K., & Toutanova, K. (2019). BERT: Pre‑training of deep bidirectional transformers for language understanding. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL‑HLT), 4171–4186. https://doi.org/10.18653/v1/N19-1423

Jurafsky, D., & Martin, J. H. (2023). Speech and language processing (3rd ed., draft). Stanford University. https://web.stanford.edu/~jurafsky/slp3/

Manning, C. D., Raghavan, P., & Schütze, H. (2008). Introduction to information retrieval. Cambridge University Press.

Reimers, N., & Gurevych, I. (2019). Sentence‑BERT: Sentence embeddings using Siamese BERT‑networks. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing. https://arxiv.org/abs/1908.10084

Liem, C. C. S., Langer, M., Demetriou, A., He, H., & Müller, K.‑R. (2018). Psychology meets machine learning: Interdisciplinary perspectives on algorithmic job candidate screening. Explainable AI Workshop at NeurIPS. https://arxiv.org/abs/1811.03371

</details>




<details>
    <summary> 4. Diagram-as-Code AI Assistant </summary>

#### Scop
Dezvoltarea unui sistem inteligent bazat pe modele de limbaj de mici dimensiuni (SLM) și tehnici de analiză statică a codului, capabil să genereze automat diagrame de arhitectură software în format „diagram as code” (diagrame formalizate, de ex. Mermaid, PlantUML), pornind de la descrieri textuale și/sau cod sursă, cu scopul de a sprijini menținerea documentației arhitecturale sincronizate cu implementarea. Proiectul se concentrează pe generarea de diagrame structurale de bază (context, componente, relații).

#### Ideea de baza
Arhitectura modernă de software se bazează puternic pe diagrame (de ex., context de sistem, diagrame container, diagrame de secvență, diagrame de infrastructură). Totuși, menținerea documentației sincronizate cu codul este adesea dificilă și consumatoare de timp.
De aceea este necesara proiectarea unei soluții bazate pe inteligență artificială care poate genera diagrame de arhitectură pornind de la descrieri în limbaj natural și/sau din codul sursă. Instrumentul ar trebui să suporte abordări de tip „diagram as code” (de ex., generarea de definiții structurate ale diagramelor, nu doar imagini statice). 

Dimensiuni de evaluare
- calitatea mecanismului de RAG si a bazei de cunostiinte cu AST-urile diagramelor
- Acuratețea generării diagramelor
- Nivelul de automatizare și ușurința mentenanței
- Utilitatea practică pentru echipele de software


#### TODOlist

Generarea diagramelor din:
- Descrieri text simple ale arhitecturii
- User stories
- Repozitoare de cod (de ex., identificarea serviciilor, API-urilor, dependențelor)

Dataset de antrenament pentru modele de limbaj de mici dimensiuni (SLM) care să învețe să genereze diagrame din text și/sau cod.
- dataset cu diagrame exprimate intr-un DSL (parsate si convertite in AST canonic) 

Output-ul diagramelor în formate precum:
- Mermaid
- PlantUML
- Structurizr DSL
- Graphviz

Integrarea soluției într-un flux GitHub de tip merge request pentru:
- Generarea automată sau actualizarea diagramelor de arhitectură când codul se schimbă.
- Adăugarea de comentarii pe merge request cu diagramele actualizate.

Implementarea unui Git hook care:
- Validează consistența arhitecturală înainte de a permite un commit.
- Regenerază automat diagramele atunci când anumite module se modifică.

Compararea generării diagramelor pe baza analizei statice a codului cu interpretarea semantică realizată de un LLM.


#### Bibliografie

Clemente, M., & Cândea, G. (2019). Software architecture documentation: A systematic mapping study. Journal of Systems and Software, 147, 124–147. https://doi.org/10.1016/j.jss.2018.10.013

Devlin, J., Chang, M.‑W., Lee, K., & Toutanova, K. (2019). BERT: Pre‑training of deep bidirectional transformers for language understanding. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL‑HLT), 4171–4186. https://doi.org/10.18653/v1/N19-1423

Jurafsky, D., & Martin, J. H. (2023). Speech and language processing (3rd ed., draft). Stanford University. https://web.stanford.edu/~jurafsky/slp3/

Richards, M., & Ford, N. (2020). Fundamentals of software architecture. O’Reilly Media.

Reimers, N., & Gurevych, I. (2019). Sentence‑BERT: Sentence embeddings using Siamese BERT‑networks. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing. https://arxiv.org/abs/1908.10084

</details>






<details>
    <summary> 5. Clinical Trial Radar – Sistem Inteligent pentru Analiza Fezabilității Studiilor Clinice </summary>

#### Scop

Dezvoltarea unui agent AI capabil să analizeze rapid peisajul studiilor clinice pentru o anumită boală și fază, generând automat indicatori de fezabilitate (trenduri, competiție pentru recrutare, distribuție geografică) și un snapshot exportabil pentru echipele din domeniul farmaceutic.

#### Ideea de baza

Studiile clinice eșuează sau sunt întârziate în mod frecvent din cauza unor estimări incorecte privind fezabilitatea și recrutarea, făcute prea devreme și pe baza unor date incomplete. Echipele trebuie să decidă rapid în ce țări și centre să deruleze studiul, dar informațiile relevante sunt dispersate, greu de comparat și adesea colectate manual în Excel, ceea ce duce la inconsistențe, costuri mari și întârzieri operaționale. 

**Clinical Trial Radar** își propune să ofere o imagine rapidă, factuală și standardizată asupra peisajului studiilor clinice pentru o anumită boală și fază. Instrumentul transformă datele din registre publice de studii clinice într-o vizualizare clară a:
- unde se desfășoară studiile
- cât de aglomerată este competiția pentru recrutare
- cum evoluează trendurile în timp
- care sunt timpii tipici ai ciclului de studiu

Scopul nu este de a înlocui expertiza medicală sau operațională, ci de a oferi o bază obiectivă, comparabilă și rapidă care poate reduce riscul, accelera deciziile și îmbunătăți consistența proceselor.

#### TODOlist
Sistemul inteligent trebuie să fie capabil să acopere funcționalități, precum:
- Căutare după boală + faza studiului - interogarea unui registru public de studii clinice (ex.: ClinicalTrials.gov).
- Generarea unui grafic de trend - evoluția în timp a numărului de studii recruiting vs completed.
- Hartă geografică - distribuția studiilor pe țări (ideal și pe orașe, dacă datele permit).
- Metrică de „aglomerare” (crowdedness) - numărul studiilor active/recruiting într-o regiune → indicator de competiție pentru recrutare.
- Tabel detaliat cu studii relevante - listă filtrabilă, cu link spre registru.
- Export „Feasibility Snapshot” (PDF sau slide) – sumar generat automat pentru prezentări și aprobări.
- Normalizarea termenilor medicali (sinonime, mapping boală).
- NLP pentru extragerea criteriilor de eligibilitate sau endpoint-uri comune.
- Estimarea duratelor obișnuite (cycle time) pe bază istorică.
- Recomandări AI pentru selecția țărilor cu cel mai mic risc.


Evaluare / KPI-uri sugerate
- Timp economisit pentru analiza fezabilității.
- Acoperire: procentul studiilor relevante identificate.
- Consistența outputului: formate standardizate între echipe.


#### Bibliografie
Primary trial data
•	ClinicalTrials.gov API v2: https://clinicaltrials.gov/data-api/about-api
•	ClinicalTrials.gov bulk downloads: https://clinicaltrials.gov/data-download
•	AACT (SQL-ready ClinicalTrials dataset): https://aact.ctti-clinicaltrials.org/
•	AACT docs: https://aact.ctti-clinicaltrials.org/documentation
Additional trial registries (open portals / datasets)
•	EU Clinical Trials Register (public search): https://www.clinicaltrialsregister.eu/
•	ISRCTN registry (public search): https://www.isrctn.com/
Terminology + enrichment
•	MeSH: https://www.nlm.nih.gov/mesh/meshhome.html
•	MeSH downloads: https://www.nlm.nih.gov/databases/download/mesh.html
•	PubMed E-utilities: https://www.ncbi.nlm.nih.gov/books/NBK25501/
•	OpenAlex: https://openalex.org/
•	NIH RePORTER: https://api.reporter.nih.gov/
Optional feasibility proxies
•	WHO GHO: https://www.who.int/data/gho
•	World Bank: https://data.worldbank.org


</details>

<details>
    <summary> 6. Pharmacovigilance Signal Triage Copilot – Agent Inteligent pentru Prioritizarea Semnalelor de Siguranță în Medicamente </summary>

#### Scop

Dezvoltarea unui agent AI capabil să analizeze volume mari de rapoarte de reacții adverse, să normalizeze datele, să identifice semnale timpurii de siguranță pentru combinații medicament–eveniment și să genereze automat pachete explicabile de evidențe pentru experții în farmacovigilență.


#### Ideea de baza

Echipele de siguranță medicamentoasă (pharmacovigilance / PV) primesc de la mii până la milioane de rapoarte privind efectele adverse ale medicamentelor. Aceste rapoarte sunt frecvent incomplete, redundante, neuniforme și greu de procesat: denumirile medicamentelor variază (brand, generic, ortografie), descrierea reacțiilor diferă de la raport la raport, iar cazurile pot fi duplicat sau lipsite de context.
Procesul actual de triaj necesită multă muncă manuală: specialiștii trebuie să curețe datele, să verifice semnalele potențiale și să compileze evidențe înainte ca experții să ia o decizie. Când triajul este lent sau supraîncărcat, semnalele critice pot fi identificate prea târziu, ceea ce crește riscul pentru pacienți și costurile pentru industrie.
Pharmacovigilance Signal Triage Copilot își propune să acționeze ca un „detector de fum” pentru siguranța medicamentelor:

identifică devreme semnale neobișnuite medicament–eveniment
explică motivele pentru care au fost detectate
pregătește automat un pachet de evidențe pentru revizuire
oferă o listă prioritizată a semnalelor

Deciziile finale rămân la experți, dar aceștia pornesc de la un top inteligent și contextualizat, nu de la o masă dezorganizată de rapoarte.

#### TODOlist

Sistemul inteligent trebuie să fie capabil să acopere funcționalități, precum:
- Selectarea unui medicament + interval de timp - filtrarea datelor privind reacțiile adverse în funcție de cerințele utilizatorului.
- Identificarea celor mai importante semnale medicament–eveniment - calcularea unor metrici standard de disproporționalitate, precum PRR (Proportional Reporting Ratio) sau ROR (Reporting Odds Ratio).
- Analiza trendului comparativ cu un baseline - detectarea creșterilor semnificative în timp pentru anumite evenimente.
- Explorarea rapoartelor individuale - funcționalitate de drill‑down pentru a vizualiza cazuri reprezentative.
- Generarea unui „Signal Packet” exportabil (PDF/slide) - pachet gata de prezentat, incluzând: descrierea semnalului, justificare, grafice
cifre relevante, exemple de rapoarte. 
- Ranking simplu al semnalelor - pe baza unor criterii precum severitatea evenimentelor + creșterea în timp.
- Normalizarea avansată a denumirilor medicamentelor (brand → INN).
- Normalizarea termenilor pentru reacțiile adverse (ex.: MedDRA).
- Deduplicare automată a cazurilor suspecte.
- Explicații generate de LLM pentru fiecare semnal.
- Detectarea semnalelor emergente cu rate neobișnuite față de istoricul medicamentului.
- Recomandări AI pentru prioritizarea investigațiilor.


Evaluare / KPI-uri sugerate
- Reducerea timpului de triaj comparativ cu analiza manuală.
- Numărul de „signal packets” generate per analist per zi.
- Timp mai scurt de la apariția semnalului până la revizuire (proxy pentru detecție timpurie).
- Grad de standardizare al pachetelor generate automat.

#### Bibliografie

Primary PV data
•	openFDA FAERS API: https://open.fda.gov/apis/drug/event/
•	FAERS background: https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers-public-dashboard
Drug normalization + open drug data
•	RxNorm: https://lhncbc.nlm.nih.gov/RxNorm/
•	DrugCentral (open drug database): https://drugcentral.org/
•	ChEMBL (bioactivity + compounds): https://www.ebi.ac.uk/chembl/
•	Open Targets (target-disease associations): https://platform.opentargets.org/

Optional safety-related sources
•	FDA Recalls (open): https://open.fda.gov/apis/food/enforcement/  (useful pattern for “alerts/recalls” style)
•	PubMed E-utilities (literature): https://www.ncbi.nlm.nih.gov/books/NBK25501/

</details>

<details>
    <summary> 7. Semantic Alarm Deduplication Engine (Reducing ICU Alarm Fatigue)
    </summary>


#### Scop
Dezvoltarea unui agent inteligent bazat pe modele de limbaj și embeddings care identifică și grupează alarme medicale similare din punct de vedere semantic, reducând alarmele redundante și generând o notificare unificată, clară și explicabilă.

#### Ideea de baza
În spitale și în special în unitățile de terapie intensivă (ICU), personalul medical este expus zilnic la un număr foarte mare de alarme generate de sisteme diferite (monitoare, pompe, sisteme EHR). Multe dintre aceste alarme descriu același eveniment clinic, dar folosesc formulări diferite sau provin din surse diferite.
Regulile simple (ex.: text identic) nu pot detecta aceste duplicări semantice, iar rezultatul este:
- zgomot excesiv,
- oboseală cauzată de alarme (alarm fatigue),
- risc de ignorare a alertelor importante.

Semantic Alarm Deduplication Engine își propune să construiască un strat inteligent care:
- „înțelege” semnificația alarmelor,
- detectează alarme redundante pe baza similitudinii semantice,
- le grupează într-o singură alertă clară și acționabilă,
- păstrează trasabilitatea către alarmele originale.

Proiectul nu presupune sisteme clinice reale sau timp real, ci folosește date simulate, fiind orientat pe validarea conceptelor AI.



#### TODOlist
Sistemul inteligent trebuie să fie capabil să acopere funcționalități, precum:
- Flux de alarme simulat - Generarea sau încărcarea unui set de alarme provenite din mai multe „surse” (texte similare, ușor diferite). Exemple: „Heart rate too high”, „Tachycardia detected”, „HR exceeds threshold”.
- Reprezentare semantică (embeddings) - Transformarea mesajelor de alarmă în vectori folosind un model de embeddings (ex.: Sentence-BERT, embeddings LLM).
- Detecția alarmelor similare - Calcularea similitudinii semantice între alarme. Gruparea alarmelor similare într-o fereastră de timp simulată.
- Generarea unei alarme unificate - Crearea unei notificări consolidate care: rezumă evenimentul, listează sursele/alarmelor originale, atribuie o prioritate simplă (ex.: medie/ridicată).
- Configurarea pragurilor - Posibilitatea de a modifica pragul de similitudine pentru deduplicare.
- Validare și evaluare - Identificarea cazurilor de „false merge” (alarme diferite grupate incorect). Afișarea unor metrici simple.
- Clasificarea severității alarmelor.
- Explicații generate de LLM despre motivul grupării.
- Dashboard simplu (ex.: Streamlit) cu: alarme brute, alarme grupate, metrici, etc.
- Compararea performanței pentru diferite modele de embeddings.


Evaluare / KPI-uri sugerate
- Rata de deduplicare (%) – câte alarme au fost consolidate.
- Rata de „false merge” – alarme diferite grupate incorect.
- Timpul până la alertă consolidată (simulat).
- Reducerea numărului de alarme/oră (proxy pentru reducerea zgomotului).


#### Bibliografy
•	Alarm fatigue primer (AHRQ): https://psnet.ahrq.gov/primer/alarm-fatigue
•	Sentence-BERT: https://www.sbert.net/
•	spaCy: https://spacy.io/
•	PhysioNet datasets (credentialed, for realistic signals): https://physionet.org/



</details>

<details>
    <summary> 8. EEG-to-Image / EEG-to-Text Reconstruction</summary>

#### Scop

Dezvoltarea unui agent inteligent care, pornind de la semnale EEG, poate aproxima conținutul perceput de utilizator sub forma unei imagini sau a unui text scurt.

#### Ideea de baza

Semnalele EEG conțin informații despre modul în care creierul procesează stimuli vizuali sau lingvistici. În ultimii ani, au apărut seturi de date publice care permit explorarea reconstrucției acestor stimuli.

Studiul acestor sisteme este important deoarece ele pot permite persoanelor cu dizabilități să comunice sau să controleze dispozitive doar prin activitatea cerebrală.

Proiectul propune dezvoltarea unui sistem care:
- primește ca input semnal EEG asociat unui stimul;
- extrage caracteristici relevante (features / embeddings);
- mapează EEG-ul către o reprezentare semantică sau vizuală;
- produce un output aproximativ (imagine sau text).


#### Seturi de date recomandate

**Pentru EEG → imagine:**
- THINGS-EEG  
- THINGS-EEG2  
- EEG-ImageNet  

**Pentru EEG → text:**
- ZuCo / ZuCo 2.0  

---

#### TODOlist

1. **Încărcare și preprocesare EEG**
- filtrare simplă;
- selectarea regiunilor relevante;
- normalizare.

2. **Feature extraction**
- conversie la spectrogramă sau features simple;
- alternativ: folosirea unui model specilizat in EEG (ex: EEGNet).

3. **Model de bază**
- varianta 1: clasificare (ce imagine / categorie);
- varianta 2: retrieval (cea mai apropiată imagine din dataset);
- varianta 3: generare text / imagine.

4. **Output**
- top-k imagini candidate sau etichetă;
- sau propoziție scurtă (pentru text).

5. **Evaluare**
- accuracy / top-k accuracy;
- cosine similarity între embeddings;
- pentru text: BLEU / similaritate semantică.

6. **Interfață simplă**
- demo Streamlit;
- input EEG → output predicție.

---

#### Evaluare / KPI-uri

- Top-1 / Top-5 accuracy;
- Similaritate embedding;
- Timp de inferență;
- Calitatea outputului (vizual sau textual).

---

#### GitHub-uri utile (EEG real, nu generale)

1. Procesare EEG:
- https://github.com/mne-tools/mne-python  
- https://github.com/braindecode/braindecode  

2. Modele EEG:
- https://github.com/vlawhern/arl-eegmodels  
- https://github.com/eeyhsong/EEG-Conformer  

3. EEG → imagine:
- https://github.com/perceivelab/eeg_visual_classification  
- https://github.com/prajwalsingh/EEG2Image  

4. EEG → text:
- https://github.com/DS3Lab/zuco-nlp
- https://github.com/norahollenstein/zuco-benchmark  


#### Bibliografie

Lawhern, V. J., Solon, A. J., Waytowich, N. R., et al. (2018).  
**EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces** Journal of Neural Engineering.

Schirrmeister, R. T., Springenberg, J. T., Fiederer, L. D. J., et al. (2017).  
**Deep learning with convolutional neural networks for EEG decoding and visualization** Human Brain Mapping.

Gifford, A. T., Dwivedi, K., Roig, G., & Cichy, R. M. (2022).  
**A large and rich EEG dataset for modeling human visual object recognition** NeuroImage.

Zhu, S., et al. (2024).  
**EEG-ImageNet: An Electroencephalogram Dataset and Benchmarks with Image Visual Stimuli of Multi-Granularity Labels** https://arxiv.org/html/2406.07151v1.

Hollenstein, N., et al. (2018).  
**ZuCo: A dataset combining EEG and eye-tracking for natural language processing** Scientific Data.

Hollenstein, N., et al. (2020).  
**ZuCo 2.0: A dataset for natural reading and annotation** LREC.

Roy, Y., Banville, H., Albuquerque, I., et al. (2019).  
**Deep learning-based electroencephalography analysis: A systematic review** Journal of Neural Engineering.

</details> 

<details>
    <summary>  9. Segmentarea arterei etmoidale anterioare pe CBCT  </summary>

#### Scop

Chirurgia endoscopică nazală necesită precizie​. Lezarea arterei etmoidale anterioare (AEA) este un risc frecvent​. Necesitatea localizării exacte preoperatorii a AEA​. Obiectivul proiectului este: segmentarea AEA pe CBCT. 




Segmentarea AEA pe CBCT presuspune crearea unei baze de date de variații anatomice​, antrenarea unei inteligențe artificiale pentru detectare automată. Ipactul clinic al unui astfel de sistem automat: reducerea riscurilor operatorii privind
lezarea AEA​, cresterea gradului de precizie pentru manoperele de endoscopie nazala​.

#### Ideea de baza

Realizarea segmentarii folosind un model de inteligență artificială, antrenat pe un set de date de CBCT-uri cu AEA segmentată manual. Modelul va învăța să recunoască caracteristicile anatomice și variațiile posibile ale AEA pentru a oferi o segmentare automată precisă.

Modelul se va baza pe un Transformer Visual, similar cu [VISTA 3D](https://openaccess.thecvf.com/content/CVPR2025/html/He_VISTA3D_A_Unified_Segmentation_Foundation_Model_For_3D_Medical_Imaging_CVPR_2025_paper.html), [SAM-Med3D](https://arxiv.org/pdf/2310.15161)

#### Data

[link](https://www.cs.ubbcluj.ro/external/mldatasets/?dir=bigdata/dateArteraEtimoidala)

#### Bibliografie

Huang, J., Habib, A. R., Mendis, D., Chong, J., Smith, M., Duvnjak, M., ... & Wong, E. (2020). An artificial intelligence algorithm that differentiates anterior ethmoidal artery location on sinus computed tomography scans. The Journal of Laryngology & Otology, 134(1), 52-55.

Amarnath, S., & Suresh Kumar, P. (2019). Study of variants of anterior ethmoidal artery on computed tomography of paranasal sinuses. Int J Otorhinolaryngol Head Neck Surg, 5, 19-23.

Itayem, D. A., Anzalone, C. L., White, J. R., Pallanch, J. F., & O’Brien, E. K. (2019). Increased accuracy, confidence, and efficiency in anterior ethmoidal artery identification with segmented image guidance. Otolaryngology–Head and Neck Surgery, 160(5), 818-821.

</details>

<details>
    <summary>  10 Monitorizarea stării de sănătate cu ajutorul SmartWatch  </summary>

### Scop

Brățările de fitness și ceasurile inteligente purtate la încheietură, bazate pe accelerometru, au apărut pe piața de consum în 2011. De atunci, au fost lansate numeroase dispozitive purtabile. Pe lângă utilizarea lor pentru monitorizarea activității fizice personale, aceste dispozitive sunt tot mai des folosite în cercetare pentru colectarea de date de sănătate. Sunt concepute pentru utilizare pe termen lung, ceea ce permite înregistrarea continuă cu un efort minim din partea participanților. Proiectul urmărește explorarea potențialului datelor colectate de ceasuri inteligente și dispozitive purtabile în domeniul sănătății, prin aplicarea tehnicilor de Business Intelligence (BI).

### Ideea de baza
Proiectul urmărește utilizarea tehnicilor de Business Intelligence (BI) pentru analiza datelor colectate de dispozitive purtabile (ex. ceasuri inteligente). Scopul este extragerea de informații relevante pentru sănătatea utilizatorului, precum nivelul de activitate fizică, calitatea somnului, ritmul cardiac și localizarea, și transformarea acestora în insight-uri utile pentru intervenții personalizate.
 
<!-- ### TODOlist
1. Iteratia1
2. Iteratia2 -->
### Data

- [link](https://bmcresnotes.biomedcentral.com/articles/10.1186/s13104-022-06146-5
https://www.researchgate.net/publication/378021834_Analysis_of_Fitness_Based_on_Smart_Watch_Data)

- [link](https://ceur-ws.org/Vol-3514/paper73.pdf)


### Bibliografie

Mogra, A., Pandey, P. K., & Panwar, R. S. (2024, December). Artificial Intelligence Enabled Sleep Health Dashboards: Power BI Integration for Data-Driven Lifestyle Modifications. In 2024 Eighth International Conference on Parallel, Distributed and Grid Computing (PDGC) (pp. 535-539). IEEE [link](https://ieeexplore.ieee.org/abstract/document/10984363)

Reddy, N. C. N., Ramesh, A., Rajasekaran, R., & Masih, J. (2020, May). Ritchie’s Smart Watch Data Analytics and Visualization. In International Conference on Image Processing and Capsule Networks (pp. 776-784). Cham: Springer International Publishing.[link](https://d1wqtxts1xzle7.cloudfront.net/96645011/978-3-030-51859-2_70-libre.pdf?1672579590=&response-content-disposition=inline%3B+filename%3DRitchie_s_Smart_Watch_Data_Analytics_and.pdf&Expires=1759213247&Signature=QSkC1ZZ1hezkhPx2bnqrWfikyhAPRw8R83lYHOrsKW2GA4nfVd~kOZ-RvFPbNCPPnK9x6b66MnJYvnR1VElnEt~Nn8dsjHjiR4WpKMJ8KhfpSqKeoPoEmTSPtTo57lcLSAyLr7XL0tbdk5YpxUrrK6GcHpG7YTfUrOu9Xh2lxi~-V1DOXFkhtHqw9wtWGoniLusVXsLuGaGdQibTMUCEUmV5Cw-fISVvv170AiNH-Lb5z4yZqaunHabVBOBWQ~dhzedn~7G7PPQEdWcIBSXf~uxQDpCfXlzRQ1F-Xh2dBDZFyOru9AxMKgElC6a6f5jMIn6YLQwPTpZBiSgW~YZYEQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)

Bhavsar, K., Singhal, S., Chandel, V., Samal, A., Khandelwal, S., Ahmed, N., & Ghose, A. (2021, March). Digital biomarkers: Using smartwatch data for clinically relevant outcomes. In 2021 IEEE International Conference on Pervasive Computing and Communications Workshops and other Affiliated Events (PerCom Workshops) (pp. 630-635). IEEE. [link](https://ieeexplore.ieee.org/abstract/document/9431000)

Del-Valle-Soto, C., Briseño, R. A., Valdivia, L. J., & Nolazco-Flores, J. A. (2024). Unveiling wearables: exploring the global landscape of biometric applications and vital signs and behavioral impact. BioData Mining, 17(1), 15. [link](https://link.springer.com/content/pdf/10.1186/s13040-024-00368-y.pdf)

</details>


