import pandas as pd  # For handling data
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle  # For creating PDF
from reportlab.lib.pagesizes import A4  # PDF page size
from reportlab.lib.styles import getSampleStyleSheet  # For text styling in PDF
from reportlab.lib import colors  # Table colors
import matplotlib.pyplot as plt  # For plotting graphs

# Load employee performance data
df = pd.read_csv("data.csv")

# Display the data
df

# Calculate average and highest performance scores
average_score = df["Performance_Score"].mean()
highest_score = df["Performance_Score"].max()

# Print the results
print("Average Performance Score:", round(average_score, 2))
print("Highest Performance Score:", highest_score)

# Plot employee performance scores
plt.figure(figsize=(6, 4))
plt.plot(df["Employee"], df["Performance_Score"], marker='o')
plt.title("Employee Performance Scores")
plt.xlabel("Employee")
plt.ylabel("Score")
plt.grid(True)
plt.show()

# Prepare PDF report
file_name = "automated_report.pdf"
doc = SimpleDocTemplate(file_name, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Add title to PDF
elements.append(Paragraph("Automated Performance Report", styles["Title"]))
elements.append(Paragraph("<br/>", styles["Normal"]))

# Add performance metrics
elements.append(Paragraph(f"Average Performance Score: {round(average_score, 2)}", styles["Normal"]))
elements.append(Paragraph(f"Highest Performance Score: {highest_score}", styles["Normal"]))

# Add table heading
elements.append(Paragraph("<br/>Employee Data Table:", styles["Heading2"]))

# Prepare table data
table_data = [df.columns.tolist()] + df.values.tolist()
table = Table(table_data)

# Style the table
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("ALIGN", (1, 1), (-1, -1), "CENTER")
]))

# Add table to PDF
elements.append(table)

# Generate PDF
doc.build(elements)

print("PDF Report Generated Successfully!")
