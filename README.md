# Hierarchical Vehicle Classification with Multi-Task Learning Group 44

![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

A PyTorch implementation of a hierarchical Multi-Task Learning (MTL) architecture for fine-grained vehicle classification. Using the **Stanford Cars Dataset**, this project demonstrates how enforcing taxonomic consistency (Make $\to$ Type $\to$ Model) significantly improves performance compared to standard flat classifiers.

**Final Result:** 88.57% Top-1 Accuracy (ResNet-50 backbone) with 97.64% Hierarchical Consistency.

## 📌 Project Overview

Distinguishing between visually similar car models (e.g., *BMW 3-Series Sedan* vs. *BMW 3-Series Coupe*) is a difficult fine-grained classification task. Standard "flat" classifiers often make illogical errors (e.g., predicting a "Toyota" make but a "Civic" model).

This project introduces a **3-Head ResNet-50** architecture that predicts **Make**, **Body Type**, and **Model** simultaneously. We employ advanced training strategies to bridge the semantic gap between coarse and fine-grained features.

### Key Techniques
* **Multi-Task Learning (MTL):** Three parallel heads sharing a ResNet-50 backbone.
* **Curriculum Learning:** A "Coarse-to-Fine" training schedule (freezing the Model head for initial epochs).
* **Hierarchical Label Smoothing (HLS):** Custom loss function that penalizes cross-family errors more than within-family errors.
* **Class Balancing:** Weighted loss to handle the long-tail distribution of rare cars.
* **Test Time Augmentation (TTA):** Robust inference using ensemble views.

## 📊 Performance Evolution

We conducted an extensive ablation study to isolate the impact of each technique.

| Phase | Configuration | Accuracy | Consistency | Key Insight |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Baseline (Frozen) | 41.72% | 100.0% | Baseline performance. |
| **2** | Fine-Tuned (Unfrozen) | 75.92% | 100.0% | Learned features, but ignored hierarchy. |
| **3** | Multi-Head (2-Head) | 77.20% | 90.44% | Structure helps, but heads conflict. |
| **4** | + Augmentation | 85.65% | 95.26% | Robustness prevents overfitting. |
| **5.5**| *Ablation: 2-Head + Curriculum* | *85.51%* | *95.77%* | *Proved necessity of the "Type" head.* |
| **7** | **3-Head + Curriculum** | **86.15%** | **95.21%** | **Synergy:** 3 heads + ordering > 2 heads. |
| **9** | + HLS & Scheduler | 87.95% | 97.66% | Convergence into sharp minimum. |
| **10**| **Final (with TTA)** | **88.57%** | **97.64%** | **Peak Performance.** |

## 🛠️ Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/fannarfreyr/Hierarchical-Vehicle-Classification-Group-44.git](https://github.com/fannarfreyr/Hierarchical-Vehicle-Classification-Group-44.git)
    cd your-repo-name
    ```

2.  **Install dependencies:**
    This project requires PyTorch, Torchvision, Scikit-Learn, Pandas, and Matplotlib.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Dataset Preparation:**
    We use the Stanford Cars Dataset hosted on GitHUb. You need to clone the repo and then move the data to the data folder.

    ```bash
    git clone https://github.com/jhpohovey/StanfordCars-Dataset.git
    mv StanfordCars/stanford_cars ./data/stanford_cars/

    ```

## 🚀 Usage

The entire training and evaluation pipeline is documented in `main.ipynb`.

1.  Open the notebook:
    ```bash
    jupyter notebook main.ipynb
    ```
2.  Run the cells sequentially. The notebook is structured to:
    * Load and preprocess data (with augmentation).
    * Train the Baseline model.
    * Train the Multi-Head models (Phases 3-9).
    * Generate evaluation metrics, confusion matrices, and Grad-CAM visualizations.

## 🖼️ Visuals

**Grad-CAM Analysis:**
*Top Row: Make Head Attention | Bottom Row: Model Head Attention*
*(Note: The Make head focuses on global shapes/grilles, while the Model head attends to specific trims/lights.)*

**Hierarchy Analysis:**
We evaluated the model not just on accuracy, but on **Consistency**: *Does the predicted Model actually belong to the predicted Make?* Our final model achieves **97.6% consistency**, effectively eliminating "Frankenstein" predictions.

## 👥 Authors

* **Fannar Freyr Jónuson**
* **Jendrik Engels**
* **András Szabolcs Gyüre**

*Course Project for Deep Learning for Visual Recognition @ Aarhus University.*
