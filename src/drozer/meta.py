from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
import json

class Version:

    def __init__(self, version, date):
        major, minor, patch = version.split(".")

        self.date = date
        self.major = int(major)
        self.minor = int(minor)
        self.patch = int(patch)

    def __eq__(self, other):
        return self.major == other.major and self.minor == other.minor and self.patch == other.patch

    def __gt__(self, other):
        return self.major > other.major or \
            self.major == other.major and self.minor > other.minor or \
            self.major == other.major and self.minor == other.minor and self.patch > other.patch

    def __lt__(self, other):
        return self.major < other.major or \
            self.major == other.major and self.minor < other.minor or \
            self.major == other.major and self.minor == other.minor and self.patch < other.patch

    def __str__(self):
        return "%d.%d.%d" % (self.major, self.minor, self.patch)

# TODO License check this stuff
name = "drozer"
vendor = "WithSecure"
version = Version("3.0.2", "2024-04-23")

contact = "drozer@withsecure.com"
description = "The Leading Android Security Testing Framework"
license = "BSD (3 clause)"
keywords = "drozer android security framework"
url = "https://labs.withsecure.com/tools/drozer/"

long_description = '''
drozer (formerly Mercury) is the leading security testing framework for Android.

drozer allows you to search for security vulnerabilities in apps and devices by assuming the role of an app and interacting with the Dalvik VM, other apps' IPC endpoints and the underlying OS.

drozer provides tools to help you use, share and understand public Android exploits. It helps you to deploy a drozer Agent to a device through exploitation or social engineering. Using weasel (MWR's advanced exploitation payload) drozer is able to maximise the permissions available to it by installing a full agent, injecting a limited agent into a running process, or connecting a reverse shell to act as a Remote Access Tool (RAT).

drozer is open source software, maintained by MWR InfoSecurity, and can be downloaded from: https://labs.f-secure.com/tools/drozer/
'''

def latest_version():
    try:
        response = urlopen(Request("https://api.github.com/repos/WithSecureLabs/drozer/releases/latest", None, {"user-agent": "drozer: %s" % str(version)}), None, 1)
        latestTag = json.load(response)
        latestVersion = Version(latestTag["tag_name"], latestTag["created_at"][:10])
        return latestVersion
    except HTTPError:
        return None
    except URLError:
        return None

def print_version():
    print("%s %s\n" % (name, version))
