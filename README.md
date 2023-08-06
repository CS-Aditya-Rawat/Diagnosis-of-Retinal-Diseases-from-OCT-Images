# Diagnosis-of-Retinal-Diseases-from-OCT-Images

## Overview

The "Diagnosis of Retinal Diseases from OCT Images" project aims to develop a deep learning-based approach for classifying retinal OCT images into one of the four categories: CNV, DME, DRUSEN, and NORMAL. Optical Coherence Tomography (OCT) is an imaging technique used to capture high-resolution cross-sections of living patents' retinas, enabling ophthalmologists to visualize different layers and diagnose various eye disorders.

OCT has become the standard method for examining and treating most eye problems, and its usage has led to the generation of millions of OCT scans annually. The interpretation of these images is time-consuming, making it essential to develop an automated classification system to aid ophthalmologists in their diagnosis.

## Dataset Description

The dataset used for this project contains 84,495 X-ray images (JPEG) divided into three folders: train, test, and validation. Each folder consists of subfolders for each image category, namely NORMAL, CNV, DME, and DRUSEN. The image filenames are labeled in the format (disease)-(randomized patient ID)-(image number by this patient).

## Problem Statement

The main objective of this project is to build a deep learning model that can accurately classify retinal OCT images into one of the four categories: CNV, DME, DRUSEN, or NORMAL. The model will be trained on the training data and evaluated on the test data to assess its performance.

## Evaluation Matrix

The performance of the classification model will be evaluated using a confusion matrix. The confusion matrix provides a summary of how well the model predicts different categories and helps identify the types of errors made by the classifier. It calculates True Positive (TP), True Negative (TN), False Positive (FP), and False Negative (FN) values for each class.
