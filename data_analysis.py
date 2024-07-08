

from book_app.db.database import engine
from pandasql import sqldf
import pandas as pd
from datetime import date,timedelta

def get_count_by_date(df,on_date):
    res=sqldf(f'select COUNT(*) from df where publication_date=="{on_date}";')
    print("The count of number of books added on {on_date} are: ",res['COUNT(*)'].iloc[0])


def get_count_by_author(df,author):
    res=sqldf(f'select COUNT(*) from df where author_user_name=="{author}"')
    print("The count of number of books writen by the author : ",res['COUNT(*)'].iloc[0])

def get_weekly_report(df):
    today=date.today()
    startday=today-timedelta(7)
    res=sqldf(f'select * from df where publication_date>="{startday}" and publication_date<="{today}"')
    
    res.to_csv("weekly_report.csv",index=False)
    print(res)


df=pd.read_sql_query("select * from sample.books;", engine)
book_df=pd.DataFrame(df)

print(book_df)

get_count_by_date(book_df,"2024-07-06")
get_count_by_author(book_df,"author1")
get_weekly_report(book_df)