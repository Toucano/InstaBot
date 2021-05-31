from selenium import webdriver
from time import sleep
import secret
import AlwaysFollow





webdriver = webdriver.Chrome()

sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)


def unfollow():
    neverUnfollow = AlwaysFollow.alwaysfollow
    print(neverUnfollow)
    following_button = webdriver.find_element_by_xpath("//a[contains(@href, '/following')]")
    following_button.click()
    sleep(2)
    # yazidtaki = webdriver.find_element_by_xpath("//a[contains(@href, '/yazid_taki')]")
    popfollow = webdriver.find_element_by_xpath("//div[@class='isgrP']")
    # webdriver.execute_script('arguments[0].scrollIntoView()', yazidtaki)
    sleep(2)
    lastht, ht = 0, 1
    while lastht != ht :
        lastht = ht
        sleep(1)
        ht = webdriver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """,popfollow)
    unfollowButtons = webdriver.find_elements_by_class_name('sqdOP  L3NKy    _8A5w5    ')
    buttons = popfollow.find_elements_by_tag_name('button')
    unFollowed = 0
    for button in buttons:
        sleep(2)
        unFollowed += 1
        try :
            sleep(1)
            button.click()
        except Exception:
            sleep(1)
            webdriver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button[1]").click()

    print(unFollowed)

    # for x in unfollowButtons:
    #     unfollowButtons[x].click()
    #     sleep(1)
    print(len(unfollowButtons))
    print(len(buttons))



username = webdriver.find_element_by_name('username')
username.send_keys(secret.username)
password = webdriver.find_element_by_name('password')
password.send_keys(secret.password)

button_login = webdriver.find_element_by_xpath("//button[@type='submit']")
button_login.click()
sleep(3)

notregistered = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
notregistered.click()
sleep(3)

notnow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

my_profile = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a')
my_profile.click()

sleep(2)

unfollow()

