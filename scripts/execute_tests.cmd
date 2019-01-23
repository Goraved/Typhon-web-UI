: Path to base folder of tests
cd ..
for /f "delims=" %%# in ('powershell get-date -format "{dd-MMM-yyyy_HH_mm}"') do @set _now=%%#
call %~dp0venv\Scripts\activate
mkdir %~dp0allure_reports\archive\%_now%


: Run The tests in project folder
python -m pytest %~dp0tests\UI\  --alluredir %~dp0allure_reports\archive\%_now%

: Environments settings
copy %~dp0allure_reports\environment.properties %~dp0allure_reports\archive\%_now%

: Copy previous history
mkdir %~dp0allure_reports\archive\%_now%\history
copy %~dp0allure_reports\history\*.json %~dp0allure_reports\archive\%_now%\history

: Generate allure report folder
powershell -command "allure generate %~dp0allure_reports\archive\%_now% -o %~dp0allure_reports\archive\%_now%\generated-report"

: Saving test run to history
del /q %~dp0allure_reports\history\*
copy %~dp0allure_reports\archive\%_now%\generated-report\history\*.json %~dp0allure_reports\history

:Open generated report
powershell -command "allure open %~dp0allure_reports\archive\%_now%\generated-report"

: Run server with generated allure report
:powershell -noexit "allure serve %~dp0allure_reports\archive\%_now%"
