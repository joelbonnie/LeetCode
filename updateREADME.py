"""
Script to update README.md with a table of folder structure
Format: Data Structure | Problem Number | Problem Name
"""


import os
import re
from pathlib import Path

def extract_number_from_filename(filename):
    name_without_ext = filename.replace('.py', '')
    numbers = re.findall(r'\d+', name_without_ext)
    number = numbers[-1] if numbers else 'N/A'
    
    clean_name = re.sub(r'_\d+$', '', name_without_ext)
    
    return number, clean_name


def scan_folders():
    current_dir = Path('.')
    folder_data = []
    
    folders = [d for d in current_dir.iterdir() 
              if d.is_dir() and not d.name.startswith('.') 
              and d.name not in ['.git', '__pycache__', 'node_modules']]
    
    for folder in sorted(folders):
        py_files = list(folder.glob('*.py'))
        
        for py_file in sorted(py_files):
            number, clean_name = extract_number_from_filename(py_file.name)
            folder_data.append({
                'folder': folder.name,
                'number': number,
                'filename': clean_name
            })
    
    return folder_data


def generate_table(folder_data):
    if not folder_data:
        return "No Python files found in folders.\n"
    
    table = "|Data Structure | Problem Number | Problem Name |\n"
    table += "|-------------|--------|----------|\n"
    
    for item in folder_data:
        table += f"| {item['folder']} | {item['number']} | {item['filename']} |\n"
    
    return table


def update_readme(table_content):
    readme_path = Path('README.md')
    
    start_marker = "<!-- AUTO-GENERATED TABLE START -->"
    end_marker = "<!-- AUTO-GENERATED TABLE END -->"
    
    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = "# Questions Solved!\n\n"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    new_section = f"{start_marker}\n\n## Questions Solved! :D\n\nCurrent Question Count: {len(folder_data)}\n{table_content}\n{end_marker}"
    
    if start_idx != -1 and end_idx != -1:
        updated_content = (content[:start_idx] + 
                         new_section + 
                         content[end_idx + len(end_marker):])
    else:
        if not content.endswith('\n'):
            content += '\n'
        updated_content = content + '\n' + new_section + '\n'
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"README.md updated with {len(folder_data)} files")


def main():
    try:
        folder_data = scan_folders()
        table_content = generate_table(folder_data)
        update_readme(table_content)
        
        print("Table generation completed successfully!")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())

