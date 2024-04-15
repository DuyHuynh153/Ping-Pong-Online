import os
import sys
from pygame import Color



ID_NONE = -1
ID_LEFT = 0
ID_RIGHT = 1


# Utils
ENCODING = 'utf-8'



def encode_str(msg: str):
    return msg.encode()

def decode_str(msg: bytes):
    return msg.decode()


def gray(i) -> Color:
    return Color(i, i, i)



# Main Vars
DEFAULT_W_WIDTH, DEFAULT_W_HEIGHT = 1300, 700
DEFAULT_FULLSCREEN = False
FPS = 60
WINNING_SCORE = 10

DISPLAY_TITLE_PART1 = "Ping"
DISPLAY_TITLE_PART2 = "Pong"
DISPLAY_TITLE = "Ping Pong Game"




STATUS_TEXT_WINNING_SCORE = "Target"

# Delimiters
REMOTE_PLAYER_DELIMITER = "%"
GAME_STATE_DELIMITER1 = ";"
GAME_STATE_DELIMITER2 = ","
SESSION_INFO_DELIMITER = "|"
STATUS_TEXT_DELIMITER = " | "


# Messages
MSG_SESSION_CONNECTING = "Connecting to server..."
MSG_SESSION_WAITING = "Waiting for players..."
MSG_ENEMY_LEFT_DEFAULT = "Other player left!"
MSG_WON_LEFT = "Left Won!"
MSG_WON_RIGHT = "Right Won!"
MSG_WON_SELF = "You Won!"
MSG_WON_ENEMY = "You Lost!"
MSG_WON_CAPTION = "Press ENTER to continue"

MSG_PAUSED = "Game Paused"
MSG_PAUSED_CAPTION = "Press SPACE to resume"

MSG_CONNECTING_CAPTION = "Press ESCAPE to stop connecting"
MSG_WAITING_CAPTION = "Press ESCAPE to stop matching"
MSG_ENEMY_LEFT_CAPTION = "Press ENTER to continue"

TITLE_CONTROLS = "CONTROLS"
DES_CONTROLS = "Player 1 : UP-DOWN\nPlayer 2 : W-S\nPause : Space\nExit : Escape\nFullscreen : Ctrl-F"

OFFLINE_MULTI_PLAYER_PLAYER1_NAME = "Player 1"
OFFLINE_MULTI_PLAYER_PLAYER2_NAME = "Player 2"
OFFLINE_SINGLE_PLAYER_AI_NAME = "AI"
DEFAULT_ENEMY_NAME = "Opponent"


def format_server_addr(server_ip: str, server_port: int) -> str:
    return f"Server {server_ip}:{server_port}"


def format_player_name(player_name: str) -> str:
    return f"Player : {player_name}"


# def format_score_text(player_name: str, score: int) -> str:
#     return f"{player_name} : {score}" if player_name else str(score)


def get_msg_enemy_left(enemy_name: str, default_msg=MSG_ENEMY_LEFT_DEFAULT) -> str:
    return f"{enemy_name} has left!" if enemy_name else default_msg




def __get_won_msg_cap(player_name: str, score_diff: int, won: bool) -> str:
    return f"{player_name} {'won' if won else 'lost'} by {score_diff} points. {MSG_WON_CAPTION}"


def __get_won_display_info_offline_single_player(self_won: bool, score_diff: int, enemy_name: str = '') -> tuple:
    _enemy_name = enemy_name if enemy_name else OFFLINE_SINGLE_PLAYER_AI_NAME
    if self_won:
        won_msg = MSG_WON_SELF
        col = COLOR_MSG_WON_SELF
    else:
        won_msg = MSG_WON_ENEMY
        col = COLOR_MSG_WON_ENEMY

    won_cap = __get_won_msg_cap(_enemy_name, score_diff, not self_won)
    return won_msg, won_cap, col


def __get_won_display_info_offline_multiplayer(self_won: bool, score_diff: int, enemy_name: str = '') -> tuple:
    if self_won:
        won_name = OFFLINE_MULTI_PLAYER_PLAYER1_NAME
        lost_name = OFFLINE_MULTI_PLAYER_PLAYER2_NAME
        col = COLOR_MSG_WON_SELF
    else:
        won_name = OFFLINE_MULTI_PLAYER_PLAYER2_NAME
        lost_name = OFFLINE_MULTI_PLAYER_PLAYER1_NAME
        col = COLOR_MSG_WON_ENEMY

    won_msg = f"{won_name} won!"
    won_cap = __get_won_msg_cap(lost_name, score_diff, False)
    return won_msg, won_cap, col


def __get_won_display_info_online_multiplayer(self_won: bool, score_diff: int, enemy_name: str = '') -> tuple:
    _enemy_name = enemy_name if enemy_name else DEFAULT_ENEMY_NAME
    if self_won:
        won_msg = MSG_WON_SELF
        col = COLOR_MSG_WON_SELF
    else:
        won_msg = MSG_WON_ENEMY
        col = COLOR_MSG_WON_ENEMY

    won_cap = __get_won_msg_cap(_enemy_name, score_diff, not self_won)
    return won_msg, won_cap, col


def get_self_name_status(name):
    # return f"{name} (You)" if name else "You"
    return f"{name} (You)"


def get_enemy_name_status(name):
    return name if name else DEFAULT_ENEMY_NAME


def get_ai_name_status(ai_efficiency_percent: int):
    # return f"{OFFLINE_SINGLE_PLAYER_AI_NAME} ({ai_efficiency_percent}%)"
    if ai_efficiency_percent >= 60:
        return f"{OFFLINE_SINGLE_PLAYER_AI_NAME} (HARD)"
    else:
        return f"{OFFLINE_SINGLE_PLAYER_AI_NAME} (EASY)"


    # return f"{OFFLINE_SINGLE_PLAYER_AI_NAME} ("hard" if {ai_efficiency_percent}%)"


# Home Screen
CLIENT_HOME_SCREEN_PADX = 20
CLIENT_HOME_SCREEN_PADY = 20

CLIENT_HOME_SCREEN_PADX_SOUND_LABEL = 26
CLIENT_HOME_SCREEN_PADY_SOUND_LABEL = 26


# Colors
WHITE = gray(255)
BLACK = gray(0)

BG_DARK = BLACK
BG_MEDIUM = gray(20)
BG_LIGHT = gray(40)

FG_DARK = WHITE
FG_MEDIUM = gray(225)
FG_LIGHT = gray(0)



# Colors
COLOR_ACCENT_DARK = Color(0, 128, 0)  # Dark green
COLOR_ACCENT_MEDIUM = Color(0, 255, 0)  # Medium green
COLOR_ACCENT_LIGHT = Color(173, 255, 47)  # Light green

COLOR_HIGHLIGHT = Color(144, 238, 144)  # Light green

COLOR_TRANSPARENT = Color(255, 255, 255, 0)  # Fully transparent white
COLOR_TRANSLUCENT = Color(0, 128, 0, 125)  # Translucent green

TINT_SELF_DARK = Color(0, 128, 0)  # Dark green
TINT_SELF_MEDIUM = Color(0, 255, 0)  # Medium green
TINT_SELF_LIGHT = Color(173, 255, 47)  # Light green


TINT_ENEMY_DARK = Color(128, 0, 0)  # Dark red (for contrast with green)
TINT_ENEMY_MEDIUM = Color(255, 0, 0)  # Medium red (for contrast with green)
TINT_ENEMY_LIGHT = Color(255, 69, 0)  # Light red (for contrast with green)








COLOR_HOME_TITLE_PART1 = COLOR_ACCENT_DARK
COLOR_HOME_TITLE_PART2 = COLOR_HIGHLIGHT
COLOR_HOME_SUMMARY = FG_MEDIUM
COLOR_STATUS_TEXT = FG_LIGHT
COLOR_PLAYER_STATUS_TEXT = COLOR_HIGHLIGHT

COLOR_PADDLE_ENEMY = TINT_ENEMY_DARK
COLOR_PADDLE_SELF = TINT_SELF_DARK

COLOR_BALL = FG_DARK

COLOR_SCORE_SELF = TINT_SELF_MEDIUM
COLOR_SCORE_ENEMY = TINT_ENEMY_MEDIUM

COLOR_MSG_WON_SELF = TINT_SELF_DARK
COLOR_MSG_WON_ENEMY = TINT_ENEMY_DARK

COLOR_VERTICAL_DIVIDER = BG_LIGHT


# Paddle
PADDLE_REL_WIDTH = 0.0075
PADDLE_REL_HEIGHT = 0.15
PADDLE_CORNERS = 10
PADDLE_REL_PAD_X = 0.01
PADDLE_REL_PAD_Y = 0.01
PADDLE_REL_VEL = 0.01


# Ball
BALL_DEFAULT_REL_RADIUS = 0.3
BALL_DEFAULT_REL_VEl_MAX_COMPONENT = 0.0075
BALL_DEFAULT_REL_VEl_MIN_COMPONENT_FACTOR = 0.66
BALL_DEFAULT_RESET_DELAY_SECS = 2
BALL_DEFAULT_RANDOM_INITIAL_VEL_ENABLED = True



# Vertical Divider
VERTICAL_DIVIDER_WIDTH = 6
VERTICAL_DIVIDER_REL_HEIGHT = 0.045
VERTICAL_DIVIDER_CORNERS = 4


# ..........................................  External Resources  ................................
FROZEN = getattr(sys, 'frozen', False)
DIR_MAIN = os.path.dirname(sys.executable) if FROZEN else os.path.dirname(os.path.abspath(os.path.realpath(__file__)))

DIR_RES = os.path.join(DIR_MAIN, "res")
# DIR_RES_IMAGES = os.path.join(DIR_RES, "images")
# DIR_RES_SOUND = os.path.join(DIR_RES, "sound")
DIR_RES_FONT = os.path.join(DIR_RES, "font")

DIR_CONFIG = os.path.join(DIR_MAIN, "config")


def is_file(path: str) -> bool:
    return path and os.path.isfile(path)


# Configs
FILE_PATH_CLIENT_LOCAL_CONFIG = os.path.join(DIR_CONFIG, "local_config.ini")
FILE_PATH_CLIENT_NETWORK_CONFIG = os.path.join(DIR_CONFIG, "client_net_config.ini")





ID_EXIT_BUTTON = -0xFF0AC
EXIT_BUTTON_TEXT = "Quit"





# Fonts
FILE_PATH_FONT_PD_SANS = os.path.join(DIR_RES_FONT, 'product_sans_regular.ttf')
FILE_PATH_FONT_PD_SANS_MEDIUM = os.path.join(DIR_RES_FONT, 'product_sans_medium.ttf')
FILE_PATH_FONT_PD_SANS_LIGHT = os.path.join(DIR_RES_FONT, 'product_sans_light.ttf')
FILE_PATH_FONT_AQUIRE = os.path.join(DIR_RES_FONT, 'aquire.otf')
FILE_PATH_FONT_AQUIRE_LIGHT = os.path.join(DIR_RES_FONT, 'aquire_light.otf')
FILE_PATH_FONT_AQUIRE_BOLD = os.path.join(DIR_RES_FONT, 'aquire_bold.otf')
