
import os
from playwright.sync_api import Playwright, sync_playwright

def convert_to_playwright(code):
    code = code.replace("package pages;", "")
    code = code.replace("import org.openqa.selenium.WebDriver;", "")
    code = code.replace("import org.openqa.selenium.chrome.ChromeDriver;", "")
    code = code.replace("import org.openqa.selenium.chrome.ChromeDriverService;", "")
    code = code.replace("import org.testng.ITestContext;", "")
    code = code.replace("import org.testng.annotations.AfterClass;", "")
    code = code.replace("import org.testng.annotations.BeforeClass;", "")
    code = code.replace("import io.github.bonigarcia.wdm.WebDriverManager;", "")
    code = code.replace("import com.relevantcodes.extentreports.ExtentReports;", "")
    code = code.replace("import com.relevantcodes.extentreports.ExtentTest;", "")
    code = code.replace("public class BasePage {", "class BasePage:")
    code = code.replace("String url = \"https://www.oculus.com/\";", "url = \"https://www.oculus.com/\"")
    code = code.replace("public static ExtentTest logger;", "logger = None")
    code = code.replace("public static ExtentReports report;", "report = None")
    code = code.replace("@BeforeClass(alwaysRun=true)", "@playwright.fixture")
    code = code.replace("System.setProperty(ChromeDriverService.CHROME_DRIVER_SILENT_OUTPUT_PROPERTY, \"true\"); // This suppresses the Severe Timed out receiving messages", "")
    code = code.replace("WebDriverManager.chromedriver().setup();", "")
    code = code.replace("driver = new ChromeDriver();", "driver = playwright.chromium.launch()")
    code = code.replace("driver.manage().window().maximize();", "page = driver.new_page()")
    code = code.replace("driver.get(url);", "page.goto(url)")
    code = code.replace("context.setAttribute(\"WebDriver\", driver);", "")
    code = code.replace("@AfterClass(alwaysRun=true)", "")
    code = code.replace("driver.quit();", "driver.close()")
    return code

def check_and_update_function_names(code):
    code = code.replace("setup(ITestContext context)", "setup(context)")
    code = code.replace("tearDown()", "teardown()")
    return code

def ensure_print_statements_are_appropriate(code):
    code = code.replace("System.out.println(", "print(")
    return code

def add_required_import_statements(code):
    import_statements = """
from playwright.sync_api import Playwright, sync_playwright
"""
    code = import_statements + code
    return code

def call_function_at_end(code):
    code = code + "\nsetup(context)"
    return code
code = """package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeDriverService;
import org.testng.ITestContext;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import io.github.bonigarcia.wdm.WebDriverManager;

import com.relevantcodes.extentreports.ExtentReports;
import com.relevantcodes.extentreports.ExtentTest;

public class BasePage {

    public static WebDriver driver;
    String url = "https://www.oculus.com/";
    public static ExtentTest logger;
    public static ExtentReports report;

    @BeforeClass(alwaysRun=true)
    public void setup(ITestContext context) {
        System.setProperty(ChromeDriverService.CHROME_DRIVER_SILENT_OUTPUT_PROPERTY, "true"); // This suppresses the Severe Timed out receiving messages
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get(url);
        context.setAttribute("WebDriver", driver);
    }

    @AfterClass(alwaysRun=true)
    public void tearDown() {
        driver.quit();
    }
}
"""
code = convert_to_playwright(code)
code = check_and_update_function_names(code)
code = ensure_print_statements_are_appropriate(code)
code = add_required_import_statements(code)
code = call_function_at_end(code)

print(code)