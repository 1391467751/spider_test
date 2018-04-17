from selenium import webdriver



def get_driver(type_str):
    if(type_str=="PhantomJS"):
        return webdriver.PhantomJS()
    elif(type_str == "Firefox"):
        return webdriver.Firefox()
    else:
        return None


class myspider:
    def __init__(self,type_str):
        self.type_str= type_str
        self.url_path = []
        self.info = []
        

    def add_url(self,url_str):
       self.url_path.append(url_str)

    def set_func(self,func):
        self.func = func

    def start(self):
        try:
            self.driver = get_driver(self.type_str)
            if(self.driver ==None):
                print("create driver fail")
                return
            print("create driver successfully")        
            if(len(self.url_path)==0):
                print("no work now...")
                return
            while(len(self.url_path)!=0):
                url = self.url_path[0]
                self.url_path.remove(url)
                info_tmp = self.func(self.driver,url)
                self.info=self.info + info_tmp

        finally:
            self.finish()

    def get_info_size(self):
        return len(self.info)

    def finish(self):
        self.driver.quit()
        
        
