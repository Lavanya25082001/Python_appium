import pytest
import time
import allure
import logging
from pages.loginPage import LoginPage
from pages.searchPage import SearchPage

class TestMobileApp :

    """Login with valid username and password"""
    @pytest.mark.run(order = 1)
    def test_login_valid_data_functionality(self,appium_driver_setup,mobile_data) :
        logging.getLogger("root").info("Starting the test_login_valid_data_functionality")
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function( mobile_data['validCredentials']['username'], mobile_data['validCredentials']['password']); 
        logging.getLogger("root").info("Login successfully")
        time.sleep(mobile_data['timeouts']['largeWait'])
        loginPage.gotoHomePage()  
        time.sleep(mobile_data['timeouts']['mediumWait'])     
        loginPage.logout_function();
        logging.getLogger("root").info("Logout successfully")
    

    """Verifying search functionality"""
    @pytest.mark.run(order=2)
    def test_Search_Field_functionality(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function( mobile_data['validCredentials']['username'], mobile_data['validCredentials']['password']); 
        logging.getLogger("root").info("Login successfully")
        time.sleep(mobile_data['timeouts']['largeWait']) 
        loginPage.gotoHomePage();
        time.sleep(mobile_data['timeouts']['mediumWait'])
        searchPage=SearchPage(driver);
        logging.getLogger("root").info("Started Search validation functionality")
        searchPage.click_searchLogo();
        time.sleep(mobile_data['timeouts']['largeWait'])
        searchPage.VerifyingSearchField(mobile_data['Search_item']);
        logging.getLogger("root").info("validated search field successfully completed")

    @pytest.mark.run(order=3)
    def test_Search_by_meals(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function( mobile_data['validCredentials']['username'], mobile_data['validCredentials']['password']); 
        logging.getLogger("root").info("Login successfully")
        time.sleep(mobile_data['timeouts']['largeWait']) 
        loginPage.gotoHomePage();
        time.sleep(mobile_data['timeouts']['mediumWait'])
        searchPage=SearchPage(driver);
        logging.getLogger("root").info("Started Search page validation functionality")
        searchPage.click_searchLogo();
        searchPage.search_by_meals();
        logging.getLogger("root").info("Search by meals successfully completed")

    @pytest.mark.run(order=4)
    def test_search_by_ingredients(self,appium_driver_setup,mobile_data):
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function( mobile_data['validCredentials']['username'], mobile_data['validCredentials']['password']); 
        logging.getLogger("root").info("Login successfully")
        time.sleep(mobile_data['timeouts']['mediumWait']) 
        loginPage.gotoHomePage();
        time.sleep(mobile_data['timeouts']['mediumWait'])
        searchPage=SearchPage(driver);
        logging.getLogger("root").info("Validating search page with ingredients")
        searchPage.click_searchLogo(); 
        searchPage.search_by_ingredients();
        logging.getLogger("root").info("Search by ingredients functionality successfully completed")
        
        @pytest.mark.run(order=4)
        def test_search_by_ingredients(self,appium_driver_setup,mobile_data):
            driver = appium_driver_setup
            loginPage = LoginPage(driver);
            loginPage.login_function( mobile_data['validCredentials']['username'], mobile_data['validCredentials']['password']); 
            logging.getLogger("root").info("Login successfully")
            time.sleep(mobile_data['timeouts']['mediumWait']) 
            loginPage.gotoHomePage();
            time.sleep(mobile_data['timeouts']['mediumWait'])
            searchPage=SearchPage(driver);
            logging.getLogger("root").info("Validating search page with ingredients")
            searchPage.click_searchLogo(); 
        """Login with invalid username and password"""
    @pytest.mark.run(order=5)
    def test_login_invalid_data_functionality(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        loginPage=LoginPage(driver);
        logging.getLogger("root").info("Starting the test_login_invalid_data_functionality")
        loginPage.login_function( mobile_data['invalidCredentials']['invalidusername'], mobile_data['invalidCredentials']['invalidpassword']); 
        logging.getLogger("root").info("Verifying Error message while entering invalid credentials")
        assert driver.find_element(* loginPage.invalid_email_errorMsg).text == mobile_data['invalidCredentials']['invalidmailError']
        self.driver.back()