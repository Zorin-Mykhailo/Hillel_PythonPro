from typing import Any

NAME = 'name'
AGE = 'age'
NUMB = 'number'


def get_name(player: dict, default: str = ""):
    return player[NAME] if NAME in player else default

def get_age(player: dict, default: int | None = None):
    return player[AGE] if AGE in player else default

def get_numb(player: dict, default: int | None = None):
    return player[NUMB] if NUMB in player else default


def player_repr(player: dict, verbose: bool) -> str:
    return f'{get_numb(player):>5} │ {get_name(player):30} │ {get_age(player):>3} '
    
    

def players_repr(players: list[dict], verbose: bool) -> None:
    if verbose:
        header: str = f'Players ({len(players)})' 
        print(f'{header:^40}')
    return f'{get_numb(player):>5} │ {get_name(player):30} │ {get_age(player):>3} '
    for player in players:
        print(player_repr(player, verbose))
        #print(f"{player['name']=}, {player['age']=}")


def players_add(players: list[dict], player: dict) -> list[dict]:
    ...


def players_del(players: list[dict], name: str) -> list[dict]:
    ...


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    ...


def players_get_by_name(players: list[dict], name: str) -> dict | None:
    """If multiple players with same name - return the first one."""


def main():
    team = [
        {"name": "John", "age": 20, "number": 1},
        {"name": "Marry", "age": 33, "number": 3},
        {"name": "Cavin", "age": 33, "number": 12},
    ]

    players_repr(team, True)
    return

    players_33: list[dict] = players_find(players=team, field="age", value=33)

    options = ["repr", "add", "del", "find", "get", "exit"]

    while True:
        if not (user_input := input(f"Enter your choice {options}:")):
            break

        if user_input == "add":
            # players_add(...)
            ...


if __name__ == "__main__":
    main()