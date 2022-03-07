import csv

with open("STOCK_DAY_0050_202202.csv") as csv_read_file:
    # csv_read_data = csv_read_file.read()
    # print(csv_read_data)

    # csv_read_data = csv_read_file.readlines()
    # print(csv_read_data)

    csv_read_data = csv.reader(csv_read_file)
    # for row in csv_read_data:
    #     print(row)

    csv_read_list = list(csv_read_data)
    # for row in csv_read_list:
    #     print(row)

    for row in range(len(csv_read_list)-1):
        if len(csv_read_list[row]) > 1:
            print(csv_read_list[row][0], csv_read_list[row][6])

with open("STOCK_DAY_0050_202202_copy.csv", mode="w", newline="") as csv_write_file:
    csv_write_data = csv.writer(csv_write_file)
    csv_write_data.writerows(csv_read_list)

with open("STOCK_DAY_0050_202202_delimiter.csv", mode="w", newline="") as csv_write_file:
    csv_write_data = csv.writer(csv_write_file, delimiter=" ")
    csv_write_data.writerows(csv_read_list)

with open("STOCK_DAY_0050_202202_delimiter.csv") as csv_read_file:
    csv_read_data = csv.reader(csv_read_file, delimiter=" ")
    csv_read_list = list(csv_read_data)
    for row in csv_read_list:
        print(row)
