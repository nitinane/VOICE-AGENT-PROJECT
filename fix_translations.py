import re
from pathlib import Path

file_path = Path(r'c:\Users\Nitin\OneDrive\Desktop\idea2.0\src\i18n\translations.ts')

content = file_path.read_text(encoding='utf-8')

replacements = {
    r'(?<!module_)ready_status': 'module_ready_status',
    r'(?<!module_)change_language_action': 'module_change_language_action',
    r'(?<!module_)audio_synthetic_label': 'module_audio_synthetic_label'
}

for pattern, new_key in replacements.items():
    content = re.sub(
        rf'(["\']){pattern}(["\']\s*:)',
        rf'\g<1>{new_key}\g<2>',
        content
    )

file_path.write_text(content, encoding='utf-8')

print("Safe key normalization complete.")
