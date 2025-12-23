
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

# Example: Load dataset
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

# Continue your full workflow here...
