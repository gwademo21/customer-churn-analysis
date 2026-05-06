import pandas as pd
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "data")
visuals_path = os.path.join(base_dir, "visuals")

os.makedirs(data_path, exist_ok=True)
os.makedirs(visuals_path, exist_ok=True)


# Create sample customer data
data = {
    "Customer_ID": range(1, 31),
    "Age": [22, 25, 30, 35, 40, 28, 33, 45, 50, 29,
            27, 31, 38, 42, 36, 26, 48, 52, 34, 39,
            41, 37, 23, 32, 44, 47, 29, 31, 36, 40],
    "Monthly_Usage_Hours": [5, 8, 12, 6, 4, 10, 9, 3, 2, 11,
                            7, 13, 6, 5, 8, 9, 3, 2, 10, 7,
                            6, 8, 12, 9, 4, 3, 11, 10, 7, 6],
    "Membership_Months": [2, 6, 12, 3, 1, 10, 8, 15, 18, 5,
                         7, 14, 9, 11, 13, 4, 16, 20, 6, 10,
                         12, 9, 3, 7, 17, 19, 8, 6, 11, 13],
    "Subscription_Type": [
        "Basic", "Standard", "Premium", "Basic", "Basic",
        "Premium", "Standard", "Premium", "Premium", "Standard",
        "Basic", "Premium", "Standard", "Standard", "Premium",
        "Basic", "Premium", "Premium", "Standard", "Standard",
        "Premium", "Standard", "Basic", "Standard", "Premium",
        "Premium", "Standard", "Standard", "Premium", "Premium"
    ],
    "Churned": [
        1, 0, 0, 1, 1,
        0, 0, 1, 1, 0,
        0, 0, 1, 1, 0,
        1, 1, 1, 0, 0,
        0, 1, 1, 0, 1,
        1, 0, 0, 1, 0
    ]
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv(os.path.join(data_path, "customer_data.csv"), index=False)


# Analysis
churn_rate = df["Churned"].mean() * 100

avg_usage_churned = df[df["Churned"] == 1]["Monthly_Usage_Hours"].mean()
avg_usage_retained = df[df["Churned"] == 0]["Monthly_Usage_Hours"].mean()

avg_membership_churned = df[df["Churned"] == 1]["Membership_Months"].mean()
avg_membership_retained = df[df["Churned"] == 0]["Membership_Months"].mean()

print("Customer Churn Summary")
print(f"Churn Rate: {churn_rate:.2f}%")
print(f"Avg Usage (Churned): {avg_usage_churned:.2f}")
print(f"Avg Usage (Retained): {avg_usage_retained:.2f}")
print(f"Avg Membership (Churned): {avg_membership_churned:.2f}")
print(f"Avg Membership (Retained): {avg_membership_retained:.2f}")


# Visuals
# Churn rate
plt.figure()
df["Churned"].value_counts().plot(kind="bar")
plt.title("Churn vs Retained Customers")
plt.tight_layout()
plt.savefig(os.path.join(visuals_path, "churn_rate.png"))
plt.close()

# Churn by age
plt.figure()
df.groupby("Age")["Churned"].mean().plot()
plt.title("Churn Rate by Age")
plt.tight_layout()
plt.savefig(os.path.join(visuals_path, "churn_by_age.png"))
plt.close()

# Churn by usage
plt.figure()
df.groupby("Monthly_Usage_Hours")["Churned"].mean().plot()
plt.title("Churn by Usage")
plt.tight_layout()
plt.savefig(os.path.join(visuals_path, "churn_by_usage.png"))
plt.close()

# Churn by membership
plt.figure()
df.groupby("Membership_Months")["Churned"].mean().plot()
plt.title("Churn by Membership Length")
plt.tight_layout()
plt.savefig(os.path.join(visuals_path, "churn_by_membership.png"))
plt.close()

print("\nCharts saved. Data saved.")