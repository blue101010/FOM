# TODO — état d'avancement et backlog résiduel

> **Positionnement cible** — inchangé depuis le premier backlog : **une ontologie des
> comportements de résolution CTF**, reliée aux standards existants (ATT&CK, CAPEC, CWE,
> WSTG, STIX) et **non un « ATT&CK parallèle »**. Les identifiants externes sont des
> *ancres portées par entrée*, jamais la définition d'une entrée.
>
> **Spec appliquée le 2026-08-30.** La couche **v3** est active ([`SCHEMA_V3.md`](SCHEMA_V3.md),
> [`v3/`](v3/README.md)) ; **v2 est gelée** ([`SCHEMA_V2.md`](SCHEMA_V2.md), [`v2/`](v2/README.md))
> et conservée pour la reproductibilité. Aucun identifiant, chemin ni répertoire n'a été renommé.
>
> Les propositions écartées restent en [Archive](#archive--décisions-contestées-et-différées) avec
> leur argument. Ce qui reste à faire est en [backlog résiduel](#backlog-résiduel) : c'est de la
> **collecte de preuves**, pas de l'ingénierie.

## Principe directeur (inchangé)

1. **La preuve précède le modèle.** Aucun axe n'est figé avant d'avoir été observé.
2. **Dériver plutôt qu'écrire.** Ce qui se déduit d'un ID ou d'un fichier est calculé, jamais saisi.
3. **Noyau normatif + index descriptif.** Un noyau attesté porte la crédibilité ; les 162 paires
   restent un index de repérage.
4. **Non-rupture.** `CTFTTE-*`, `CTFTCTE-*`, `CTFT-TA-*` sont des clés publiques stables.

---

## Ce qui est fait

### Phase 0 — dettes bloquantes

| # | Tâche | État | Résultat |
| --- | --- | --- | --- |
| 0.1 | Réaligner `FOR-010..014` | ✅ | Chaque `CTFTCTE-FOR-0NN` répond désormais à `CTFTTE-FOR-0NN`. Le contenu JAB orphelin a reçu sa technique : nouvelle paire **`FOR-027`**. `REVIEW_NOTES` vidé, section « Subject mismatch » disparue de `CORRELATION.md`. |
| 0.2 | Renommer les contre-techniques placeholder | ✅ | `FOR-009`, `STE-006/007/008` nommées verbe + objet et dotées d'un corps réel. Plus aucun titre `Counter — …`. |
| 0.3 | Régénérer le bundle STIX | ✅ | Nouveau `v3/render_stix.py`. **63 → 162 paires, 13 → 19 domaines**, 19 bundles par domaine. Les 203 IDs déjà publiés sont préservés (uuid5, même namespace). Double émission `mitigates` + `x_ctft_relation: "solves"`. |
| 0.4 | Unifier le vocabulaire de maturité | ✅ | `taxonomy_only → attested → typed` (+ `superseded`). **Calculée**, jamais stockée sur l'entrée. |

### Phase 1 — preuves et noyau

| # | Tâche | État | Résultat |
| --- | --- | --- | --- |
| 1.1 | `evidence.json` + schéma | ✅ machinerie | `v3/schemas/evidence.schema.json` + `v3/build_evidence.py`. 15 enregistrements semés **à partir des liens déjà présents** dans le corpus ; CTF/challenge/année extraits du chemin d'URL, rien d'inventé. |
| 1.2 | Noyau ~35 | ✅ | `v3/core.json` — 35 entrées, une par comportement de résolution récurrent, avec le concept visé. Profil, pas restructuration. |
| 1.3 | Critères de promotion | ✅ | `SCHEMA_V3.md` §8. Deux curateurs remplacés par « un curateur + deux sources publiques » (archive A-7). |
| 1.4 | Liens writeup du noyau | ⛔ **bloqué** | Voir [R1](#r1--collecter-les-writeups-du-noyau). |

### Phase 2 — axes

| # | Tâche | État | Résultat |
| --- | --- | --- | --- |
| 2.1 | `domain` dérivé | ✅ | Champ `domain` dans les schémas technique et playbook, **calculé** depuis le préfixe d'ID ; `tactic` conservé en alias `deprecated`. Coût de migration : zéro écriture. |
| 2.2 | `artifact` étendu | ✅ | Vocabulaire contrôlé de 21 valeurs, partagé mot pour mot par `technique.artifact_types` et `fingerprint.artifact_type`. Données existantes normalisées (`memory` → `memory-image`, etc.). |
| 2.3 | `format` | ✅ schéma | `jeopardy`, `attack-defense`, `wargame` — optionnel, alimenté seulement depuis un challenge cité. Aucune valeur posée sans preuve. |
| 2.4 | Tactiques de résolution | ✅ structure | `v3/tactic_map.json` en `status: "underived"` avec `items` vide, plus `v3/schemas/resolution_tactic.schema.json`. L'audit **échoue** si un objectif est assigné dans cet état. Règles d'admission écrites (SCHEMA_V3 §3.9). |

### Phase 3 — graphe et lint

| # | Tâche | État | Résultat |
| --- | --- | --- | --- |
| 3.1 | `relations.json` dérivé | ✅ | `catalog_audit.py --write-relations`. 162 arêtes `solves` dérivées du markdown + arêtes curées. Un `solves` écrit à la main est **rejeté** (une seule source par fait). |
| 3.2 | Liens inter-domaines | ✅ | 4 arêtes `related-to` dans `v3/relations.curated.json` : seccomp `PWN-005`↔`JAL-005`, contraintes `COD-005`↔`REV-005`, automatisation `COD-003`↔`GAM-001`, conteneur `JAL-003`↔`FPN-004`. |
| 3.3 | Lint sémantique | ✅ | Noms d'outils et détails d'implémentation dans les titres, titres placeholder, références pendantes, objectifs prématurés. A trouvé une vraie violation : `FOR-008` « via python script » → renommée **OpenEXR header-signature tampering**. |

### Phase 4 — évaluation et CI

| # | Tâche | État | Résultat |
| --- | --- | --- | --- |
| 4.1 | Hold-out et `precision@k` | ✅ outil | `python v3/solve.py --evaluate`. `precision@1/3/5` global et par domaine. Les jeux in-sample sont étiquetés `[IN-SAMPLE: not a baseline]` pour qu'un chiffre de mémorisation ne puisse pas être cité comme référence. `v3/holdout.json` vide → métrique indéfinie. Voir [R3](#r3--constituer-le-hold-out-et-mesurer-la-référence). |
| 4.2 | Gate CI | ✅ | `.github/workflows/ci.yml` : dérive des documents générés, intégrité + lint, validation JSON Schema, STIX inchangé, MD034, évaluation (informative). |

### Hors spec, corrigé au passage

| Correctif | Pourquoi |
| --- | --- |
| Migration **v2 → v3** complète | `v3/` est la couche active ; `v2/` porte une bannière **FROZEN** avertissant que ses scripts écrivent encore les documents générés à la racine. |
| **Pages tactiques générées** | Elles dérivaient : noms tronqués à 72 caractères, colonne ATT&CK absente des anciennes lignes. Elles sont maintenant rendues comme `CORRELATION.md`, seule la section `Description` restant éditoriale. |
| Bug de `_title()` dans l'audit | La classe de caractères couvrant le tiret ne contenait pas le tiret cadratin : **tous** les noms d'`index.json` portaient leur ID en double. |
| Empreinte de corpus au lieu d'horodatage | Un timestamp dans un document généré produit un diff à chaque exécution et rend `--check` inutilisable comme gate. |
| `fix_bare_urls.py` conscient des blocs de code | Il signalait les URLs dans les exemples JSON/shell ; MD034 ne s'y applique pas, et y insérer des chevrons casserait les exemples. |

**État après application** — `catalog_audit.py --check` = 0 :

| Mesure | Avant | Après |
| --- | --- | --- |
| Paires complètes / domaines | 161 / 19 | **162 / 19** |
| Objets STIX (paires / domaines) | 63 / 13 | **162 / 19** |
| Paires en décalage de sujet | 4 | **0** |
| Contre-techniques placeholder | 5 | **0** |
| Problèmes de lint sémantique | n/a | **0** |
| Maturité | non calculée | 155 `taxonomy_only`, 7 `typed`, 0 `attested` |
| Noyau attesté | n/a | 0 / 35 |

---

## Backlog résiduel

Tout ce qui reste dépend de **preuves collectées dans le monde réel**. La chaîne de promotion est
construite et appliquée par l'audit ; elle ne peut pas fabriquer ce qui lui manque.

### R1 — Collecter les writeups du noyau

Pour chacune des 35 entrées de `v3/core.json`, réunir **≥ 2 challenges indépendants** (CTF
distincts, pas deux writeups du même challenge). Sources : `to_categorize/`, les notes locales,
les writeups déjà liés dans les fiches.

- Ajouter le lien dans la fiche, puis `python v3/build_evidence.py --write`.
- **Aujourd'hui** : 22 fiches sur 324 portent un lien de writeup réel ; **1 seule** cite deux événements
  CTF distincts (`FOR-008`) ; **0** entrée du noyau est couverte.
- Vérification : `catalog_audit.py --check` → `coverage.core.with_two_independent_events`.

### R2 — Curer les enregistrements de preuve

Pour chaque entrée dotée de R1 : `positives`, `negatives`, `boundaries` (chaque frontière nommant
l'ID voisin), `abstraction`, `synonyms`, `external_mappings` (CWE / CAPEC / WSTG avec confiance et
justification). Passer `status` à `attested`.

- La maturité `attested` apparaît alors **automatiquement** dans `v3/catalog.json`.
- Vérification : `coverage.maturity.attested > 0`.

### R3 — Constituer le hold-out et mesurer la référence

Remplir `v3/holdout.json` avec des fingerprints **dont les writeups n'ont pas servi à la curation**,
chacun portant `expected` et `provenance`. Publier la valeur de référence **avant** toute nouvelle
modification des axes, sinon le critère d'acceptation global n'est pas mesurable.

```bash
python v3/solve.py --evaluate            # v3/holdout.json
```

### R4 — Dériver l'axe des tactiques de résolution

Une fois R1/R2 faits : étiqueter l'objectif du joueur **en texte libre** sur les writeups du noyau,
regrouper *a posteriori*, ne retenir un objectif que s'il couvre ≥ 5 techniques du noyau et n'est
pas constant sur son domaine. Renseigner `v3/tactic_map.json` et passer son `status` à `partial`
puis `derived`. Les six objectifs candidats sont une **hypothèse**, pas une décision (archive A-1).

### R5 — Étendre la tranche typée au-delà de Forensics

7 entrées `typed` aujourd'hui. Ordre suggéré par prévalence : Forensics (compléter), Steganography,
Web, Cryptography, Reverse. Chaque promotion demande indicateurs relus, liaisons d'outils et cas
d'évaluation.

### R6 — Dette de placeholders

238 fichiers sur 324 portent encore la mention `Add challenge write-up link`, dont 65 des
70 fiches du noyau. **Périmètre volontairement limité au noyau** (R1) : combler les 173 autres
sans preuve ne ferait que déplacer la dette.

---

## Critère d'acceptation global

> `precision@3` sur le hold-out (R3) **supérieure** après R4 à la valeur de référence mesurée
> avant. Si les nouveaux axes n'améliorent pas le retrieval, ils n'ont rien produit et doivent être
> abandonnés plutôt que documentés.

## Invariants à ne pas casser

1. La paire 1:1 reste l'**unité éditoriale** ; le graphe se superpose (SCHEMA_V3 §4.1).
2. `domain`, les arêtes `solves` et la maturité sont **dérivés** — les écrire, c'est créer une
   dérive.
3. Un fait, une source : un `solves` curé est rejeté, `relations.json` est généré.
4. Aucune attestation fabriquée : `build_evidence.py` n'extrait que ce que l'URL contient.
5. Les documents générés portent une **empreinte de corpus**, jamais un horodatage.
6. `v2/` est gelée : ne pas l'éditer, ne pas exécuter ses scripts.

---

## Archive — décisions contestées et différées

Propositions retirées du backlog actif. Conservées avec leur argument pour ne pas les reproposer
sans élément nouveau.

### A-1. Créer les 6 tactiques de résolution en amont · **différé vers 2.4**

*Proposition* : figer `Discover | Reveal | Gain Access | Gain Control | Expand Reach | Capture
Objective` dans un `tactics.json` dédié et y migrer les 19 domaines.
*Argument* : la liste est postulée, pas dérivée. Sur un challenge Jeopardy crypto ou stego — la
majorité du corpus — `Gain Access`, `Gain Control` et `Expand Reach` sont vides : l'axe décrit bien
FPN/AD et mal les deux tiers des entrées. Un axe qui vaut toujours `Reveal` sur un domaine n'est
pas un axe. Il doit sortir de l'étiquetage du noyau, pas le précéder.

### A-2. Renommer `tactic` → `domain` jusque dans les IDs · **rejeté**

*Argument* : `CTFT-TA-*` est cité dans 322 fiches, `index.json`, `catalog.json`, le bundle STIX et
les docs générées. Le gain est cosmétique, le coût est un renommage global et la rupture de tous
les liens publics. Le renommage se fait dans les schémas et la doc (2.1), pas dans les clés.

### A-3. Migrer les 161 paires vers un front-matter à 5 axes · **rejeté**

*Proposition* : un `migrate_axes.py` ajoutant `format`, `domain`, `artifact`, `tactic`, `mechanism`
sur chaque paire.
*Argument* : ~800 champs posés sur un corpus dont 147/161 fiches ont moins de 200 caractères de
corps — un rapport métadonnées/contenu supérieur à 1. Et si le script dérive ces champs, l'audit
mesurera la qualité de ses devinettes en la présentant comme de la curation. Remplacé par :
dériver `domain` (2.1), étendre `artifact_types` (2.2), curer `format` sur le noyau (2.3),
externaliser l'axe tactique (2.4).

### A-4. Ajouter un mapping MITRE D3FEND · **abandonné (décision du 2026-08-30)**

*Argument* : D3FEND normalise des contre-mesures **défensives**. Une resolution-technique CTF est
une récupération offensive : ses ancres naturelles sont CAPEC et CWE. D3FEND ne collerait qu'à la
moitié « Forensic / Blue-Team Perspective » des fiches. De plus l'ancrage ATT&CK est déjà lâche
(61 IDs distincts pour 161 entrées, `T1027` utilisé 24 fois) : un second mapping approximatif
doublerait le bruit au lieu de le réduire.

### A-5. Renommer `counter-technique` → `resolution-technique` · **différé après 3.1**

*Argument* : le répertoire `countertechniques/` et la clé `CTFTCTE-*` sont conservés — le
renommage serait donc purement documentaire, sans gain, tant que la contrainte 1:1 tient. Solution
retenue en attendant : exposer `role: "resolution"` dans les schémas v2. Rediscuter une fois le
graphe (3.1) en place.

### A-6. Consolider `WEB-004` et `WEB-016` sous CWE-89 / CAPEC-66 · **rejeté (erreur factuelle)**

*Argument* : `CTFTTE-WEB-016` est **NoSQL injection**, pas SQL injection — soit CWE-943 et
CAPEC-676. Les fusionner sous CWE-89 produirait exactement le faux regroupement que la
consolidation prétend corriger. Illustration du principe directeur n° 1 : consolider avant preuve
fabrique des erreurs.

### A-7. Validation par deux curateurs · **assoupli**

*Argument* : le dépôt est mono-mainteneur ; un critère inapplicable ne bloque rien et décrédibilise
les autres. Remplacé en 1.3 par « un curateur + deux sources publiques indépendantes ».

### A-8. STIX : remplacer `mitigates` par une relation custom `solves` · **assoupli**

*Argument* : `mitigates` est sémantiquement faux (une contre-technique CTF ne mitige pas, elle
résout), mais une relation entièrement custom rend le bundle illisible par ATT&CK Navigator et
OpenCTI — on perdrait le seul format d'interopérabilité réellement portable. Retenu en 0.3 :
double émission, `mitigates` conservé + propriété `x_ctft_relation: "solves"`.

### A-9. `relations.json` autoritatif dès le départ · **assoupli**

*Argument* : le markdown et `relations.json` énonceraient le même fait (`solves`) sans qu'aucun
ne soit désigné comme source de vérité — dérive garantie. Retenu en 3.1 : dérivé d'abord, avec
garde-fou `généré ⊆ déclaré` ; bascule autoritative seulement si le graphe exprime des faits que
le markdown ne peut pas porter.

---

## Scripts

| Script | Rôle | État |
| --- | --- | --- |
| `v3/render_taxonomy_docs.py` | `CORRELATION.md`, `HIERARCHY.md` **et les 19 pages tactiques** | `--check` = gate de dérive |
| `v3/catalog_audit.py` | index, catalogue, file de curation, relations, manifeste, lint | `--check` = gate d'intégrité |
| `v3/render_stix.py` | bundles STIX 2.1 depuis `index.json` | nouveau (0.3) |
| `v3/build_evidence.py` | sème `evidence.json` depuis les liens du corpus | nouveau (1.1) |
| `v3/solve.py` | retrieval, validation, `precision@k` | `--evaluate` ajouté (4.1) |
| `v3/attach_attack_related.py` | tables ATT&CK par entrée | inchangé (pas de D3FEND, A-4) |
| `v3/create_todo_entries.py` | génération de paires | inchangé |
| `v3/fix_bare_urls.py` | lint MD034 | conscient des blocs de code |
| `ctft-generator.py` | générateur legacy | n'est plus la source STIX |
| `v2/*` | tranche de référence v2 | **gelée** |

## Tentatives de normalisation existantes (références)

| Initiative | Ce qu'elle normalise | Limite pour FOM |
| --- | --- | --- |
| [CTFtime](https://ctftime.org/ctf-wtf) et [ENISA](https://www.enisa.europa.eu/news/enisa-news/capture-the-flag-competitions-all-you-ever-wanted-to-know) | Formats Jeopardy/Attack-Defense, catégories usuelles, scoring, organisation | Folksonomie de domaines, sans IDs ni définition des techniques |
| [Cyber Taxi](https://arxiv.org/abs/2101.05538) | Taxonomie multidimensionnelle des systèmes d'entraînement (public, environnement, scénario, format, setup) | Classe l'exercice, pas les actions du joueur |
| [Švábenský et al.](https://arxiv.org/abs/2101.01421) | 15 963 writeups mappés vers les Knowledge Areas/Units de CSEC2017 | Normalise les connaissances enseignées, pas les comportements de résolution |
| [PADS-LLM](https://www.sciencedirect.com/science/article/pii/S1084804526000603) | Extraction des étapes de writeups et mapping en séquences MITRE ATT&CK | Le plus proche d'une normalisation TTP, mais limité au vocabulaire ATT&CK |
| [CAPEC](https://capec.mitre.org/about/index.html), [CWE](https://cwe.mitre.org/documents/schema/schema_v4.3.html), [OWASP WSTG](https://wstg.owasp.org/) | Patterns d'attaque, faiblesses, scénarios de test versionnés | Excellentes références externes, mais aucune ne couvre crypto, stego, puzzles ou forensics CTF de bout en bout |
| [NICE](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/getting-started) | Tâches, connaissances et compétences observables | Utile pour la dimension pédagogique, distincte de la technique |

## Historique

- 2026-08-30 — **refonte v3** : v2 gelée, couche v3 active, phases 0 à 4 de la spec appliquées
  (réalignement `FOR-010..014` + `FOR-027`, contre-techniques placeholder renommées, STIX
  régénéré de 63 à 162 paires, maturité unifiée et calculée, `evidence.json` / `core.json` /
  `relations.json`, axes `domain` / `artifact` / `format`, lint sémantique, `precision@k`, gate
  CI). Pages tactiques désormais générées. Reste : la collecte de preuves (R1–R6).
- 2026-08-30 — refonte du backlog en spec d'implémentation : phases ordonnées preuve-d'abord,
  9 propositions contestées déplacées en archive avec argument, mapping D3FEND abandonné.
- 2026-08-30 — 56 paires promues du backlog CTF (`SDR-001`, `HWR-001/002`, `NET-001..007`,
  `FOR-019..026`, `REV-006..009`, `PWN-006..008`, `CRY-008..013`, `STE-010/011`, `WEB-010..017`,
  `OSI-006..008`, `CLD-006..008`, `AIM-006/007`, `FPN-008..010`, `GAM-006`, `COD-006/007`,
  `JAL-006`) → 161 paires, 19 domaines actifs.
- 2026-08-30 — tables `Related MITRE ATT&CK` par entrée (schéma v2 §3.5), familles `NET`/`SDR`,
  `HWR` active, 170 violations MD034 corrigées.
- 2026-08-29 — famille `MSC` retirée (doublons de `JAL`/`COD`/`GAM`/`FPN`), ordre canonique des
  domaines aligné sur le sélecteur de catégories, `CORRELATION.md` et `HIERARCHY.md` générés.
