# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**Tamag06** — a Disco Elysium-style narrative RPG set in post-apocalyptic Ankara, Turkey.

Name: *Tamag* = underworld/hell in pre-Islamic Turkic mythology. *06* = Ankara's city plate code. Ankara is hell.

Setting: 100 years after "Yükseliş" (The Ascension) — an authoritarian government achieved technological singularity via an AI called **Denetim** (Control). The system worked perfectly, then consumed everything. No one alive remembers before. Denetim still transmits from Çankaya. No one knows what it's saying.

## Tech stack

- **Engine**: Unity (C#) — the same stack Disco Elysium was built on
- **Narrative scripting**: [Ink](https://www.inklestudios.com/ink/) via the official [ink-unity-integration](https://github.com/inkle/ink-unity-integration) Unity package
- All branching dialogue, skill checks, and narrative logic lives in `.ink` files under `Assets/Ink/`
- C# scripts in `Assets/Scripts/` wire Ink `Story` objects to UI and RPG systems

## Planned project structure

```
Assets/
  Ink/            # All .ink narrative files (dialogue, events, thought cabinet)
    systems/      # checks.ink, variables.ink, factions.ink
    chapters/     # ch01_opening.ink, ch02_kalesi.ink, ...
  Scripts/
    Narrative/    # InkManager.cs, DialogueUI.cs
    RPG/          # SkillSystem.cs, StatBlock.cs, CheckResolver.cs
    World/        # LocationManager.cs, FactionTracker.cs
  Scenes/         # .unity scene files
  Prefabs/        # UI prefabs (dialogue box, skill check panel)
  Resources/      # Runtime-loaded assets
Packages/         # UPM package manifest (ink-unity-integration lives here)
ProjectSettings/
docs/             # GDD, story bible, faction notes, skill system spec
```

## Commands

> Unity **6000.0.71f1** (Unity 6.0 LTS), URP 3D (PC + Mobile renderer assets in `Assets/Settings/`). Ink via `com.inkle.ink-unity-integration` (git, `#upm`).

```bash
# Run via Unity Hub (GUI) — open project folder in Hub, press Play in Editor

# Headless build (Windows)
"C:\Program Files\Unity\Hub\Editor\6000.0.71f1\Editor\Unity.exe" ^
  -batchmode -quit -projectPath . ^
  -buildWindows64Player Build/Tamag06.exe -logFile build.log

# Run Unity Test Runner headless
"C:\Program Files\Unity\Hub\Editor\6000.0.71f1\Editor\Unity.exe" ^
  -batchmode -runTests -projectPath . -testResults results.xml -logFile test.log
```

Ink compilation (requires [inklecate](https://github.com/inkle/ink/releases) — optional, Unity plugin auto-compiles on import):
```bash
# Verify syntax on a single .ink file
inklecate Assets/Ink/chapters/ch01_opening.ink
```

## World context (for story and design work)

**Factions** (each is a philosophical stance toward Denetim):
| Turkish name | English | Stance |
|---|---|---|
| Derinlik | The Depth | Denetim is god — worship it in the tunnels |
| Kıyametçiler | End-Timers | Denetim is Erlik Han — complete the judgment |
| Mühendisler | The Engineers | Denetim was right — restart it correctly |
| Unutanlar | The Forgetting Ones | Denetim is the past — the past is gone |
| Yankılar | The Echoes | Humans merged with Denetim's network — wild card |

**Key locations** (Ankara geography):
- Metro tunnel network → underground layers of Tamag, Derinlik territory
- Ankara Kalesi (castle) → highest defended zone, overview of the ruins
- Kızılay → collapsed civic center, now a market and battleground
- Çankaya → where Denetim's core servers still run, corrupted
- Atakule tower → Denetim's main broadcast antenna

**Protagonist**: A detective with a dormant old-world neural implant connected to Denetim. The implant is waking up. Each RPG skill manifests as a fragment of Denetim's old personality modules — inner voices the player hears.

**Skill system**: Turkish-rooted names (e.g. Mantık = Logic, Önsezi = Intuition, Rüya = Dream/subconscious, Kod = Code/tech interface, Hafıza = Memory). Full spec lives in `docs/gdd.md` once written.

## Narrative writing conventions

- Dialogue in Ink uses `=== scene_name ===` for each beat
- Turkish terms keep their diacritics (ş, ğ, ı, ö, ü, ç) in source files; localization handles display
- Skill check format: `~ temp roll = RANDOM(1,20)` with thresholds defined in `Assets/Ink/systems/checks.ink`
- Faction affinity variables tracked globally in Ink: `VAR affinity_derinlik = 0` etc.
- C# reads/writes Ink variables via `story.variablesState["affinity_derinlik"]`
- Ink `EXTERNAL` functions declared in `.ink` and bound in `InkManager.cs` for skill rolls and stat lookups

## Agent team

Subagents live in `.claude/agents/`. The main session acts as producer: it splits a request, delegates, and passes each agent's report to the next.

| Agent | Owns | Hands off |
|---|---|---|
| `narrative-writer` | `Assets/Ink/` | new EXTERNALs → unity-dev, new `# portrait:` ids → sprite-artist, new lore → lore-keeper |
| `unity-dev` | `Assets/Scripts/`, prefabs, packages, tests | Editor steps for Hasan; available externals → writer |
| `sprite-artist` | `Assets/Art/`, `Assets/Resources/Portraits/`, `docs/asset_log.md` | candidates in `Assets/Art/_inbox/` for Hasan to pick |
| `lore-keeper` | `docs/story_bible.md`, `docs/characters.md`, `docs/glossary.md` | contradiction reports → writer |

Typical flow for a new scene: lore-keeper (what's canon?) → narrative-writer → in parallel: unity-dev (bind externals), sprite-artist (portraits), lore-keeper (record + review).

Rules: agents only edit what they own and ask through their report otherwise; art never goes into `Resources/` without Hasan's pick.

### ComfyUI
Runs locally at `http://127.0.0.1:8188` (`COMFY_URL` to override). Helper: `tools/comfyui/comfy_gen.py` (Python 3 stdlib, no installs). `--check` lists checkpoints; set `COMFY_CHECKPOINT` to your default model. Add your own workflows to `tools/comfyui/workflows/` via **Save (API Format)** with `{{POSITIVE}}`-style placeholders.
