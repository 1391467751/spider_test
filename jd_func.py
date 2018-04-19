from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
import pymysql

def JD_func_test(spider,url):
    lis_ans =[]
    driver = spider.driver
    actions = ActionChains(driver)
    #driver.maximize_window()
    driver.get(url)
    for i in range(3):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        temp = driver.find_element_by_id('J_goodsList')
        ul = temp.find_element_by_tag_name("ul")
        lis = ul.find_elements_by_tag_name('li')
        lis_ans =lis_ans + lis
        actions.send_keys(Keys.LEFT).perform()
        print('finish ' ,i)
    return lis_ans


def JD_info_save(lis_info):
    fd = open("info.txt",'w',encoding="gb18030")
    index = 1
    item_list=[]
    for item in lis_info:
        str1 = re.search(r"tab-content-item[\S\s]*?tab-content-item",item)
        if(str1 == None):
            str1 = item
        else:
            str1=str1.group()
        price = re.search(r"<em>￥</em>.*?</",str1).group()
        price =price.replace('<em>','')
        price =price.replace('</em>','')
        price =price.replace('</','')
        price =price.replace('<i>','')
        price =price.replace('￥','')
        price = int(float(price))
        if((price<3000) | (price>5000) ):
            continue
        str2 = re.search(r"p-name p-name-type-2[\s\S]*?p-commit",str1).group()
        name = re.search(r"em>[\s\S]*?</em",str2).group()
        name = name.replace('em>','')
        name = name.replace('</em','')
        name = name.replace("<font class=\"skcolor_ljg\">",'')
        name = name.replace("</font>",'')
        fd.write(str(index)+": name = "+name+" price = ￥"+str(price)+"\n")
        item_list.append([index,name,price])
        index =index+1
    fd.close()
    return item_list

def JD_info_sql(item_lists ,table="JD_test"):
    dp = pymysql.connect("localhost","root","root",db ="python_test",use_unicode=True, charset="utf8")
    cursor = dp.cursor()
    sql_str = "DROP Table " + " IF EXISTS " + table +";"
    cursor.execute(sql_str)
    sql_str ="create table "+ table + """(
        id int not null,
        name TEXT(1024),
        price int);
        """
    cursor.execute(sql_str)
    for item in item_lists:
        temp_list =["insert into",table,"(id,name,price) values (",str(item[0]),",\'",item[1],"\',",str(item[2]),")"]
        ppp=" ".join(temp_list)
        #print(ppp)
        cursor.execute(ppp)
        dp.commit()
    
    cursor.close()
    
        
        
