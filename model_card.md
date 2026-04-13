# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

Goal / Task: Recommend top songs that best match a user's stated preferences.

This recommender suggests songs based on a user's preferred genre, mood, and audio traits.
It is designed for classroom learning and small experiments.
It assumes users can describe their taste with simple preferences like target energy and acousticness.

Intended use:
- Learning how ranking systems work
- Trying different user profiles and seeing ranking changes

Non-intended use:
- Real medical, mental health, or safety decisions
- High-stakes personalization in production apps
- Representing full human music taste in a fair or complete way

---

## 3. How the Model Works  

The model compares each song to a user profile.
It gives points for exact genre and mood matches.
It also gives points when song values are close to user targets for energy, tempo, valence, danceability, and acousticness.
Then it adds a small bonus when acoustic preference matches (likes acoustic or low acoustic).
After scoring all songs, it sorts by score and returns the top results.
In my experiment, I lowered genre weight and increased energy influence to test sensitivity.

---

## 4. Data  

The dataset has 20 songs.
Each song has id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, and acousticness.
Genres include pop, lofi, rock, jazz, ambient, metal, house, classical, hip hop, and others.
This is a small dataset, so many tastes are missing (language preference, era, lyrics, culture, context, and personal history).

---

## 5. Strengths  

It works well when users have clear preferences.
It clearly separates opposite profiles, like Chill Lofi vs Deep Intense Rock.
It gives understandable reasons for each recommendation, so results are easier to inspect.
For the tested profiles, top songs often matched the expected vibe.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

One weakness I observed is an energy-driven filter bubble in the ranking logic. In my sensitivity experiment (lower genre weight + higher energy contribution), songs with close energy scores moved up even when they did not match the user's preferred genre, which can narrow recommendations around a single vibe. Because the model only adds positive similarity and does not include a diversity term or a mismatch penalty, users who want mixed or exploratory playlists may be under-served. This means the system can be "more similar" without being meaningfully more accurate for users whose taste depends on variety.

---

## 7. Evaluation  

I tested three profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock.
I compared their top-5 outputs and checked whether the recommendations matched each profile's vibe.
I also ran a small sensitivity experiment by lowering genre weight and increasing energy impact.
A key surprise was that Gym Hero often appeared for Happy Pop users because energy and danceability matched very closely, even when mood/genre match was not perfect.
I used pairwise profile comparisons in reflection.md to explain what changed and why it made sense.

---

## 8. Future Work  

1. Add a diversity rule so top results are not all the same style.
2. Add more user features (favorite artists, language, release era, skip history).
3. Learn weights from feedback instead of using fixed manual weights.

---

## 9. Personal Reflection  

My biggest learning moment was seeing how one weight change can shift the entire top-5 list.
AI tools helped me move faster by suggesting test profiles, edge cases, and clearer explanations, but I still had to double-check outputs by rerunning the program and reading the scoring logic line by line.
What surprised me most is that even a simple point-based algorithm can feel like a real recommendation system when the profile features are chosen well.
At the same time, it can sound convincing while still being biased, so I learned not to trust "good-looking" results without validation.
If I extend this project, I would add diversity controls, learn weights from user feedback, and test on a much larger dataset.
