"""
3. kodune ülesanne.
Eesmärk on anda kasutajale n.ö. pseudo mängukonsool, kus ta saab valida mingit mängu, mida mängida.
1. ülesandeks on lõpetada ära kahe klassi meetodi play() sisu:
Trips Traps Trull ja Kivi Paber Käärid
play sisu siis võiks panna vastava mängu mängima
kivi paber käärid mäng on player vs computer
Trips Traps Trull käib kahe mängija vahel, sinna pole vaja hakata välja mõtlema AI vastast (kui viitsimist on siis miks mitte)

Kivi paber käärid mängu üks sessioon ei koosne ainult ühest kordusest. Kasutaja käest küsitakse peale igat kordust,
kas ta soovib uuesti mängida. Lisaks hoitakse mälus mängu seisu, palju mängija on võitnud, palju on viike jne.
Trips Traps Trullil neid nõudmisi pole.

2. ülesandeks on lisada juurde veel omal valikul 2 mängu sama loogika põhjal mis eelmised
Kui ei suuda välja mõelda ühtegi mängu, siis võid asendada need 2 mängu ussimänguga (see kus uss kasvab kui õuna sööd ja saad punkte).
Ühtegi pythonivälist raamistiku ei tohi siinkohal kasutada (näiteks "pygame"). Ainuke lubatud raamistik on "keyboard" klaviatuuri sisendi saamiseks.
Oma lisatud mäng(ud) peab saama samast kohast käivitada kus teised lähevad käima.

Ülesande lahendus on parem siis, kui klassidest väljaspoole pole pandud ühtegi koodirida.
Lisaks: See, mis on minu poolt ette antud, see peab jääma alles.
"""
from typing import Dict


"""This is base class for a game."""
class Game:
    def __init__(self, name: str):
        self.name = name

    def play(self):
        raise NotImplementedError()

    def get_name(self):
        return self.name


class TicTacToe(Game):
    def __init__(self):
        super().__init__("Tic Tac Toe")

    def play(self):
        ## TODO:
        print("Tic Tac Toe")


class RockPaperScissors(Game):
    def __init__(self):
        super().__init__("Rock Paper Scissors")

    def play(self):
        ## TODO:
        print("rock paper scissors")


if __name__ == '__main__':
    games: Dict[str, Game] = {
        '1': RockPaperScissors(),
        '2': TicTacToe()
    }

    for game in games:
        print(f"{game}) {games[game].get_name()}")
    choice = input("Choose game: ")
    if choice in games:
        games[choice].play()
    else:
        print(f"Choice {choice} is not defined!")
