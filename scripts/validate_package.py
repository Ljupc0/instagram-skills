from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
folders = sorted((root / 'skills').iterdir())
manifest = json.loads((root / 'skill-manifest.json').read_text(encoding='utf-8'))
assert sorted(p.name for p in folders) == sorted(manifest['skills'])
assert len(manifest['skills']) == len(set(manifest['skills']))
contracts = []
templates = []
cycles = []
for folder in folders:
    text = (folder / 'SKILL.md').read_text(encoding='utf-8')
    assert text.startswith('---\n')
    front = text.split('---', 2)[1]
    assert f'name: {folder.name}\n' in front
    assert re.fullmatch(r'[a-z0-9-]{1,63}', folder.name)
    description = json.loads(re.search(r'^description: (.+)$', front, re.M).group(1))
    assert description and len(description) < 1024
    for link in re.findall(r'\]\(([^)]+)\)', text):
        assert (folder / link).is_file(), (folder, link)
    for relative in re.findall(r'references/[a-z-]+\.md', text):
        assert (folder / relative).is_file(), (folder, relative)
    ui = (folder / 'agents/openai.yaml').read_text(encoding='utf-8')
    assert '$' + folder.name in ui
    short = json.loads(re.search(r'short_description: (.+)', ui).group(1))
    assert 25 <= len(short) <= 64, (folder, len(short))
    contracts.append((folder / 'references/profile-contract.md').read_bytes())
    templates.append((folder / 'references/profile-template.md').read_bytes())
    contract = (folder / 'references/profile-contract.md').read_text(encoding='utf-8')
    for relative in re.findall(r'references/[a-z-]+\.md', contract):
        assert (folder / relative).is_file(), (folder, relative)
    cycles.append((folder / 'references/improvement-cycle.md').read_bytes())
assert len(set(contracts)) == 1
assert len(set(templates)) == 1
assert len(set(cycles)) == 1
assert not (root / 'profiles').exists(), 'Keep real profile data outside the package'
print(f'PASS: {len(folders)} skills; manifest, metadata, references, UI prompts and shared contracts valid.')
