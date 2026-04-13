# Reflection on Profile Comparisons

I compared the outputs for each pair of user profiles to check whether the recommendations changed in a way that makes sense.

## High-Energy Pop vs Chill Lofi

High-Energy Pop returned bright, upbeat, high-energy songs like Sunrise City and Gym Hero, while Chill Lofi returned softer tracks like Midnight Coding and Library Rain. This makes sense because the lofi profile asks for lower energy and higher acousticness, so the system shifts away from dance-heavy songs.

## High-Energy Pop vs Deep Intense Rock

Both profiles often include Gym Hero, but for different reasons. For Happy Pop, Gym Hero appears because its energy and danceability are a very close fit, even though mood/genre are not a perfect match; for Deep Intense Rock, it appears because the profile also demands very high energy and low acousticness. In plain language: Gym Hero keeps showing up because the model rewards songs that are "close in feel" (high energy) very strongly.

## Chill Lofi vs Deep Intense Rock

Chill Lofi and Deep Intense Rock gave very different top results, which is what we want. Chill Lofi prefers calm, acoustic, mid-low tempo songs, while Deep Intense Rock favors loud, fast, low-acoustic tracks like Storm Runner and Kingdom Static. The gap between these outputs shows the model is at least sensitive to opposite listening intents.
