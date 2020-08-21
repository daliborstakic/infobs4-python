from matplotlib import pyplot as plt
import csv

# Empty lists for appending
words = []
count = []

# Setting the windows label
fig = plt.gcf()
fig.canvas.set_window_title('Informer Data')

# Opening CSV file for reading
with open('infodata.csv', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)

    # Adding the data to the empty lists
    for line in reader:
        words.append(line[0])
        count.append(line[1])

# Reversing the lists for descending order
words.reverse()
count.reverse()

# Style plot
plt.style.use('ggplot')
plt.xlabel("Number of uses")

# Plotting the data
plt.barh(words, count)

# Displaying the plot
plt.tight_layout()
plt.show()
