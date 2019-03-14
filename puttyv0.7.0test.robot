*** Settings ***
Documentation     测试putty v0.7.0
Force Tags        puttyv0.7.0 test  owner-xuqiuying
Library           SoftLibrary
Variables         ${CURDIR}/resources/test_data.py
Variables         ${CURDIR}/resources/app_data.py

*** Variables ***
${APP NAME}     putty.exe
${LAST DIR}     resources


*** Test Cases ***
Test Close window on exit Button By SSH
    ${operation}     ENTER MESSAGE     ${CURRENT DATA}
    : FOR  ${CLOSE STATE}  IN   @{CLOSE STATES}
    \      OPEN APP    ${LAST DIR}   ${APP NAME}
    \      ${NAME}     GET URL
    \      ${WIN}      CONNECT SETTING   ${IP}   ${NAME}
    \      SAVE CONNECT   ${WIN}     ${CLOSE STATE}
    \      OPEN CONNECT   ${WIN}
    \      CONNECT     ${operation}
    \      CLOSE SESSION

Test Close window on exit Button By Telnet
    ${operation}     ENTER MESSAGE     ${CURRENT DATA}
    : FOR  ${CLOSE STATE}  IN   @{CLOSE STATES}
    \      OPEN APP    ${LAST DIR}   ${APP NAME}
    \      ${NAME}     GET URL
    \      ${WIN}      CONNECT SETTING   ${IP}    ${NAME}
    \      CONNECT TYPE   ${WIN}     RadioButton2
    \      SAVE CONNECT   ${WIN}     ${CLOSE STATE}
    \      OPEN CONNECT   ${WIN}
    \      SLEEP    6
    \      CONNECT    ${operation}
    \      CLOSE SESSION

Test Connection SSH By Error Password
    ${operation}     ENTER MESSAGE     ${ERROR DATA}
    : FOR  ${CLOSE STATE}  IN   @{CLOSE STATES}
    \      OPEN APP    ${LAST DIR}   ${APP NAME}
    \      ${NAME}     GET URL
    \      ${WIN}      CONNECT SETTING   ${IP}   ${NAME}
    \      SAVE CONNECT   ${WIN}     ${CLOSE STATE}
    \      OPEN CONNECT   ${WIN}
    \      CONNECT     ${operation}
    \      CLOSE SESSION

Test Delete Saved Connection
    ${operation}     ENTER MESSAGE     ${DATA}
    OPEN APP    ${LAST DIR}   ${APP NAME}
    ${NAME}     GET URL
    ${WIN}      CONNECT SETTING   ${IP}   ${NAME}
    SAVE CONNECT   ${WIN}     Always
    DELETE CONNECT   ${WIN}    ${NAME}
    CLOSE SETTING   ${WIN}



