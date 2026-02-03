# Duchenne Smile Detection (OpenFace)

This project detects **Duchenne smiles** by extracting facial Action Units
(AU6 and AU12) using **OpenFace**, then computing smile **duration** and
**intensity** from video input.

---

## Requirements
- macOS or Linux
- Python 3
- git
- cmake
- OpenCV

---

## Step 1: Install OpenFace (one time)

```bash
git clone https://github.com/TadasBaltrusaitis/OpenFace.git
cd OpenFace
mkdir build && cd build
cmake ..
make

git clone git@github.com:Lydia-xinger/Duchenne-smile-MASL.git
cd Duchenne-smile-MASL

chmod +x run_openface_duchenne.sh
./run_openface_duchenne.sh path/to/video.mp4


---

### Save the file
- Press **Ctrl + O**
- Press **Enter**
- Press **Ctrl + X**

---

## Commit and push the README

```bash
git add README.md
git commit -m "Add README with usage instructions"
git push
