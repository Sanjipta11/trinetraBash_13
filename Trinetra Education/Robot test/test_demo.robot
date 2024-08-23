*** Settings ***
Documentation    To validate the Login form
Library    SeleniumLibrary
Library    Collections
Test Setup    Open the browser with perfect url
Resource    resource.robot


*** Variables ***
${error_message_login}    css:.alert-danger
${shop_page_load}    css:.nav-link

*** Test Cases ***
Validate UnSuccesful Login
    Fill the login form    ${user_name}    ${invalid_password}    ${sign_buttom}
    Wait until Element is loacted in the page    ${error_message_login}
#    Verify error message is correct

Validate Card dispaly in the Shopping Page
    Fill the login form    ${user_name}    ${valid_password}    ${sign_buttom}
    Wait until Element is loacted in the page    ${shop_page_load}
    Verify Card Titles in the shop page
    Select the Card    Nokia Edge


*** Keywords ***
Fill the login form
    [Arguments]    ${user_name}    ${password}    ${sign_buttom}
    Input Text    id:username    ${user_name}
    Input Password    id:password    ${password}
    Click Button    ${sign_buttom}

Wait until Element is loacted in the page
    [Arguments]    ${element}
    Wait Until Element Is Visible    ${element}

#Verify error message is correct
#    ${result}=    Get Text    ${error_message_login}
##    Should Be Equal As Strings    ${result}    Incorrect username/password.
#    Element Text Should Be    ${error_message_login}    Incorrect username/password.

Verify Card Titles in the shop page
    @{expected_list}=    Create List    iphone X    Samsung Note 8    Nokia Edge    Blackberry
    ${elements}=    Get WebElements    css:.card-title
    @{actuallist}=    Create List
    FOR    ${i}    IN    @{elements}
        Log    ${i.text}
        Append To List    ${actuallist}    ${i.text}
    END
    Lists Should Be Equal    ${expected_list}    ${actuallist}

Select the Card
    [Arguments]    ${card_name}
    ${elements}=    Get WebElements    css:.card-title
    FOR    ${i}    IN     @{elements}
        Exit For Loop If    '${card_name}' == '${i.text}'