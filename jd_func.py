
import time


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
