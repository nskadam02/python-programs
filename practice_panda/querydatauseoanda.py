import pandas as pd
import pandasql as ps

input_data = "John 2020 80, John 2021 94, John 2022 97," + \
            "James 2019 70, James 2020 32, James 2021 99," + \
            "John 2029 35, John 2023 66, John 2019 78,"+ \
            "Peter 2019 80, Peter 2020 32, Peter 2021 86,"+\
            "Eloise 2019 80, Eloise 2020 32, Eloise 2021 78,"+\
            "James 2022 70, James 2023 32, James 2024 85"
list_d = input_data.split(",")
# print(list_d)
# listq=[sub.split() for sub in list_d]
# print(listq)

data = pd.DataFrame([sub.split() for sub in list_d], columns=['name', 'year','marks'])
# print(data)

# for given student what score did she received name = JOhn year = 2023
sql = """select marks from data where name='John' and year='2023'"""
print(ps.sqldf(sql))
# for given score what his best score
sql2="""select min(marks) as worst from data where name='John' group by name"""
print(ps.sqldf(sql2))
# worst score
sql3="""select max(marks) as best from data where name='John' group by name"""
print(ps.sqldf(sql3))
# avregae score
sql4="""select avg(marks) as average from data where name='John' group by name"""
print(ps.sqldf(sql4))


