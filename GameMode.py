

from Resource import __get_won_display_info_offline_single_player, \
    __get_won_display_info_offline_multiplayer, \
    __get_won_display_info_online_multiplayer

class GameMode:



    def __init__(self, _id: int, display_name: str, online: bool, self_left_preference: bool,
                 won_display_info_provider):
        self.id = _id
        self.display_name = display_name
        # self.short_name = short_name
        self.online = online
        self.self_left_preference = self_left_preference
        self._won_display_info_provider = won_display_info_provider

    def get_won_display_info(self, self_won: bool, score_diff: int, enemy_name: str):
        return self._won_display_info_provider(self_won, score_diff, enemy_name)




# Game Modes
GAME_MODE_OFFLINE_SINGLE_PLAYER = GameMode(_id=0xFFF0,
                                           display_name="single player VS AI",
                                           online=False, self_left_preference=False,
                                           won_display_info_provider=__get_won_display_info_offline_single_player)

GAME_MODE_OFFLINE_MULTI_PLAYER = GameMode(_id=0xFFF1,
                                          display_name="Offline - 2 player",
                                          online=False, self_left_preference=True,
                                          won_display_info_provider=__get_won_display_info_offline_multiplayer)

GAME_MODE_ONLINE_MULTI_PLAYER = GameMode(_id=0xFFF2,
                                         display_name="Online - 2 Player",
                                         online=True, self_left_preference=False,  # self_left pref does not matter
                                         won_display_info_provider=__get_won_display_info_online_multiplayer)

GAME_MODE_DEFAULT = GAME_MODE_ONLINE_MULTI_PLAYER

GAME_MODES = [
    GAME_MODE_OFFLINE_SINGLE_PLAYER,
    GAME_MODE_OFFLINE_MULTI_PLAYER,
    GAME_MODE_ONLINE_MULTI_PLAYER
]


def load_game_mode(_id: int, default: GameMode = GAME_MODE_DEFAULT) -> GameMode:
    for gm in GAME_MODES:
        if gm.id == _id:
            return gm
    return default
