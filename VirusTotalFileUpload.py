import hashlib
import webbrowser
import argparse
import vt

# Parser
parser = argparse.ArgumentParser()
parser.add_argument('input_file',nargs='?', help='Indicate the file to read in order to generate its SHA-256 hash.')
parser.add_argument('--apikey', help='Your account API key to connect to VirusTotal.', required=True)
parser.add_argument('key',nargs='?',help='Your account API key to connect to VirusTotal.')
args = parser.parse_args()
# Parser End
if not args.apikey:
    args.apikey = args.key
elif not args.key:
    print('API Key not specified.')
    quit(0)
client = vt.Client(args.apikey)

# File Hashing
file = args.input_file
with open(file, 'rb') as f:
       content = f.read()
       enc = hashlib.sha256()
       enc.update(content)
       print('\n{} HASH OF FILE "{}" : {}\n'.format(enc.name, args.input_file, enc.hexdigest()))
# File Hashing End

# VirusTotal File Upload
print('Uploading to VirusTotal... Please wait')
with open(args.input_file, 'rb') as f2:
    upload = client.scan_file(f2,wait_for_completion=True)
    print(upload)
    vt.Client.close(client)
    hash = enc.hexdigest()
    url = (f'https://virustotal.com/gui/file/{hash}'.format(hash))
    webbrowser.open_new_tab(url)
    print('\nA new browser window containing the analysis has been open.')
# VirusTotal File Upload End