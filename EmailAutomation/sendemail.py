from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1582308422&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3dde0ae34f-4a1b-ecd6-cd71-f8978fc880ff&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")

driver.find_element_by_name("loginfmt").send_keys("tarundude678@gmail.com")
driver.find_element_by_css_selector("#idSIButton9").click()
time.sleep(5)
driver.find_element_by_name("passwd").send_keys("Tarun8572")
driver.find_element_by_css_selector('#idSIButton9').click()

time.sleep(7)

driver.find_element_by_css_selector('#id__3').click()
time.sleep(10)
driver.find_element_by_css_selector('#app > div > div._3KAPMPOz8KsW24ooeUflK2 > div._2jR8Yc0t2ByBbcz_HIGqZ4 > div._1TpU2KF6f_EeQiytBaYj8I > div._3mBjlqTqXMUiRuuWRKCPtX.css-41 > div._1jw6v9zFEgnOiXShpU1qqM > div > div.mm4nCLKbIRtx5HvuorDWT > div._1QDTZfBsizkS8O4Jej5a3A > div > div > div > div._29NreFcQ3QoBPNO3rKXKB0 > div._3Yr_hO7j5doGUkhrRiP6uY > div:nth-child(1) > div:nth-child(2) > div > div > div > div > div > div.ms-FocusZone.css-58 > div > div > input').send_keys("priyankashahane3696@gmail.com")
driver.find_element_by_css_selector('#subjectLine0').send_keys("Hi")
driver.find_element_by_css_selector('#app > div > div._3KAPMPOz8KsW24ooeUflK2 > div._2jR8Yc0t2ByBbcz_HIGqZ4 > div._1TpU2KF6f_EeQiytBaYj8I > div._3mBjlqTqXMUiRuuWRKCPtX.css-41 > div._1jw6v9zFEgnOiXShpU1qqM > div > div.mm4nCLKbIRtx5HvuorDWT > div._1QDTZfBsizkS8O4Jej5a3A > div > div > div > div._29NreFcQ3QoBPNO3rKXKB0 > div._2_G1lB2DCB_6t73ZTT6vX3._2Hl0t2u2yIjuWmfatKUaJ2 > div._4utP_vaqQ3UQZH0GEBVQe.B1QSRkzQCtvCtutReyNZ._17ghdPL1NLKYjRvmoJgpoK._2s9KmFMlfdGElivl0o-GZb').send_keys("Hello selenium")
time.sleep(10)
driver.find_element_by_css_selector('#app > div > div._3KAPMPOz8KsW24ooeUflK2 > div._2jR8Yc0t2ByBbcz_HIGqZ4 > div._1TpU2KF6f_EeQiytBaYj8I > div._3mBjlqTqXMUiRuuWRKCPtX.css-41 > div._1jw6v9zFEgnOiXShpU1qqM > div > div.mm4nCLKbIRtx5HvuorDWT > div._1QDTZfBsizkS8O4Jej5a3A > div > div > div > div._29NreFcQ3QoBPNO3rKXKB0 > div._1vGTUqFfb2m4yyZJJPHFDg._1PGX4GmfSf_CaaQSnoiB4l > div._3_ptG0kLp__HkP_iDhvXmm > div.ivs3kF0TSy1MNYEjC_hAw > button.ms-Button.ms-Button--primary.y8XIN4EAeheOqsn4BJB7R._1aULoKiKSQ3J7ZKBzQCv6Q.root-120 > span > i').click()
#to_ele.send_keys("tarundhiman8572@gmail.com")
#subj_ele=driver.find_element_by_name("subjectbox")
#subj_ele.send_keys("Hello selenium")

