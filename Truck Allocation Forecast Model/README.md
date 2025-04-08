# Random Data Model Evaluation

## Overview
This project evaluates the performance of different machine learning models (Linear Regression and Random Forest) on randomly generated data. The aim is to explore how well these models can generalize to data without a clear underlying pattern.

## Tools and Libraries
- Python
- Pandas
- Scikit-learn
- Matplotlib

## Dataset
The data used in this project is synthetic and random. It includes multiple features such as `U_d`, `R_single`, `R_multi`, and `U_multi`.


## Results
- **Linear Regression MAE**: 0.351
- **Random Forest MAE (Tuned)**: 0.85

## Considerations
- **Random Data Handling**: Given that the data is random, it is important to consider the potential for overfitting. Linear models showed better generalization compared to Random Forest, which might have overfitted on random features.
- **Model Selection**: For random data, simpler models like linear regression can sometimes outperform complex models like random forests, which are more prone to overfitting without enough data.

## Future Improvements
- **More Data**: Using a larger dataset could provide a more realistic evaluation.
- **Cross-validation**: Implementing cross-validation to better evaluate model performance across multiple subsets of data.

