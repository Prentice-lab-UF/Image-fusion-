# Image-fusion-
# Multi-Modal Image Fusion Workflow for MALDI Imaging Mass Spectrometry and Microscopy
This repository contains Python and MATLAB code used for the manuscript A multi-modal image fusion workflow incorporating MALDI imaging mass spectrometry and microscopy for the study of small pharmaceutical compound. The mass spectrometry image dataset used is in .imzML format, while the H&E and autofluorescence images are in TIF format.

## Workflow Overview

1. **Extract Ion Image:**
   - Run the Python script `extracting_ion_image_imzml.py` to extract the ion image of interest in .csv file from the .imzML format.

2. **Image Registration and Feature Extraction:**
   - Utilize the MATLAB image fusion code to register images and extract features from the H&E images.

3. **Regression Analysis:**
   - Perform linear regression and Partial Least Squares (PLS) regression using the MATLAB image fusion code.
   - Execute the Python script `regression_tree.py` for Random Forest regression.

4. **2-D CNN Model Training:**
   - Train the 2-D Convolutional Neural Network (CNN) model using the Python script `2D_CNN_imagefusion.py`.

## File Structure

- `extracting_ion_image_imzml.py`: Python script for extracting ion image from .imzML format.
- `matlab_image_fusion_code.docx`: MATLAB code for image registration, feature extraction, linear regression, and PLS regression.
- `regression_tree.py`: Python script for Random Forest regression.
- `2D_CNN_imagefusion.py`: Python script for training the 2-D CNN model.

## Dataset Format

- Mass spectrometry images: .imzML format.
- H&E and autofluorescence images: TIF format.

## Usage

1. Run `extracting_ion_image_imzml.py` to extract the ion image.
2. Execute `matlab_image_fusion_code.m` for image registration and feature extraction.
3. Perform regression analysis using `matlab_image_fusion_code.m` and `regression_tree.py`.
4. Train the 2-D CNN model by running `2D_CNN_imagefusion.py`.

## Dependencies

- Python 3.11
- MATLAB
- Required Python packages to install: Tensorflow (2.13.0), pyimzML
