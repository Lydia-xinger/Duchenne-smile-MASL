import pandas as pd
import os

base_path = "/Users/lixinger/OpenFace/openface_output"

def load_and_extract(path):
    df = pd.read_csv(path)
    df = df.rename(columns={"AU06_r": "AU06_intensity", "AU12_r": "AU12_intensity"})
    return df[["AU06_intensity", "AU12_intensity"]]

# Load and extract
neutral = load_and_extract(os.path.join(base_path, "neutral.csv"))
maximum = load_and_extract(os.path.join(base_path, "maximum.csv"))
interview = load_and_extract(os.path.join(base_path, "interview.csv"))

# Calculate calibration values
AU06_min = neutral["AU06_intensity"].mean()
AU12_min = neutral["AU12_intensity"].mean()
AU06_max = maximum["AU06_intensity"].max()
AU12_max = maximum["AU12_intensity"].max()

def normalize(x, min_val, max_val):
    return max(0, min(5, (x - min_val) / (max_val - min_val) * 5)) if max_val != min_val else 0

# Normalize
interview["AU06_norm"] = interview["AU06_intensity"].apply(lambda x: normalize(x, AU06_min, AU06_max))
interview["AU12_norm"] = interview["AU12_intensity"].apply(lambda x: normalize(x, AU12_min, AU12_max))

# Save
interview.to_csv(os.path.join(base_path, "interview_normalized.csv"), index=False)
print("✅ Saved normalized AU06 and AU12 to interview_normalized.csv")

