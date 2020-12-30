import gs as gs
import pandas as pd

path = '/Users/tehila/PycharmProjects/salary_us/chromedriver'


df = gs.get_jobs('data scientist',1000, False, path, 15)
df.to_csv('glassdoor_jobs_us.csv', index = False)
