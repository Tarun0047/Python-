from appium import webdriver

desired_cap={
   "deviceName": "emulator-5554",
   "platformName": "android",
   "appPackage": "com.ATG.World",
   "appActivity": "com.atg.world.activity.SplashActivity",
   "appWaitDuration": "50",
   "uiautomator2ServerLaunchTimeout": "50000",
   "uiautomator2ServerInstallTimeout": "50000",
   "appWaitActivity": "com.atg.world.activity.IntroActivity",
   "app": "D:\\HR\\11012020.apk"
}

driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

#click the current window using Id
driver.implicitly_wait(30)
driver.find_element_by_id('com.ATG.World:id/getStartedTv').click()
driver.find_element_by_id('com.ATG.World:id/login_email').click()

#send values through xpath

value1=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
value1.send_keys('wiz_saurabh@rediffmail.com')
value2=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText')
value2.send_keys('Pass@123')

#sign in
driver.find_element_by_id('com.ATG.World:id/email_sign_in_button').click()