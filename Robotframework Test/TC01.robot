*** Settings ***

Library    SeleniumLibrary

*** Variables ***
${browser}    chrome
${url}    https://rahulshettyacademy.com/loginpagePractise/

*** Test Cases ***
LoginTest
    Open Browser    ${url}    ${browser}
    Fill The Login Form
    Close Browser


*** Keywords ***
loginToApplication
    Click Link    /html/body/div[7]/header/nav/ul/li[3]/ul/li[1]/a/span
    


