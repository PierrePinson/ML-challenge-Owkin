# ML-challenge-Owkin
## Pierre Pinson
All the code is in the notebook "Main Notebook Owkin challenge"
## Objective
The aim of this challenge is to perform survival analysis on censored data. 
We have for each patient of the dataset clinical features, radiomic features and segmented images.

## Data extraction
I didn't have time to implement a CNN. So I just merged radiomic and clinical features in a single dataset, and I extracted a number proportionnal to the number of tumorous cells by summing the segmentation masks. 
The functions for features extraction are in the python module "extract_features.py"

## Model comparison
I compared different models found in the litterature. First I tried a basic Random Forest to have an idea how data is separable. This model performed poorely with a c_index of 0.55 +-0.03.

Then I tried the Cox model that was the state of the art at the beginning of survival analysis. 
This model performed a decent score (c_index around 0.65)

I tried then a Random Forest model based on Cox model from the library pysurv. The c_index result was far better than the previous Cox model (c_index around 0.70)

I finally chose a two layer simple NN with a custom loss adapted to censored data, from the library [DeepSurv](https://arxiv.org/abs/1606.00931). The result was a little better than the random forest (**c_index around 0.71**). That is why I was surprised when I see a 0.55 score on the test set, and I am afraid I made an error writing the .csv file. Unfortunately I wasn't allowed to make an other submission.

## What else I could have done
I didn't use the radio images. I could have use them through a CNN. If I a had more time, I would have built a CNN, and add the clinical features after the max pooling and then do a regression on these features. 
