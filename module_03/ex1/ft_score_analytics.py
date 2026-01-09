import sys


def player_score_analytics_tester() -> None:
    """
    Basic tester for analystics
    """
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. \
    Usage: python3 ft_score_analytics.py <score1> <score2> ...")

    else:
        data = sys.argv[1:]
        scores = []
        try:
            for score in data:
                scores.append(int(score))
        except ValueError:
            print(f"Error in input data: '{score}' is not a number")
        else:
            print(f"Score Process: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}\n")


if __name__ == "__main__":
    player_score_analytics_tester()
