*** Settings ***
Documentation    Suite description
Library      SeleniumLibrary
Library      BuiltIn

Suite Setup     Run Keywords
...   Open Browser    https://www.google.co.in      Chrome   executable_path=
...   AND    Sleep   2s
#...   AND    SKIP      don't execute it further

*** Test Cases ***
Seach Content
    Input Text      name=q      Selenium


Click on Search Button
     Click Element      name=btnK



*** Keywords ***
Provided precondition
    Setup system under test