*** Settings ***
Library     SeleniumLibrary
Library     BuiltIn
Resource    locators.robot
Resource    timing.robot
*** Variables ***
${browser}  Chrome
${url}      https://www.google.com/
${name1}     Javeed
${list1}     Create List     10 20  30  40
@{list2}    10  20  30  40
${var1}     name
${int}      name    ${10}

*** Test Cases ***
LoginTest
    ${len_var1}     Get Length  ${var1}
    Log to Console      ${len_var1}
    ${edokati}      Set Variable    ${var1.__len__()}
    ${int}      Set Variable    name    ${10}
    ${type_check}       Evaluate    type(${int})
    Log to Console      ${type_check}
    ${var1}      Set Variable       javeed
    FOR     ${i}    IN RANGE    1
        Log to Console      ${var1}[${i}]
    END
    log to console    javeed