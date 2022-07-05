from typing import List

from database import schemas
from database.models.player import PlayerMessage, BasePlayer
from services.helpers.helper import get_dict_from_model


def player_model_mapper(players: List[schemas.Player]) -> List[PlayerMessage]:
    """ Mapper for creating the PlayerMessage model """
    players_models = []
    for player in players:
        player_to_gives = player.gives_to
        players_models.append(PlayerMessage(
            name=player.name,
            username=player.username,
            social_url=player.social_url,
            gives_to=BasePlayer(
                name=player_to_gives.name,
                username=player_to_gives.username,
                social_url=player_to_gives.social_url,
            )
        ))
    return players_models


def forming_players_message(santa_code: int, players: List[schemas.Player]):
    """ Forming message about players """
    processed_players = player_model_mapper(players)
    dict_players = get_dict_from_model(processed_players)
    return [santa_code, ] + dict_players

