import mysql.connector
import datetime
import config
import os
class Video_Url():
    def __init__(self,startdate,enddate):
        self.mydb = mysql.connector.connect(host='81.68.190.21', port='30203', user='root',
                                            password='iLabService123')
        self.mycursor = self.mydb.cursor()
        self.startdate = startdate
        self.enddate = enddate


    def get_video_url(self):
        with open('mysql','r') as mysql:
            sql = mysql.read()
        print(sql)
        # os.system('pause')



        # val = (self.startdate,self.enddate)
        val = ()
        self.mycursor .execute(sql, val)
        with open('url_'+str(self.startdate)+'.txt','w')as url:
            for row in self.mycursor:
                out = []
                for item in row:
                    if type(item)==datetime.datetime:
                        item = item.strftime("%Y-%m-%d %H:%M:%S")
                    out.append(item)
                print(out)
                url.write(','.join(out)+'\n')
        return 'url_'+str(self.startdate)+'.txt'

if __name__ == '__main__':
    start_date = datetime.date(2020, 11, 10)
    end_date = datetime.date(2020, 11, 11)
    delta = datetime.timedelta(days=1)

    while start_date <= end_date:
        print(start_date)
        day_end = start_date + delta
        url = Video_Url(str(start_date), str(day_end))
        url.get_video_url()
        start_date += delta

