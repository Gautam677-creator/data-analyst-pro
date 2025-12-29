import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
filename = "sales_data.csv" 
df = pd.read_csv(filename, parse_dates=['Date'])

# Quick look at the data
print("First 5 rows:\n", df.head())
print("\nData Summary:\n", df.describe(include='all'))
print("\nColumn Info:\n", df.info())

# Basic Total Sales Calculations
total_sales = df['Total_Amount_INR'].sum()
print(f"\n Total Sales (INR): {total_sales}")

# Sales by Product
sales_by_product = df.groupby('Product')['Total_Amount_INR'].sum().sort_values(ascending=False)
print("\n Sales by Product:\n", sales_by_product)

# Sales by City
sales_by_city = df.groupby('City')['Total_Amount_INR'].sum().sort_values(ascending=False)
print("\n Sales by City:\n", sales_by_city)

# Quantity Sold by Product
qty_by_product = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print("\n Quantity Sold by Product:\n", qty_by_product)


# Plot Total Sales by Product
plt.figure(figsize=(8,5))
sales_by_product.plot(kind='bar', color='skyblue')
plt.title("Total Sales by Product")
plt.ylabel("Sales (INR)")
plt.xlabel("Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot Total Sales by City
plt.figure(figsize=(8,5))
sales_by_city.plot(kind='bar', color='orange')
plt.title("Total Sales by City")
plt.ylabel("Sales (INR)")
plt.xlabel("City")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Quantity Sold by Product - Bar Chart
plt.figure(figsize=(8,5))
qty_by_product.plot(kind='bar', color='green')
plt.title("Quantity Sold by Product")
plt.ylabel("Total Quantity")
plt.xlabel("Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
