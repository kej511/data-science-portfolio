# Truck Allocation Forecast Model

## Background and Objective
The goal of this project is to build a model that predicts the number of trucks required for daily shipments in a logistics optimization context. Specifically, the objective is to predict the number of trucks needed per day, which helps in streamlining the logistics process and improving delivery efficiency.

## Logic and Formulas

### 1. Shipment Units Calculation
The number of shipment units is calculated using the following formulas:

#### 1.1 Single Shipment Units

$$S_{\text{single}} = U_d \times R_{\text{single}}$$

where:

- $U_d$ is the daily shipment volume (in units)
- $R_{\text{single}}$ is the single shipment ratio

#### 1.2 Multi Shipment Units

$$S_{\text{multi}} = \frac{U_d \times R_{\text{multi}}}{U_{\text{multi}}}$$

where:

- $U_{\text{multi}}$ is the average units per multi shipment
- $R_{\text{multi}}$ is the multi shipment ratio

### 2. Email and Box Shipment Ratios
The total shipment units are divided into email and box shipments, calculated based on the following ratios:

#### 2.1 Email Shipments

$$S_M = S_{\text{total}} \times S_{M\text{ratio}}$$

#### 2.2 Box Shipments

$$S_B = S_{\text{total}} \times S_{B\text{ratio}}$$

where:

- $S_M$ is the total email shipments
- $S_B$ is the total box shipments
- $S_{\text{total}}$ is the total shipment units
- $S_{M\text{ratio}}$ is the email shipment ratio
- $S_{B\text{ratio}}$ is the box shipment ratio

### 3. Truck Allocation Calculation
The total number of trucks required is calculated by dividing the email and box shipments by their respective cargo capacities, then summing the results and dividing by the truck capacity. The final truck allocation is calculated as follows:

$$\text{Total Trucks} = \left\lceil \frac{\frac{S_M}{S_{M\text{capacity}}} + \frac{S_B}{S_{B\text{capacity}}}}{\text{cargo\_per\_truck}} \right\rceil$$

where:

- $S_{M\text{capacity}} = 400$ is the email shipment capacity
- $S_{B\text{capacity}} = 75$ is the box shipment capacity
- $\text{cargo\_per\_truck} = 22$ is the cargo capacity per truck

### 4. Moving Average
A 7-day moving average of the truck numbers is added as a feature to improve the model's accuracy. The moving average of truck numbers is calculated as follows:

$$\text{Moving Average of Trucks} = \frac{1}{7}\sum_{i=t-6}^t T_i$$

where:

- $T_i$ is the truck number for day $i$
- $t$ is the current day

## Models Used

### 1. Linear Regression
Linear regression assumes a linear relationship between the explanatory variables and the target variable. While simple and interpretable, linear regression may struggle to capture complex nonlinear relationships in the data.

$$y = \beta_0 + \beta_1X_1 + \beta_2X_2 + \cdots + \beta_nX_n$$

where:

- $y$ is the target variable (truck number)
- $X_1, X_2, \ldots, X_n$ are the explanatory variables (daily shipment volume, shipment ratios, moving average, etc.)

### 2. Random Forest
Random Forest is an ensemble learning method that builds multiple decision trees and aggregates their predictions. It is capable of capturing complex nonlinear relationships between the features and the target variable.

The Random Forest model involves the following hyperparameters:

- $\text{max\_depth} = \text{None}$
- $\text{min\_samples\_split} = 2$
- $\text{min\_samples\_leaf} = 2$
- $\text{n\_estimators} = 50$

These parameters were optimized using GridSearch.

## Results
Linear Regression MAE: 0.59

Random Forest MAE (after hyperparameter tuning): 1.93

## Next Steps

### 1. Model Improvement
Further improvements to the Random Forest model by refining the data preprocessing steps or exploring other models (e.g., Gradient Boosting) to improve accuracy.

### 2. Data Collection
Use real-world data to assess the model's accuracy. Incorporating external data, such as weather forecasts or public holiday schedules, may improve prediction accuracy.

### 3. Model Evaluation
Evaluate the model using additional metrics such as RMSE and $R^2$, to gain a more comprehensive understanding of the model's performance.

## Explanation for the Models and Methods

### Linear Regression
Linear regression assumes a simple relationship between input features and the target variable. However, in real-world problems, relationships are often more complex and nonlinear. Linear regression provides a baseline to compare more complex models like Random Forest.

### Random Forest
Random Forest is an ensemble technique that helps reduce overfitting compared to a single decision tree by averaging the predictions of multiple trees. This makes it more robust and suitable for complex datasets with nonlinear relationships. The model's performance is further enhanced by hyperparameter tuning, which helps find the best settings for the trees.

### Moving Average
The moving average of the truck numbers over the past 7 days is used to capture trends and seasonal effects. This feature can help improve prediction accuracy by providing the model with information on recent trends.

## Why We Chose These Approaches
The linear regression model was chosen to provide a baseline comparison. Random Forest, with its ability to capture complex patterns in data, was selected as a more powerful model. Hyperparameter tuning was essential for optimizing the Random Forest model's performance. 