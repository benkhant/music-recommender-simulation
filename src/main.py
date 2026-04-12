"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Specific taste profile used for content-based comparison.
    # Intentionally set near chill/lofi characteristics to contrast with intense rock.
    user_prefs = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.38,
        "target_tempo_bpm": 78,
        "target_valence": 0.58,
        "target_danceability": 0.60,
        "target_acousticness": 0.80,
        "likes_acoustic": True,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for index, rec in enumerate(recommendations, start=1):
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        reasons = [part.strip() for part in explanation.split(";") if part.strip()]

        print(f"{index}. {song['title']}")
        print(f"   Score  : {score:.2f}")
        print("   Reasons:")

        if reasons:
            for reason in reasons:
                print(f"   - {reason}")
        else:
            print("   - No strong feature matches")

        print()


if __name__ == "__main__":
    main()
