# **🧲 Magnetic Cave - AI-Powered Board Game** 🎮  

**A strategic Python board game with AI-powered decision-making using Minimax Algorithm & Alpha-Beta Pruning.**  

---

## **📌 Overview**
Magnetic Cave is a **two-player board game** where players **place bricks on an 8x8 grid**, aiming to form a **sequence of five consecutive bricks** **horizontally, vertically, or diagonally**.  

### **🎮 Game Modes**
1️⃣ **Player vs Player (PvP)** – Both players make manual moves.  
2️⃣ **Player vs AI** – Player controls '■' while AI plays as '□'.  
3️⃣ **AI vs Player** – AI plays as '■', while the player controls '□'.  

---

## **✨ Features**
- 🎨 **Graphical User Interface (GUI)** using **Tkinter**
- 🤖 **AI Player** powered by **Minimax Algorithm & Alpha-Beta Pruning**
- 🏆 **Win and Tie Detection** (Game auto-detects when a player wins or ties)
- 🔄 **Dynamic Game Modes** (PvP, AI-assisted, AI vs Player)
- 🎯 **Heuristic Evaluation** (AI makes strategic moves using a scoring system)
- ⚡ **Optimized Performance** with **Alpha-Beta Pruning**

---

## **🖥️ Technologies & Tools**

<img align="left" alt="Python" width="50px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"/>
<br><br>

| Technology  | Purpose |
|-------------|---------|
| **Python**  | Core Programming Language |
| **Tkinter** | GUI Implementation |
| **Minimax Algorithm** | AI Decision Making |
| **Alpha-Beta Pruning** | Optimized AI Move Selection |

---

## **📸 Screenshots**
### 🎲 Game Board (GUI)
![image](https://github.com/user-attachments/assets/ff849479-55ba-46e5-9702-139a117673a7)

### 🏆 Winning Condition
![image](https://github.com/user-attachments/assets/b3a3f5ea-7f1b-4f96-a300-49ae01778929)

---

## **🧠 AI Algorithm - Minimax with Alpha-Beta Pruning**
The **Minimax Algorithm** searches possible moves and selects the best one using **heuristic evaluation**.  
**Alpha-Beta Pruning** optimizes this search, cutting unnecessary calculations, making AI moves **faster and more efficient**.

### **🏆 AI Heuristic Evaluation Function**
The AI assigns **scores** to different board configurations:

| Situation | AI Score |
|-----------|---------|
| **AI Wins (5 in a row)** | +1000 |
| **AI has 4 in a row** | +30 |
| **AI has 3 in a row** | +10 |
| **AI has 2 in a row** | +2 |
| **Opponent has 4 in a row (AI must block)** | -90 |
| **Opponent has 3 in a row (AI should counter)** | -30 |

---

## **🚀 Installation**
### **1️⃣ Install Python**
Ensure you have **Python 3.x** installed.

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/zainabja52/Magnetic-Cave-.git
cd Magnetic-Cave-
```

### **3️⃣ Run the Game**
```bash
python main.py
```

### **4️⃣ Select Game Mode**
Once the program starts, choose a mode:
```
Enter the mode:
1. Player vs Player (PvP)
2. Player vs AI ('■' vs '□')
3. AI vs Player ('■' vs '□')
```
Start playing and enjoy! 🎮

---

## **🧪 Testing**
### **Mode 1 - Player vs Player**
- Two players take turns placing bricks.

### **Mode 2 - Player vs AI ('□')**
- AI **predicts optimal moves** and tries to win.

### **Mode 3 - AI ('■') vs Player**
- AI plays aggressively and blocks winning paths.

**Results:**  
✅ AI **successfully blocks opponents' moves**  
✅ AI **outperforms human players** in **strategic planning**  

---

## **📝 Conclusion**
- The **AI player effectively blocks opponents** while also maximizing its own chances to win.
- The **heuristic evaluation function** makes AI moves more strategic.
- Future improvements could include **advanced offensive strategies**.

---

## **⭐ Support the Project**
If you found this project useful, consider **starring** ⭐ the repository on GitHub! 😊

