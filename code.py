import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
df
average_score = df["Performance_Score"].mean()
highest_score = df["Performance_Score"].max()

print("Average Performance Score:", round(average_score, 2))
print("Highest Performance Score:", highest_score)
plt.figure(figsize=(6,4))
plt.plot(df["Employee"], df["Performance_Score"], marker='o')
plt.title("Employee Performance Scores")
plt.xlabel("Employee")
plt.ylabel("Score")
plt.grid(True)
plt.show()
file_name = "automated_report.pdf"
doc = SimpleDocTemplate(file_name, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

elements.append(Paragraph("Automated Performance Report", styles["Title"]))
elements.append(Paragraph("<br/>", styles["Normal"]))

elements.append(Paragraph(
    f"Average Performance Score: {round(average_score,2)}",
    styles["Normal"]
))

elements.append(Paragraph(
    f"Highest Performance Score: {highest_score}",
    styles["Normal"]
))

elements.append(Paragraph("<br/>Employee Data Table:", styles["Heading2"]))

table_data = [df.columns.tolist()] + df.values.tolist()

table = Table(table_data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightblue),
    ("GRID", (0,0), (-1,-1), 1, colors.black),
    ("ALIGN", (1,1), (-1,-1), "CENTER")
]))

elements.append(table)

doc.build(elements)

print("PDF Report Generated Successfully!")


