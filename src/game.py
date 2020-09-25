from typing import List

from src import config


class Game:
    EMPTY_CELL = ' '
    TO_CONNECT = 4

    def __init__(self, x_length: int, y_length: int, players_signs: List[str]) -> None:
        self.columns = y_length
        self.rows = x_length
        self.board = [
            [Game.EMPTY_CELL for _ in range(x_length)]
            for _ in range(y_length)
        ]
        self.players = players_signs

    def render(self) -> str:
        res = ''
        for line in self.board:
            for cell in line:
                res += f'[{cell}]'
            res += '\n'
        return res

    def read_column(self, player_sign: str) -> int:
        while True:
            column = input(f"{player_sign}, please input correct column number: ")
            try:
                column = int(column)
            except ValueError:
                pass
            else:
                if 0 <= column < self.columns:
                    return column

    def shoot(self, player_sign: str, column: int) -> None:
        for line in reversed(self.board):
            if line[column] == Game.EMPTY_CELL:
                line[column] = player_sign
                return
        raise ValueError(f"Cannot shoot column {column}, it's full")

    def make_turn(self, player_sign: str) -> None:
        while True:
            column = self.read_column(player_sign)
            try:
                return self.shoot(player_sign, column)
            except ValueError:
                print(f"{player_sign}, you cannot shoot at column {column}, it's full!")

    def check_endgame(self) -> bool:
        def check_up(i: int, j: int) -> bool:
            for inc in range(1, Game.TO_CONNECT):
                if i + inc >= self.rows or self.board[i][j] != self.board[i + inc][j]:
                    return False
            return True

        def check_right(i: int, j: int) -> bool:
            for inc in range(1, Game.TO_CONNECT):
                if j + inc >= self.columns or self.board[i][j] != self.board[i][j + inc]:
                    return False
            return True

        def check_up_right(i: int, j: int) -> bool:
            for inc in range(1, Game.TO_CONNECT):
                if (
                        i + inc >= self.rows or
                        j + inc >= self.rows or
                        self.board[i][j] != self.board[i + inc][j + inc]
                ):
                    return False
            return True

        def check_up_left(i: int, j: int) -> bool:
            for inc in range(1, Game.TO_CONNECT):
                if (
                        i + inc >= self.rows or
                        j - inc < 0 or
                        self.board[i][j] != self.board[i + inc][j - inc]
                ):
                    return False
            return True

        for x in range(self.rows):
            for y in range(self.columns):
                if self.board[x][y] != ' ':
                    if any((
                            check_up(x, y),
                            check_right(x, y),
                            check_up_right(x, y),
                            check_up_left(x, y),
                    )):
                        return True

        return False

    def play(self) -> None:
        print(self.render())
        turn_number = 0

        while turn_number < self.columns * self.rows:
            current_player = self.players[turn_number % len(self.players)]
            turn_number += 1
            self.make_turn(current_player)

            print(self.render())
            if self.check_endgame():
                print(
                    f"Congratulations, {current_player}!\n"
                    f"You won in {turn_number} turns!"
                )
                return


def main():
    game = Game(config.X, config.Y, config.PLAYERS_SIGNS)
    game.play()


if __name__ == '__main__':
    main()
