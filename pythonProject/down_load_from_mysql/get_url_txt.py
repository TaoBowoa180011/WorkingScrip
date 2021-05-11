import mysql.connector
import datetime
import config
class Video_Url():
    def __init__(self,startdate,enddate):
        self.mydb = mysql.connector.connect(host="81.68.190.21", port='30203', user='root',
                                            password='iLabService123')
        self.mycursor = self.mydb.cursor()
        self.startdate = startdate
        self.enddate = enddate


    def get_video_url(self):
        # sql ="select d.device_serial,d.video_url,d.start_date,d.end_date from ( select * from video_0.video_data_motion_0 "\
        #            "union all " \
        #            "select * from video_0.video_data_motion_2 " \
        #            "union all " \
        #            "select * from video_1.video_data_motion_1 " \
        #            "union all " \
        #            "select * from video_1.video_data_motion_3 " \
        #            "union all " \
        #        	   "select * from video_0.video_data_motion_1 ) as d where start_date> %s and start_date < %s and "\
        #            "TIMESTAMPDIFF(minute ,start_date,end_date) >1 and device_serial in ('D81142839', 'E57378929', 'C90843471', 'E57381746', 'D70017230', 'D81142945', 'E82843244', 'D81142649', 'E57381872', 'E57378277', 'D70017095', 'C90840351', 'E57378215', 'D00269712', 'E57379385', 'E57381678', 'D00269151', 'D81141170', 'D88628881', 'C90843675', 'E57381808', 'E57378962', 'D00268323', 'E57379050', 'C90842468', 'D70007845', 'D81141546', 'E57381705', 'D00268328')"\
        #            "group by d.device_serial"
        sql ='select a.video_name ,a.event_start_time,a.event_end_time,a.video_url, a.yolo_results, a.create_date from analysis.ai_video_tag as a where create_date >=\'2020-12-16\''
        # val = (self.startdate,self.enddate)
        val=()
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
    start_date = datetime.date(2020, 12, 16)
    end_date = datetime.date(2020, 12, 16)
    delta = datetime.timedelta(days=1)

    while start_date <= end_date:
        print(start_date)
        day_end = start_date + delta
        url = Video_Url(str(start_date), str(day_end))
        url.get_video_url()
        start_date += delta

