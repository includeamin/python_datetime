days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
today_date = datetime.datetime.today()
last30date = today_date - datetime.timedelta(days=30)
todayname = today_date.strftime("%A")
startweek = ""
endweek = ""
if todayname == days[0]:
    startweek = today_date
else:
    index = days.index(todayname)
    startweek = today_date - datetime.timedelta(days=index)
    endweek = today_date + datetime.timedelta(days=(len(days)-index))

startOflastweek = startweek - datetime.timedelta(days=6)
endOflastweek = startweek - datetime.timedelta(days=1)
startOfthisMonth =  datetime.datetime(today_date.year, today_date.month, 1)
startOfLastMonth = startOfthisMonth - datetime.timedelta(days=30)
endOfLastMonth = startOfLastMonth + datetime.timedelta(days=29)
