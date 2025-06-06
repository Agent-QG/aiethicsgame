import os

characters_path = 'characters'
output_file = 'index.html'

html_header = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Character Gallery</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        img { max-width: 300px; margin: 10px; border: 1px solid #ccc; }
        h2 { margin-top: 40px; }
    </style>
</head>
<body>
    <h1>Character Gallery</h1>
'''

html_footer = '''
</body>
</html>
'''

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_header)

    for role_folder in sorted(os.listdir(characters_path)):
        role_path = os.path.join(characters_path, role_folder)
        if os.path.isdir(role_path):
            f.write(f'<h2>{role_folder}</h2>\n')
            for filename in sorted(os.listdir(role_path)):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    img_path = f'characters/{role_folder}/{filename}'
                    f.write(f'<img src="{img_path}" alt="{filename}">\n')

    f.write(html_footer)

print("✅ index.html generated successfully.")
