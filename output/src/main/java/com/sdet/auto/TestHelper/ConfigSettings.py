```
import os

class ConfigSettings:
    web_url = None
    web_browser = None

    @staticmethod
    def get_web_url():
        return ConfigSettings.web_url

    @staticmethod
    def set_web_url(web_url):
        ConfigSettings.web_url = web_url

    @staticmethod
    def get_web_browser():
        return ConfigSettings.web_browser

    @staticmethod
    def set_web_browser(web_browser):
        ConfigSettings.web_browser = web_browser

    @staticmethod
    def get_config_settings():
        config_file_path = os.path.join(os.path.dirname(__file__), "config.properties")

        with open(config_file_path) as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith("webUrl"):
                ConfigSettings.set_web_url(line.split("=")[1].strip())
            elif line.startswith("webBrowser"):
                ConfigSettings.set_web_browser(line.split("=")[1].strip())

        print("Test Config Settings")
        print(f"WebUrl: {ConfigSettings.get_web_url()}")
        print(f"WebBrowser: {ConfigSettings.get_web_browser()}")
```