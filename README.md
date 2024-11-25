# Diamond Price Prediction

## Overview

This project focuses on predicting the prices of diamonds based on various features such as carat, cut, color, clarity, and more. By leveraging machine learning algorithms, we aim to create a model that can accurately estimate the price of a diamond given its attributes.

## Introduction

Diamonds are one of the most valuable and sought-after gemstones. Their prices vary greatly depending on several factors such as carat weight, cut quality, color, and clarity. This project aims to develop a predictive model to estimate the price of a diamond based on these features.
### For Domain Knowledge you can visit a website which i have preferred earlier 
Website link :- https://www.americangemsociety.org/buying-diamonds-with-confidence ags-diamond-grading-system/

## Dataset

There are 10 independent variables (including `id`):

* `id` : unique identifier of each diamond
* `carat` : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
* `cut` : Quality of Diamond Cut
* `color` : Color of Diamond
* `clarity` : Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
* `depth` : The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)
* `table` : A diamond's table is the facet which can be seen when the stone is viewed face up.
* `x` : Diamond X dimension
* `y` : Diamond Y dimension
* `x` : Diamond Z dimension

Target variable:
* `price`: Price of the given Diamond.

### Dataset Source Link :
[https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv](https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv)

## Installation

To run this project, you need to have Python installed on your machine. You can install the required packages using `pip`:
just type in your terminal "pip install -r requirements.txt"

## Data Preprocessing

Applied DATA ENCODING on categorical columns like 
   * `cut` : Quality of Diamond Cut
   * `color` : Color of Diamond
   * `clarity` : Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
The DATA ENCODING technique Which is used in this project is `Ordinal and Label Encoding`
The ranking of each categorical columns are
`cut_categories` = ['Fair','Good','Very Good','Premium','Ideal']
`color_categories` = ['D','E','F','G','H','I','J']
`clarity_categories` = ['I1', 'SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2', 'IF', 'FL']
This is the exact ranking order which i have referred From the website :- https://www.americangemsociety.org/buying-diamonds-with-confidence ags-diamond-grading-system/

## Model Training

I have used multiple Machine Learning Models like 
* `LinearRegression`
* `RidgeRegression`
* `LassoRegression`
* `ElasticNet Regression`

### Performance of the Model

#### LinearRegression Model is training
#### mae : 701.8210523683321
#### rmse : 1080.2291894474297
#### r2_score : 92.83642124049126

#### Lasso Model is training
#### mae : 702.4736206129112
#### rmse : 1080.1873387587316
#### r2_score : 92.83697629843647

#### Ridge Model is training
#### mae : 701.8417403564985
#### rmse : 1080.2314311720318
#### r2_score : 92.83639150830561

#### ElasticNet Model is training
#### mae : 1074.4658387222544
#### rmse : 1559.8660512966787
#### r2_score : 85.06267481176508