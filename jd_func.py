
import time
import re

def JD_func_test(driver,url):
    driver.maximize_window()
    driver.get(url)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    temp = driver.find_element_by_id('J_goodsList')
    ul = temp.find_element_by_tag_name("ul")
    lis = ul.find_elements_by_tag_name('li')
    return lis


def JD_info_save(lis_info):
    fd = open("info.txt",'w',encoding="gb18030")
    for item in lis_info:
        str1 = re.search(r"tab-content-item[\S\s]*?tab-content-item",item)
        if(str1 == None):
            str1 = item
        else:
            str1=str1.group()
        price = re.search(r"<em>￥</em>.*</i>",str1).group()
        str2 = re.search(r"p-name p-name-type-2[\s\S]*?p-commit",str1).group()
        name = re.search(r"em>[\s\S]*?</em",str2).group()
        print("name = ",name)
        print("price= ",price)
        print("\n")
    
