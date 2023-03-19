import humanfriendly as hf
import subprocess
import re

output_path = 'C:/Users/obewi/Documents/Tachyon/GitHub/Tachyon/'
mod_type = input('Are these server mods or client mods? (Enter "server" or "client"): ')

if mod_type.lower() == 'server':
    mod_type = 'SERVER'
    md_hd = '# Server Mods'
elif mod_type.lower() == 'client':
    mod_type = 'CLIENT'
    md_hd = '# Client Mods'
else:
    raise Exception('Unknown type')

print('Getting verbose mod list from ferium ...')
output = subprocess.check_output(['ferium', 'list', '-v']).decode('utf-8')
lines = output.strip().split('\n\n')
header = ['Mod Name + link', 'Mod Authors', 'Downloads', 'License']
mods = []

print('Converting verbose mod list into seperate strings ...')
for line in lines:
    name_match = re.search(r'^\s*(.+?)\s*$', line.split('\n')[0])
    name = name_match.group(1) if name_match else ''

    if 'Link' in name:
        name = correct_name
    else:
        correct_name = name

    url_match = re.search(r'Link:\s+(.+)', line)
    url = url_match.group(1) if url_match else ''

    author_match = re.search(r'Authors:\s+(.+)', line)
    author = author_match.group(1) if author_match else ''

    downloads_match = re.search(r'Downloads:\s+(.+)', line)
    downloads = int(downloads_match.group(1)) if downloads_match else 0
    formatted_downloads = hf.format_number(downloads)

    license_match = re.search(r'License:\s+(.+)', line)
    license = license_match.group(1) if license_match else ''

    mods.append([correct_name, url, author, formatted_downloads, license])

markdown = md_hd + '\n'
markdown += '| ' + ' | '.join(header) + ' |\n'
markdown += '|---' * len(header) + '|\n'

print('Making markdown table ...')
for mod in mods:
    correct_name, url, author, formatted_downloads, license = mod
    if url != '':
        markdown += f'| [{correct_name}]({url}) | {author} | {formatted_downloads} | {license} |\n'

with open(f'{output_path}{mod_type}MODS.md', 'w', encoding='utf-8') as f:
    f.write(markdown)