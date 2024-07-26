
from playwright.sync_api import Page
from playwright.sync_api import Browser
from playwright.sync_api import BrowserContext
from playwright.sync_api import BrowserType
from playwright.sync_api import BrowserConnectOptions
from playwright.sync_api import BrowserContextOptions
from playwright.sync_api import BrowserTypeLaunchOptions
from playwright.sync_api import BrowserTypeLaunchPersistentContextOptions
from playwright.sync_api import BrowserTypeLaunchServerOptions
from playwright.sync_api import BrowserTypeLaunchServerContextOptions
from playwright.sync_api import BrowserContextCookiesOptions
from playwright.sync_api import BrowserContextAddInitScriptOptions
from playwright.sync_api import BrowserContextClearCookiesOptions
from playwright.sync_api import BrowserContextClearPermissionsOptions
from playwright.sync_api import BrowserContextClearStorageOptions
from playwright.sync_api import BrowserContextCloseOptions
from playwright.sync_api import BrowserContextCoverageOptions
from playwright.sync_api import BrowserContextExposeBindingOptions
from playwright.sync_api import BrowserContextGrantPermissionsOptions
from playwright.sync_api import BrowserContextNewPageOptions
from playwright.sync_api import BrowserContextRouteOptions
from playwright.sync_api import BrowserContextSetDefaultNavigationTimeoutOptions
from playwright.sync_api import BrowserContextSetDefaultTimeoutOptions
from playwright.sync_api import BrowserContextSetExtraHTTPHeadersOptions
from playwright.sync_api import BrowserContextSetGeolocationOptions
from playwright.sync_api import BrowserContextSetOfflineOptions
from playwright.sync_api import BrowserContextSetViewportSizeOptions
from playwright.sync_api import BrowserContextSetRequestInterceptionOptions
from playwright.sync_api import BrowserContextSetRequestTimeoutOptions
from playwright.sync_api import BrowserContextSetResponseTimeoutOptions
from playwright.sync_api import BrowserContextSetUserAgentOptions
from playwright.sync_api import BrowserContextUnrouteOptions
from playwright.sync_api import BrowserContextWaitForEventOptions
from playwright.sync_api import BrowserNewContextOptions
from playwright.sync_api import BrowserNewPageOptions
from playwright.sync_api import BrowserTypeConnectOptions
from playwright.sync_api import BrowserTypeConnectOverCDPOptions
from playwright.sync_api import BrowserTypeLaunchOptions
from playwright.sync_api import BrowserTypeLaunchPersistentContextOptions
from playwright.sync_api import BrowserTypeLaunchServerOptions
from playwright.sync_api import BrowserTypeLaunchServerContextOptions
from playwright.sync_api import BrowserTypeNewContextOptions
from playwright.sync_api import BrowserTypeNewPageOptions
from playwright.sync_api import ConsoleMessage
from playwright.sync_api import Dialog
from playwright.sync_api import Download
from playwright.sync_api import ElementHandle
from playwright.sync_api importFileChooser
from playwright.sync_api import Frame
from playwright.sync_api import JSHandle
from playwright.sync_api import Keyboard
from playwright.sync_api import Mouse
from playwright.sync_api import PageBindingCallback
from playwright.sync_api import PageConsoleMessage
from playwright.sync_api import PageDialog
from playwright.sync_api import PageDownload
from playwright.sync_api import PageFileChooser
from playwright.sync_api import PageRequest
from playwright.sync_api import PageResponse
from playwright.sync_api import PageRoute
from playwright.sync_api import PageWorker
from playwright.sync_api import Request
from playwright.sync_api import Response
from playwright.sync_api import Route
from playwright.sync_api import Selectors
from playwright.sync_api import TimeoutError
from playwright.sync_api import Touchscreen
from playwright.sync_api import Video
from playwright.sync_api import WebSocket
from playwright.sync_api import WebSocketFrame
from playwright.sync_api import Worker

import datetime
import os
import sys

from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

class ExtentReportListener:
    def __init__(self):
        pass

    def on_test_start(self, result: Any) -> None:
        logger = report.start_test(result.get_method().get_method_name())
        logger.log(LogStatus.INFO, "Executing test: " + result.get_method().get_method_name())

    def on_test_success(self, result: Any) -> None:
        logger.log(LogStatus.INFO, "Finished executing test")

    def on_test_failure(self, result: Any) -> None:
        file_name = "Screenshot-{}.jpg".format(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        driver = result.get_test_context().get_attribute("WebDriver") #use string from setAttribute from BasePage
        src_file = driver.get_screenshot_as(OutputType.FILE)
        dest_file = os.path.join("./screenshots", file_name)
        try:
            shutil.copyfile(src_file, dest_file)
            print("Screenshot taken, saved in screenshots folder")
        except IOError:
            print("Failed to take screenshot")
        logger.log(LogStatus.FAIL, "Test failed, attaching screenshot in screenshots folder")

    def on_test_skipped(self, result: Any) -> None:
        logger.log(LogStatus.SKIP, "Test skipped")