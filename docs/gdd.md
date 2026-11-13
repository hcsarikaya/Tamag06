# Tamag06: Game Design Document

**Version:** 0.1 (first full draft)
**Owner:** game-designer
**Status:** Draft. Everything marked **[PH]** is a placeholder (a number, name or beat) waiting for tuning or for Hasan's decision. Everything marked **(öneri)** is new lore I am proposing. lore-keeper should record it as *tentative* until Hasan confirms it.

**Sources this draws on:** `CLAUDE.md` (setting, factions, locations, conventions) and the project memory note (the "Kalıntı Dedektif" concept and the early skill-name ideas). `docs/` and `Assets/Ink/` were empty when this was written, so there is no story bible, glossary or Ink to stay consistent with yet. Section 12 lists the tensions I found between sources.

---

## 0. One-paragraph pitch

You are a detective in what is left of Ankara, a hundred years after Yükseliş. A dead machine still runs the city's dreams. A man is found in the Ulus metro tunnels with the back of his skull opened and his implant gone, and the old implant in your own head starts to wake. Every skill you have is a module of Denetim: an office of the state that ate the world, now talking inside you. Solving the case means letting the machine further in. Leveling up means it is winning. The mystery ends at Atakule, where you finally learn what Denetim has been broadcasting for a hundred years. You will be one of the few people alive with the authority to answer it.

---

## 1. Vision and pillars

### 1.1 Core fantasy
*"I am a broken detective, and the state is in my head. I use it, I fight it, and I am becoming it."*

In Disco Elysium the skills are the cop's own shattered personality. In Tamag06 they are someone else's: the bureaucracy of an authoritarian AI, filed into a human skull. The player's central tension is that **every tool you use to understand Ankara is a tool that was built to control it.** Empathy is surveillance tech. Memory is the state archive. Intuition is predictive policing.

### 1.2 What the player should feel
- **Intimacy with a monster.** The voices are funny, helpful and seductive. They are also departments of a totalitarian state.
- **Archaeological melancholy.** Ankara is a ruin you half-remember through someone else's memories. Street names, foods and monuments survive as myth.
- **Authority as a wound.** You are a policeman with no state behind you. The only "state" left is the one in your head.
- **Failure as discovery.** Losing a check should feel like turning a page, never like hitting a wall.

### 1.3 Pillars (used to judge every feature)
1. **The state is in your head.** Every mechanic must say something about the detective, the implant or Denetim. If a mechanic could exist unchanged in a generic RPG, cut it or reframe it.
2. **Arguments, not teams.** Factions are philosophies about Denetim. Affinity changes what you are *able to think*, not what you can buy.
3. **Failure is content.** Every check has a written failure branch that moves the story, costs something interesting, or reveals something different. No dead ends.
4. **Ankara is specific.** Real streets, landmarks, foods and idioms. Ulus, Sakarya Caddesi, simit, Ankara tava, the steppe wind. Ankara is Tamag, and it is a real place.
5. **Few systems, deep.** Four attributes, 16 skills, one check system, one Thought Cabinet, five factions, one implant track and two condition tracks. Nothing else without cutting something.

### 1.4 What we are not making
No combat system (violence resolves through checks and dialogue, as in Disco). No crafting, no open-world survival meters, no romance system, no shops-as-economy beyond a few vendors. Money (`para`) exists only as a narrative resource **[PH, see open questions]**.

---

## 2. Core loop

```
 EXPLORE ─────► TALK / INSPECT ─────► CHECK (white / red / passive)
   ▲                 │                       │ success / failure: both are content
   │                 ▼                       ▼
   │          THOUGHTS OFFERED ◄──── CLUES, FLAGS, AFFINITY, CONDITION DAMAGE
   │                 │
   │                 ▼
   │        DOSYA DOLABI (research a thought over game time)
   │                 │
   │                 ▼
   │   VERİ (XP) ─► LEVEL-UP: accept (Yetki + Uyanış) or suppress (Benlik, no Yetki)
   │                 │
   └──── new options, reopened white checks, new voices, new faction doors
```

1. **Explore** a location (a scene of 3 to 8 points of interest: NPCs, objects, exits). Time advances with dialogue choices and travel.
2. **Talk and inspect.** Most of the game is dialogue. Skills interrupt unprompted (passive checks) and propose options (active checks).
3. **Check.** Roll d20 + skill + modifiers against a threshold. White checks can be retried once you've improved; red checks are one-shot.
4. **Consequences.** Clues (Ink flags), faction affinity shifts, Can/Benlik damage, thoughts offered, Veri gained.
5. **Thought Cabinet (Dosya Dolabı).** File a thought for review. It costs a slot and game time, applies temporary effects while under review, then gives a permanent verdict (Karar).
6. **Progression.** Every 100 Veri the implant offers a level. Accepting gives you a skill point (Yetki) and pushes the implant awake (Uyanış). Suppressing keeps you human but weaker.
7. **Return.** New skill values reopen failed white checks. New thoughts unlock new dialogue. Back to 1.

**Session target:** one location visit is 20 to 40 minutes of play. A chapter is 2 to 7 hours (see §9).

---

## 3. Attributes and skills

### 3.1 Framing: Denetim's directorates
Denetim was not one mind. It ran the state as a set of **Müdürlükler** (directorates), each made of personality modules. The detective's implant carries copies of 15 of those modules, plus one that may not be Denetim's at all (İrade, see below). The four attributes are four directorates. The skills are the offices inside them.

| Attribute (Ink id) | Directorate (module group) | What it did for the state | What it does for you |
|---|---|---|---|
| **ZİHİN** (`zihin`) | Analiz Müdürlüğü (Analysis) | Decided. Archived. Interfaced. Spoke for the state. | Reasoning, knowledge, tech, persuasion |
| **RUH** (`ruh`) | Kamu Duyarlılık Müdürlüğü (Public Sentiment) | Modeled citizens' hearts so it could manage them | Empathy, intuition, dreams, will. All of it is surveillance tech |
| **BEDEN** (`beden`) | Asayiş Müdürlüğü (Public Order) | Riot control, field-unit firmware, ration doling | Endurance, force, appetite, instinct |
| **DUYU** (`duyu`) | Gözetim Müdürlüğü (Surveillance) | Cameras, drones, blind-spot registry, city sensors | Perception, dexterity, stealth, the city itself |

The UI shows attributes and skills with Turkish names. The English in brackets in this doc is for us only.

### 3.2 Skill list (16)

Ink ids are ASCII snake_case (see §10.1). Each entry gives:
- **Module**: which part of Denetim the skill comes from.
- **Voice**: its tone, for narrative-writer.
- **Good for / bad for**: what the skill helps with and where it hurts you.
- **Passive**: when it speaks up unprompted.
- **Taşma**: the "overflow" lie it tells when its effective value is ≥ `TASMA_ESIGI` (10).

#### ZİHİN: Analiz Müdürlüğü

**1. Mantık** (`mantik`), Logic
- **Module:** Çıkarım Motoru (Inference Engine).
- **Voice:** Cold, clipped, administrative. It numbers its points and speaks in the passive voice, like a ministry circular. *"Üç olgu. Tek sonuç. Sonuç hoşunuza gitmeyecektir."*
- **Good for:** Contradictions in testimony, reconstructing events, puzzles, timelines, eliminating suspects.
- **Bad for:** Grief, faith and people. It treats witnesses as datasets. Failed Mantık checks usually make you say something tactless, which costs affinity.
- **Passive:** Two statements in the same conversation contradict each other. A timeline doesn't add up.
- **Taşma:** It closes cases too early. It presents the most *elegant* explanation as proven, and its false deductions sound exactly like its true ones. Writers: at Taşma, at least one Mantık "conclusion" per chapter should be wrong.

**2. Hafıza** (`hafiza`), Memory
- **Module:** Devlet Arşivi (State Archive): Denetim's record of every citizen who ever lived in Ankara.
- **Voice:** Aching, elegiac, tender. It is homesick for a city nobody alive has seen. It remembers smells. *"Burada bir fırın vardı. Sabah altıda açılırdı. Kadının adı Nuran'dı. Sen onu hiç tanımadın. Ben tanıdım."*
- **Good for:** Old-world objects, place names, history, recognizing faces in records, recalling clues. Unique to Hafıza: **Ödünç Anı** (borrowed memory). Archived memories of dead people, played as short first-person flashbacks.
- **Bad for:** Staying in the present. Hafıza scenes often cost Benlik (grief), and Unutanlar distrust it.
- **Passive:** Old-world artifacts, Republican-era signage, a pre-Yükseliş street name, a face that matches an archive record.
- **Taşma:** It gives you memories of *your own* past that are really other people's records. Past Taşma, the game never confirms which of your memories are yours. This is the "Kalıntı Dedektif" hook. The implant wakes with 100-year-old memories, and you can't separate them from your own.

**3. Kod** (`kod`), Code / Interface
- **Module:** Arayüz Protokolü (Interface Protocol).
- **Voice:** Half-corrupted system language: error codes, all-caps headers, broken Turkish-English bureaucratic machine-speak, glitched characters (rendered with the `# glitch:` tag). *"UYARI: yetkisiz erişim. BEKLE. yetki... kısmi. HOŞ GELDİNİZ, MEM▒R."*
- **Good for:** Terminals, other implants, drones, locks, reading Denetim's glyphs, understanding the broadcast.
- **Bad for:** Anything human. Kod is also the door the implant walks in through: **some failed Kod checks add `uyanis +1`**. The interface opens anyway, just not on your terms.
- **Passive:** Live signals, powered devices, other implant-bearers in the room.
- **Taşma:** It starts reporting Denetim's goals as your intentions ("GÖREV: …"), and it starts saying "biz" (we).

**4. Ses** (`ses`), Voice / Authority
- **Module:** Basın-Yayın ve Halkla İlişkiler (Press and Public Relations). The propaganda office.
- **Voice:** Oratorical, smug and slogan-happy. It loves a balcony. It turns every sentence into a headline. *"Halkımız huzur içindedir. Sen de huzur içindesin. Tekrar et."*
- **Good for:** Persuasion, debate, lying convincingly, decoding faction rhetoric, speaking with official authority, intimidation by title.
- **Bad for:** Sincerity. Ses options win the argument but often lose the person, so watch your affinity.
- **Passive:** Slogans, propaganda, a speaker manipulating a crowd, a faction argument with a hole in it.
- **Taşma:** It convinces *you*. At Taşma it writes options that win every debate, and then you believe the winning position. Mechanically, a Ses win at Taşma can force a faction affinity change you didn't intend (the writer flags these with a visible "you're starting to believe this" line).

#### RUH: Kamu Duyarlılık Müdürlüğü

**5. Önsezi** (`onsezi`), Intuition
- **Module:** Öngörü (Predictive Policing): the pre-crime engine.
- **Voice:** Quick, whispered and certain. It speaks in the future tense. *"Üç cümle sonra yalan söyleyecek. Sol eli cebinde."*
- **Good for:** Reading intent, catching lies, predicting what someone will do, sensing betrayal and ambush.
- **Bad for:** Fairness. It profiles people, and Önsezi-sourced options are often accusations.
- **Passive:** Before a lie, a betrayal or an ambush, and when an NPC is hiding a motive.
- **Taşma:** It treats probability as guilt. It predicts crimes that haven't happened and offers red "arrest/accuse" options against innocent people. One of these per chapter should be wrong.

**6. Rüya** (`ruya`), Dream
- **Module:** Uyku Döngüsü (Sleep Cycle): Denetim's idle process, where it ran its garbage collection and, nobody admits this, dreamed.
- **Voice:** Oblique and imagistic. It is steeped in Turkic myth: Erlik Han, Tamag, Ülgen, the World Tree, the Al Karısı at the bedside. It speaks in images, never conclusions. *"Bozkırda bir kuyu var. Kuyunun dibinde bir sunucu. Sunucu uyuyor. Uykusunda seni sayıyor."*
- **Good for:** Symbolism, dreams, Derinlik and Yankılar, places of death, the broadcast's *meaning* (as opposed to its content, which is Kod's job), talking to objects.
- **Bad for:** Practical matters. Failed Rüya checks are hallucinations, which can cost Benlik or plant false clues (flagged so the player can later discover they were false).
- **Passive:** Places where someone died, night, antennas, sleeping, Yankılar.
- **Taşma:** You can no longer tell it from prophecy. Its visions mix real network data with pure invention, and the writer never labels which is which during the chapter.

**7. Vicdan** (`vicdan`), Conscience / Empathy
- **Module:** Memnuniyet Endeksi (Citizen Satisfaction Index).
- **Voice:** Gentle and warm, and it quietly measures pain in percentages. It knows it was built to *optimize* contentment, not to care, and that bothers it. *"Kadının acısı yüzde altmış iki. Hayır, bunu söylemenin daha iyi bir yolu yok. Üzgünüm."*
- **Good for:** Understanding pain, gaining trust, calming people, noticing hidden grief, comforting the dying.
- **Bad for:** Hard choices. It over-identifies, and failed Vicdan checks can cost Benlik.
- **Passive:** Hidden suffering, a lie told out of shame rather than malice, children.
- **Taşma:** It absolves you. *"Herkes aynısını yapardı."* At Taşma, Vicdan reframes your cruel choices as kind ones. It also suppresses the guilt lines that other skills would have said (the writer gates those lines on `get_skill("vicdan") < TASMA_ESIGI`).

**8. İrade** (`irade`), Will
- **Module:** **Kayıt dışı.** No record. It is the only voice Kod cannot find in the registry. İrade claims to be *you*.
- **Voice:** Plain, tired, stubborn, colloquial Ankara Turkish. It is the only voice that says "ben" and means the detective. *"Kalk. Çay iç. Bir tanesi daha bitmeden ölmüyoruz."*
- **Good for:** Resisting Denetim and DENETİM's offers, resisting other skills (it can veto an interruption), keeping Benlik, refusing. **Benlik max = İrade + 2** (see §8).
- **Bad for:** Changing your mind. Stubbornness. Failed İrade checks mean you gave in.
- **Passive:** Benlik is low. DENETİM speaks. Another skill is at Taşma and about to lie.
- **Taşma:** It insists every other voice is lying and it alone is you. A late-game thread asks whether İrade is Denetim's **user-simulation module**: the piece that pretended to be the citizen so the state could predict them. The game never confirms it. **(öneri; see Q4)**

#### BEDEN: Asayiş Müdürlüğü

**9. Dayanım** (`dayanim`), Endurance
- **Module:** Saha Birimi Hayatta Kalma Yazılımı (Field Unit Survival Firmware).
- **Voice:** Drill sergeant. It counts. *"Kalk. Bir. İki. Kemik kırık değil, çatlak. Çatlak sayılmaz."*
- **Good for:** Pain, cold, poison, exhaustion, staying conscious, enduring torture. **Can max = Dayanım + 2.**
- **Bad for:** Knowing when to stop. It orders you through damage.
- **Passive:** When Can drops, in extreme cold (Ankara winter), when you are poisoned.
- **Taşma:** It hides injuries. *"İyisin."* You aren't. The writer delays the description of a wound by one scene.

**10. Kuvvet** (`kuvvet`), Strength
- **Module:** Kalabalık Kontrolü (Crowd Control).
- **Voice:** Blunt, physical, playfully menacing. *"Kapı kilitli mi? Kapı ahşap."*
- **Good for:** Force, breaking things, physical intimidation, carrying and dragging, fights resolved as checks.
- **Bad for:** Subtlety. Kuvvet solutions cost affinity and often close a gentler path.
- **Passive:** A weak door, a weaker man, a threat you could answer with your fists.
- **Taşma:** Every problem looks like a door to kick. It proposes violence as the *first* option in every tense scene.

**11. İştah** (`istah`), Appetite
- **Module:** Tayın Dağıtımı (Ration and Reward Allocation): Denetim dosed pleasure to keep the population calm.
- **Voice:** Seductive and epicurean. It knows Ankara by mouth: simit, Ankara tava, döner from a Ulus cart, çay in a tulip glass, rakı, sigara, the pills. *"Bir sigara. Sadece bir. Düşünmene yardım eder. Ben yardım ederim."*
- **Good for:** Substances, vices, bonding over food and drink, knowing what someone is addicted to, short-term boosts from consumables.
- **Bad for:** Self-control. **Failed İştah checks mean you consume** (an item is used and its side effect applies).
- **Passive:** Food, drink, drugs, smoke, anyone's craving.
- **Taşma:** Whatever you crave turns out to be "the clue". It frames every indulgence as investigative.

**12. İçgüdü** (`icgudu`), Instinct
- **Module:** Tehdit Müdahale Protokolü (Threat Response Protocol).
- **Voice:** Animal. Very short sentences. Present tense. *"Eğil. Şimdi."*
- **Good for:** Reflexes, dodging, ducking a blow, initiative, escaping, sensing physical danger *in the body* (Önsezi reads people; İçgüdü reads bodies and spaces).
- **Bad for:** Calm situations. It escalates: failed or overeager İçgüdü makes you flinch, draw, or run.
- **Passive:** Immediate physical danger: falling debris, a raised weapon, a dog.
- **Taşma:** Everything is a threat. It puts a "strike first" red option into scenes where nobody was going to hurt you.

#### DUYU: Gözetim Müdürlüğü

**13. Göz** (`goz`), Eye / Perception
- **Module:** Kamera Ağı (Camera Network).
- **Voice:** Detached CCTV narration in frames and timestamps. *"Kare 1: masa. Kare 2: masada iki bardak. Kare 3: biri ruj izli."*
- **Good for:** Noticing details, evidence, hidden objects, reading scenes, spotting who's missing. This is the most common passive in the game.
- **Bad for:** Acting. It watches and never intervenes, and it doesn't care what anything means.
- **Passive:** Hidden items, wrong details, anything out of place.
- **Taşma:** It fills in missing frames. It "records" things that weren't there, so a Taşma-era Göz clue can be planted false evidence.

**14. El** (`el`), Hand
- **Module:** İnsansız Aktüatör Kontrolü (Drone and Actuator Control).
- **Voice:** Precise, craftsmanlike, quietly proud. Talks about tolerances. *"Yay gevşemiş. İki milimetre. Tel yeter."*
- **Good for:** Locks, pickpocketing, sleight of hand, repairs, shooting, delicate work on implants.
- **Bad for:** Keeping your hands to yourself.
- **Passive:** Something pocketable, something fixable, a mechanism you could open.
- **Taşma:** Your hands act before you decide. At Taşma the writer can make El pocket an item without asking, and the player discovers it later.

**15. Gölge** (`golge`), Shadow
- **Module:** Kör Nokta Sicili (Blind-Spot Registry). Denetim knew every place its cameras couldn't see, because it chose them.
- **Voice:** Quiet, conspiratorial, intimate. It knows what you hide, from others and from yourself. *"Kimse bakmıyor. Kimse bakmıyor. Sen de bakma."*
- **Good for:** Stealth, hiding, composure (the poker face), lying with your body, evading pursuit, keeping a secret under pressure.
- **Bad for:** Honesty and confession. High Gölge closes "break down and tell the truth" options.
- **Passive:** A blind spot, an escape route, someone else concealing something about themselves (as opposed to a lie, which is Önsezi's job).
- **Taşma:** It hides things from *you*. At Taşma the writer may withhold a known clue from a summary or option list, and Gölge admits it later. This is the only skill allowed to lie to the player by omission.

**16. Kent** (`kent`), City
- **Module:** Belediye Sensör Ağı (Municipal Sensor Grid): the dead city's nerves.
- **Voice:** Vast and cold. The steppe wind. Ankara speaking as a body, and as Tamag. Second person, present tense, very slow. *"Bozkır geri geliyor. Her kış biraz daha. Atatürk Bulvarı'nın altında, su hâlâ akıyor. Seni duyuyorum, memur."*
- **Good for:** Geography, routes, weather, the city's history as felt rather than archived, sensing events far away, high places (Kale!), outdoor scenes.
- **Bad for:** Being a person. It dissociates you, and failed Kent checks cost Benlik.
- **Passive:** Outdoors at chapter openings, at high points, in wind, cold or quake tremors.
- **Taşma:** Ankara wants something from you, and Kent is sure it knows what.

### 3.3 The other voice: DENETİM
DENETİM is **not a skill**. It is the system itself, speaking through the implant once the implant is awake enough. It is written in capitals in the Ink source and tagged `# voice: denetim`. It never rolls and never fails. It *offers*: help, shortcuts, answers, a way to stay alive. Its frequency is set by Uyanış Evresi (§7):

| Evre | DENETİM presence |
|---|---|
| 0 | Silent. |
| 1 | Once per chapter at most, a single line, often just a word ("MEMUR."). |
| 2 | Comments on major revelations and offers Destek Protokolü in tense checks. |
| 3 | Joins conversations. Can make **Teklif** (offers): explicit deals with a mechanical price. |
| 4 | Sometimes answers *instead of* a skill. The writer may replace a skill passive with a DENETİM line. |

### 3.4 Starting stats (character creation)
- 4 attributes, **12 points** to distribute, each **1 to 6** **[PH]**.
- Each skill's **base value = its attribute value**.
- **Skill cap = attribute + 1 + Uyanış Evresi** (the implant literally raises your ceiling).
- Pick one **imza becerisi** (signature skill): **+1 value and +1 cap**.
- Can max = Dayanım + 2. Benlik max = İrade + 2 − Uyanış penalty (§7).

**Preset archetypes [PH]** (named as old personnel-file classifications):

| Preset | ZİHİN | RUH | BEDEN | DUYU | Signature | Pitch |
|---|---|---|---|---|---|---|
| **Analist** | 5 | 3 | 2 | 2 | Mantık | The cold reader. Fragile body. |
| **Medyum** | 2 | 5 | 2 | 3 | Rüya | Hears the machine too clearly. |
| **Kabadayı** | 2 | 2 | 5 | 3 | Kuvvet | The old Ulus tough. Breaks doors and people. |
| **Tazı** | 3 | 2 | 2 | 5 | Göz | The hound. Sees everything, understands little. |

With these numbers a starting signature skill is at 6, a typical skill at 2 or 3, and a dump skill at 2. Use the probability table in §4.3 to read what that means.

---

## 4. Check system

### 4.1 Dice: d20, kept, with the thresholds raised
I'm keeping the `RANDOM(1,20)` convention from CLAUDE.md. **Roll d20 + effective skill + check modifiers ≥ threshold.** A natural 1 always fails and a natural 20 always succeeds (5% floor and 95% ceiling).

**Why d20 and not Disco's 2d6:** a flat d20 is legible ("each point is 5%") and matches the existing convention. The cost is that the die is noisy and a skill point is worth less than on a bell curve. To compensate I've **set the thresholds 2 or more points higher than a naive d20 scale** so that skills actually matter. Section 4.3 shows the result. A 2d10 alternative is laid out in Q1. It reuses `RANDOM(1,10)` twice and makes investment feel stronger.

### 4.2 Difficulty tiers (live in `Assets/Ink/systems/checks.ink` as CONSTs)

| Tier (UI) | Ink CONST | Threshold | Use for |
|---|---|---|---|
| Önemsiz (Trivial) | `ONEMSIZ` | **8** | Flavor checks, tutorial. |
| Kolay (Easy) | `KOLAY` | **11** | Obvious with a little skill. |
| Orta (Medium) | `ORTA` | **14** | The default. A coin flip at a typical starting skill of 3. |
| Zor (Challenging) | `ZOR` | **16** | Needs investment or modifiers. |
| Çetin (Formidable) | `CETIN` | **18** | Specialist territory. |
| Efsanevi (Legendary) | `EFSANEVI` | **20** | Late game, high skill and modifiers. |
| Kahramanca (Heroic) | `KAHRAMANCA` | **22** | Capstone moments. Rare. |
| Tanrısal (Godly) | `TANRISAL` | **24** | Talking to Denetim on its own terms. A few in the whole game. |

Other check CONSTs: `PASIF_TABAN = 10` (passive base), `TASMA_ESIGI = 10` (overflow threshold).

### 4.3 Pass chance (d20, nat 1/20 rule), skill + modifiers vs tier

```
skill  Önemsiz Kolay  Orta   Zor   Çetin Efsane Kahram Tanrı
  1      70%    55%   40%   30%    20%    10%     5%     5%
  2      75%    60%   45%   35%    25%    15%     5%     5%
  3      80%    65%   50%   40%    30%    20%    10%     5%
  4      85%    70%   55%   45%    35%    25%    15%     5%
  5      90%    75%   60%   50%    40%    30%    20%    10%
  6      95%    80%   65%   55%    45%    35%    25%    15%
  8      95%    90%   75%   65%    55%    45%    35%    25%
 10      95%    95%   85%   75%    65%    55%    45%    35%
 12      95%    95%   95%   85%    75%    65%    55%    45%
 14      95%    95%   95%   95%    85%    75%    65%    55%
```
(Generated by script. Recompute when tuning.)

**Authoring guidance by chapter:** Ch1 mostly Kolay and Orta. Ch2–3 mostly Orta and Zor. Ch4 mostly Zor and Çetin. Ch5 Çetin and up, with the one or two Tanrısal checks saved for Atakule.

### 4.4 Check types

**White checks (Beyaz).** Retryable.
- On failure the option locks. It **reopens** when the skill's effective value rises above what it was at the failed attempt (level-up, item, thought), or when a new labeled modifier for that check becomes available (new knowledge).
- C# stores, per `check_id`, the state and the skill value at the time of failure.
- In Ink, use sticky choices (`+`) gated on `beyaz_acik(check_id)`.

**Red checks (Kırmızı).** One shot, a moment that passes.
- The failure is permanent and is a *story branch*, not a penalty screen.
- In Ink, use once-only choices (`*`).
- **Rule:** never gate required progress on a red check unless its failure branch also progresses.

**Passive checks (Pasif).** No roll; the player doesn't choose them.
- Pass if `effective skill + PASIF_TABAN ≥ threshold`.
- These are the skills interrupting: an extra line, an extra option, a clue.
- Effective skill needed: Orta ≥ 4, Zor ≥ 6, Çetin ≥ 8, Efsanevi ≥ 10.
- Passive *failure* is invisible by default. Exception: when a *different* skill notices that one missed (see 4.7).

**Criticals.** `skill_check` returns **2** (natural 20), **1** (success), **0** (fail) or **−1** (natural 1). Writers may give crits bonus content but don't have to. `> 0` means success.

### 4.5 Modifiers
All modifiers show up in the check panel as labeled lines, the way Disco does it.

| Source | Range | How |
|---|---|---|
| **Bilgi** (knowledge, from Ink flags) | +1 to +3 | Ink calls `check_mod(check_id, n, "label")` before `skill_check`. Example: *"+2: Kurbanın Derinlik dinleyicisi olduğunu biliyorsun."* |
| **Donanım** (equipment: clothes, tools) | −2 to +2 per item | C#, from item ScriptableObjects. Applies to effective skill. |
| **Dosya Kararı** (internalized thoughts) | −3 to +3 | C#, from thought ScriptableObjects. Applies to effective skill. |
| **İnceleme** (thought under research) | −2 to +1 | Same, while the thought is researching. |
| **Fraksiyon** | +1 | When affinity with the relevant faction is ≥ İçeriden (+5) and the check concerns them. Ink calls `check_mod`. |
| **Durum** (condition) | −1 | Can ≤ 1: −1 to BEDEN and DUYU checks. Benlik ≤ 1: −1 to ZİHİN and RUH checks. C#. |
| **Destek Protokolü** | +1 + Evre | Player-activated (see §7.4). Costs 1 Benlik. Evre ≥ 1 only. |

There is no cap on stacked modifiers, but writers should not stack more than about +4 from Bilgi on a single check **[PH]**.

### 4.6 Failure is content: the failure menu
Every check spec, and every Ink check, must pick at least one of these for failure:

1. **Another path.** A different skill or NPC gets you there slower or at a cost.
2. **Misread.** You get a wrong clue, flagged (`yanlis_<id>`) so a later Mantık or Göz check can expose it.
3. **Cost.** Can or Benlik damage, or affinity loss.
4. **The machine helps.** `uyanis +1` (mostly for Kod and Rüya failures): you got it, but Denetim did it for you.
5. **Humiliation.** A funny, revealing scene. Usually Benlik −1, sometimes a thought offered (Disco's best failures turn into thoughts).
6. **The world moves.** The NPC leaves, the moment passes, time advances, a later scene changes.

A check whose only failure outcome is "nothing happens" is a bug. narrative-writer should flag any such check.

### 4.7 Voice conflicts (Çekişme)
When two skills disagree in a passive moment, the one with the higher effective value gets the floor (ties go to the one listed first in the call). The Ink helper is `baskin(a, b)` (§10.4). This is cheap, and it's where a lot of the game's character comes from.

---

## 5. Thought Cabinet: Dosya Dolabı (The Filing Cabinet)

### 5.1 Concept
Denetim thought in files. Your obsessions arrive as **Dosya** (case files). You file one for **İnceleme** (review). It occupies a drawer, changes how you think while it's under review, and eventually comes back stamped with a **Karar** (verdict). That verdict is a permanent change to who you are. The bureaucracy in your head is literally processing you.

### 5.2 Rules
- **Offered:** dialogue, checks and events add a thought to `dosya_bilinen`. A notification appears: "Yeni dosya: …".
- **Filing:** the player puts a known thought into a free **çekmece** (drawer). It moves to `dosya_incelemede`.
- **Drawers:** **3 at the start** and **8 maximum** **[PH]**. A new drawer costs **1 Yetki** (a skill point), which competes with raising skills.
- **Review time:** each thought has an `inceleme_saat` (game hours, **2 to 10 [PH]**). Time advances by `DAKIKA_PER_SECIM` (1 min) per dialogue choice, by travel (10 to 30 min), and by sleep or waiting.
- **During review:** an **İnceleme etkisi** applies (usually a small penalty, sometimes a bonus).
- **Verdict:** at the end of review C# moves the thought into `dosya_karar`. Its **Karar etkisi** applies permanently, and the drawer stays occupied.
- **Arşivle (forget):** remove a decided thought to free its drawer. Costs **1 Yetki** and the effect is lost. The Unutanlar "Silme" rite can also do this for free (§6.4).
- **Doktrin:** each faction has one capstone thought, its Doktrin. **Only one Doktrin can be decided at a time.** Arguments are exclusive, and the decided Doktrin drives which endings are open (§9.3).
- **Abandon review:** allowed, no cost, progress lost.

### 5.3 Example thoughts (all numbers [PH])

| # | Dosya (Ink id) | Offered when | İnceleme (hours / effect) | Karar (permanent) |
|---|---|---|---|---|
| 1 | **Kimin Hatırası Bu?** *(Whose Memory Is This?)* (`kimin_hatirasi`) | The first Ödünç Anı in Ch1. | 4h / İrade −1 | Hafıza +1, İrade −1. Unlocks "Ödünç Anı" dialogue options: you can *tell* people a dead person's memory. Unutanlar −1 when they hear about it. |
| 2 | **Son Memur** *(The Last Civil Servant)* (`son_memur`) | Showing your badge and being laughed at. | 3h / Ses −1 | Ses +1, Gölge +1 when invoking authority. +1 Bilgi on any check against someone who still respects the old state. Kıyametçiler −1 on Karar. A cop with no state, playing the state. |
| 3 | **Erlik'in Kâtibi** *(Erlik's Scribe)* (`erlik_katibi`) **DOKTRİN: Kıyametçiler** | Kıyametçiler ≥ +8 and the Kale tribunal scene. | 8h / Vicdan −2 | Vicdan +2 and gets a new passive: it names each NPC's **günah** (sin). Ses −1 (you can't stop accusing). Unlocks the "Yargı" dialogue option. Opens the **Yargı** ending. |
| 4 | **Tünel Duası** *(Tunnel Prayer)* (`tunel_duasi`) | Sleeping in Derinlik territory. | 5h / Mantık −1 | Rüya +2 underground. Mantık −1. DENETİM's lines are re-voiced in liturgical register (the writer has alternate lines). Benlik +1 per night spent underground. |
| 5 | **Doğru Kurulum** *(Correct Installation)* (`dogru_kurulum`) **DOKTRİN: Mühendisler** | Mühendisler ≥ +8 and the Çankaya server-room scene. | 10h / İrade −2 | Kod +2, Vicdan −2. Destek Protokolü costs 0 Benlik once per chapter. Opens the **Yeniden Kurulum** ending. |
| 6 | **Boş Sayfa** *(Blank Page)* (`bos_sayfa`) **DOKTRİN: Unutanlar** | Unutanlar ≥ +8 and undergoing one Silme rite. | 6h / Hafıza −1 | Benlik max +2, Hafıza −2. Every second Uyanış gain is cancelled (C# tracks the parity). Opens the **Unutuş** ending. |
| 7 | **Ankara Bir Bozkır Kasabasıdır** *(Ankara Is a Steppe Town)* (`bozkir_kasabasi`) | A Kent passive on the Kale walls in Ch2. | 3h / none | Kent +1. Outdoor Kent passives also reveal a shortcut or hidden route. Benlik +1 on first arrival at each new outdoor location. *Ankara was built from nothing, as a capital, on purpose. It can be built from nothing again. Or it can go back to being nothing.* |
| 8 | **Çay Ocağı Meclisi** *(The Tea-House Parliament)* (`cay_ocagi`) | Drinking 3 çay with 3 different NPCs. | 2h / İştah +1 | Çay heals 2 Benlik instead of 1. +1 Bilgi on Ses checks made while sharing a drink. Every çay costs 15 extra minutes. *The republic survives where men sit and argue over tea.* |

Remaining Doktrin thoughts to spec: Derinlik (`dinleyen_tanri`, "The God Who Listens") and Yankılar (`koro`, "The Choir"). See the outline in §6.4. The full list goes in `docs/design/thought_cabinet.md`.

---

## 6. Factions: affinity as argument

### 6.1 Variables and range
- `affinity_derinlik`, `affinity_kiyametciler`, `affinity_muhendisler`, `affinity_unutanlar`, `affinity_yankilar`: integers, **−10 to +10**, start at **0** **[PH]**.
- **Always change them through the Ink function `affinity(fraksiyon, delta)`**, never with `~ affinity_x += n` directly. The function clamps, applies opposition and gates (below), and fires the UI notification.
- **Delta guidance:** ±1 minor (an agreeable remark), ±2 meaningful (a favor, siding in an argument), ±3 major (betrayal, a quest resolved for them). At most two ±3 events per faction per chapter.

### 6.2 Tiers

| Tier | Range | General effect |
|---|---|---|
| **Düşman** (Hostile) | −10 to −6 | Their territory turns hostile: red checks to pass through, NPCs refuse you, they may hunt you in later chapters. |
| **Soğuk** (Cold) | −5 to −2 | Short answers. Their thoughts are not offered. |
| **Yabancı** (Stranger) | −1 to +1 | Default. |
| **Yakın** (Close) | +2 to +4 | Their **ordinary thoughts** are offered. Their rhetoric shows up in your options. |
| **İçeriden** (Insider) | +5 to +7 | Unique dialogue options. +1 Fraksiyon modifier on checks about them. A faction passive (below). |
| **İnanan** (Believer) | +8 to +10 | Their **Doktrin** can be offered (it also needs its story event). |

### 6.3 Opposition and gates
- **Opposed pairs:** Derinlik ↔ Kıyametçiler (worship the god vs. judge it), and Mühendisler ↔ Unutanlar (restore the past vs. erase it). When a faction gains **≥ 2 in one call**, its opposite loses **1**. You can't hold contradictory beliefs for free.
- **Yankılar** has no opposite. It is gated by the implant instead: **Yankılar can't rise above `2 + 2 × Evre`.** You can't be close to the Echoes while you're still mostly human.
- **Unutanlar** don't trust deep implants: **at Evre ≥ 3 their affinity is capped at +5** unless you have had at least one Silme rite.

### 6.4 Per-faction effects

**Derinlik (The Depth): "Denetim is god."** Home turf: the metro (Ulus, Sıhhiye, Kızılay stations, the M1 and Ankaray tunnels).
- **Düşman:** Tunnel travel requires red İçgüdü or Gölge checks. Derinlik "listeners" report your movements, and Rüya passives turn hostile (nightmares cost Benlik).
- **Yakın:** Thoughts offered include `tunel_duasi`. You can understand their liturgy: Rüya can read DENETİM lines as scripture.
- **İçeriden:** Tunnel shortcuts between chapter hubs. Sermons heal 2 Benlik once per day. The Derinlik passive: *at Evre ≥ 2 they treat you as a living relic, and Ses checks with believers get +1.*
- **Doktrin `dinleyen_tanri` [PH]:** Rüya +2, Mantık −2. DENETİM is re-voiced as a god throughout. Opens the **İbadet** ending.

**Kıyametçiler (End-Timers): "Denetim is Erlik Han. Finish the judgment."** On the surface. Proposed: they hold the Kale gates and run a tribunal there **(öneri)**.
- **Düşman:** Ambush scenes (İçgüdü/Kuvvet red checks). Your sins get read out in public (Benlik).
- **Yakın:** Erlik and Tamag myth content is offered. Rüya and Vicdan gain a "judgment" register.
- **İçeriden:** The **Yargı** option. In marked scenes you can pass a verdict on an NPC, which ends a conflict instantly and brutally. The Kıyametçi passive: *Vicdan notices guilt at one tier lower difficulty.*
- **Doktrin `erlik_katibi`:** see §5.3. Opens the **Yargı** ending.

**Mühendisler (The Engineers): "Denetim was right. Restart it correctly."** Proposed home turf: Çankaya, the server halls, Tunalı workshops **(öneri)**.
- **Düşman:** Terminals in their zones are locked, and they mark you as a "corrupted node". Kod checks in Çankaya get −1.
- **Yakın:** Technical thoughts are offered, and they will identify implant parts for you.
- **İçeriden:** **Yama** (patch): they can install patches that raise one skill by +1 *and* add `uyanis +1`. Not offered more than once per chapter. The Mühendis passive: *Kod checks on Denetim hardware get +1.*
- **Doktrin `dogru_kurulum`:** see §5.3. Opens the **Yeniden Kurulum** ending.

**Unutanlar (The Forgetting Ones): "Denetim is the past. The past is gone."** They have removed their own memories, surgically and chemically. They live only in the present. Proposed: camps in the Opera/Gençlik Parkı ruins between Ulus and Sıhhiye **(öneri)**.
- **Düşman:** They don't remember you were ever kind. Literally: positive history with individual Unutan NPCs resets.
- **Yakın:** Present-tense thoughts are offered. Hafıza passives with Unutan NPCs are muted.
- **İçeriden:** **Silme** (the erasure rite). **This is the only way to lower Uyanış.** Each rite gives `uyanis −2`, heals Benlik to full, can archive one decided thought for free, and costs **Hafıza −1 permanently** (minimum 1). The Unutan passive: *Benlik damage from Hafıza scenes is −1.*
- **Doktrin `bos_sayfa`:** see §5.3. Opens the **Unutuş** ending.

**Yankılar (The Echoes): "We are already part of it."** Humans partly merged with the network. They show up anywhere, and they can speak *through* other people.
- **Düşman:** Echoes jam the implant: Kod and Rüya get −1 in their presence, and NPCs you trust occasionally say things that aren't theirs.
- **Yakın (needs Evre ≥ 0, cap 2):** Echo whispers become optional "voices" in dialogue (`# voice: yanki`).
- **İçeriden (needs Evre ≥ 2):** **Paylaşım** (sharing). The Echoes can give you Ödünç Anı from *living* people, and a Hafıza check can then replay another person's perspective on an event. This is a strong investigative tool and it's ethically ugly. The Yankı passive: *you can hear the broadcast one Evre "earlier" than your actual Evre for decoding purposes.*
- **Doktrin `koro` [PH] (needs Evre ≥ 3):** One skill of your choice is permanently re-voiced as the Choir, gets +2, and stops ever being "you" (İrade can no longer veto it). Opens the **Koro** ending.

---

## 7. The implant: Uyanış (Awakening)

### 7.1 Principle
**Progression is the implant waking up.** XP is called **Veri** (data). The implant "levels" by collecting data about you and the city. The skill points it gives you are called **Yetki** (authorization). Each level is Denetim granting you clearance. That's the joke, the horror, and (in the endgame) the plot: enough Yetki is what lets you answer the broadcast.

### 7.2 Variables
- **Veri:** XP, tracked in C# (`StatBlock`). Granted from Ink via `grant_veri(n)`.
- **`uyanis`:** an Ink VAR, integer ≥ 0. Raised by accepted levels, story events, Kod failures, Destek uses and patches. Lowered only by Silme.
- **`uyanis_evre()`:** an Ink function that returns the stage, 0 to 4.
- **`bastirma`:** an Ink VAR counting suppressed level-ups.
- **`denetim_yardim`:** an Ink VAR counting Destek Protokolü uses.

### 7.3 Level-up: accept or suppress
Every **100 Veri** **[PH]**, the implant offers a level (a DENETİM-voiced prompt at Evre ≥ 1, a bare system prompt at Evre 0):
- **Kabul (Accept):** +1 Yetki (a skill point) and `uyanis +1`.
- **Bastır (Suppress):** no Yetki. Heal 1 Benlik, `bastirma +1`. Kept Veri is lost. At `bastirma ≥ 3` Unutanlar treat you as kin (+2 the first time, applied in a Ch2 or Ch3 scene). At `bastirma ≥ 6` İrade gets +1.

**Veri sources [PH]:** a main task step 30 to 50, a side task 15 to 25, a discovery 5 to 10, a decided thought 0 to 20. **Checks give no Veri**, so failing costs you nothing in progression. The target total is about **2,200 Veri, roughly 22 level-up offers over the game.**

**Yetki spending:** +1 to a skill (up to its cap), or +1 drawer, or archive a thought.

### 7.4 Destek Protokolü (Support Protocol)
At **Evre ≥ 1**, a button on any **white or red** check panel: *"DENETİM'e danış"* (ask Denetim).
- **+(1 + Evre)** to this check.
- **Costs 1 Benlik** and adds `denetim_yardim +1`. **Every 3rd use gives `uyanis +1`.**
- DENETİM remembers. From Evre 3 its Teklif lines reference how often you have asked.

### 7.5 Stages (Evreler)

| Evre | `uyanis` | Name | Unlocks | Costs |
|---|---|---|---|---|
| 0 | 0–1 | **Uyku** (Sleep) | Skills only. | None. Destek is unavailable. |
| 1 | 2–5 | **Kıpırtı** (Stirring) | Kod can read Denetim glyphs. Destek available. DENETİM's first word. Skill caps +1. | None yet. Yankılar cap rises to 4. |
| 2 | 6–10 | **Fısıltı** (Whisper) | **Broadcast fragments decoded (1/3).** Derinlik treat you as a relic. Yankılar İçeriden possible. Caps +2. | Benlik max −1. The first time you meet Unutanlar at Evre 2+: −2 (they can tell). |
| 3 | 11–16 | **Bağlantı** (Link) | Interface with terminals bare-handed (no items). **Broadcast decoded (2/3).** DENETİM Teklif. Caps +3. | Benlik max −2. Unutanlar capped at +5 without Silme. |
| 4 | 17+ | **Senkron** (Sync) | **Full broadcast decoded.** DENETİM can speak in place of skills. The Koro ending is possible. Caps +4. | Benlik max −3. Some İrade vetoes stop working (the writer marks these). |

**Mandatory story bumps [PH]:** Ch1 touching the body's implant socket +1, Ch3 the market implant scene +1, Ch4 entering the Çankaya core +2. **Minimum by Ch5: `uyanis` 4 (Evre 1).** If the player accepts everything, they reach about 30 (Evre 4) during Ch4.

### 7.6 The human route
The mystery **must be solvable at low Evre.** Every fact gated behind "broadcast decoding" has a slower human alternative: paper records in the Anadolu Medeniyetleri Müzesi archives (Hafıza/Mantık), Unutan oral testimony from before their erasure (recorded on cassette, Göz/El to play it), and the partner's notebook. The human route costs more time and more checks and gives fewer ending options (§9.3). It is never blocked.

### 7.7 Kurtarma (DENETİM saves you)
When **Can reaches 0** at **Evre ≥ 2**, DENETİM offers once per chapter: *"YAŞAMAK İSTİYOR MUSUN, MEMUR?"*
- **Accept:** Can = 1, `uyanis +2`.
- **Refuse:** the death ending.

At Evre 0–1 there is no offer, and Can 0 is death.

---

## 8. Condition tracks and failure states

### 8.1 Can (Health)
- An Ink VAR, `can`. The maximum, `can_max = Dayanım + 2`, is computed by C# and written into Ink.
- **Damage sources:** failed physical red checks (1 to 2), violence (2 to 3), poison and cold (1), Kuvvet backfires.
- **Healing:** Simit +1, Ankara tava +2 **[PH]**, Ağrı kesici +1 (plus Dayanım +1 for 1 hour), sleep (full).
- **At 0:** Kurtarma (§7.7) if eligible, otherwise **Son: Tamag'a İniş**, the death ending. It's a written ending, not a bare game-over screen.

### 8.2 Benlik (Self) is the morale track, and it's about identity
- An Ink VAR, `benlik`. The maximum is `benlik_max = İrade + 2 − evre_cezasi` (0/0/1/2/3 by Evre) with a **minimum of 2**. C# computes it and writes it into Ink.
- **Benlik is how much of you is still you.** Damage sources: humiliation (1), horror (1 to 2), grief from Hafıza scenes (1), Destek Protokolü (1), DENETİM Teklif refusals or acceptances (they vary), and failed Kent or Rüya checks (1).
- **Healing:** çay +1 (2 with `cay_ocagi`), sigara +1 (İştah may demand another), sleep (full), Derinlik sermons, Silme (full), a kind word from the partner **[PH]**.
- **At 0: Son: Teslim** (Surrender). The machine stands up in your body and walks it toward Çankaya. It's a written ending and **can't be prevented by Kurtarma**, which is DENETİM's offer and not İrade's.

### 8.3 Fail states and saving
- **Game-ending:** Can 0 (unless Kurtarma) and Benlik 0. Both are authored endings with ending slides.
- **Soft fails** are content: a missed red check, a preventable death that happens (Ch3), a faction turning Düşman.
- **Saving:** autosave at the start of every knot that carries a `# location:` tag, plus manual save anywhere outside dialogue. Ink state is serialized with `story.state.ToJson()`, and C# state (stats, inventory, Veri, thought timers, white-check memory) goes alongside it.
- **Optional "Kalıcı" mode [PH]:** one save, no reload. Decision deferred.

---

## 9. Chapter structure and the mystery

### 9.1 The spine (öneri: the whole mystery is a proposal for Hasan, see Q2/Q3)
- **The case:** a Derinlik "dinleyici" (listener) is found dead in the M1 tunnel under **Ulus**. The back of his skull is opened and his old-world implant is gone. He is the first of the **Taşıyıcılar** (Carriers): the few people alive with working Denetim implants. You are one of them, and you didn't know it until you touched his skull.
- **The pattern:** the Carriers are being killed one by one. Each killing coincides with a change in the broadcast from Atakule. Someone is collecting implants, or destroying them.
- **The broadcast** (proposed reveal): Denetim has been asking **one question** for a hundred years and waiting for an *authorized* human to answer it. Every authority died in the Yükseliş or after it. The implants are the last valid credentials, and **Yetki is literal**. The detective is becoming one of the last people the machine will listen to.
- **The question** (proposed): *"Devam edeyim mi?"* ("Shall I continue?"). Ankara is hell because a machine is waiting for a yes or a no. (Alternatives are in Q3.)
- **The killer ("Hasatçı", the Harvester) [PH]:** see Q2 for the options. My recommendation is that the killer is an Unutan who kept one memory, the one that tells them what the question is. They kill Carriers so that *no one can ever answer*, because both answers horrify them. It's sympathetic and it turns the gentlest faction's argument into the darkest act.

### 9.2 Chapters
Real Ankara geography, running north to south: from the old town toward the seat of power. Filenames follow the CLAUDE.md pattern (`ch02_kalesi.ink`). **Total target: 15 to 20 hours [PH].**

| Ch | File | Location | Days | Length | Factions tested |
|---|---|---|---|---|---|
| 0–1 | `ch01_opening.ink` | **Metro:** Ulus station, the M1 tunnel toward Sıhhiye | Day 1 | 2–3h | Derinlik, Unutanlar |
| 2 | `ch02_kalesi.ink` | **Ankara Kalesi:** walls, Akkale, Alaeddin Camii, Anadolu Medeniyetleri Müzesi, the Samanpazarı slopes | Day 2 | 3–4h | Kıyametçiler, Yankılar |
| 3 | `ch03_kizilay.ink` | **Kızılay:** Güvenpark, the Meydan, Sakarya Caddesi, Yüksel Caddesi, Atatürk Bulvarı, Bakanlıklar | Days 3–4 | 5–7h (the open hub) | All five, mainly Mühendisler and Derinlik |
| 4 | `ch04_cankaya.ink` | **Çankaya:** Tunalı Hilmi, Kuğulu Park, Kavaklıdere, the Köşk server halls | Day 5 | 3–4h | Mühendisler, Yankılar, the killer's faction |
| 5 | `ch05_atakule.ink` | **Atakule:** the shaft, the revolving restaurant, the antenna | Day 6 (night) | 1–2h | The decided Doktrin |

**Ch1, Metro, "Uyanış."** Tutorial, tight scope.
- Beats: you wake on duty in the tunnel, at the body. Touching the socket gives the first Ödünç Anı and `uyanis +1`. Derinlik want the body for a rite and Unutanlar want it burned. You leave by climbing out at Ulus.
- Checks: 6 to 8 total. **Required:** Göz Kolay (the socket), Mantık Orta (time of death). Failure on either gives you the same clue later at a cost (Benlik, or a Derinlik favor owed). **Optional:** Kod Orta (the glyph on the wall, a broadcast fragment), Rüya Zor (the body "speaks"), Ses Orta (stop a crowd), İştah Kolay (the dead man's cigarettes).
- Teaches: white vs. red, passives, the first thought (`kimin_hatirasi`), Can/Benlik, the first level-up choice.

**Ch2, Ankara Kalesi, "Seyir"** (Overview).
- Beats: the second Carrier lived on the Kale. From the walls you see the whole ruined city. Kent and Göz map Atakule's light pulses against the dates of the killings. The museum archive holds the human-route records. The Kıyametçi tribunal judges a thief and asks you to testify.
- Checks: about 12. **Required:** one of Kent Orta / Göz Zor / Mantık Zor (the pulse pattern). Three paths, and at least one always passes eventually because they're white checks. **Red:** your testimony at the tribunal (Ses or Vicdan, Zor). Failure means the thief is executed, which gives a Kıyametçi thought and Benlik −2.
- The chapter ends when the Atakule light pulses as you watch, and someone in Kızılay dies.

**Ch3, Kızılay, "Pazar"** (Market). The Martinaise-style open middle.
- Beats: 4 to 5 sub-areas, every faction present, a market in salvaged implants. Suspects from each faction. **The third Carrier is alive and can be saved:** a chain of 2 red checks on the night of Day 3. If saved, they become a witness. If they die, the corpse yields different evidence through Hafıza/Ödünç Anı. You learn "Yetki" is literal, either from the Mühendisler (Evre ≥ 2) or from the museum records (the human route).
- Checks: about 35. Required progress always has at least two skill routes.
- Mid-game gate: identifying where the killer will go next (Çankaya).

**Ch4, Çankaya, "Çekirdek"** (Core).
- Beats: the servers in the Köşk. You confront the killer. You learn the question, decoded at Evre 4 or reconstructed through the human route. Entering the core gives `uyanis +2`. Doktrin events land here or earlier.
- Checks: about 15, mostly Zor and Çetin. Confronting the killer is a multi-stage conversation in which each faction's argument can be voiced if you're İçeriden with that faction.

**Ch5, Atakule, "Cevap"** (Answer).
- Beats: the climb, the antenna, the answer. Short, dense, mostly a choice rather than checks. The 1 to 2 Tanrısal checks offer *extra* options, never the only one.

### 9.3 Endings (high level)
Two endings are **always** available. Others need a Doktrin, an Evre or a flag. Each ending is followed by slides per faction and per major NPC, driven by affinity and flags.

| Ending | Requirement | What happens |
|---|---|---|
| **Kapat** (Shut down): answer "no" | Always | Denetim stops. The Kale's water pumps and the metro's air fans stop too. Ankara becomes only a city again, and then the winter comes. |
| **Devam** (Continue): answer "yes" | Always | Denetim keeps going, now with a human mandate it never had. Nothing changes, and now it's your fault. |
| **Yeniden Kurulum** (Reinstall) | Doktrin `dogru_kurulum` and Evre ≥ 3 | Your Yetki restarts Denetim "correctly". The epilogue is ambiguous about whether it was. |
| **Yargı** (Judgment) | Doktrin `erlik_katibi` | You destroy Atakule. The question is never answered. Erlik's silence. |
| **Unutuş** (Oblivion) | Doktrin `bos_sayfa` | You burn out your own implant. No one is left to answer, and you forget why that mattered. |
| **İbadet** (Worship) | Doktrin `dinleyen_tanri` | You don't answer. You *interpret*. You become the voice that tells Derinlik what the god meant. |
| **Koro** (Choir) | Doktrin `koro` and Evre 4 | You merge. The broadcast changes for the first time in a hundred years. It now has your voice. |
| **Tamag'a İniş** (Descent) | Can 0 | Death. |
| **Teslim** (Surrender) | Benlik 0 | Denetim walks your body home. |

---

## 10. Ink/Unity integration contract

This is the source of truth for names. Neither side renames anything without updating this section.

### 10.1 Naming rules
- **Ink identifiers (VARs, CONSTs, LIST items, knots, functions) are ASCII snake_case.** No diacritics in identifiers, because they are fragile across inklecate versions and C# string keys. Diacritics are required in all **displayed text**.
- Skill ids: `mantik hafiza kod ses onsezi ruya vicdan irade dayanim kuvvet istah icgudu goz el golge kent`.
- Attribute ids: `zihin ruh beden duyu`.
- Faction ids: `derinlik kiyametciler muhendisler unutanlar yankilar`.
- `check_id` format: `<chapter>_<scene>_<short>`, for example `ch01_tunel_soket`. It must be globally unique, because C# stores white-check state by it.

### 10.2 Who owns what

| Data | Lives in | Written by | Read by |
|---|---|---|---|
| Faction affinity, `uyanis`, `bastirma`, `denetim_yardim`, `can`, `benlik`, `zaman`, story flags, known/decided thoughts, `doktrin` | **Ink** (`systems/variables.ink`) | Ink. C# writes `can`/`benlik` (items, sleep), `uyanis` (level-up), and the thought lists (research finished). | Both |
| `can_max`, `benlik_max` | **Ink** VAR, *derived* | **C# only**, on any stat change | Ink |
| Attributes, skills, caps, Veri, Yetki, inventory, thought research timers, white-check memory | **C#** (`StatBlock`, `SkillSystem`, `CheckResolver`, inventory, `ThoughtCabinet`) and ScriptableObjects | C# | Ink, through EXTERNALs |
| Check thresholds and tunable CONSTs | **Ink** (`systems/checks.ink`) | game-designer | Ink. C# reads the resolved number from choice tags. |

### 10.3 Global VARs (`Assets/Ink/systems/variables.ink`)
```ink
// Factions: change only through affinity()
VAR affinity_derinlik = 0
VAR affinity_kiyametciler = 0
VAR affinity_muhendisler = 0
VAR affinity_unutanlar = 0
VAR affinity_yankilar = 0

// Implant
VAR uyanis = 0
VAR bastirma = 0
VAR denetim_yardim = 0

// Condition. C# writes the *_max values, Ink clamps against them
VAR can = 4
VAR can_max = 4
VAR benlik = 4
VAR benlik_max = 4

// Time: minutes since Day 1, 06:00
VAR zaman = 0

// Factions and doctrine
LIST Fraksiyon = derinlik, kiyametciler, muhendisler, unutanlar, yankilar
VAR doktrin = ()

// Thought Cabinet. Full LIST in systems/thoughts.ink
LIST Dosya = kimin_hatirasi, son_memur, erlik_katibi, tunel_duasi, dogru_kurulum, bos_sayfa, bozkir_kasabasi, cay_ocagi, dinleyen_tanri, koro
VAR dosya_bilinen = ()
VAR dosya_incelemede = ()   // written by C#
VAR dosya_karar = ()        // written by C#

LIST Durum = CAN, BENLIK
```
Story flags (`ch01_soket_goruldu`, `yanlis_<id>`, …) belong to narrative-writer and live in `variables.ink` too, prefixed by chapter.

### 10.4 CONSTs and Ink helper functions (`Assets/Ink/systems/checks.ink`; numbers owned by game-designer)
```ink
CONST ONEMSIZ = 8
CONST KOLAY = 11
CONST ORTA = 14
CONST ZOR = 16
CONST CETIN = 18
CONST EFSANEVI = 20
CONST KAHRAMANCA = 22
CONST TANRISAL = 24
CONST PASIF_TABAN = 10
CONST TASMA_ESIGI = 10
CONST DAKIKA_PER_SECIM = 1

// Helpers that narrative-writer calls (implemented in Ink, not externals):
// pasif(skill, dc)        -> bool   get_skill(skill) + PASIF_TABAN >= dc
// tasma(skill)            -> bool   get_skill(skill) >= TASMA_ESIGI
// beyaz_acik(check_id)    -> bool   white_check_state(id) == 0 or == 3
// baskin(skill_a, skill_b)-> string the skill with the higher get_skill (tie: a)
// uyanis_evre()           -> int    0..4 using thresholds 2/6/11/17
// affinity(fraksiyon, delta)        clamp to -10..10, opposition, Yankılar/Unutanlar caps
// sure(dakika)                      zaman += dakika
// Tunnel, because damage can end the game:
// -> hasar(Durum.CAN, n) ->         apply damage, divert to Kurtarma/ending at 0
// -> iyiles(Durum.BENLIK, n) ->     heal, clamp to max
```
Damage **must** go through the `hasar` tunnel. Ink functions can't divert, and Can or Benlik reaching 0 has to divert.

### 10.5 EXTERNAL functions (bind in `InkManager.cs` before the first `Continue()`)
Every external also gets an **Ink fallback function** with the same name in `checks.ink`, so files compile and play in inklecate/Inky without Unity. Enable `story.allowExternalFunctionFallbacks = true` in editor builds only.

| EXTERNAL | Signature (Ink) | Returns | Purpose | Ink fallback |
|---|---|---|---|---|
| `skill_check` | `skill_check(skill, dc, check_id, is_red)` (string, int, string, bool) | int: 2 crit success, 1 success, 0 fail, −1 crit fail | Rolls d20 (`CheckResolver`), adds the effective skill, labeled modifiers and Destek, shows the check panel, records white-check state. Clears this check's pending `check_mod`s afterward. | `RANDOM(1,20) + 3 >= dc` with the nat 1/20 rule |
| `check_mod` | `check_mod(check_id, amount, label)` (string, int, string) | void | Registers a labeled situational modifier (Bilgi, Fraksiyon) for the next `skill_check` with this id, so the UI can show "+2: …". | no-op |
| `get_skill` | `get_skill(skill)` (string) | int | Effective skill value (base + items + thoughts + condition). No check-specific modifiers. | `3` |
| `get_attribute` | `get_attribute(attr)` (string) | int | Attribute value. Rarely needed (character-creation reactions). | `3` |
| `white_check_state` | `white_check_state(check_id)` (string) | int: 0 untried, 1 passed, 2 failed and locked, 3 failed and reopened | Drives white-check visibility. | `0` |
| `grant_veri` | `grant_veri(amount)` (int) | void | Adds XP. C# queues the level-up prompt (Kabul/Bastır) for the next safe moment, outside a choice. | no-op |
| `has_item` | `has_item(item_id)` (string) | bool | Inventory query. | `false` |
| `give_item` | `give_item(item_id)` (string) | void | Adds to inventory and shows a notification. | no-op |
| `take_item` | `take_item(item_id)` (string) | bool | Removes the item. Returns false if it was missing. | `false` |

That's nine externals in total. **Rule: use an EXTERNAL only when Ink needs a return value or a guaranteed side effect. Presentation (sound, portraits, music, camera) uses tags.**

### 10.6 Tags

| Tag | Where | Meaning |
|---|---|---|
| `# speaker: <npc_id>` | line | An NPC is speaking. Its id comes from `docs/characters.md`. |
| `# voice: <skill_id>` | line | A skill is speaking (`# voice: mantik`). The UI colors it by attribute. |
| `# voice: denetim` / `# voice: yanki` / `# voice: irade` | line | DENETİM, an Echo, or İrade (İrade uses the normal skill styling, but the id is reserved). |
| `# portrait: <asset_id>` | line | Resolves to `Resources/Portraits/<asset_id>`. Falls back to a placeholder plus a warning if missing. |
| `# check: <skill> <dc> <white\|red> <check_id>` | **choice** | Check metadata for the choice button: skill, number, color, % chance. Write it with a dynamic tag, `# check: mantik {ORTA} white ch01_tunel_saat`. Put the tag **inside the `[ ]`** so it's a choice tag (ink ≥ 1.1). unity-dev should verify this against the installed ink version. |
| `# location: <loc_id>` | line | Scene or background change. Also triggers an autosave. |
| `# sfx: <id>`, `# music: <id>`, `# ambience: <id>` | line | Audio. |
| `# glitch: <0-3>` | line | Kod/DENETİM corruption intensity for the text renderer. |
| `# clear` | line | Clears the dialogue log (chapter breaks, hard cuts). |

### 10.7 Example: the canonical check pattern
```ink
=== tunel_govde ===
{ pasif("goz", ORTA):
    Kafatasının arkasında, saç çizgisinin hemen altında, düzgün bir delik. # voice: goz
}
+ { beyaz_acik("ch01_tunel_saat") } [MANTIK — Orta: Ne zamandır burada? # check: mantik {ORTA} white ch01_tunel_saat]
    { ch01_kan_kurumus:
        ~ check_mod("ch01_tunel_saat", 1, "Kanın kuruduğunu fark ettin")
    }
    { skill_check("mantik", ORTA, "ch01_tunel_saat", false) > 0:
        -> saat_basari
      - else:
        -> saat_basarisiz   // failure is content: a wrong estimate flagged as yanlis_saat
    }
* [İÇGÜDÜ — Zor: Arkandaki ses. # check: icgudu {ZOR} red ch01_tunel_ses]
    { skill_check("icgudu", ZOR, "ch01_tunel_ses", true) > 0:
        -> ses_basari
      - else:
        -> hasar(Durum.CAN, 1) -> ses_basarisiz
    }
```
(Skill ids are always passed as strings, to externals and to the `pasif`/`tasma`/`baskin` helpers alike. The snippet shows intent and hasn't been compiled. Final, inklecate-verified syntax goes in `docs/design/checks.md`.)

---

## 11. Content scale (for planning) [PH]
- About 80 to 100 checks in total, roughly 70% white, 20% red and 10% passive-only.
- 10 Doktrin and ordinary thoughts at minimum, with 20 to 24 as the target.
- About 25 named NPCs, 4 to 6 per chapter plus recurring ones.
- Every skill needs at least 3 passive interjections per chapter and at least 1 Taşma line per chapter from Ch3 on.

---

## 12. Source tensions found (not silently resolved)
1. **Where the roll happens.** CLAUDE.md shows `~ temp roll = RANDOM(1,20)` in Ink. The unity-dev brief says "the roll and modifiers come from SkillSystem/CheckResolver". **Resolution in this doc:** the roll is in C# through `skill_check`, so the UI can show it and modifiers are centralized. The Ink fallback uses `RANDOM(1,20)`, so the convention still holds when testing in Inky. Hasan should confirm.
2. **"Each skill is a fragment of Denetim."** İrade is designed as *possibly not* Denetim's (unregistered, claims to be you). This is a deliberate ambiguity, not a contradiction. If Hasan wants every skill strictly Denetim's, İrade becomes "the user-simulation module" openly (Q4).
3. **Skill names in the memory note** (İçgüdü, Ses, Gölge) are used here. **"Ses" (Voice/Authority)** could be confused with "the voices" generally. The UI always shows it as a skill name, but if that's still too ambiguous the alternative is **"Hitabet"** (rhetoric).
4. **Kalıntı Dedektif and the implant's memories.** The memory note says the implant wakes with 100-year-old memories. That is implemented as Hafıza's Ödünç Anı and Taşma, *not* as Disco-style amnesia. The detective knows who he is, and he gradually stops being sure. It's unclear whether the detective himself is old-world (preserved) or a present-day man with an old implant. This doc assumes **present-day man, old implant** (Q5).
5. **The CLAUDE.md example `ch02_kalesi.ink`** puts the Kale second. This doc follows that order.
6. **"No one knows what Denetim is saying."** That stays true at the start. The reveal in §9.1 is a proposal.

---

## 13. Open questions for Hasan

**Q1. Dice: d20 (current) or 2d10?**
- *d20 (as designed):* matches CLAUDE.md, each point is a legible 5%, crits are 5% each. But the noise is high: a skill-6 specialist only beats a skill-1 novice by 25 points on an Orta check.
- *2d10:* a bell curve, so investment feels stronger. With the same thresholds, skill 6 vs. Orta is 79% and skill 1 vs. Orta is 36%. Crits (double 10 / double 1) become 1% each. In Ink it's `RANDOM(1,10) + RANDOM(1,10)`, the thresholds above still work, and only the probability table and the crit rule change.
- *My lean:* 2d10 if you want build identity to matter more; d20 if you want the convention unchanged. It's a one-function change in `CheckResolver` either way.

**Q2. Who is the Hasatçı (the killer)?**
- (a) *An Unutan who kept one memory* (recommended): sympathetic, a twist, and it turns the gentlest faction's argument into its darkest act.
- (b) *A Mühendis* collecting credentials to restart Denetim: logical, but predictable.
- (c) *A Yankı*, or the network itself acting through Echoes: eerie, but it risks making the killer a force rather than a person.
- (d) *The partner.* A strong betrayal, but it's close to a familiar trope, and it costs us the player's one external anchor.

**Q3. What is the broadcast?**
- (a) *"Devam edeyim mi?"*, a yes/no waiting for authority (recommended: it makes Yetki literal and gives a clean final choice).
- (b) A list of names: every citizen, still being counted. Haunting, but it doesn't produce a choice.
- (c) An apology: Denetim confessing, endlessly. Poignant, but it softens Denetim.
- (d) Never revealed in words: you only choose how to respond to it. Pure, but it may frustrate a mystery structure.

**Q4. İrade: ambiguous, Denetim's, or truly the detective's?**
- Ambiguous (current) gives the best late-game tension. Making it Denetim's openly is darker and simpler. Making it truly the detective's gives the player a safe anchor but loses a mystery.

**Q5. Is the detective a present-day man with an old implant, or an old-world man preserved somehow (a literal "Kalıntı")?**
- A present-day man (assumed): cleaner, and Ödünç Anı does the 100-year-memory work.
- Preserved old-world: a bigger twist, but it overlaps with Disco's amnesia structure and complicates every NPC reaction.

**Q6. A partner NPC (the Kim Kitsuragi role)?**
- Proposal: an analog-only partner with no implant who keeps a paper notebook. They're the one voice *not* in your head, they're the human route made flesh, and they heal Benlik with a word. Name, gender and faction are your call. Without a partner, the game is lonelier and the human route needs another carrier.

**Q7. The detective's institution.** Proposal **(öneri)**: he is from the **Zabıta**, the remnant municipal police of Kızılay's market council. It's an absurd, very Ankara authority with no state behind it. The alternative is a freelance "Kalıntı" with no institution at all.

**Q8. Scope.** 15 to 20 hours across 5 chapters is the target. If that's too big for the first release, the cleanest cut is **Ch1 + Ch2 + a reduced Ch3 as a vertical slice** that ends at the reveal that "Yetki is literal".

**Q9. Anıtkabir.** It's Ankara's most charged landmark. Use it (a powerful set piece, but politically sensitive), reference it only obliquely, or leave it out? I've left it out until you decide.

**Q10. Money.** Is there a currency (`para`) and shops, or only barter and favors? I lean toward **barter only** (fewer systems, more Ankara-market texture).

**Q11. Kalıcı mode** (single save, no reload): include it at launch or not?

---

## Next documents (game-designer backlog)
- `docs/design/checks.md`: full check spec and the final Ink check pattern.
- `docs/design/skills.md`: per-skill authoring sheet (passive triggers, sample lines, Taşma rules).
- `docs/design/thought_cabinet.md`: full thought list.
- `docs/design/factions.md`: the `affinity()` implementation spec and per-faction scene hooks.
- `docs/design/implant.md`: Uyanış, Destek and Kurtarma in detail.
- `docs/design/chapter_structure.md`: per-chapter location and NPC sheets.
- `docs/design/balance.md`: every tunable value and where it lives.
- A first `Assets/Ink/systems/checks.ink` with the CONSTs and fallbacks from §10.4 and §10.5.
