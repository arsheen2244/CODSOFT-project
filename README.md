<div align="center">

# 🐍 CodSoft Python Internship Projects

**Three small Python apps from the CodSoft Python Programming internship:**
a password generator, Rock‑Paper‑Scissors and a calculator.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-2b5b84)
![pyperclip](https://img.shields.io/badge/clipboard-pyperclip-6e40c9)
![Internship](https://img.shields.io/badge/CodSoft-Internship-1f6feb)

</div>

---

## 📦 What's Inside

| # | Project | File | Interface | Highlights |
|:-:|--------|------|:---------:|-----------|
| 1 | 🔐 **Password Generator** | [`PasswordGeneraator.py`](PasswordGeneraator.py) | Tkinter GUI | Choose a length (5–18) and strength level (weak / medium / strong) and copy the password to the clipboard with `pyperclip` |
| 2 | ✊ **Rock · Paper · Scissors** | [`Rock_Paper_Scissors.py`](Rock_Paper_Scissors.py) | Tkinter GUI | Play against the computer, which picks at random. A running scoreboard counts the wins and has a reset button |
| 3 | 🧮 **Simple Calculator** | [`calculator.py`](calculator.py) | Command line | Add, subtract, multiply, divide (guards against division by zero) and raise to a power |

## 🔍 How Each One Works

### 🔐 Password Generator

```mermaid
flowchart LR
    A[User sets length<br/>+ strength radio button] --> B{Strength}
    B -->|Weak| C[lowercase]
    B -->|Medium| D[lower + UPPER + digits]
    B -->|Strong| E[lower + UPPER + digits + symbols]
    C & D & E --> F[random.sample<br/>n unique characters]
    F --> G[Show in entry box]
    G --> H[📋 Copy → pyperclip]
```

### ✊ Rock · Paper · Scissors

```mermaid
flowchart LR
    U[Player clicks<br/>Rock / Paper / Scissors] --> W{winner}
    CPU[Computer:<br/>random.choice] --> W
    W -->|same| T[🤝 Tie]
    W -->|"rock beats scissors,<br/>paper beats rock,<br/>scissors beats paper"| P[🏆 You win]
    W -->|otherwise| L[💻 Computer wins]
    T & P & L --> M[messagebox shows result<br/>+ running score]
```

### 🧮 Calculator

```mermaid
flowchart LR
    I[Input two numbers] --> M[Menu 1–5]
    M --> O["+ / − / × / ÷ / ^"]
    O --> R[Print result]
    O -. "÷ by 0" .-> E[Error message]
```

## 🧰 Tech Stack

| Purpose | Tool |
|--------|------|
| Language | Python 3 |
| GUI | Tkinter (standard library) |
| Randomness | `random` |
| Character sets | `string` |
| Clipboard | `pyperclip` |

## 🚀 Run Them

```bash
git clone https://github.com/arsheen2244/CODSOFT-project.git
cd CODSOFT-project
pip install pyperclip            # only the password generator needs it

python PasswordGeneraator.py     # GUI
python Rock_Paper_Scissors.py    # GUI
python calculator.py             # terminal
```

## 🎯 What I Practised

- Building event‑driven GUIs with Tkinter widgets (`Entry`, `Radiobutton`, `Button`, `messagebox`)
- Breaking game logic into small, testable functions (`Computer_choice`, `winner`, `display_winners`)
- Validating input and handling edge cases such as division by zero

> 🔒 For real passwords, use `secrets.choice` rather than `random`. It draws from a cryptographically secure source.

---

<div align="center">Built by <a href="https://github.com/arsheen2244">Arsheen Inamdar</a> during the CodSoft internship</div>
