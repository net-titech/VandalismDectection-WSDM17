# WSDM Cup 2017: Valdalism Detection

![WSDM Cup 2017](https://pbs.twimg.com/profile_images/580289463374352384/Umr5vfDV_400x400.png)

Vandalism detection (task 2) - WSDM Cup 2017

## Introduction

We are a team of 4 from Complex Network Research Group 
(Murata Laboratory) - Tokyo Insitute of Technology. This repository
is our submission to the 2017 WSDM Cup. In summary, the task is to
detect vandalism in Wikidata dumps.

## Milestones

### Preparation: 2016/09/26 - 2016/09/30

#### Objective

1. Setup personal computer to match each others. (Python 3.5.2, Tensorflow 0.10, scikit-learn 0.17.1, Anaconda virtual env, coding style, etc.)
2. Literature review. (Paper listing, reading, and discussion)
3. Competition score metric analysis.
4. Finalize and present possible approaches.

#### Daily log

1. 27th: List of vandalism detection papers; setup working environments; study wikidata dumps; analyze WSDM'17 score metrics.
2. 28th: Paper reading; discussion about Random Forest and features selection; focusing on Random Forest model and its variations.
3. 29th: Run the provided reference paper's code on the lab's machine; study related techniques to RR; study NN techiqnues that complement RR.
4. 30th: Review week 1.

### Baseline model: 2016/10/03 - 2016/10/07

#### Objective

1. Preprocess wikimedia data, study previous features extration code.
2. Implement simple random forest model based on [1].
3. Working baseline model and sketch of neural network model.

#### Daily log

1. 3rd: Features from the baseline model [1] are all hand-picked. 
2. 4th: Meeting cancelled.
3. 5th: Meeting cancelled.
4. 6th: Some features are missing compared to the original implementation [1]. Using only 29 available features now yeilds 0.02 on ROC. This result is extremely low. 
5. 7th:
