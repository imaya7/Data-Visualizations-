import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
def load_data(file_path):
    #looks for file path 
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    return pd.read_csv(file_path)

# Clean data
def clean_data(data):
    # Replace currency symbols and convert to float
    data['loan_amnt'] = data['loan_amnt'].replace('[£,]', '', regex=True).astype(float)
    data['loan_int_rate'] = data['loan_int_rate'].astype(float)
    return data

# Plot loan intents
def plot_bar(data):
    plt.figure(figsize=(8, 6))
    #counts the number of each loan intent 
    loan_intent_counts = data['loan_intent'].value_counts()
    colors = plt.cm.Paired(range(len(loan_intent_counts)))  # Use a paired colormap
    plt.bar(loan_intent_counts.index, loan_intent_counts.values, color=colors)
    plt.title('Distribution of Loan Intents', fontsize=16, fontweight='bold')
    #adds labels to the x and y axis
    plt.xlabel('Loan Intent', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Plot interest rates by grade
def plot_box(data):
    # Drop rows with missing loan_int_rate or loan_grade
    filtered_data = data.dropna(subset=['loan_int_rate', 'loan_grade'])
    
    plt.figure(figsize=(10, 6))
    #sorted list of interest rates by loan grade
    loan_grades = sorted(filtered_data['loan_grade'].unique())
    # list of interest rates by loan grade
    box_data = [filtered_data[filtered_data['loan_grade'] == grade]['loan_int_rate'] for grade in loan_grades]
    colors = plt.cm.Set3(range(len(loan_grades)))  # Use a Set3 colormap
    box = plt.boxplot(box_data, labels=loan_grades, patch_artist=True)
    
    # Apply colors to each box
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
    # adds labels to the x and y axis
    plt.title('Interest Rates by Loan Grade', fontsize=16, fontweight='bold')
    plt.xlabel('Loan Grade', fontsize=14)
    plt.ylabel('Interest Rate (%)', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Plot loan status by home ownership
def plot_stacked(data):
    # Group by home ownership and current loan status
    home_status = data.groupby(['home_ownership', 'Current_loan_status']).size().unstack(fill_value=0)
    colors = ['#4daf4a', '#377eb8']  # Use a custom color palette
    #blue and green colors
    ax = home_status.plot(kind='bar', stacked=True, figsize=(10, 6), color=colors)
    #adds labels to the x and y axis
    plt.title('Loan Default Status by Home Ownership', fontsize=16, fontweight='bold')
    plt.xlabel('Home Ownership', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.legend(title='Loan Status', labels=['No Default', 'Default'], fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=0, fontsize=12)
    plt.tight_layout()

    # Add annotations to the stacked bar plot
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='center', fontsize=10, color='white')
    plt.show()

# Main
if __name__ == "__main__":
    # Specify the file path
    file_path = r"C:\Users\trash\Downloads\LoanDataset - LoansDatasest.csv"
    # Load the data
    data = load_data(file_path)
    
    # Check if data is loaded successfully
    if data is not None:
        data = clean_data(data)
        plot_bar(data)
        plot_box(data)
        plot_stacked(data)




# The three visualizations provide a good insight into the Loan Dataset. The bar plot shows the distribution of the loan intents
# across all the different types of loan categories. From this, we can conclude that the most common loan intent is for education, 
#  while the least common loan intent is for home improvements. 
# This could suggest that education is a priority for most individuals so it is necessary to take loans out for it. 
# The box plot shows the distribution of interest rates across all the different loan grades. 
# From this we can conclude that the interest rates are a lot higher for those with lower grades such as 
#  grade D and E. This helps us visualize the loan grades and the risk that people might face due to there 
#credit score. The worse someone's score is the higher the interest rate they will have to pay. 
# The stacked bar plot shows the default status of loans across all the different home ownership categories.
# No Default means that the loan was paid back while default means that the loan was not paid back. From this, we can 
#conclude that that individuals with a mortgage and who own their own homes tend to have more defaults than those who are renting.
#This could be because those who are renting may have less financial stress as they have roommates to help pay the rent, while 
#those with a home may have a more challenging time as they have to handle all the bills independently. 
