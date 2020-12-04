import pandas

data = pandas.read_csv(".\Resources\cities.csv")
weatherDF = pandas.DataFrame(data)
htmlDF = pandas.DataFrame.to_html(weatherDF)
print(htmlDF)

table = open("dataTable.html", "w")
table.write(htmlDF)
table.close()