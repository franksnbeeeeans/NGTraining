from collections import Counter
# File path hardcoded for now.  Can be changed later to add an argparse statement for file input or:
# LOGFILE = input("What is the path to your log file?\n")
LOGFILE = 'web-log.txt'

# Create variable to hold the data as a list
data = []

# Create variables to hold the various data points
ip_data = []
path_data = []
request_data = []

# Open the file as read only
with open(LOGFILE, 'r') as f:
    # Take each line of the file and append the needed information onto the data variable
    for line in f.readlines():
        lineData = line.split(" ")
        data.append(lineData)


def process_all_data():
    for entry in data:
        ip_data.append(entry[0])
        path_data.append(entry[6])
        request_data.append(entry[5].strip("\""))


def process_individual_data(category_data, plural_name):
    common_data = Counter(category_data).most_common(10)
    print("Top Ten {}\nCount\t\t{}".format(plural_name,plural_name))
    # On the latest Python version 3.6+, you can use the following syntax:
    # print(f"Top Ten {plural_name}\nCount\t\t{plural_name}")
    for ip in common_data:
        print("{}\t{}".format(ip[1]:<10,ip[0]})
        # print(f'{ip[1]:<10}\t{ip[0]}')
        
    print('\n\n')


def main():
    process_all_data()
    process_individual_data(ip_data, 'IPs')
    process_individual_data(path_data, 'Paths')
    process_individual_data(request_data, 'Request Types')


if __name__ == "__main__":
    main()
