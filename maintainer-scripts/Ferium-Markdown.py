# Import all the nessecairy modules
import humanfriendly as hf
import subprocess
import sys
import os
import re


try:
    # Get the path you run the file in and remove the last folder where the python file is located
    output_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    path_components = output_path.split(os.path.sep)
    path_components.pop()
    output_path = os.path.sep.join(path_components)
    # Check if the output path exists
    if not os.path.exists(output_path):
        raise Exception(f'Output path:{output_path} does not exist')
    
    # Ask if it are client or server mods (used for the markdown header and the name of the file)
    mod_type = input('Are these server mods or client mods? (Enter "server" or "client"): ')
    # Check if the input is valid
    if mod_type.lower() == 'server':
        mod_type = mod_type.upper()
        md_hd = '# Server Mods'
    elif mod_type.lower() == 'client':
        mod_type = mod_type.upper()
        md_hd = '# Client Mods'
    else:
        raise Exception('Unknown type', mod_type)

    # Get verbose mod list from ferium with the command 'ferium list -v'
    print('Getting verbose mod list from ferium ...')
    output = subprocess.check_output(['ferium', 'list', '-v']).decode('utf-8')
    text_block = output.strip().split('\n\n')
    # Create the markdown header
    header = ['Mod Name + link', 'Mod Authors', 'Desciption', 'Downloads', 'Project ID', 'License']
    mods = []

    print('Converting verbose mod list into seperate strings ...')
    # Search in each line  for the mod name, link, authors, downloads, project id and license
    for lines in text_block:
        name = re.search(r'^\s*(.+?)\s*$', lines.split('\n')[0]).group(1)
        
        if 'Link' in name:
            name = correct_name

            url = re.search(r'Link:\s+(.+)', lines).group(1)

            author = re.search(r'Authors:\s+(.+)', lines).group(1)

            downloads = re.search(r'Downloads:\s+(.+)', lines).group(1)
            formatted_downloads = hf.format_number(downloads)

            id_match = re.search(r'Project ID:\s+(.+)', lines)
            id = id_match.group(1) if id_match else 'Not a Modrinth/Curseforge project'

            license_match = re.search(r'License:\s+(.+)', lines)
            license = license_match.group(1) if license_match else 'Curseforge project, unable to read license'

            mods.append([name, url, author, formatted_downloads, id, license, desc])
        else:
            correct_name = name

            line = lines.split('\n')
            desc = line[1]

    # Sort the mods by name
    mods.sort(key=lambda mod: mod[0].lower())

    # Make the top of the markdown table
    markdown = md_hd + '\n'
    markdown += '| ' + ' | '.join(header) + ' |\n'
    markdown += '|---' * len(header) + '|\n'

    print('Making markdown table ...')
    # Unpack the name and link, author, formatted_downloads, id, license from the list mod in the list mods
    for mod in mods:
        name, url, author, formatted_downloads, id, license, desc = mod
        # Add the row of the specific mod
        markdown += f'| [{name}]({url}) | {author} | {desc} | {formatted_downloads} | {id} | {license} |\n'

    # Save the markdown table to a file in the variable output_path
    with open(f'{output_path}{os.path.sep}{mod_type}MODS.md', 'w', encoding='utf-8') as f:
        f.write(markdown)

    print(f'Done! The {mod_type.lower()} mods have been saved to {output_path}{os.path.sep}{mod_type}MODS.md file.')   
    input("Press enter to exit")

# Stop the program from running if there is an error and print the error out.
except Exception as e:
    print("An error occurred:", e)
    input("Press enter to exit")