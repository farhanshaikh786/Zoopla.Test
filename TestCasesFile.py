import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Test(unittest.TestCase):

    def setUp(self):
        dir=os.getcwd()
        self.driver = webdriver.Chrome(dir+"/ChromeDriver/chromedriver")
        wait=WebDriverWait(self.driver,60)
        self.driver.get("https://www.zoopla.co.uk/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)

    def atest_A_Registerd_for_daily_email_updates_on_rental_property_in_london_for_1_bed_and_price_between_800_1000(self):
        try:
            driver = self.driver
            driver.find_element_by_xpath("//button[text()='Save my preferences']").click()
            driver.find_element_by_xpath("//a[@aria-label='Zoopla']/following-sibling::div//a[text()='Sign in']").click()
            driver.find_element_by_id("signin_email").send_keys("testinrstar05@gmail.com")
            driver.find_element_by_id("signin_password").send_keys("Test@123")
            driver.find_element_by_id("signin_submit").click()
            time.sleep(3)
            print("Login successfull")
            driver.find_element_by_xpath("//span[text()='To rent']").click()
            driver.find_element_by_id("search-input-location").send_keys("London")
            time.sleep(2)
            print("Search for property in : " + "London")
            driver.find_element_by_id("search-input-location").click()
            time.sleep(2)
            driver.find_element_by_id("rent_price_min_per_month").click()
            driver.find_element_by_xpath("//option[text()='£800 pcm']").click()
            print("min Rent selected")
            driver.find_element_by_id("rent_price_min_per_month").click()
            time.sleep(2)
            driver.find_element_by_id("rent_price_max_per_month").click()
            driver.find_element_by_xpath("(//option[text()='£1,000 pcm'])[2]").click()
            time.sleep(2)
            print("Max Rent selected")
            driver.find_element_by_id("beds_min").click()
            driver.find_element_by_xpath("//option[text()='1+']").click()
            time.sleep(2)
            print("Number of bedroom selected")
            ActionChains(driver).move_to_element(driver.find_element_by_id("search-submit")).perform()
            driver.find_element_by_id("search-submit").click()
            print("Search Result displayed")
            driver.find_element_by_xpath("//a[@id='alert-btn-create']").click()
            driver.find_element_by_xpath("//button[@value='Save search']").click()
            time.sleep(5)
            if(len(driver.find_elements_by_xpath("//div[text()='Search saved']"))>0):
                print("Daily Email updated alert for specified property is registed : Pass")
            else:
                print("Daily Email Update alert for seficied property is not registerd : Fail")
                self.fail("Daily Email Update alert for seficied property is not registerd : Fail")
            driver.find_element_by_xpath("//span[contains(text(),'Instant property alerts')]").click()
            driver.find_element_by_xpath("//label[text()='Daily summary emails']").click()
            driver.find_element_by_xpath("//button[@value='Save search']").click()
            time.sleep(5)
            if(len(driver.find_elements_by_xpath("//span[text()='Daily summary emails']"))>0):
                print("Frequency of email alert change successfully : Pass")
            else:
                print("Frequency of email alert change successfully : Fail")
                self.fail("Frequency of email alert change successfully : Fail")
            
            
            
        except Exception as e:
            self.fail()

    def atest_B_verify_search_for_perticular_property_in_house_price_search_and_confirm_it_appears_first(self):
        try:
            driver = self.driver
            driver.find_element_by_xpath("//button[text()='Save my preferences']").click()
            driver.find_element_by_xpath("//span[text()='House prices']").click()
            driver.find_element_by_id("search-input-location").send_keys("189 Coppermill Road, TW19 5NW")
            driver.find_element_by_id("search-submit").click()
            time.sleep(5)
            print("Search for House in : " + "189 Coppermill Road, TW19 5NW")
            if(len(driver.find_elements_by_xpath("//div[@class='hp-card-list']/section[1]//*[contains(text(),'189 Coppermill Road, TW19 5NW')]"))>0):
                print("Search House price properties appears first : Pass")
            else:
                print("Searched House prices properties not appear first in search result : Fail")
                self.fail("Searched House prices properties not appear first in search result : Fail")
            
            
        except Exception as e:
            self.fail()

    def test_C_verify_search_house_for_sale_including_keyword_garage_and_check_result_have_garages(self):
        try:
            driver = self.driver
            driver.find_element_by_xpath("//button[text()='Save my preferences']").click()
            driver.find_element_by_id("search-input-location").send_keys("London" + Keys.TAB)
            print("Search : London")
            time.sleep(2)
            driver.find_element_by_id("search-input-location").click()
            driver.find_element_by_id("property_type").click()
            driver.find_element_by_xpath("//option[text()='Houses']").click()
            print("Selected Houses as type")
            driver.find_element_by_xpath("//span[text()='Advanced search options']").click()
            print("Clicked on Advance Search")
            ActionChains(driver).move_to_element(driver.find_element_by_id("keywords")).perform()
            driver.find_element_by_id("keywords").send_keys("Garage")
            print("Type Keyword : " + "Garage")
            time.sleep(2)

            driver.find_element_by_id("search-submit").click()
            print("Clicked on Search button")
            time.sleep(5)
            print("Search Result displayed : Pass")
            driver.find_element_by_xpath("//div[@id='content']/ul/li[1]//a[@class='photo-hover']").click()
            print("Open first search result")
            if(len(driver.find_elements_by_xpath("//section[@class='dp-features']//*[contains(text(),'Garage')]"))>0):
                print("Search keyword displayed in search result : Pass")
            else:
                print("Search keyword not  displayed in search result : Fail")
                self.fail("Search keyword not displayed in search result : Fail")
            driver.find_element_by_xpath("//span[contains(text(),'Back to search results')]").click()
            print("Click on Back to search resutl button")
            driver.find_element_by_xpath("//div[@id='content']/ul/li[2]//a[@class='photo-hover']").click()
            print("Open second search result")
            if(len(driver.find_elements_by_xpath("//section[@class='dp-features']//*[contains(text(),'Garage')]"))>0):
                print("Search keyword displayed in second search result : Pass")
            else:
                print("Search keyword not  displayed in second search result : Fail")
                self.fail("Search keyword not displayed in second search result : Fail")
            
        except Exception as e:
            self.fail()

    def atest_D_Verify_Save_Search_property(self):
        try:
            driver = self.driver
            driver.find_element_by_xpath("//button[text()='Save my preferences']").click()
            driver.find_element_by_xpath("//a[@aria-label='Zoopla']/following-sibling::div//a[text()='Sign in']").click()
            driver.find_element_by_id("signin_email").send_keys("testinrstar05@gmail.com")
            driver.find_element_by_id("signin_password").send_keys("Test@123")
            driver.find_element_by_id("signin_submit").click()
            print("Login Successfully")
            time.sleep(3)
            driver.find_element_by_id("search-input-location").send_keys("Putney, London")
            time.sleep(2)
            driver.find_element_by_id("search-input-location").click()
            time.sleep(2)
            print("Seaerch for property in " + "Putney, London")
            ActionChains(driver).move_to_element(driver.find_element_by_id("search-submit")).perform()
            driver.find_element_by_id("search-submit").click()
            print("Clickon Search button")
            print("Search Result displayed")
            driver.find_element_by_xpath("//a[@id='alert-btn-save' and @data-title='Save search']").click()
            driver.find_element_by_xpath("//button[@value='Save search']").click()
            time.sleep(5)
            if(len(driver.find_elements_by_xpath("//div[text()='Search saved']"))>0):
                print("Propety Searche is saved successfully : Pass")
            else:
                print("Propety Searche is saved successfully : Pass : Fail")
                self.fail("Propety Searche is saved successfully : Pass : Fail")
            
        except Exception as e:
            self.fail()

    def atest_E_Verify_Retrive_Save_property(self):
        try:
            driver = self.driver
            driver.find_element_by_xpath("//button[text()='Save my preferences']").click()
            driver.find_element_by_xpath("//a[@aria-label='Zoopla']/following-sibling::div//a[text()='Sign in']").click()
            driver.find_element_by_id("signin_email").send_keys("testinrstar05@gmail.com")
            driver.find_element_by_id("signin_password").send_keys("Test@123")
            driver.find_element_by_id("signin_submit").click()
            print("Login successfully : Pass")
            time.sleep(3)
            driver.find_element_by_xpath("//a[@aria-label='Zoopla']/following-sibling::div//a[@data-testid='header-profile-account']").click()
            time.sleep(3)
            print("Click on Username")
            driver.find_element_by_xpath("//a[contains(text(),'Alerts & searches')]").click()
            time.sleep(2)
            driver.find_element_by_xpath("(//h4[contains(text(),'Putney, London')]/parent::div/following-sibling::div//a[contains(text(),'View')])[1]").click()
            print("Click on view link to check saved search")
            time.sleep(5)
            if(len(driver.find_elements_by_xpath("//form[@id='form-search-and-refine']//span[contains(text(),'Putney, London')]"))>0):
                print("Search Result Retrived successufully : Pass")
            else:
                print("Search Result Retrived not successufully : Pass : Fail")
                self.fail("Search Result Retrived not successufully : Pass : Fail")
            driver.find_element_by_xpath("//a[@aria-label='Zoopla']/following-sibling::div//a[@data-testid='header-profile-account']").click()
            time.sleep(3)
            driver.find_element_by_xpath("//a[contains(text(),'Alerts & searches')]").click()
            if(len(driver.find_elements_by_xpath("(//h4[contains(text(),'Putney, London')]/parent::div/following-sibling::div//a[contains(text(),'Delete')])[1]"))>0):
                driver.find_element_by_xpath("(//h4[contains(text(),'Putney, London')]/parent::div/following-sibling::div//a[contains(text(),'Delete')])[1]").click()
            if(len(driver.find_elements_by_xpath("(//a[text()='Delete all recent searches'])[1]"))>0):
                driver.find_element_by_xpath("(//a[text()='Delete all recent searches'])[1]").click()
            if(len(driver.find_elements_by_xpath("(//a[text()='Delete all recent searches'])[1]"))>0):
                driver.find_element_by_xpath("(//a[text()='Delete all recent searches'])[1]").click()
            if(len(driver.find_elements_by_xpath("(//a[contains(text(),'Delete')])[1]"))>0):
                driver.find_element_by_xpath("(//a[contains(text(),'Delete')])[1]").click()

            print("All searches are deleted ")
        except Exception as e:
            self.fail()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()