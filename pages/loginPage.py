
from actions.mobile_actions import Appium_Actions
from appium.webdriver.common.appiumby import AppiumBy
import time

class LoginPage(Appium_Actions) :

    skipToLoginPage=(AppiumBy.XPATH,"(//android.widget.TextView[text(),'SKIP'])[3]");
    login_button = (AppiumBy.XPATH , "//android.widget.TextView[@text='Already have an account? Log In']");
    loginPage_Text=(AppiumBy.XPATH , '//android.widget.TextView[@text="Log In"]');
    username_input = (AppiumBy.XPATH , '(//android.widget.EditText)[1]');
    password_input = (AppiumBy.XPATH , '(//android.widget.EditText)[2]');
    startCooking_button = (AppiumBy.XPATH , '//android.widget.TextView[@text="START COOKING!"]')
    skip_button = (AppiumBy.XPATH , '//android.widget.TextView[@text="SKIP"]');
    gotIt_button=(AppiumBy.XPATH,"//android.widget.TextView[@text='GOT IT']")
    Account_logo = (AppiumBy.XPATH , '//android.view.ViewGroup[@content-desc="avatar"]/android.view.ViewGroup/android.widget.ImageView');
    logout_button = (AppiumBy.XPATH , '//android.widget.TextView[@text="Log Out"]');
    confirm_signout_button = (AppiumBy.XPATH , '//android.widget.Button[@resource-id="android:id/button1"]');
    invalid_email_errorMsg=(AppiumBy.XPATH , '//android.widget.TextView[@resource-id="input error"]');

    def __init__(self, driver) :
        super().__init__(driver);

    def login_function(self,username,password) :
        # self.click_webelement(self.skipToLoginPage);
        self.click_webelement(self.login_button);
        self.input_webelement(self.username_input, username);
        self.input_webelement(self.password_input, password);
        self.click_webelement(self.startCooking_button);

    def gotoHomePage(self):
        self.click_webelement(self.skip_button);
        time.sleep(1)
        self.click_webelement(self.skip_button);
        time.sleep(1)
        self.click_webelement(self.skip_button);
        time.sleep(1)
        self.click_webelement(self.skip_button);
        time.sleep(1)
        self.click_webelement(self.gotIt_button);
    
    def logout_function(self) :
        self.click_webelement(self.Account_logo);
        self.click_webelement(self.logout_button);
        self.click_webelement(self.confirm_signout_button);

	

