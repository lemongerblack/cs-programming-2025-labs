protocols = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
]

protocolstxt = list(map(lambda x: f"Protocol Lockdown - {x[0]} {str(x[1])}", protocols))
print(protocolstxt)