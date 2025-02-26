*** Settings ***
Library     SeleniumLibrary



*** Variables ***


*** Keywords ***


*** Test Cases ***
LoginTest
    open browser    https://www.instagram.com/accounts/login/      Chrome   options=add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
    maximize browser window
    #Set Selenium Implicit Wait    15s
    #Wait Until Element Is Visible    //*[@id='loginForm']//input[@name='username']    10s
    WAIT UNTIL ELEMENT IS VISIBLE    //*[@id='loginForm']//input[@name='username']  10s
    input text    xpath://*[@id='loginForm']//input[@name='username']   vhyshu2022
    wait until keyword succeeds    5x   2s  ELEMENT SHOULD BE VISIBLE    //*[@id='loginForm']//input[@name='password']
    input text    xpath://*[@id='loginForm']//input[@name='password']   147t1A0119@
    #Sleep    3s
    click element    xpath://*[@id='loginForm']//button/div[text()='Log in']
    wait until keyword succeeds     10s     2s    wait until element is visible    //*[contains(@class, 'x1n2onr6')]//span[text()='Home']
    click element    xpath://*[contains(@class, 'x1n2onr6')]//span[text()='Home']
    #sleep    10s
    #Wait Until Element Is Visible   //*[contains(@class,'x1n2onr6')]//span[text()='Search']     10s
    wait until keyword succeeds     10s     2s    wait until element is visible    //*[contains(@class,'x1n2onr6')]//span[text()='Search']
    click element    xpath://*[contains(@class,'x1n2onr6')]//span[text()='Search']
    wait until keyword succeeds     10s     2s    wait until element is visible    //*[@class='xjoudau x6s0dn4 x78zum5 xdt5ytf x1c4vz4f xs83m0k xrf2nzk x1n2onr6 xh8yej3 x1hq5gj4']//input[@type='text']
    input text    xpath://*[@class='xjoudau x6s0dn4 x78zum5 xdt5ytf x1c4vz4f xs83m0k xrf2nzk x1n2onr6 xh8yej3 x1hq5gj4']//input[@type='text']   rados
    wait until keyword succeeds     10s     2s    wait until element is visible    //*[@class='x6s0dn4 x78zum5 xdt5ytf x5yr21d x1odjw0f x1n2onr6 xh8yej3']//span[text()='radoss.co.in']
    click element    xpath://*[@class='x6s0dn4 x78zum5 xdt5ytf x5yr21d x1odjw0f x1n2onr6 xh8yej3']//span[text()='radoss.co.in']
    wait until keyword succeeds     10s     2s    wait until element is visible    //*[contains(@class,'x6ikm8r x10wlt62')]//span[text()='linktr.ee/radoss.co.in']
    click element    xpath://*[contains(@class,'x6ikm8r x10wlt62')]//span[text()='linktr.ee/radoss.co.in']
    sleep    10s
    close browser







