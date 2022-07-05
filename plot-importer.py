#!/usr/bin/python3
# Plot Importer by Zorlin
# Intended for importing plots into PlotFS.
from os import listdir,getcwd,chdir
from os.path import isfile, join

# Get a list of all files
directory = getcwd()
files_list = [f for f in sorted(listdir(directory)) if isfile(join(directory, f))]

# Detect if the directory we are in contains plotfiles.
plots_in_dir = any(".plot" in string for string in files_list)
# If not, ask for a directory.
if(plots_in_dir == False):
    plots_provided = False
    while plots_provided == False:
        print("No plots found in " + directory)
        directory = input("Please enter a directory to import: ")
        files_list = [f for f in listdir(directory) if isfile(join(directory, f))]
        if any(".plot" in string for string in files_list):
            plots_provided = True
else:
    directory = getcwd()

# Count the number of plot files in this directory
plot_count = sum('.plot' in string for string in files_list)
print("Found " + str(plot_count) + " plots in " + directory)
print(files_list)

# Create a new list containing only plot files
plots_list = []
for file in files_list:
    if ".plot" in file:
        plots_list.append(file)

# Change to directory
chdir(directory)

# Main loop
plots_done = 0
for plot in plots_list:
    print("sudo plotfs --add_plot " + plot)
    plots_done += 1
    print("Plots imported: " + str(plots_done) + "/" + str(plot_count))