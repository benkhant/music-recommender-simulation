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

    user_profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.88,
            "target_tempo_bpm": 128,
            "target_valence": 0.84,
            "target_danceability": 0.86,
            "target_acousticness": 0.20,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.38,
            "target_tempo_bpm": 78,
            "target_valence": 0.58,
            "target_danceability": 0.60,
            "target_acousticness": 0.80,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.92,
            "target_tempo_bpm": 150,
            "target_valence": 0.45,
            "target_danceability": 0.62,
            "target_acousticness": 0.12,
            "likes_acoustic": False,
        },
    }

    for profile_name, user_prefs in user_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\nTop recommendations for {profile_name}:\n")
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
