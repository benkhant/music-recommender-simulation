from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv
from pathlib import Path

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    songs: List[Dict] = []
    int_fields = {"id", "tempo_bpm"}
    float_fields = {"energy", "valence", "danceability", "acousticness"}
    path = Path(csv_path)

    if not path.is_absolute() and not path.exists():
        project_root = Path(__file__).resolve().parent.parent
        path = project_root / path

    with path.open(mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key in int_fields:
                    song[key] = int(value)
                elif key in float_fields:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against the user's preferences and return reasons."""
    score = 0.0
    reasons: List[str] = []

    # Phase-2 style weighted exact matches.
    genre_weight = 1.0
    mood_weight = 1.5

    favorite_genre = str(user_prefs.get("favorite_genre", "")).strip().lower()
    favorite_mood = str(user_prefs.get("favorite_mood", "")).strip().lower()
    song_genre = str(song.get("genre", "")).strip().lower()
    song_mood = str(song.get("mood", "")).strip().lower()

    if favorite_genre and song_genre == favorite_genre:
        score += genre_weight
        reasons.append(f"genre match (+{genre_weight:.1f})")

    if favorite_mood and song_mood == favorite_mood:
        score += mood_weight
        reasons.append(f"mood match (+{mood_weight:.1f})")

    # Numeric closeness: 1 - normalized distance, clamped to [0, 1].
    numeric_targets = {
        "energy": "target_energy",
        "tempo_bpm": "target_tempo_bpm",
        "valence": "target_valence",
        "danceability": "target_danceability",
        "acousticness": "target_acousticness",
    }
    tempo_range = 120.0

    for song_key, target_key in numeric_targets.items():
        if target_key not in user_prefs or song_key not in song:
            continue

        target = float(user_prefs[target_key])
        value = float(song[song_key])
        if song_key == "tempo_bpm":
            closeness = max(0.0, 1.0 - abs(value - target) / tempo_range)
        else:
            closeness = max(0.0, 1.0 - abs(value - target))

        contribution = closeness * 2.0 if song_key == "energy" else closeness
        score += contribution
        reasons.append(f"{song_key} closeness (+{contribution:.2f})")

    if "likes_acoustic" in user_prefs and "acousticness" in song:
        likes_acoustic = bool(user_prefs["likes_acoustic"])
        acousticness = float(song["acousticness"])
        if likes_acoustic and acousticness >= 0.6:
            score += 0.5
            reasons.append("acoustic preference match (+0.5)")
        elif not likes_acoustic and acousticness <= 0.4:
            score += 0.5
            reasons.append("low acoustic preference match (+0.5)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs, sort them, and return the top k recommendations."""
    scored = [
        (
            song,
            score,
            "; ".join(reasons) if reasons else "No strong feature matches",
        )
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    return sorted(scored, key=lambda item: item[1], reverse=True)[:k]
