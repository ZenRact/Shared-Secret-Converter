import json
import uuid
import biplist


def _exit(data):
    input(data + '\n\nPress ENTER to exit...')
    exit(0)


print('Shared Secret Converter [v1.0] [Coded by @ZenRact]')
filename = input('[?] Enter a filename: ')
try:
    pl_file = biplist.readPlist(filename)
except biplist.InvalidPlistException:
    _exit('[!] Can\'t open Steamguard file')
data_array = {}
for i in range(2, 14):
    data_array[pl_file.get('$objects')[i]] = pl_file.get('$objects')[12+i]
data_array['device_id'] = 'android:' + str(uuid.uuid4())
data_array['fully_enrolled'] = True
data_array['Session'] = {}
data_array['Session']['SessionID'] = ''
data_array['Session']['SteamLogin'] = ''
data_array['Session']['SteamLoginSecure'] = ''
data_array['Session']['WebCookie'] = None
data_array['Session']['OAuthToken'] = ''
data_array['Session']['SteamID'] = data_array['steamid']
del data_array['steamguard_scheme'], data_array['steamid']
result = open(data_array['account_name'] + '.maFile', 'w')
result.write(json.dumps(data_array))
result.close()
_exit('[+] Success: ' + filename + ' => ' + data_array['account_name'] + '.maFile')
