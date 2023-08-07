# Diagnosis-of-Retinal-Diseases-from-OCT-Images

## Table of Contents

1. [Introduction](#introduction)
2. [Dataset Description](#Dataset-Description)
3. [Problem Statement](#Problem-Statement)
4. [Evaluation Matrix](#Evaluation-Matrix)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Performance](#Performance)
8. [Accuracy & Loss Graphs](#Accuracy-&-Loss-Graphs)

## Introduction

The "Diagnosis of Retinal Diseases from OCT Images" project aims to develop a deep learning-based approach for classifying retinal OCT images into one of the four categories: CNV, DME, DRUSEN, and NORMAL. Optical Coherence Tomography (OCT) is an imaging technique used to capture high-resolution cross-sections of living patents' retinas, enabling ophthalmologists to visualize different layers and diagnose various eye disorders.

OCT has become the standard method for examining and treating most eye problems, and its usage has led to the generation of millions of OCT scans annually. The interpretation of these images is time-consuming, making it essential to develop an automated classification system to aid ophthalmologists in their diagnosis.

## Dataset Description

The dataset used for this project contains 84,495 X-ray images (JPEG) divided into three folders: train, test, and validation. Each folder consists of subfolders for each image category, namely NORMAL, CNV, DME, and DRUSEN. The image filenames are labeled in the format (disease)-(randomized patient ID)-(image number by this patient).

## Problem Statement

The main objective of this project is to build a deep learning model that can accurately classify retinal OCT images into one of the four categories: CNV, DME, DRUSEN, or NORMAL. The model will be trained on the training data and evaluated on the test data to assess its performance.

## Evaluation Matrix

The performance of the classification model will be evaluated using a confusion matrix. The confusion matrix provides a summary of how well the model predicts different categories and helps identify the types of errors made by the classifier. It calculates True Positive (TP), True Negative (TN), False Positive (FP), and False Negative (FN) values for each class.

## Installation

```
pip install -r requirements.txt
```

## Usage

```
streamlit run app.py
```

## Performance

| Model Name                                              | Train Accuracy | Validation Accuracy | Test Accuracy |
| ------------------------------------------------------- | -------------- | ------------------- | ------------- |
| 3CNN (without Image Augmentation)                       | 0.9355         | 0.8916              | 0.9277        |
| 3CNN (with Image Augmentation)                          | 0.9121         | 0.7046              | 0.6560        |
| 7CNN (with Image Augmentation)                          | 0.9636         | 0.8816              | 0.9638        |
| VGG16 Transfer Learning (with Image Augmentation)       | 0.8886         | 0.8876              | 0.9039        |
| ResNet50 Transfer Learning (with Image Augmentation)    | 0.9171         | 0.93663             | 0.9618        |
| DenseNet121 Transfer Learning (with Image Augmentation) | 0.9479         | 0.9342              | 0.9845        |

## Accuracy & Loss Graphs

| Models                                  | Accuracy & Loss Graphs                                                                                                                                                                                                         |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 3 Layers CNN With Image Augmentation    | ![CNN with Image Augmentation](https://github.com/CS-Aditya-Rawat/Diagnosis-of-Retinal-Diseases-from-OCT-Images-/blob/main/Accuracy&Loss_graphs/3_CNN/with_augmentation/Screenshot_2023-08-06-12-57-36_1920x1080.png?raw=true) |
| 3 Layers CNN Without Image Augmentation | ![Model 2](https://github.com/CS-Aditya-Rawat/Diagnosis-of-Retinal-Diseases-from-OCT-Images-/blob/main/Accuracy&Loss_graphs/3_CNN/without_augmentation/Screenshot_2023-08-06-12-56-22_1920x1080.png?raw=true)                  |
| 7 layers CNN with Image Augmentation    | ![Model 3](https://github.com/CS-Aditya-Rawat/Diagnosis-of-Retinal-Diseases-from-OCT-Images-/blob/main/Accuracy&Loss_graphs/7_CNN/Screenshot_2023-08-06-13-03-18_1920x1080.png?raw=true)                                       |
| VGG 16                                  | ![Model 4](https://github.com/CS-Aditya-Rawat/Diagnosis-of-Retinal-Diseases-from-OCT-Images-/blob/main/Accuracy&Loss_graphs/VGG_16/Screenshot_2023-08-06-00-28-06_1920x1080.png?raw=true)                                      |
| ResNet50                                | ![Model 5](https://github.com/CS-Aditya-Rawat/Diagnosis-of-Retinal-Diseases-from-OCT-Images-/blob/main/Accuracy&Loss_graphs/ResNet50/Screenshot_2023-08-06-13-00-30_1920x1080.png?raw=true)                                    |
| DenseNet121                             | ![Model 6](https://github.com/CS-Aditya-Rawat/Diagnosis-of-Retinal-Diseases-from-OCT-Images-/blob/main/Accuracy&Loss_graphs/DenseNet121/Screenshot_2023-08-06-13-01-48_1920x1080.png?raw=true)                                 |
