
@echo off

:: to be changed by the user
SET EP_VERSION=23.2p0
SET INSTALL_DIR=C:/Program Files/BTC
SET PORT=1337

echo.
echo INSTALL_DIR="%INSTALL_DIR%"
echo EP_VERSION=%EP_VERSION%
echo PORT=%PORT%
echo.
echo Starting BTC EmbeddedPlatform REST API Endpoint...
echo.
echo Check status at: http://localhost:%PORT%/ep/documentation/index.html
echo.

:: local auxilary vars
SET appdata_location=%APPDATA%/BTC/ep/%EP_VERSION%/%PORT%

call "%INSTALL_DIR%/ep%EP_VERSION%/rcp/ep.exe" ^
-clearPersistedState ^
-application ep.application.headless ^
-nosplash ^
-vmargs ^
-Dep.rest.port=%port% ^
-Dep.runtime.batch=ep ^
-Dep.runtime.api.port=29300 ^
-Dosgi.configuration.area.default=%appdata_location%/configuration ^
-Dosgi.instance.area.default=%appdata_location%/workspace ^
-Dep.configuration.logpath=%appdata_location%/logs ^
-Dep.runtime.workdir=%appdata_location%
