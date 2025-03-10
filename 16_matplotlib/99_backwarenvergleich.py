import matplotlib.pyplot as plt
import numpy as np

products = ("Brot", "Brötchen")
suppliers = {
    'Liebler': (3.99, 1.05),
    'Niemeyer': (4.25, 1.05),
    'Kreßmann': (3.79, 1.05),
    'Mechlinski': (3.49, 0.90),
}

x = np.arange(len(products))  # the label locations
width = 0.15  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for product_name, price in suppliers.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, price, width, label=product_name)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Preis (€)')
ax.set_title('Produkt')
ax.set_xticks(x + (len(suppliers)/2.0-0.5)*width, products)
ax.legend(loc='upper left', ncols=len(suppliers))
ax.set_ylim(0, 6)

plt.show()