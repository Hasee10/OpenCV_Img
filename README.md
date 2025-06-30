# 🖼️ OpenCV Image Processing Project

![OpenCV Logo](https://upload.wikimedia.org/wikipedia/commons/3/32/OpenCV_Logo_with_text_svg_version.svg)

> A modern, modular image processing toolkit built using **Python** and **OpenCV**.

---

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Tech](https://img.shields.io/badge/Built%20With-Python%20%7C%20OpenCV-blue)
![License](https://img.shields.io/badge/License-MIT-purple)

---

## 📖 Overview

**OpenCV_Img** is a collection of image processing scripts and utilities built with `OpenCV` in Python. It includes ready-to-use tools for:

- Edge detection
- Color filters
- Thresholding
- Contour detection
- Morphological transformations
- Perspective transforms
- Document scanning

Whether you're prototyping, building a vision-based tool, or exploring computer vision — this repo gets you started.

---

## 🎥 Demo (Optional GIF)

> Add your demo GIF here (e.g. a before/after or real-time filter preview):

```markdown
![Demo](assets/demo.gif)
````

You can use [ScreenToGif](https://www.screentogif.com/) to record your screen and place the `.gif` under `/assets`.

---

## 🧪 Features

* ✅ Live webcam capture & frame processing
* 🧠 Modular code for filter pipelines
* 🎨 Real-time color and edge detection
* 📄 Document scanning using perspective transform
* 📷 Image reading and saving utilities

---

## 🛠 Tech Stack

| Component     | Tool / Library        |
| ------------- | --------------------- |
| Language      | Python 3.x            |
| Image Library | OpenCV (cv2)          |
| UI (optional) | Tkinter / PyQt5 (TBD) |
| IDE           | VS Code / Jupyter     |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:Hasee10/OpenCV_Img.git
cd OpenCV_Img
```

### 2. Set Up a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn't exist, just install manually:

```bash
pip install opencv-python
```

### 4. Run the Project

```bash
python main.py
```

---

## 🧾 Folder Structure

```bash
OpenCV_Img/
│
├── src/                  # Main processing modules
│   ├── filters.py
│   ├── scanner.py
│   └── utils.py
│
├── assets/               # Demo images, GIFs
├── main.py               # Entry point
├── README.md
└── requirements.txt
```

---

## ✅ Example Usage

```python
import cv2
from src.filters import apply_edge_detection

img = cv2.imread('assets/sample.jpg')
edges = apply_edge_detection(img)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 🤝 Contributing

Contributions are welcome! Here’s how:

1. Fork the repo
2. Create your feature branch:

   ```bash
   git checkout -b feature/new-filter
   ```
3. Commit your changes and push
4. Open a Pull Request

---

## 📜 License

Licensed under the [MIT License](LICENSE).

---

## 🙋 About the Author

**Muhammad Haseeb Arshad**
Python & Computer Vision Enthusiast | Data Science Undergraduate
📫 [LinkedIn](https://linkedin.com/in/haseebarshad10)
📧 [ihaseebarshad10@gmail.com](mailto:ihaseebarshad10@gmail.com)

---
> 🧠 “See beyond pixels — automate with vision.”
---
