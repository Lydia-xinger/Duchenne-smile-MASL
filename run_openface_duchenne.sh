#!/bin/bash
# Usage: ./run_openface_duchenne.sh /path/to/video.mp4

VIDEO=$1
OUTDIR="./openface_output"

# Make sure output directory exists
mkdir -p "$OUTDIR"

# Run OpenFace
~/OpenFace/build/bin/FeatureExtraction -f "$1" -aus -out_dir ~/OpenFace/build/openface_output


# Run the Python processing
python3 /Users/lixinger/OpenFace/duchenne_extractor.py /Users/lixinger/OpenFace/build/openface_output


