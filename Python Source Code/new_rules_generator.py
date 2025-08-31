latest_rule_id = int(input("Enter the latest rule id: "))
link = input("Enter the link: ")
rule = ""

while link != "end":

    if link[0:2] == "||" and link[-1:] == "^":
        link = "*"+link[2:-1]+"*"

    latest_rule_id += 1
    rule += '''
    {
        "id": '''+str(latest_rule_id)+''',
        "priority": 1,
        "action": { "type": "block" },
        "condition": {
            "urlFilter": "'''+link+'''",
            "resourceTypes": ["main_frame", "sub_frame", "script", "xmlhttprequest", "image", "media", "stylesheet", "font"]
        }
    },'''

    link = input("Enter the link: ")

rule = rule[:-1]

print(rule)