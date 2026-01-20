from ex4.TournamentCard import TournamentCard


class TournamentPlatform:  # Platform Management
    def __init__(self):
        self.id_players = {}
        self.matches_played = 0
        self.platform_status = "active"

    def register_card(self, card: TournamentCard) -> str:
        if card.player_id in self.id_players:
            raise Exception("Card allready register")
        self.id_players[card.player_id] = card

        print(f"{card.info['name']} (ID: {card.player_id})")
        print("- Rating:", card.base_rating)
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Record: {card.win}-{card.losse}")
        print()

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.id_players or card2_id not in self.id_players:
            raise Exception("At least one card is not register")

        p1_atk = self.id_players[card1_id].attack(self.id_players[card2_id])
        p2_atk = self.id_players[card2_id].attack(self.id_players[card1_id])
        p1_dmg_taken = self.id_players[card1_id].defend(p2_atk["dmg send"])
        p2_dmg_taken = self.id_players[card2_id].defend(p1_atk["dmg send"])

        winner = self.id_players[card2_id if p1_dmg_taken["dmg_taken"] <=
                                 p2_dmg_taken["dmg_taken"] else card1_id]
        winner.update_wins(1)
        loser = self.id_players[card1_id if p1_dmg_taken["dmg_taken"] <=
                                p2_dmg_taken["dmg_taken"] else card2_id]
        loser.update_losses(1)

        match_result = {
            "winner": winner.player_id,
            "loser": loser.player_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }
        self.matches_played += 1
        return match_result

    def get_leaderboard(self) -> list:
        pos = sorted([value for value in self.id_players.values()],
                     key=lambda x: x.calculate_rating(), reverse=True)

        print("Tournament Leaderboard")
        for position, player in enumerate(pos):
            print(f"{position + 1}. {player.info['name']}"
                  f" - Rating: {player.calculate_rating()} "
                  f"({player.win} - {player.losse})")

        return pos

    def generate_tournament_report(self) -> dict:
        report = {
            "total_cards": len(self.id_players),
            "matches_played": self.matches_played,
            "avg_rating": sum(card.calculate_rating()
                              for card in
                              self.id_players.values()) // len(
                                  self.id_players),
            "platform_status": self.platform_status
        }
        return report
