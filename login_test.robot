*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://localhost:3000/login
${BROWSER}    chrome

*** Test Cases ***
User Can Login Successfully
    Open Browser    ${URL}    ${BROWSER}
    Input Text      id=username    testuser
    Input Text      id=password    testpassword
    Click Button    id=loginButton
    Page Should Contain    Welcome, testuser
    Close Browser
