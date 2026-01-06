alice = ("alice", {
    'first_kill',
    'level_10',
    'treasure_hunter',
    'speed_demon'
})
bob = ("bob", {
    'first_kill',
    'level_10',
    'boss_slayer',
    'collector'
})
charlie = ("charlie", {
    'level_10',
    'treasure_hunter',
    'boss_slayer',
    'speed_demon',
    'perfectionist'
})
player_achievements = [alice, bob, charlie]


def commonAchievement(player_achievements: list[str, set]) -> set:
    common_set = player_achievements[0][1]
    for _, achievement in player_achievements[1:]:
        common_set = common_set & achievement
    return common_set


def ultraRareAchievement(player_achievements: list[str, set]) -> set:
    seen_once = set()
    seen_many_time = set()

    for _, achievements in player_achievements:
        for achievement in achievements:
            if achievement not in seen_many_time:
                if achievement in seen_once:
                    seen_once.remove(achievement)
                    seen_many_time.add(achievement)
                else:
                    seen_once.add(achievement)
    return seen_once


def competition(first_player: tuple, second_player: tuple) -> None:
    """
    competition b/w two player
    """
    print(f"{first_player[0]} vs {second_player[0]} \
common: {first_player[1] & second_player[1]}")
    print(f"{first_player[0]} unique: {first_player[1] - second_player[1]}")
    print(f"{second_player[0]} unique: {second_player[1] - first_player[1]}")


def AchievementTrackerTester():
    print("=== Achievement Tracker System ===\n")

    for name, achievements in player_achievements:
        print(f"Player {name} achievments: {achievements}")

    print("\n=== Achievement Analytics ===")
    all_achievement = {each for _, st in player_achievements for each in st}
    print(f"All unique achievements: {all_achievement}")
    print(f"total Achievements: {len(all_achievement)}\n")

    print(f"Common to all players: {commonAchievement(player_achievements)}")
    print(f"Rare achievements (1 player): \
{ultraRareAchievement(player_achievements)}\n")
    competition(alice, bob)


if __name__ == "__main__":
    AchievementTrackerTester()
