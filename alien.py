users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princetion',
    },
    'mucire':{
        'first':'marie',
        'last':'curie',
        'location':'princetion',
    },
}
for username,user_info in users.items():
    print("\nusername:"+username)
    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location']

    print("\tFull name:"+full_name.title())
    print("\tLocation:"+location.title())