import pandas as pd
import matplotlib.pyplot as plt

# Load your normalized AU06/AU12 intensity file
df = pd.read_csv("openface_output/interview_normalized.csv")

# Threshold for smile
threshold = 2.5

# Frame rate (OpenFace default is 30 FPS, adjust if needed)
fps = 30
frame_duration = 1/30

# Identify frames where both AU06 and AU12 >= 2.5
smile_mask = (df["AU06_norm"] >= threshold) & (df["AU12_norm"] >= threshold)

# Calculate smile duration in seconds
smile_frame_count = smile_mask.sum()
smile_duration_seconds = smile_mask.sum() * frame_duration
smile_strength = ((df["AU06_norm"] + df["AU12_norm"]) * smile_mask).sum() * frame_duration


# calculate the unit time one
total_duration = len(df) * frame_duration
smile_strength_per_second = smile_strength / total_duration

# Convert frame index to time (seconds)
frame_duration = 0.033  # seconds per frame
df["time_sec"] = df.index * frame_duration

# Plotting AU06 and AU12 normalized intensities over time
plt.figure(figsize=(10, 5))
plt.plot(df["time_sec"], df["AU06_norm"], label="AU06 (cheek raise)", linewidth=1.5)
plt.plot(df["time_sec"], df["AU12_norm"], label="AU12 (lip corner pull)", linewidth=1.5)
plt.axhline(2.5, color="red", linestyle="--", label="Smile Threshold = 2.5")

plt.title("Smile Intensity Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Normalized Intensity (0–5)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print(f"Smile Duration: {smile_duration_seconds:.2f} seconds")
print(f"Smile Strength (AU06 + AU12): {smile_strength:.2f}")
print(f"Smile Strength per Second: {smile_strength_per_second:.2f}")

