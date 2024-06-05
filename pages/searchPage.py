from actions.mobile_actions import Appium_Actions
from appium.webdriver.common.appiumby import AppiumBy
import time

class SearchPage(Appium_Actions) :

    searchLogo=(AppiumBy.XPATH,"//android.widget.Button[@content-desc='Search']/android.view.ViewGroup/android.view.ViewGroup");
    searchPage_text = (AppiumBy.XPATH , "//android.widget.TextView[@text='Search']");
    breakfast_optn=(AppiumBy.XPATH , '//android.widget.TextView[@text="Breakfast"]');
    brunch_optn = (AppiumBy.XPATH , '//android.widget.TextView[@text="Brunch"]');
    lunch_optn = (AppiumBy.XPATH , '//android.widget.TextView[@text="Lunch"]');
    snacks_optn = (AppiumBy.XPATH , '//android.widget.TextView[@text="Snack"]')
    dinner_optn = (AppiumBy.XPATH , '//android.widget.TextView[@text="Dinner"]')
    dessert_optn = (AppiumBy.XPATH , '//android.widget.TextView[@text="Dessert"]');
    pasta_optn=(AppiumBy.XPATH,'//android.widget.TextView[@text="Pasta"]')
    quick_optn = (AppiumBy.XPATH , '//android.widget.TextView[@text="Quick & Easy"]');
    spring_optn = (AppiumBy.XPATH , '//android.widget.TextView[@text="Spring"]');
    salad_optn = (AppiumBy.XPATH , '//android.widget.TextView[@text="Salad"]');
    save_item = (AppiumBy.XPATH , '(//android.view.ViewGroup[@content-desc="save"])[1]');
    item = (AppiumBy.XPATH , '(//android.view.ViewGroup[@resource-id="container"])[1]');
    addtoCart = (AppiumBy.XPATH , '(//android.view.ViewGroup[@resource-id="addToCart"])[1]');
    saveList = (AppiumBy.XPATH , '(//android.widget.TextView)[1]');
    cartList = (AppiumBy.XPATH , '(//android.widget.TextView)[2]');
    viewAllItem = (AppiumBy.XPATH , '//android.widget.TextView[@text="VIEW ALL"]');
    Item1 = (AppiumBy.XPATH , '(//android.widget.ImageView)[1]');
    Item2 = (AppiumBy.XPATH , '(//android.widget.ImageView)[3]');
    Item3 = (AppiumBy.XPATH , '(//android.widget.ImageView)[5]');
    Item4 = (AppiumBy.XPATH , '(//android.widget.ImageView)[7]');
    Item5 = (AppiumBy.XPATH , '(//android.widget.ImageView)[9]');
    Item6 = (AppiumBy.XPATH , '(//android.widget.ImageView)[11]');
    Item7 = (AppiumBy.XPATH , '(//android.widget.ImageView)[13]');
    Item8 = (AppiumBy.XPATH , '(//android.widget.ImageView)[15]');
    searchWithIngredients_btn = (AppiumBy.XPATH , '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]');
    ingredientsPageText= (AppiumBy.XPATH , '(//android.widget.TextView)[3]');
    searchInput = (AppiumBy.XPATH , '//android.widget.EditText[@text="Search Recipes"]');
    searchResults = (AppiumBy.XPATH , '(//android.widget.TextView)[2]');
    clear = (AppiumBy.XPATH , '//android.view.ViewGroup[@resource-id="clear"]');
    cancel = (AppiumBy.XPATH , '//android.widget.TextView[@text="CANCEL"]');
    cart_List_optns= (AppiumBy.XPATH , '//android.view.ViewGroup[@content-desc="options"]/android.view.ViewGroup');
    clearList= (AppiumBy.XPATH , '//android.widget.TextView[@text="Clear List"]');
    clearList_confirm= (AppiumBy.XPATH , '//android.widget.Button[@resource-id="android:id/button1"]');
    back_btn=(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="back"]')


    def __init__(self, driver) :
        super().__init__(driver);

    def click_searchLogo(self) :
        self.click_webelement(self.searchLogo);
    
    def search_by_meals(self) :
        time.sleep(3) 
        self.click_webelement(self.breakfast_optn);
        self.click_webelement(self.save_item);
        time.sleep(1)
        self.click_webelement(self.addtoCart)
        self.driver.back()
        self.click_webelement(self.brunch_optn);
        self.click_webelement(self.save_item);
        time.sleep(1)
        self.click_webelement(self.addtoCart)
        self.driver.back()
        self.click_webelement(self.lunch_optn);
        self.click_webelement(self.save_item);
        time.sleep(1)
        self.click_webelement(self.addtoCart)
        self.driver.back()
        self.click_webelement(self.snacks_optn);
        self.click_webelement(self.save_item);
        time.sleep(1)
        self.click_webelement(self.addtoCart)
        self.driver.back()
        self.click_webelement(self.dinner_optn);
        self.click_webelement(self.save_item);
        time.sleep(1)
        self.click_webelement(self.addtoCart)
        self.driver.back()
        time.sleep(5)
        self.click_webelement(self.dessert_optn);
        self.click_webelement(self.save_item);
        time.sleep(1)
        self.click_webelement(self.addtoCart)
        self.driver.back()
        

    def search_by_ingredients(self):
        self.click_webelement(self.viewAllItem);
        time.sleep(1)
        self.click_webelement(self.Item1);
        time.sleep(1)
        self.click_webelement(self.Item2);
        time.sleep(1)
        self.click_webelement(self.Item3);
        time.sleep(1)
        self.click_webelement(self.Item4);
        time.sleep(1)
        self.click_webelement(self.Item5);
        time.sleep(1)
        self.click_webelement(self.Item6);
        time.sleep(1)
        self.click_webelement(self.searchWithIngredients_btn);
        self.driver.back()
    
    def VerifyingSearchField(self,searchitem) :
        self.click_webelement(self.searchInput);
        time.sleep(2)
        self.input_webelement(self.searchInput,searchitem)
        time.sleep(2)
        self.is_webelement_displayed(self.searchResults);
        self.click_webelement(self.clear);
        self.click_webelement(self.cancel);
        self.driver.back()
        time.sleep(2)
        
    def Clearing_data(self):
        self.click_webelement(self.cartList);
        self.click_webelement(self.cart_List_optns);
        self.click_webelement(self.clearList);
        self.click_webelement(self.clearList_confirm);
        self.click_webelement(self.back_btn);

