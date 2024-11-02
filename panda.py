import pandas as pd

df = pd.read_excel("cities.xlsx")
random_variable_price = df.Price
random_variable_length = df['Length']
q1 = random_variable_price.quantile(0.25)
q3 = random_variable_price.quantile(0.75)
IQR = q3 - q1
lower_fence = q1 - 1.5 * IQR
upper_fence = q3 + 1.5 * IQR
print(f"Lower fence={lower_fence}, upper fence={upper_fence}")

outliers = df[(random_variable_price > upper_fence) | (random_variable_price < lower_fence)]
print(f"Outliers: {outliers}")

df_no_outliers = df[(random_variable_price < upper_fence) & (random_variable_price > lower_fence)]
df_no_outliers.to_excel("cleaned_cities.xlsx", index=False)
print(df_no_outliers)

# Covariance between length and price
mean_price = random_variable_price.mean()
mean_length = random_variable_length.mean()
size = random_variable_price.size
sum = 0.0
for i in range(0, size):
    sum += (random_variable_price[i] - mean_price) * (random_variable_length[i] - mean_length)

covariance = sum / (size - 1)
correlation=covariance/(random_variable_price.std()*random_variable_length.std())

print(f"Manual Covariance: {covariance}")
print(f"Built-in Covariance: {df[['Price', 'Length']].cov().iloc[0, 1]}")
print(f"Correlation:{correlation}")
print(f"Built-in Correlation:{df[['Price', 'Length']].corr().iloc[0, 1]}")
