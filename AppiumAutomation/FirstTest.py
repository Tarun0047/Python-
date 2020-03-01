from appium import webdriver

desired_cap={
   "deviceName": "Android Emulator",
   "platformName": "android",
   "appPackage": "com.ATG.World",
   "appWaitActivity": "com.atg.world.activity.IntroActivity",
   "app": "D:\\HR\\11012020.apk"
}

driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
