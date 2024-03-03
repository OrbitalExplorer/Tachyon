import json
import humanfriendly as hf
import os
import sys
import platform

def modlistCreation():
    try:
        header = ['', 'Project Name', 'Authors', 'Desciption', 'Downloads']

        class Content:
                def __init__(self, name, description, authorsList, downloads, slug, pr_type):
                    self.name = name
                    self.desc = description
                    self.authorsList = authorsList
                    self.downloadCount = downloads
                    self.link = 'https://modrinth.com/' + pr_type + '/' + slug
                    self.project_type = pr_type
                    self.markdownRow = f'| [{self.name}]({self.link}) '+ f'| {self.authorsList} | {self.desc} | {self.downloadCount} |\n' if slug != '/' else f'| {self.name}' + f'| {self.authorsList} | {self.desc} | {self.downloadCount} | {self.project_type} |\n'

        def getModrinthConfigPath():
            osName = platform.system()
            try:
                if osName == 'Windows':
                    appdata_path = os.getenv('APPDATA')
                    modrinthPath = os.path.join(appdata_path, 'com.modrinth.theseus', 'profiles')
                elif osName == 'Darwin':
                    modrinthPath = os.path.expanduser('~/Library/Application Support/com.modrinth.theseus/profiles')
                elif osName == 'Linux':
                    modrinthPath = os.path.expanduser('~/.config/com.modrinth.theseus/profiles')
                    
                profileName = input('Please right click your profile and paste "Path" here: ')
                modrinthConfigPath = modrinthPath + os.path.sep + profileName + os.path.sep + 'profile.json'
            except:
                modrinthPath = input('Unknown os, please manually paste your path to your modrinth profile here: ')
                
            return modrinthConfigPath
            
        def readJson(modrinthConfig_path):
            try:
                with open(modrinthConfig_path, encoding='utf-8') as config:
                        data = json.load(config)
                        
                return data
            except:
                print(f"{modrinthConfig_path} doesn't exist, please try again.")
                getModrinthConfigPath()     
        
        def mdHeader(header, prtype):
            md_hd = ''
            mod_type = None
            if prtype == 'mods':
                mod_type = input('Are these server mods or client mods? (Enter "server" or "client"): ')
                md_hd = f'# {mod_type.capitalize()} Pack\n' if mod_type.lower() == 'server' or mod_type.lower() == 'client' else None
                
                if md_hd == None:
                    raise Exception('Unknown type', mod_type)
                
            md_hd += f'\n## {prtype.capitalize()}\n'
                
            markdownHeader = md_hd
            markdownHeader += '| ' + ' | '.join(header) + ' |\n'
            markdownHeader += '|---' * len(header) + '|\n'
            markdown = markdownHeader
                
            return markdown, mod_type

        def getInfo(project_value, wantedInfo):
                try:
                    return project_value["metadata"]["project"][wantedInfo]
                except:
                    try:
                        return project_value["metadata"][wantedInfo]
                    except:
                        return '/'

        def extractInfo(data):
                contents = []
                
                print('Extracting data from profile.json.')
                for project_key, project_value in data["projects"].items():
                    authorsList = []
                    try:
                        for member in project_value['metadata']['members']:
                            authorsList.append(member['user']['username'])
                    except:
                        authorsList = getInfo(project_value, 'authors')
                        
                    authors = ', '.join(authorsList)
                        
                    name = getInfo(project_value, 'title')
                    desc = getInfo(project_value, 'description').replace("\n", "")
                    downs = getInfo(project_value, 'downloads')
                    try:
                        downs = hf.format_number(downs)
                    except:
                        downs = downs
                        
                    slug = getInfo(project_value, 'slug')
                    prType = getInfo(project_value, 'project_type')
                    
                    content = Content(name, desc, authors, downs, slug, prType)
                    contents.append(content)
                    
                return sort_contents_by_name(contents)
            
        def sort_contents_by_name(contents):
                return sorted(contents, key=lambda x: x.name)

        def mdConversion(markdown, header, contents, prType):     
            if prType != 'mods' and len(contents) > 0:
                prHeader, usseles = mdHeader(header, prType)
                markdown += prHeader
            
            for index, content in enumerate(contents):
                markdown += f'| {index + 1} ' + content.markdownRow
                    
            return markdown

        def outputPath():
                output_path = os.path.dirname(os.path.realpath(sys.argv[0]))
                path_components = output_path.split(os.path.sep)
                path_components.pop()
                output_path = os.path.sep.join(path_components)
                # Check if the output path exists
                if not os.path.exists(output_path):
                    raise Exception(f'Output path:{output_path} does not exist')
                
                return output_path
                    
        def saveMd(outputPath, contentType, markdown):
            print('Saving file ...')
            with open(f'{outputPath}{os.path.sep}{contentType.upper()}MODS.md', 'w', encoding='utf-8') as f:
                f.write(markdown)
                
        def splitTypes(contents):
            mods = []
            shaders = []
            resourcePacks = []
            unknown = []
            for content in contents:
                if content.project_type == 'mod':
                    mods.append(content)
                elif content.project_type == 'shader':
                    shaders.append(content)
                elif content.project_type == 'resourcepack':
                    resourcePacks.append(content)
                else:
                    unknown.append(content)
                    
            return mods, shaders, resourcePacks, unknown
                
        modrinthCofigPath = getModrinthConfigPath()

        markdownHeader, contentType = mdHeader(header, 'mods')
        data = readJson(modrinthCofigPath)
        contents = extractInfo(data)
        
        mods, shaders, resourcePacs, unknown = splitTypes(contents)
        
        markdown = mdConversion(markdownHeader, header, mods, 'mods')
        markdown = mdConversion(markdown, header, shaders, 'shaders')
        markdown = mdConversion(markdown, header, resourcePacs, 'resource packs')
        markdown = mdConversion(markdown, header, unknown, 'unknown')
        
        outputPath = outputPath()
        saveMd(outputPath, contentType, markdown)

        return modrinthCofigPath        
    except Exception as e:
        print("An error occurred:", e)
        input("Press enter to quit")
        
if __name__ == '__main__':
    modlistCreation()