import unittest
import numpy as np
import scipy.interpolate as si
from datetime import datetime
from time import sleep
from random import uniform
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Randomization Related
MIN_RAND = 0.64
MAX_RAND = 1.27
LONG_MIN_RAND = 4.78
LONG_MAX_RAND = 11.1

# Update this list with proxybroker http://proxybroker.readthedocs.io
PROXY = [
    {"host": "70.169.70.90", "port": 80,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.15, "error_rate": 0.0},
    {"host": "70.60.132.34", "port": 1080,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.36, "error_rate": 0.0},
    {"host": "96.66.200.209", "port": 64312,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.62, "error_rate": 0.0},
    {"host": "97.90.49.141", "port": 54321,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.22, "error_rate": 0.0},
    {"host": "70.169.129.246", "port": 48678,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.3, "error_rate": 0.0},
    {"host": "68.183.237.129", "port": 8080,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.32, "error_rate": 0.0},
    {"host": "54.174.159.255", "port": 8080,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.63, "error_rate": 0.0},
    {"host": " 54.213.173.231", "port": 80,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.4, "error_rate": 0.0},
    {"host": "74.214.177.61", "port": 8080,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.41, "error_rate": 0.0},
    {"host": "206.222.219.69", "port": 9,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.92, "error_rate": 0.0},
    {"host": "34.105.59.26", "port": 80,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.61, "error_rate": 0.0},
    {"host": "54.214.52.181", "port": 80,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.71, "error_rate": 0.0},
    {"host": "52.179.18.244", "port": 8080,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.65, "error_rate": 0.0},
    {"host": "199.195.252.161", "port": 8080,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.7, "error_rate": 0.0},
    {"host": "206.221.186.36", "port": 3128,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.76, "error_rate": 0.0},
    {"host": "64.71.145.122", "port": 3128,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.78, "error_rate": 0.0},
    {"host": "209.141.49.11", "port": 8080,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.82, "error_rate": 0.0},
    {"host": "104.244.75.26", "port": 8080,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.29, "error_rate": 0.0},
    {"host": "184.168.131.233", "port": 80,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.85, "error_rate": 0.0},
    {"host": "196.52.97.19", "port": 80,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.87, "error_rate": 0.0},
    {"host": "152.26.66.140", "port": 3128,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.88, "error_rate": 0.0},
    {"host": "196.52.97.129", "port": 80,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.34, "error_rate": 0.0},
    {"host": "35.169.156.54", "port": 3128,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.92, "error_rate": 0.0},
    {"host": "196.55.16.254", "port": 80,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.45, "error_rate": 0.0},
    {"host": "196.54.47.247", "port": 80,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 1.01, "error_rate": 0.0},
    {"host": "196.54.47.4", "port": 80,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.47, "error_rate": 0.0},
    {"host": "168.169.96.2", "port": 8080,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 1.03, "error_rate": 0.0},
    {"host": "70.169.145.164", "port": 808,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.51, "error_rate": 0.0},
    {"host": "196.54.47.167", "port": 80,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 1.14, "error_rate": 0.0},
    {"host": "104.45.188.43", "port": 3128,
     "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"},
             "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.64, "error_rate": 0.0}
]

index = int(uniform(0, len(PROXY)))
PROXY = PROXY[index]["host"] + ":" + str(PROXY[index]["port"])


class SyncMe(unittest.TestCase):
    headless = False
    options = None
    profile = None
    capabilities = None

    # Setup options for webdriver
    def setUpOptions(self):
        self.options = webdriver.FirefoxOptions()
        self.options.headless = self.headless

    # Setup profile with buster captcha solver
    def setUpProfile(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile._install_extension("buster_captcha_solver_for_humans-0.7.2-an+fx.xpi", unpack=False)
        self.profile.set_preference("security.fileuri.strict_origin_policy", False)
        self.profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0")
        self.profile.update_preferences()

    # Enable Marionette, An automation driver for Mozilla's Gecko engine
    def setUpCapabilities(self):
        self.capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.capabilities['marionette'] = True

    # Setup proxy
    def setUpProxy(self):
        self.log(PROXY)
        self.capabilities['proxy'] = {
            "proxyType": "MANUAL",
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY
        }

    # Setup settings
    def setUp(self):
        self.setUpProfile()
        self.setUpOptions()
        self.setUpCapabilities()
        # self.setUpProxy() # comment this line for ignore proxy
        self.driver = webdriver.Firefox(options=self.options, capabilities=self.capabilities,
                                        firefox_profile=self.profile, executable_path='./geckodriver')

    # Simple logging method
    def log(s, t=None):
        now = datetime.now()
        if t == None:
            t = "Main"
        print("%s :: %s -> %s " % (str(now), t, s))

    # Use time.sleep for waiting and uniform for randomizing
    def wait_between(self, a, b):
        rand = uniform(a, b)
        sleep(rand)

    # Using B-spline for simulate humane like mouse movements
    def human_like_mouse_move(self, action, start_element):
        points = [[6, 2], [3, 2], [0, 0], [0, 2]]
        points = np.array(points)
        x = points[:, 0]
        y = points[:, 1]

        t = range(len(points))
        ipl_t = np.linspace(0.0, len(points) - 1, 100)

        x_tup = si.splrep(t, x, k=1)
        y_tup = si.splrep(t, y, k=1)

        x_list = list(x_tup)
        xl = x.tolist()
        x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

        y_list = list(y_tup)
        yl = y.tolist()
        y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

        x_i = si.splev(ipl_t, x_list)
        y_i = si.splev(ipl_t, y_list)

        startElement = start_element

        action.move_to_element(startElement)
        action.perform()

        c = 5  # change it for more move
        i = 0
        for mouse_x, mouse_y in zip(x_i, y_i):
            action.move_by_offset(mouse_x, mouse_y)
            action.perform()
            self.log("Move mouse to, %s ,%s" % (mouse_x, mouse_y))
            i += 1
            if i == c:
                break

    def do_captcha(self, driver):
        # 1. Click recaptcha anchor
        self.log("Wait for recaptcha-anchor")
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))

        check_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']")))
        self.log("Wait")
        self.wait_between(MIN_RAND, MAX_RAND)
        action = ActionChains(driver)
        self.human_like_mouse_move(action, check_box)
        self.log("Click")
        check_box.click()

        # 2. Press solver button
        self.log("Wait")
        self.wait_between(MIN_RAND, MAX_RAND)
        self.log("Mouse movements")
        action = ActionChains(driver)
        self.human_like_mouse_move(action, check_box)
        # 2a. Switch Frame
        self.log("Switch Frame")
        driver.switch_to.default_content()
        WebDriverWait(driver, 0).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@title="recaptcha challenge"]')))
        self.log("Wait")
        self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)
        self.log("Find solver button")
        solver_button = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="solver-button"]')))
        self.log("Wait")
        self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)
        self.log("Click")
        solver_button.click()
        self.log("Wait")
        self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

        try:
            self.log("Alert exists")
            alert_handler = WebDriverWait(driver, 20).until(
                EC.alert_is_present()
            )
            alert = driver.switch_to.alert
            self.log("Wait before accept alert")
            self.wait_between(MIN_RAND, MAX_RAND)

            alert.accept()

            self.wait_between(MIN_RAND, MAX_RAND)
            self.log("Alert accepted, retry captcha solver")

            self.do_captcha(driver)
        except:
            self.log("No alert")

        self.log("Wait")
        driver.implicitly_wait(5)
        self.log("Switch")
        driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])

    # Main function  
    def test_run(self):
        driver = self.driver

        self.log("Start get")
        driver.get(WEBSITE LINK HERE)
        self.log("End get")

        self.log("Wait 1")
        self.wait_between(MIN_RAND, MAX_RAND)

        continue_btn = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "submit"))
        )

        self.log("Wait 2")
        self.wait_between(MIN_RAND, MAX_RAND)
        continue_btn.click()

        self.log("Wait 3")
        self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

        self.do_captcha(driver)
        self.log("Done")

    def tearDown(self):
        self.wait_between(21.13, 31.05)


if __name__ == "__main__":
    SyncMe
    unittest.main()
