users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princetion'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername:" + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print(full_name.title())
    print((location.title()))
