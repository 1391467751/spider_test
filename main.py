from myspider import myspider
import jd_func


mysp = myspider("PhantomJS")
mysp.set_func(jd_func.JD_func_test)
mysp.add_url('https://search.jd.com/Search?keyword=8700k&enc=utf-8&wq=8700k&pvid=819bfb1b473b4f739e6f13959ec836e2')
mysp.start()
lis_info = mysp.get_info()


jd_func.JD_info_sql(jd_func.JD_info_save(lis_info))

print(len(lis_info))

