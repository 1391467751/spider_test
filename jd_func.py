from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re

def JD_func_test(spider,url):
    lis_ans =[]
    driver = spider.driver
    actions = ActionChains(driver)
    driver.maximize_window()
    driver.get(url)
    for i in range(20):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        temp = driver.find_element_by_id('J_goodsList')
        ul = temp.find_element_by_tag_name("ul")
        lis = ul.find_elements_by_tag_name('li')
        lis_ans =lis_ans + lis
        actions.send_keys(Keys.LEFT).perform()
        print('finish ' ,i)
    return lis_ans


def JD_info_save(lis_info):
    fd = open("info.txt",'w',encoding="gb18030")
    for item in lis_info:
        str1 = re.search(r"tab-content-item[\S\s]*?tab-content-item",item)
        if(str1 == None):
            str1 = item
        else:
            str1=str1.group()
        price = re.search(r"<em>￥</em>.*</i>",str1).group()
        price =price.replace('<em>','')
        price =price.replace('</em>','')
        price =price.replace('</i>','')
        price =price.replace('<i>','')
        str2 = re.search(r"p-name p-name-type-2[\s\S]*?p-commit",str1).group()
        name = re.search(r"em>[\s\S]*?</em",str2).group()
        name = name.replace('em>','')
        name = name.replace('</em','')
        name = name.replace("<font class=\"skcolor_ljg\">",'')
        name = name.replace("</font>",'')
        print("name = ",name)
        print("price= ",price)
        print("\n")
    
