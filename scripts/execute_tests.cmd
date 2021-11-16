: Path to base folder of tests
cd ..
for /f "delims=" %%# in ('powershell get-date -format "{dd-MMM-yyyy_HH_mm}"') do @set _now=%%#
call %~dp0venv\Scripts\activate
mkdir %~dp0allure-results\archive\%_now%


: Run The tests in project folder
python -m pytest %~dp0tests\UI\  --alluredir %~dp0allure-results\archive\%_now%

: Environments settings
copy %~dp0allure-results\environment.properties %~dp0allure-results\archive\%_now%

: Copy previous history
mkdir %~dp0allure-results\archive\%_now%\history
copy %~dp0allure-results\history\*.json %~dp0allure-results\archive\%_now%\history

: Generate allure report folder
powershell -command "allure generate %~dp0allure-results\archive\%_now% -o %~dp0allure-results\archive\%_now%\generated-report"

: Saving test run to history
del /q %~dp0allure-results\history\*
copy %~dp0allure-results\archive\%_now%\generated-report\history\*.json %~dp0allure-results\history

:Open generated report
powershell -command "allure open %~dp0allure-results\archive\%_now%\generated-report"

: Run server with generated allure report
:powershell -noexit "allure serve %~dp0allure-results\archive\%_now%"
