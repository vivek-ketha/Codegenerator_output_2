  Here is the code for the `MavenWrapperDownloader` class:

```python
from playwright.sync_api import sync_playwright

class MavenWrapperDownloader:
    DEFAULT_DOWNLOAD_URL = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.4.2/maven-wrapper-0.4.2.jar"
    MAVEN_WRAPPER_PROPERTIES_PATH = ".mvn/wrapper/maven-wrapper.properties"
    MAVEN_WRAPPER_JAR_PATH = ".mvn/wrapper/maven-wrapper.jar"
    PROPERTY_NAME_WRAPPER_URL = "wrapperUrl"

    def __init__(self, base_directory):
        self.base_directory = base_directory

    def download(self):
        print("- Downloader started")
        print(f"- Using base directory: {self.base_directory}")

        maven_wrapper_property_file = os.path.join(self.base_directory, self.MAVEN_WRAPPER_PROPERTIES_PATH)
        url = self.DEFAULT_DOWNLOAD_URL
        if os.path.exists(maven_wrapper_property_file):
            with open(maven_wrapper_property_file, "r") as f:
                properties = dict(line.strip().split("=") for line in f)
                url = properties.get(self.PROPERTY_NAME_WRAPPER_URL, url)
        print(f"- Downloading from: {url}")

        output_file = os.path.join(self.base_directory, self.MAVEN_WRAPPER_JAR_PATH)
        if not os.path.exists(os.path.dirname(output_file)):
            os.makedirs(os.path.dirname(output_file))
        print(f"- Downloading to: {output_file}")

        with urllib.request.urlopen(url) as response, open(output_file, "wb") as out_file:
            data = response.read()
            out_file.write(data)

        print("Done")
```