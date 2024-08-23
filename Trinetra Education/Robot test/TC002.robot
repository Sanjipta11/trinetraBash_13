*** Settings ***
Documentation    To validate the log in form
Library    SeleniumLibrary

*** Variables ***


*** Test Cases ***
Validate Unsuccessful Login
    Open the browser with perfect url
    Fill the log in form
#    wait untill it check and display the error message
#    verify error message correct

*** Keywords ***
Open the browser with perfect url
    Create Webdriver   Chrome
    Go To    https://rahulshettyacademy.com/loginpagePractise/
Fill the log in form
    Input Text    id:Username    sanjipt@gmail.com
    Input Password    id:password    qwerty
    Click Button    id:signInBtn
    
