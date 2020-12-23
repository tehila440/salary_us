import glassdoor_scraper_us as gs
import pandas as pd

path = '/Users/tehila/PycharmProjects/salary_us/chromedriver'


df = gs.get_jobs('engineer',15, False, path, 15)
#df.to_csv('glassdoor_jobs.csv', index = False)

