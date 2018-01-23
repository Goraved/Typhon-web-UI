: Path to base folder of tests
for /f "delims=" %%# in ('powershell get-date -format "{dd-MMM-yyyy_HH_mm}"') do @set _now=%%#
call %~dp0venv\Scripts\activate
mkdir %~dp0allureReports\archive\%_now%


: Run The tests in project folder
python -m pytest %~dp0tests\UI\  --alluredir %~dp0allureReports\archive\%_now%

: Environments settings
copy %~dp0allureReports\environment.properties %~dp0allureReports\archive\%_now%

: Copy previous history
mkdir %~dp0allureReports\archive\%_now%\history
copy %~dp0allureReports\history\*.json %~dp0allureReports\archive\%_now%\history

: Generate allure report folder
powershell -command "allure generate %~dp0allureReports\archive\%_now% -o %~dp0allureReports\archive\%_now%\generated-report"

: Saving test run to history
del /q %~dp0allureReports\history\*
copy %~dp0allureReports\archive\%_now%\generated-report\history\*.json %~dp0allureReports\history

:Open generated report
powershell -command "allure open %~dp0allureReports\archive\%_now%\generated-report"

: Run server with generated allure report
:powershell -noexit "allure serve %~dp0allureReports\archive\%_now%"
