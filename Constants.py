# UI
DOUBLE_CLICK_MS = 200

# Message Types
MSG_TYPE_SESSION_WAITING = "0"
MSG_TYPE_SESSION_START = "1"
MSG_TYPE_COORDS_UPDATE = "2"
MSG_TYPE_SCORE_UPDATE = "3"
MSG_TYPE_COORDS_AND_SCORE_UPDATE = "4"
MSG_TYPE_ENEMY_LEFT = "5"


# Request Types
REQ_TYPE_NEW_PLAYER = "10"
REQ_TYPE_UPDATE_PLAYER_COORDS = "11"
REQ_TYPE_REMOVE_PLAYER = "20"


# States
CLIENT_SESSION_STATE_IDLE = 0
CLIENT_SESSION_STATE_CONNECTING = 1
CLIENT_SESSION_STATE_WAITING = 2
CLIENT_SESSION_STATE_RUNNING = 3
CLIENT_SESSION_STATE_ENEMY_LEFT = 4



# Game Update Results
GAME_UPDATE_RESULT_NORMAL = 1
GAME_UPDATE_RESULT_BALL_HIT_TOP_WALL = 10
GAME_UPDATE_RESULT_BALL_HIT_BOTTOM_WALL = 11
GAME_UPDATE_RESULT_BALL_HIT_PADDLE_LEFT = 20
GAME_UPDATE_RESULT_BALL_HIT_PADDLE_RIGHT = 30
GAME_UPDATE_RESULT_SCORE_UP_LEFT = 40
GAME_UPDATE_RESULT_SCORE_UP_RIGHT = 50
GAME_UPDATE_RESULT_WON_LEFT = 60
GAME_UPDATE_RESULT_WON_RIGHT = 70


def is_won(_update_result: int) -> bool:
    return _update_result == GAME_UPDATE_RESULT_WON_LEFT or _update_result == GAME_UPDATE_RESULT_WON_RIGHT


def is_score_changed(_update_result: int) -> bool:
    return _update_result == GAME_UPDATE_RESULT_SCORE_UP_LEFT \
           or _update_result == GAME_UPDATE_RESULT_SCORE_UP_RIGHT \
           or is_won(_update_result)
