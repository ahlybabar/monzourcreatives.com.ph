import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ('vendor', '.git', 'skills-main')]
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Found {len(html_files)} HTML files:")
broken = []
for hf in sorted(html_files):
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check internal links (href)
    hrefs = re.findall(r'href=["\']([^"\'#]+)', content)
    base_dir = os.path.dirname(hf)
    for link in hrefs:
        if link.startswith(('http', 'mailto:', 'tel:')):
            continue
        # handle query params if any
        clean_link = link.split('?')[0]
        target = os.path.normpath(os.path.join(base_dir, clean_link))
        if not os.path.exists(target):
            broken.append((hf, 'href: ' + link, target))

    # Check images/scripts (src)
    srcs = re.findall(r'src=["\']([^"\'#]+)', content)
    for src in srcs:
        if src.startswith(('http', '//')):
            continue
        clean_src = src.split('?')[0]
        target = os.path.normpath(os.path.join(base_dir, clean_src))
        if not os.path.exists(target):
            broken.append((hf, 'src: ' + src, target))

if broken:
    print(f"FAILED: Found {len(broken)} missing targets:")
    for src_file, item, target in broken:
        print(f"  [{src_file}] {item} -> {target}")
else:
    print("SUCCESS: All internal links, scripts, stylesheets, and local image assets are 100% valid and verified across all pages!")
