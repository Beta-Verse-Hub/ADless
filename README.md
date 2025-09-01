# ADless
ADless is a simple browser extension that removes those ads from web pages which are from googleadservices.com, adservice.google.com, doubleclick.net, adsterra.com, adzerk.net, openx.com, inmobi.com, tyroo.com, collectcent.com, affle.com, pubmatic.com, adpushup.com, adnimation.com, adsterra.com and cloudfront.net.

# Installation

1. Download the extension from [here](https://github.com/Beta-Verse-Hub/ADless/releases/latest).
2. Install the zip file.
3. Extract the zip file.
4. Open the browser and click on the extension icon.
5. Go to Manage extensions.
6. Add unpacked extension.
7. Select the manifest.json file.
8. Enable the extension.

# How to Use: Rule Generator Script
## Overview

This script generates a set of rules in JSON format for blocking specific URLs. It prompts the user to input the latest rule ID and a list of URLs to block.

## Usage

Run the script and enter the latest rule ID when prompted.
Enter the link you want to block. The script will format the link and add it to the rule set.
Continue entering links until you want to stop. Type "end" to finish.
The script will output the generated rule set in JSON format.
#### Example Input/Output

Enter the latest rule ID: 10
Enter the link: ||example.com^
Enter the link: ||sub.example.com^
Enter the link: end
#### Output:

```json
,
{
    "id": 11,
    "priority": 1,
    "action": { "type": "block" },
    "condition": {
        "urlFilter": "*example.com*",
        "resourceTypes": ["main_frame", "sub_frame", "script", "xmlhttprequest", "image", "media", "stylesheet", "font"]
    }
},
{
    "id": 12,
    "priority": 1,
    "action": { "type": "block" },
    "condition": {
        "urlFilter": "*sub.example.com*",
        "resourceTypes": ["main_frame", "sub_frame", "script", "xmlhttprequest", "image", "media", "stylesheet", "font"]
    }
}
```

## Notes

1. **The links should be this format :- `||example.com^`.**
2. The script will automatically increment the rule ID for each new link.
3. The output rule set is in JSON format, with each rule separated by a comma.
4. Add this to the rules.json file in the extension folder (do this only if you know what a json is and how it works).
