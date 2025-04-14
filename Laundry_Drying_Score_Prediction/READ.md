🧺 Laundry Drying Score Prediction
This notebook predicts how well laundry will dry, based on weather conditions.
It provides a "drying score" that can be used to make decisions like:

"Should I hang laundry outside or indoors today?"

"Will my laundry dry completely before evening?"

📌 Features
Calculates a score from 0 to 10 indicating drying potential

Based on weather data including:

Temperature

Humidity

Wind speed

Sunshine duration

Uses a machine learning regression model (Random Forest)

🧠 Model
Algorithm: Random Forest Regressor

Evaluation Metric: Mean Absolute Error (MAE)

Feature importance is visualised to show key weather factors

🧪 Example Use Case
For example, if the predicted drying score is:

8–10 → Excellent for outdoor drying

5–7 → Might be OK if you hang it early

0–4 → Consider drying indoors or using a dryer

📁 Files
Laundry_Drying_Score_Prediction_woD.ipynb
→ Main notebook for training and predicting the drying score

🔧 Future Work
Integrate with real-time weather APIs

Create a mobile-friendly web app for everyday use

Improve the score with household-specific preferences

