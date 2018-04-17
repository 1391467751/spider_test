from myspider import myspider
import jd_func


mysp = myspider("Firefox")
mysp.set_func(jd_func.JD_func_test)
mysp.add_url('https://search.jd.com/Search?keyword=7700k&enc=utf-8&wq=7700k&pvid=819bfb1b473b4f739e6f13959ec836e2')
mysp.start()
print(mysp.get_info_size())

