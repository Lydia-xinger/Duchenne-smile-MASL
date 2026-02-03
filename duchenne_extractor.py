import sys
import pandas as pd
import os

out_dir = "/Users/lixinger/OpenFace/build/openface_output"


# Directly load the known CSV
df = pd.read_csv("/Users/lixinger/OpenFace/build/openface_output/test.csv")
# Check if required columns exist
required_cols = ['AU06_c', 'AU12_c', 'AU06_r', 'AU12_r']
missing_cols = [col for col in required_cols if col not in df.columns]
if missing_cols:
    print(f"Missing columns in OpenFace output: {', '.join(missing_cols)}")
    sys.exit(1)

# Create new column for Duchenne smile: both AU06_c and AU12_c are active
df['duchenne_smile'] = (df['AU06_c'] == 1) & (df['AU12_c'] == 1)

# Rename intensity columns (optional: remove leading spaces)
df.rename(columns={
    'AU06_r': 'AU06_intensity',
    'AU12_r': 'AU12_intensity'
}, inplace=True)

# Keep only relevant columns
output_df = df[['frame', 'duchenne_smile', 'AU06_intensity', 'AU12_intensity']]

# Save result
output_path = f"./openface_output/duchenne_result.csv"
output_df.to_csv(output_path, index=False)
print(f"Saved filtered result to: {output_path}")


