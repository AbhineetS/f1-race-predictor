import os
import re

directory = '/Users/abhineetsingh/Downloads/f1-race-predictor/frontend/src/assets/teams'

for filename in os.listdir(directory):
    if filename.endswith('.svg'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            content = f.read()

        # Replace explicit black fills with white
        content = content.replace('fill="#000000"', 'fill="#FFFFFF"')
        content = content.replace('fill="black"', 'fill="#FFFFFF"')
        content = content.replace('fill="#000"', 'fill="#FFFFFF"')
        
        # For McLaren specifically, the first path has no fill
        if filename == 'mclaren.svg':
            content = content.replace('<path d="M157.91', '<path fill="#FFFFFF" d="M157.91')
            content = content.replace('<path d="M58.92', '<path fill="#FFFFFF" d="M58.92')
            content = content.replace('<path d="M73.43', '<path fill="#FFFFFF" d="M73.43')
            content = content.replace('<path d="M91.42', '<path fill="#FFFFFF" d="M91.42')
            content = content.replace('<path d="M107.67', '<path fill="#FFFFFF" d="M107.67')
            content = content.replace('<path d="M125.73', '<path fill="#FFFFFF" d="M125.73')
            content = content.replace('<path d="M142.6', '<path fill="#FFFFFF" d="M142.6')
            content = content.replace('<path d="M160.5', '<path fill="#FFFFFF" d="M160.5')
            content = content.replace('<path d="M186.41', '<path fill="#FFFFFF" d="M186.41')
            content = content.replace('<path d="M210.41', '<path fill="#FFFFFF" d="M210.41')
            content = content.replace('<path d="M223.44', '<path fill="#FFFFFF" d="M223.44')
            content = content.replace('<path d="M241.84', '<path fill="#FFFFFF" d="M241.84')
            content = content.replace('<path d="M255.81', '<path fill="#FFFFFF" d="M255.81')
            content = re.sub(r'<path d="([^"]+)"', r'<path fill="#FFFFFF" d="\1"', content)

        with open(filepath, 'w') as f:
            f.write(content)
