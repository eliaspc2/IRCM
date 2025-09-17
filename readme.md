# It’s Raining Coins and Monsters (IRCM)

**Capstone Project – Programming MOOC 2025 (University of Helsinki, 10 ECTS)**
Final project developed for the **Introduction to Programming** (5 ECTS, \~135h) and **Advanced Course in Programming** (5 ECTS, \~135h) modules. These MOOCs are internationally recognized, university-level courses delivered by the University of Helsinki.

Due to course restrictions, the entire game had to be implemented in a **single Python file (`main.py`)**, and only the **provided images (`coin.png`, `monster.png`, `robot.png`, `door.png`)** could be used. These constraints highlight my ability to design, structure, and deliver a complete, functional project even under tight limitations.

---

## Overview

* **Engine:** Pygame
* **Window resolution:** 640×420 @ 60 FPS
* **States:** Intro → Game → Game Over
* **Platforms:** Windows, macOS, Linux (Python 3.10+ recommended)

---

## What this project demonstrates

* **Self-contained code:** all classes and logic in a single file, as required by the course.
* **Object-Oriented Programming:** `Player` and `Drop` classes (for coins and enemies) with reusable logic and pixel-perfect collision detection via masks.
* **Game management:** main loop handling events, updates, and rendering.
* **Dynamic difficulty:** increasing frequency and speed of enemies as the score grows.
* **User feedback:** real-time scoring, intro message, Game Over screen, and reset with F2.

This project shows how it is possible to deliver a complete, playable experience even under strict technical and pedagogical restrictions.

---

## Gameplay

* **Goal:** catch coins, avoid monsters.
* **Scoring:** +1 per collected coin, −1 per missed coin.
* **Game Over:** collision with a monster.

### Controls

* **Move:** A / ← (left), D / → (right)
* **New game:** F2
* **Exit:** Esc or close window

---

## Requirements

* Python 3.10+ (3.12 OK)
* Pygame ≥ 2.5
* Mandatory assets in the same folder as `main.py`: `coin.png`, `monster.png`, `robot.png`, `door.png`

### Installation

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate

pip install --upgrade pip
pip install pygame
```

### Run

```bash
python main.py
```

---

## Project structure

```
.
└─ main.py     # Single file with all logic, classes, and game loop
```

---

## Value highlights

* **Strict compliance with requirements:** full project in a single file and only with provided assets.
* **Best practices under constraints:** clear classes, logical separation between player, coins, and enemies.
* **Creativity under limitations:** simple yet effective concept, playable and scalable.
* **Professionalism:** commented, organized code ready for future reuse in larger projects.

> This game proves I can deliver concrete results even in constrained environments, focusing on clarity, functionality, and user experience.

---

## Roadmap (future improvements)

* Levels with progressive difficulty
* Power-ups (extra lives, coin magnets)
* Custom graphics and sounds
* High score ranking

---

## License and credits

* **Code:** André Câmara
* **Course:** Final project – Programming MOOC 2025 (University of Helsinki, 10 ECTS)
* **Assets:** provided images (`coin.png`, `monster.png`, `robot.png`, `door.png`)

---

## Quick start

1. `pip install pygame`
2. Place `coin.png`, `monster.png`, `robot.png`, and `door.png` in the same folder as `main.py`
3. `python main.py`
4. Have fun!

---

### About me

I am a career-changer programmer, focused on Python and software development. This project was my final assignment in the **Programming MOOC 2025 (University of Helsinki, 10 ECTS)**, showcasing my **resilience, technical ability, and passion for clean, functional code**.
