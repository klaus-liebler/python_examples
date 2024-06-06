import time
import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi
import fpdf

df = pd.read_csv("data/KleineHochschulstatistik WiSe2019.csv", header=2)

def color_pos_neg_value(value):
    if value < 0:
        color = 'red'
    elif value > 0:
        color = 'green'
    else:
        color = 'black'
    return 'color: %s' % color

# Apply styling to dataframe
df=df.hide_index()
styled_df=df.bar(subset=["Total Sales",], color='lightgreen').applymap(color_pos_neg_value, subset=['Sales Pct Change'])


dfi.export(styled_df, 'resources/annual_sales.png')

def generate_matplotlib_stackbars(df, filename):
    
    # Create subplot and bar
    fig, ax = plt.subplots()
    ax.plot(df['Year of Release'].values, df['Total Sales'].values, color="#E63946", marker='D') 

    # Set Title
    ax.set_title('Heicoders Academy Annual Sales', fontweight="bold")

    # Set xticklabels
    ax.set_xticklabels(df['Year of Release'].values, rotation=90)
    plt.xticks(df['Year of Release'].values)

    # Set ylabel
    ax.set_ylabel('Total Sales (USD $)') 

    # Save the plot as a PNG
    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    
    plt.show()
    
def generate_matplotlib_piechart(df, filename):
    
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = ["NA Sales", "EU Sales", "JP Sales", "Other Sales", "Global Sales"]
    sales_value = df[["NA Sales", "EU Sales", "JP Sales", "Other Sales", "Global Sales"]].tail(1)
    
    # Colors
    colors = ['#E63946','#F1FAEE','#A8DADC','#457B9D','#1D3557', '#9BF6FF']
    
    # Create subplot
    fig, ax = plt.subplots()
    
    # Generate pie chart
    ax.pie(sales_value, labels=labels, autopct='%1.1f%%', startangle=90, colors = colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Set Title
    ax.set_title('Heicoders Academy 2016 Sales Breakdown', fontweight="bold")
    
    # Save the plot as a PNG
    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    
    plt.show()

generate_matplotlib_stackbars(df, 'resources/heicoders_annual_sales.png')
generate_matplotlib_piechart(df, 'resources/heicoders_2016_sales_breakdown.png')

def create_letterhead(pdf, WIDTH):
    pdf.image("./resources/heicoders_letterhead_cropped.png", 0, 0, WIDTH)

def create_title(title, pdf):
    
    # Add main title
    pdf.set_font('Helvetica', 'b', 20)  
    pdf.ln(40)
    pdf.write(5, title)
    pdf.ln(10)
    
    # Add date of report
    pdf.set_font('Helvetica', '', 14)
    pdf.set_text_color(r=128,g=128,b=128)
    today = time.strftime("%d/%m/%Y")
    pdf.write(4, f'{today}')
    
    # Add line break
    pdf.ln(10)

def write_to_pdf(pdf, words):
    
    # Set text colour, font size, and font type
    pdf.set_text_color(r=0,g=0,b=0)
    pdf.set_font('Helvetica', '', 12)
    
    pdf.write(5, words)

class PDF(fpdf.FPDF):

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')


# Global Variables
TITLE = "Monthly Business Report"
WIDTH = 210
HEIGHT = 297

# Create PDF
pdf = PDF() # A4 (210 by 297 mm)


'''
First Page of PDF
'''
# Add Page
pdf.add_page()

# Add lettterhead and title
create_letterhead(pdf, WIDTH)
create_title(TITLE, pdf)

# Add some words to PDF
write_to_pdf(pdf, "1. The table below illustrates the annual sales of Heicoders Academy:")
pdf.ln(15)

# Add table
pdf.image("./resources/annual_sales.png", w=170)
pdf.ln(10)

# Add some words to PDF
write_to_pdf(pdf, "2. The visualisations below shows the trend of total sales for Heicoders Academy and the breakdown of revenue for year 2016:")

# Add the generated visualisations to the PDF
pdf.image("resources/heicoders_annual_sales.png", 5, 200, WIDTH/2-10)
pdf.image("resources/heicoders_2016_sales_breakdown.png", WIDTH/2, 200, WIDTH/2-10)
pdf.ln(10)


'''
Second Page of PDF
'''

# Add Page
pdf.add_page()

# Add lettterhead
create_letterhead(pdf, WIDTH)

# Add some words to PDF
pdf.ln(40)
write_to_pdf(pdf, "3. In conclusion, the year-on-year sales of Heicoders Academy continue to show a healthy upward trend. Majority of the sales could be attributed to the global sales which accounts for 58.0% of sales in 2016.")
pdf.ln(15)

# Generate the PDF
pdf.output("annual_performance_report.pdf", 'F')