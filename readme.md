# Picnic Invaders

Projeto final desenvolvido no âmbito do **Curso de Programação em Python (IEFP)**. Este jogo não é apenas um exercício académico: é a prova prática da minha capacidade de conceber, estruturar e entregar um projeto completo em **Python + Pygame**, unindo programação, lógica de jogo e criatividade.

---

## Visão geral

* **Engine:** Pygame
* **Resolução da janela:** 1120×747 @ 60 FPS
* **Estados:** Splash → Jogo → Fim (vitória/derrota)
* **Plataformas:** Windows, macOS, Linux (Python 3.10+ recomendado)

---

## O que demonstra este projeto

* **Arquitetura modular**: código organizado em múltiplos ficheiros (`player`, `enemy`, `bullet`, `configs`, etc.), mostrando boas práticas de estrutura.
* **Orientação a objetos**: reutilização de classes base, herança e encapsulamento.
* **Gestão de assets**: carregamento dinâmico de imagens e sons.
* **Mecânicas de jogo**: colisões pixel-perfect, cadência adaptativa de disparos, sistema de vidas e estados do jogo.
* **Ciclo completo**: desde splash screen até vitória/derrota, com transição fluida e feedback audiovisual.

Este projeto mostra não só a minha capacidade técnica, mas também atenção ao detalhe, organização e preocupação com a experiência do utilizador.

---

## Jogabilidade

* **Objetivo:** eliminar todos os inimigos antes que as vidas acabem.
* **Vidas do jogador:** 3
* **Inimigos:**

  * **Fly** (mosca) – 2 vidas
  * **Ant** (formiga) – 1 vida
* **Tiro do jogador:** *napkin* (sobe)
* **Tiro inimigo:** *poo* (desce)
* **Dificuldade dinâmica:** a cadência dos tiros inimigos acelera à medida que restam menos inimigos.

### Controlos

* **Mover:** A / ← (esquerda), D / → (direita)
* **Disparar:** Espaço
* **Sair:** fechar janela

---

## Requisitos

* Python 3.10+ (3.12 OK)
* Pygame ≥ 2.5
* Assets nas pastas `imgs/` e `sounds/`

### Instalação

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate

pip install --upgrade pip
pip install pygame
```

### Executar

```bash
python main.py
```

---

## Estrutura do projeto

```
.
├─ main.py              # Loop principal, ecrãs e fluxo de jogo
├─ configs.py           # Constantes e definições
├─ character.py         # Base para entidades
├─ player.py            # Lógica do jogador
├─ enemy.py             # Lógica dos inimigos
├─ bullet.py            # Projéteis genéricos
├─ imgs/                # Sprites
└─ sounds/              # Áudio
```

---

## Diferenciais de valor

* **Clareza do código**: preparado para ser lido e expandido.
* **Flexibilidade**: `configs.py` permite alterar facilmente regras, velocidades e dificuldade.
* **Escalabilidade**: formação de ondas de inimigos, introdução de novos tipos e power-ups.
* **Profissionalismo**: README documentado, organização modular, código comentado.

> Este não é apenas um jogo, é uma demonstração do que consigo construir como programador Python.

---

## Roadmap (próximos passos)

* Sistema de pontuação e leaderboard
* Power-ups (escudos, tiro duplo, etc.)
* Novos padrões de inimigos
* Integração com comandos de jogo (gamepad)

---

## Licença e créditos

* **Código:** André Câmara
* **Curso:** Projeto final – IEFP, Programação em Python
* **Assets:** Arte e sons a definir (ou substituíveis pelo utilizador)

---

## Começa já

1. `pip install pygame`
2. Garante as pastas `imgs/` e `sounds/`
3. `python main.py`
4. Diverte-te!

---

### Sobre mim

Sou programador em fase de transição de carreira, focado em Python e desenvolvimento de software. Este projeto é a primeira de muitas provas do meu compromisso com **código limpo, funcional e criativo**.
