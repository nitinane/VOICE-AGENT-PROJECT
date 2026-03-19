import re

file_path = r'c:\Users\Nitin\OneDrive\Desktop\idea2.0\src\app\page.tsx'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace "Ready" with {t('module_ready_status')} in the module card section
new_content = content.replace('>Ready</span>', ">{t('module_ready_status')}</span>")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Ready status localized successfully.")
