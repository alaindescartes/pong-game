

# 🏓 Pong Game (Python Edition)

A modern implementation of the classic Pong game using Python's `turtle` graphics library. This game features two paddles, a moving ball, and a scoring system, providing an exciting head-to-head competition!

---

## 🛠 Features  

- **Paddle Controls**:  
  - Player 1: `W` (Up), `S` (Down)  
  - Player 2: `Arrow Up`, `Arrow Down`  
- **Ball Physics**: The ball bounces off the paddles and updates the score when it crosses the screen boundary.  
- **Scoreboard**: Displays real-time scores for both players.  
- **Separator Line**: A visual separator to split the playing field.  

---

## 📂 Project Structure  

- **`ball.py`**: Defines the `Ball` class for creating and controlling the ball's movement and bounce behavior.  
- **`screen.py`**: Manages the game screen with `GameScreen`.  
- **`paddle.py`**: Defines the `Paddle` class for player-controlled paddles.  
- **`separator.py`**: Draws a vertical separator on the screen.  
- **`scoreboard.py`**: Manages the scorekeeping and displays it on the screen.  

---

## 🚀 How to Run  

### Prerequisites  
- Python 3.x  
- `turtle` graphics library (pre-installed with Python)  

### Steps  
1. Clone the repository:  
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```  
2. Run the game:  
   ```bash
   python main.py
   ```  

---

## 🎮 Game Controls  

### Player 1 (Right Paddle)  
- **Move Up**: `Up Arrow`  
- **Move Down**: `Down Arrow`  

### Player 2 (Left Paddle)  
- **Move Up**: `W`  
- **Move Down**: `S`  

---

## 🛡️ Future Enhancements  
- Add sound effects for ball bounces and scoring.  
- Introduce power-ups and special abilities for paddles.  
- Implement a start menu and customizable controls.  
- Create an AI opponent for single-player mode.  

