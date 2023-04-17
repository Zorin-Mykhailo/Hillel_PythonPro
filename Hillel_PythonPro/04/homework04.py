from lib2to3.pgen2.token import NUMBER
from typing import Any
from helpers import ColumnInfo, StrHelper, UsrInput

NAME = "name"
AGE = "age"
NUMB = "number"


# def get_name(player: dict, default: str = ""):
#    return player[NAME] if NAME in player else default


# def get_age(player: dict, default: int | None = None):
#    return player[AGE] if AGE in player else default


# def get_numb(player: dict, default: int | None = None):
#    return player[NUMB] if NUMB in player else default


def as_view_str(title: str, records: list[dict]) -> str:
    _str_table = StrHelper.as_table(
        title,
        records,
        [
            ColumnInfo(">Number", lambda e: str(e["number"])),
            ColumnInfo("Name", lambda e: e["name"]),
            ColumnInfo(">Age", lambda e: str(e["age"])),
        ],
    )
    return _str_table


def players_repr(players: list[dict], verbose: bool) -> None:
    table_header = "List of team members" if verbose else "Players"
    print(as_view_str(table_header, players))


def players_add(players: list[dict], player: dict) -> list[dict]:
    if players is None:
        raise Exception("players is None")
    if player is None:
        raise Exception("Player is None")
    players.append(player)
    return players


def players_index(players: list[dict], field: str, value: Any) -> int:
    if players is None:
        raise Exception("players is None")
    if value is None:
        raise Exception("value is None")
    _indexes = []
    _index = 0
    _value = None
    while _index < len(players):
        _player = players[_index]
        if field.lower() == NAME:
            _value = _player[NAME] if NAME in _player else None
        elif field.lower() == AGE:
            _value = str(_player[AGE]) if AGE in _player else None
        elif field.lower() == NUMBER:
            _value = str(_player[NUMBER]) if NUMBER in _player else None
        else:
            raise Exception(f'Field "{field}" is unknown')
        if _value.lower() == value.lower():
            _indexes.append(_index)
        _index += 1
    return _indexes


def players_del(players: list[dict], name: str) -> list[dict]:
    _indexes = players_index(players, NAME, name)
    if len(_indexes) == 0:
        return players
    players.pop(_indexes[0])
    return players


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    _indexes = players_index(players, field, value)
    _founded_players = []
    for index in _indexes:
        _founded_players.append(players[index])
    return _founded_players


def players_get_by_name(players: list[dict], name: str) -> dict | None:
    """If multiple players with same name - return the first one."""
    _indexes = players_index(players, NAME, name)
    if len(_indexes) == 0:
        return None
    return players[_indexes[0]]


def main():
    team = [
        {"name": "John", "age": 20, "number": 1},
        {"name": "Marry", "age": 33, "number": 3},
        {"name": "Cavin", "age": 33, "number": 12},
    ]

    options = ["repr", "add", "del", "find", "get", "exit"]
    available_fields = [NUMB, NAME, AGE]

    while True:
        match UsrInput.get_str(f"\n\nEnter your choice {options}", None, options):
            case "repr":
                players_repr(team, False)
            case "add":
                print("New player")
                _number = UsrInput.get_number(" - number")
                _name = UsrInput.get_str(" - name  ", 3)
                _age = UsrInput.get_number(" - age   ")
                _new_player = {NAME: _name, AGE: _age, NUMB: _number}
                players_repr(players_add(team, _new_player), True)
            case "del":
                _player_name = UsrInput.get_str("Player name", 1)
                players_repr(players_del(team, _player_name), False)
            case "find":
                _field_name = UsrInput.get_str(
                    f"Field name (from {available_fields})", None, available_fields
                )
                _value = UsrInput.get_str("Field value")
                _founded_players = players_find(team, _field_name, _value)
                players_repr(_founded_players, True)
            case "get":
                _player_name = UsrInput.get_str("Player name", 1)
                _founded_player = players_get_by_name(team, _player_name)
                if _founded_player is None:
                    print("No one player found")
                else:
                    players_repr([_founded_player], True)
            case "exit":
                print("Program exit")
                break


if __name__ == "__main__":
    main()
