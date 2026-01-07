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


def common_achievement(player_achievements: list[str, set]) -> set:
    """
    return a set w/ all the achievments present in at least one player list
    """
    common_set = player_achievements[0][1]
    for _, achievement in player_achievements[1:]:
        common_set = common_set.intersection(achievement)
    return common_set


def ultra_rare_achievement(player_achievements: list[str, set]) -> set:
    """
    return a set w/ only achivment obteine by one person
    """
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
    first_name, first_achievement = first_player
    second_name, second_achievement = second_player

    print(f"{first_name} vs {second_name} \
common: {first_achievement.intersection(second_achievement)}")
    print(f"{first_name} unique: \
{first_achievement.difference(second_achievement)}")
    print(f"{second_name} unique: \
{second_achievement.difference(first_achievement)}")


def achievement_tracker_tester():
    """
    A script that the the exercie w/ basic test and print it
    """
    print("=== Achievement Tracker System ===\n")

    for name, achievements in player_achievements:
        print(f"Player {name} achievments: {achievements}")

    print("\n=== Achievement Analytics ===")
    all_achievement = {each for _, st in player_achievements for each in st}
    print(f"All unique achievements: {all_achievement}")
    print(f"total Achievements: {len(all_achievement)}\n")

    print(f"Common to all players: {common_achievement(player_achievements)}")
    print(f"Rare achievements (1 player): \
{ultra_rare_achievement(player_achievements)}\n")
    competition(alice, bob)


if __name__ == "__main__":
    achievement_tracker_tester()
