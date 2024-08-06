An error occurred: HTTPConnectionPool(host='209.20.158.190', port=8000): Max retries exceeded with url: /ask?instruction=convert+code+to+playwright%3Apackage+com.sdet.auto%3B%0A%0Aimport+com.sdet.auto.PageObjects.%2A%3B%0Aimport+com.sdet.auto.TestHelper.AccessibilityHelper%3B%0Aimport+org.junit.FixMethodOrder%3B%0Aimport+org.junit.Test%3B%0Aimport+org.junit.runners.MethodSorters%3B%0A%0A%40FixMethodOrder%28MethodSorters.NAME_ASCENDING%29%0Apublic+class+SeleniumTest+extends+TestBaseClass%7B%0A%0A++++%40Test%0A++++public+void+TC0001_SmokeTest%28%29+%7B%0A%0A++++++++GuiHelper.openWebBrowser%28%29%3B%0A++++++++Navigation.navToWebPageUnderTest%28%29%3B%0A++++++++HomePage.VerifyOnHomePage%28testAssert%29%3B%0A++++++++GuiHelper.closeWebBrowser%28%29%3B%0A++++%7D%0A%0A++++%40Test%0A++++public+void+TC0002_ForgetPasswordTest%28%29+%7B%0A%0A++++++++final+String+email+%3D+%22sdet.testautomation%40gmail.com%22%3B%0A++++++++final+String+expectedMsg+%3D+%22Your+e-mail%27s+been+sent%21%22%3B%0A%0A++++++++GuiHelper.openWebBrowser%28%29%3B%0A++++++++Navigation.navToWebPageUnderTest%28%29%3B%0A++++++++HomePage.ClickForgetPassword%28%29%3B%0A++++++++ForgetPasswordPage.EnterEmail%28email%29%3B%0A++++++++ForgetPasswordPage.ClickRetrieveButton%28%29%3B%0A++++++++EmailSentPage.VerifyEmailSent%28testAssert%2C+expectedMsg%29%3B%0A++++++++GuiHelper.closeWebBrowser%28%29%3B%0A++++%7D%0A%0A++++%40Test%0A++++public+void+TC0003_FormAuthentication%28%29+%7B%0A%0A++++++++final+String+userId+%3D+%22tomsmith%22%3B%0A++++++++final+String+password+%3D+%22SuperSecretPassword%21%22%3B%0A++++++++final+String+expectedLoginMsg+%3D+%22You+logged+into+a+secure+area%21%22%3B%0A++++++++final+String+expectedLogoutMsg+%3D+%22You+logged+out+of+the+secure+area%21%22%3B%0A%0A++++++++GuiHelper.openWebBrowser%28%29%3B%0A++++++++Navigation.navToWebPageUnderTest%28%29%3B%0A++++++++HomePage.clickFormAuthentication%28%29%3B%0A++++++++LoginPage.enterCredentials%28userId%2C+password%29%3B%0A++++++++SecureAreaPage.verifyMessage%28testAssert%2C+expectedLoginMsg%29%3B%0A++++++++SecureAreaPage.clickLogoutButton%28%29%3B%0A++++++++LoginPage.verifyMessage%28testAssert%2C+expectedLogoutMsg%29%3B%0A++++++++GuiHelper.closeWebBrowser%28%29%3B%0A++++%7D%0A%0A++++%40Test%0A++++public+void+TC0004_FormAuthenticationBadInfo%28%29+%7B%0A%0A++++++++final+String+userId+%3D+%22sdetAutomatiom%22%3B%0A++++++++final+String+password+%3D+%22pass%40word%22%3B%0A++++++++final+String+expectedMsg+%3D+%22Your+username+is+invalid%21%22%3B%0A%0A++++++++GuiHelper.openWebBrowser%28%29%3B%0A++++++++Navigation.navToWebPageUnderTest%28%29%3B%0A++++++++HomePage.clickFormAuthentication%28%29%3B%0A++++++++LoginPage.enterCredentials%28userId%2C+password%29%3B%0A++++++++LoginPage.verifyMessage%28testAssert%2C+expectedMsg%29%3B%0A++++++++GuiHelper.closeWebBrowser%28%29%3B%0A++++%7D%0A%0A++++%40Test%0A++++public+void+TC0005_A11y_Accessibility%28%29+%7B%0A%0A++++++++GuiHelper.openWebBrowser%28%29%3B%0A++++++++Navigation.navToWebPageUnderTest%28%29%3B%0A%0A++++++++AccessibilityHelper.basicAccessibilityCheck%28testAssert%29%3B%0A%0A++++++++GuiHelper.closeWebBrowser%28%29%3B%0A++++%7D%0A%7D%0A (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f59cc5511b0>: Failed to establish a new connection: [Errno 113] No route to host'))