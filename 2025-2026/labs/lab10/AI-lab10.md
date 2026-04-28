# Lab10 - Reinforcement Learning: *The Cliff Walker's Dilemma*

## :microscope: Obiective

Înțelegerea conceptelor fundamentale din Reinforcement Learning (RL) prin
implementarea și compararea a doi algoritmi clasici de învățare prin diferențe
temporale (Temporal Difference Learning), cu aplicații diverse, precum:
- navigarea agenților autonomi într-un mediu cu obstacole și risc
- controlul roboților în medii parțial stochastice
- luarea deciziilor secvențiale sub incertitudine (trading, planificare, jocuri)
- proiectarea funcțiilor de recompensă (reward shaping) în sisteme reale

La finalul laboratorului, studentul trebuie să înțeleagă **de ce** doi algoritmi
aparent foarte asemănători (diferă printr-o singură linie în update rule) pot
învăța politici fundamental diferite pe același mediu.

## :book: Aspecte teoretice

Spre deosebire de învățarea supervizată, în RL agentul nu primește perechi
(input, output corect), ci interacționează cu un mediu și primește o
**recompensă** scalară după fiecare acțiune. Scopul agentului este să învețe o
**politică** π(a|s) care maximizează suma cumulată de recompense viitoare.

Formalism - **Markov Decision Process (MDP)** definit de tuplul (S, A, P, R, γ):
- S - spațiul stărilor
- A - spațiul acțiunilor
- P(s'|s,a) - funcția de tranziție
- R(s,a) - funcția de recompensă
- γ ∈ [0,1] - factorul de discount

Funcția de valoare-acțiune: Q(s,a) = E[Σ γ^t · r_t | s_0=s, a_0=a, π]

Algoritmi studiați:
- **Q-learning (off-policy)** - update rule:

  `Q(s,a) ← Q(s,a) + α · [r + γ · max_{a'} Q(s',a') − Q(s,a)]`

  Ținta este construită folosind acțiunea **optimă** în starea următoare,
  indiferent de ce face agentul în realitate.

- **SARSA (on-policy)** - update rule:

  `Q(s,a) ← Q(s,a) + α · [r + γ · Q(s',a') − Q(s,a)]`

  Ținta este construită folosind acțiunea **efectiv aleasă** a' în s' (eșantionată
  din politica agentului, inclusiv explorarea ε-greedy).

Concepte cheie:
- **exploration vs. exploitation** - strategia ε-greedy
- **on-policy vs. off-policy** - cine generează ținta din update rule
- **reward shaping** - modificarea semnalului de recompensă pentru a ghida învățarea
- **temporal difference (TD) error** - δ = r + γ · Q(s',a') − Q(s,a)

Referință: Sutton & Barto, *Reinforcement Learning: An Introduction*, Capitolul 6.

## :bulb: Problema

**The Cliff Walker's Dilemma.** Un agent trebuie să traverseze o grilă de la
punctul de Start până la punctul Goal. De-a lungul marginii inferioare se află
o **prăpastie (cliff)**: orice pas în prăpastie penalizează sever agentul și îl
trimite înapoi la Start. Agentul nu cunoaște harta - trebuie să învețe din
experiență.

Întrebarea centrală a laboratorului:

> *Dacă antrenez Q-learning și SARSA pe exact același mediu, cu exact aceiași
> hiperparametri, vor învăța aceeași politică? Dacă nu, de ce nu?*

## :world_map: Specificația mediului

Mediul este **complet deterministic** și trebuie implementat de voi (nu folosiți
`gymnasium.make("CliffWalking-v0")`).

- Grilă: 4 rânduri × 12 coloane. Coordonate `(row, col)` cu `(0,0)` stânga-sus.
- **Start**: `(3, 0)`. **Goal**: `(3, 11)` (stare terminală).
- **Cliff**: celulele `(3, 1)` ... `(3, 10)`.
- Acțiuni: `UP`, `DOWN`, `LEFT`, `RIGHT` (4 acțiuni).
- Tranziții: deterministice. Dacă acțiunea ar scoate agentul din grilă, acesta
  rămâne pe loc.
- Recompense:
  - `−1` pentru orice pas normal
  - `−100` dacă agentul intră pe o celulă de tip cliff; apoi este **teleportat
    înapoi la Start** și episodul **continuă** (nu este terminal)
  - `0` la atingerea celulei Goal (stare terminală)
- Discount: `γ = 1.0` (nedisconted, setting clasic).

Schelet obligatoriu:
```python
class CliffWalkingEnv:
    def reset(self) -> int: ...          # returnează starea inițială
    def step(self, action: int) -> tuple: # returnează (next_state, reward, done)
        ...
```

## :memo: Cerințe

1. **Implementarea mediului** conform specificației de mai sus, folosind doar
   `numpy`. Adăugați o funcție `render()` (ASCII) care afișează poziția curentă
   a agentului.

2. **Implementarea Q-learning și SARSA** de la zero (nu se acceptă
   `stable-baselines`, `tianshou`, `rllib`). Ambii algoritmi folosesc:
   - tabel Q de dimensiune `|S| × |A|`, inițializat cu 0
   - politică de explorare ε-greedy
   - aceiași hiperparametri: `α = 0.1`, `γ = 1.0`, `ε = 0.1`, `500` episoade

3. **Experimentul central - divergența politicilor.** Rulați ambii algoritmi
   și generați:
   - graficul sumei recompenselor per episod (mediat pe o fereastră mobilă de
     10 episoade), pentru ambii algoritmi pe **aceeași figură**
   - vizualizarea politicii greedy învățate de fiecare algoritm pe grilă
     (săgeți sau simboluri pentru fiecare celulă)

   **Răspundeți în scris** (200-400 cuvinte) la:

   (a) Care algoritm învață un drum mai scurt în politica greedy finală? Care
   algoritm obține o sumă cumulată mai mare *în timpul antrenării*?

   (b) **De ce** cei doi algoritmi converg la politici diferite? Răspunsul
   trebuie să facă referire explicită la diferența dintre ținte (`max` vs.
   acțiune eșantionată) și la conceptul on-policy vs. off-policy.

   (c) De ce nu există o contradicție între (a) și răspunsul la (b)?

   *Această cerință reprezintă miezul conceptual al laboratorului și este
   evaluată preponderent pe calitatea explicației, nu pe cod.*

4. **Provocare - reward shaping.** Modificați **doar funcția de recompensă** (NU
   hiperparametrii, NU algoritmul) astfel încât ambii algoritmi să conveargă
   la **aceeași** politică greedy. Există mai multe soluții valide. Justificați
   în scris de ce modificarea voastră forțează echivalența, cu referire la
   mecanismul identificat la cerința 3.

5. **Provocare - ε-scheduling.** Reveniți la funcția de recompensă originală.
   Proiectați o schemă de descreștere a lui ε (ex. `ε_t = ε_0 · decay^t`, sau
   liniară) astfel încât politica greedy finală a lui SARSA să coincidă cu cea
   învățată de Q-learning. Argumentați: ce se întâmplă cu ținta SARSA atunci
   când `ε → 0`?

6. **Reflecție teoretică** (răspunsuri scurte, 2-4 propoziții fiecare):
   - Ce se întâmplă dacă setați `ε = 0` de la început pentru Q-learning? Dar
     pentru SARSA? De ce?
   - Dacă `γ < 1` (ex. `γ = 0.9`), cum se schimbă preferința fiecărui algoritm
     pentru drumul scurt vs. drumul sigur? Argumentați.
   - Dați un exemplu **din lumea reală** (nu joc de grilă) în care ați prefera
     SARSA în locul Q-learning și explicați de ce.

## 🏵️ Cerințe opționale

**Reward hacking în Tetris RL Framework.** Clonați repository-ul
`Tetris-Research-RL-Framework`. Studiați funcția de recompensă folosită de
`HeuristicRLAgent` (fișierul `advanced_rl_agents.py`).

- Alegeți **o singură componentă** a recompensei (line clears, height penalty,
  hole penalty, survival, game over).
- **Formulați în scris o predicție**, **înainte de a rula cod**: ce se va
  întâmpla cu politica învățată dacă dublez / anulez / inversez semnul acelei
  componente? De ce?
- Rulați antrenamentul (număr redus de episoade - suficient cât să observați
  tendința) și verificați empiric predicția.
- Scrieți un raport de maxim o pagină: predicție → rezultat → explicație.
  Dacă predicția a fost greșită, aceasta nu afectează punctajul; calitatea
  analizei *post-hoc* da.

Scopul acestei cerințe este de a conecta intuiția despre reward shaping
construită în cerințele 3-4 cu un sistem real, mai complex.

## :hourglass: Termen de predare

Laboratorul 11.

## :package: Livrabile

- Un **Jupyter notebook** (`.ipynb`) sau un script Python împreună cu un PDF/
  markdown ce conține răspunsurile scrise
- Graficele cerute (inclus în notebook sau ca fișiere separate)
- Pentru cerința opțională: raportul de o pagină, separat

Codul trebuie să ruleze la o singură comandă (`python lab.py` sau Run All
în notebook). Setați un `random seed` fix pentru reproducibilitate.

## :no_entry: Restricții

- Mediul trebuie **implementat de voi**. Folosirea `gymnasium.make("CliffWalking-v0")`
  sau a oricărui mediu preconstruit echivalent este **interzisă** și se
  penalizează cu 0 puncte pentru cerința 1.
- Pentru cerințele 2-6: doar `numpy` și `matplotlib`. Nu se acceptă biblioteci
  de RL de nivel înalt (`stable-baselines3`, `rllib`, `tianshou`, `keras-rl` etc.).
- Răspunsurile scrise trebuie să fie **în cuvintele voastre**. Citatele
  necesită sursă. Răspunsurile generate AI neverificate și neînțelese vor fi
  identificate la susținerea orală.

## :moneybag: Evaluarea

Punctajele acordate:
- Implementarea mediului `CliffWalkingEnv` - **50 puncte**
- Implementarea Q-learning (tabelar, ε-greedy, from scratch) - **75 puncte**
- Implementarea SARSA (tabelar, ε-greedy, from scratch) - **75 puncte**
- Experimentul central - plots + vizualizare politici - **50 puncte**
- Experimentul central - explicația scrisă (cerința 3, a/b/c) - **100 puncte**
- Provocare reward shaping - soluție funcțională + justificare - **100 puncte**
- Provocare ε-scheduling - soluție funcțională + justificare - **100 puncte**
- Reflecție teoretică (3 întrebări scurte) - **50 puncte**

Punctaj opțional (bonus):
- Reward hacking în Tetris framework - predicție + experiment + raport - **+150 puncte**

Notă: 
- punctajul maxim = **600 puncte** (+150 bonus); 
- punctajul minim pentru validare = **150 puncte**.

Susținerea se face oral: fiecare student trebuie să poată explica codul propriu
și răspunsurile scrise. Întrebările de control pot viza:
- de ce ați inițializat tabelul Q cu 0 (și ce s-ar întâmpla cu valori mari
  pozitive / negative)
- ce s-ar schimba dacă mediul ar deveni stochastic
- cum s-ar scala abordarea voastră la un mediu cu 10^6 stări
