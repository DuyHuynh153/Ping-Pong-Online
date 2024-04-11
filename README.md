# Ping Pong Game

Welcome to the Ping Pong Game! This is a simple yet addictive game built using Python 3 and Pygame library. It offers various gameplay modes to keep you entertained whether you're playing alone or with friends.

## Features

- **Single Player Mode**: Play against an AI opponent with varying difficulty levels.
- **Two Player Mode (Offline)**: Compete against a friend in a classic 1v1 match.
- **Online Mode**: Play against friends or family members over the same network.

### Home Screen
![HomeScreen](res/images/home_screen.png)

## Gameplay Modes

### Play With AI
![Play With AI](res/images/play_with_ai.png)

### Two Player Mode (Offline)
![Two Player Offline](res/images/play_offline_2_player.png)

### PLay Online 
![Online Mode](res/images/play_online.png)



## Instsallation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/ping-pong-game.git

```
2. Create a Virtual Environment:
```bash
python3 -m venv venv
```
3. Activate the Virtual Environment

```bash
- *On macOS and Linux*: source venv/bin/activate

- *On Windows*: venv\Scripts\activate

```
4. Install Dependencies from requirements.txt:
```bash
python3 -m pip install -r requirements.txt
```
5. Run Game:
- Play with AI or Play Offline:
   
```bash
-  python3 pong_client.py
```

- Play Online:
  
```bash
- At Server side:
    *Config IP and Port*: Go to pong_server.py -> Adjust IP into you computer IP or your Network IP
    *Run Server*: python3 pong_server.py


 - At Client side:
    *Config IP and Port*: Go to pong_client.py -> Adjust IP into the same IP as server IP
    *Run Client*: python3 client.py
```

