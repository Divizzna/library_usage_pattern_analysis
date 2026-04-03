import pandas as pd
import matplotlib.pyplot as plt

# =========================
# GOOGLE SHEET
# =========================
sheet_id = "1GwocFxBzhj-Or5iqhs3ms95_8TulwN85bag1uU9z7zM"
gid = "1297665301"

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

# =========================
# LOAD DATA
# =========================
data = pd.read_csv(url)
data.columns = data.columns.str.strip()

# =========================
# PRINT RESPONSE DATA
# =========================
print("\n========== 📋 GOOGLE FORM RESPONSES ==========\n")

print(data)

print("\nTotal Responses Received:", len(data))

print("\n=============================================\n")

# =========================
# TIME PROCESSING
# =========================
data["Entry DateTime"] = pd.to_datetime(
    data["Visit Date"].astype(str) + " " + data["Entry Time"].astype(str),
    errors='coerce'
)

data["Exit DateTime"] = pd.to_datetime(
    data["Visit Date"].astype(str) + " " + data["Exit Time"].astype(str),
    errors='coerce'
)

data = data.dropna(subset=["Entry DateTime", "Exit DateTime"])

# Study hours
data["Study Hours"] = (
    data["Exit DateTime"] - data["Entry DateTime"]
).dt.total_seconds() / 3600

# remove negative values
data["Study Hours"] = data["Study Hours"].clip(lower=0)

# =========================
# ANALYSIS
# =========================
dept_counts = data["Department"].value_counts()
purpose_counts = data["Purpose of Visit"].value_counts()
book_counts = data["Book Category"].value_counts()

print("\n========== 📊 ANALYSIS REPORT ==========")

print("\nTotal Visits:", len(data))

print("\nAverage Study Hours:", round(data["Study Hours"].mean(), 2))

print("\nMaximum Study Hours:", round(data["Study Hours"].max(), 2))

print("Minimum Study Hours:", round(data["Study Hours"].min(), 2))

print("\nMost Active Department:")
print(dept_counts.idxmax(), "->", dept_counts.max(), "visits")

print("\nMost Common Purpose of Visit:")
print(purpose_counts.idxmax(), "->", purpose_counts.max())

print("\nMost Popular Book Category:")
print(book_counts.idxmax(), "->", book_counts.max())

print("\n=======================================")

# =========================
# STYLE
# =========================
plt.style.use('ggplot')

# =========================
# BAR CHART FUNCTION
# =========================
def plot_bar(data_counts, title, xlabel, ylabel):

    plt.figure(figsize=(8,5))

    ax = data_counts.plot(kind='bar', edgecolor='black')

    plt.title(title, fontsize=14)

    plt.xlabel(xlabel)

    plt.ylabel(ylabel)

    plt.xticks(rotation=25)

    # show values on top of bars
    for i, v in enumerate(data_counts):

        ax.text(i, v + 0.05, str(v), ha='center', fontsize=10)

    plt.grid(axis='y', linestyle='--')

    plt.tight_layout()

    plt.show()

# =========================
# GRAPHS
# =========================

# Department chart
plot_bar(
    dept_counts,
    "Department-wise Library Usage",
    "Department",
    "Number of Students"
)

# Book category chart
plot_bar(
    book_counts,
    "Book Category Popularity",
    "Category",
    "Count"
)

# Pie chart
plt.figure(figsize=(6,6))

if not purpose_counts.empty:

    purpose_counts.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Purpose of Visit Distribution")

    plt.ylabel("")

    plt.tight_layout()

    plt.show()

else:

    print("No data available for pie chart")