import pytest
from appium.webdriver.appium_service import AppiumService
from appium.options.common import AppiumOptions
from selenium import webdriver
from typing import Dict,Any
import os
import configparser
import json
import logging

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, '..', 'config', 'config.ini')
mobile_data_path = os.path.join(current_dir,'..','data','data.json')




"""Mobile fixtures are started"""
"""This function provides the data for the mobile automation"""
def read_mobile_configuration() :
    configuration = configparser.ConfigParser();
    configuration.read(config_path)
    if 'Mobile' in configuration :
        mobile_configuration = configuration['Mobile']
        return mobile_configuration
    else :
        raise Exception("Mobile section is not found in config.ini")
    
"""This function provides the driver for the mobile automation"""
@pytest.fixture(scope='function')
def appium_driver_setup(request) :
    mobile_configuration = read_mobile_configuration();
    appium_server = AppiumService();
    appium_server.start();
    capabilities : Dict[str , Any ] = {
        "platformName" : mobile_configuration["platformName"],
        "appium:deviceName" : mobile_configuration["deviceName"],
        "appium:automationName" : mobile_configuration["automationName"],
        "appium:appPackage" : mobile_configuration["appPackage"],
        "appium:appActivity" : mobile_configuration["appActivity"],
        "appium:platformVersion" : mobile_configuration["platformVersion"],
        "appium:appPath" : mobile_configuration["appPath"]
    }
    driver = webdriver.Remote(mobile_configuration["appium_server_url"], options= AppiumOptions().load_capabilities(capabilities));
    yield driver
    driver.quit();
    appium_server.stop();

"""This function will provides the mobile data"""
@pytest.fixture
def mobile_data() :
    return json_data(mobile_data_path)
"""Mobile fixtures are ended"""

#This function is used to return the data from the json file common for ui,api,mobile
def json_data(filepath) :
    with open(filepath, "r") as file :
        data = json.load(file)
    return data;




@pytest.fixture(scope='function', autouse=True)
def logger_setup(request):
    # Configuring root logger
    logger_name = "root"
    root_logger = logging.getLogger(logger_name)
    root_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    # Adding console handler for displaying logs in the console
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    root_logger.addHandler(ch)
    # Creating log folder and file
    log_folder = os.path.abspath(os.path.join(current_dir, '..', 'Log'))  # Assuming 'Log' folder is located one level up
    try:
        os.makedirs(log_folder, exist_ok=True)
        log_file = os.path.join(log_folder, 'test_logs.log')
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        root_logger.addHandler(fh)
    except Exception as e:
        print(f"Error creating log folder or file: {e}")
    # Adjusting logging levels for specific loggers
    webdriver_logger = logging.getLogger('selenium.webdriver')  # Adjusting logging level for selenium.webdriver logger
    webdriver_logger.setLevel(logging.WARNING)
    urllib3_logger = logging.getLogger('urllib3')  # Adjusting logging level for urllib3 logger
    urllib3_logger.setLevel(logging.WARNING)
    yield  # Executing test functions
    # Cleaning up log handlers to avoid duplicate log entries
    root_logger.removeHandler(ch)
    if fh:
        root_logger.removeHandler(fh)
        fh.close()
