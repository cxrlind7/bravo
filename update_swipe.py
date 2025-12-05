import os

file_path = r'c:\Users\CarlosOmarAldabaEstr\Documents\proy\Bravo\bravo\src\views\HomeView.vue'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Insert Template HTML
# Find the closing div of services-snap-container
# It should be around line 71.
# We look for the line that closes the container.
insertion_index = -1
for i, line in enumerate(lines):
    if 'class="services-snap-container"' in line:
        # Found the start. Now find the matching closing div.
        # Since it's a simple structure, we can look for the next closing div that has the same indentation as the start?
        # Or just look for the specific context we know:
        #             </div>
        #         </div>
        pass

# Let's use the context we know from view_file
# Line 71:             </div>
# Line 72:         </div>
# We want to insert between them.

found_template = False
for i in range(len(lines) - 1):
    if lines[i].strip() == '</div>' and lines[i+1].strip() == '</div>':
        # Check indentation
        if lines[i].startswith('            </div>') and lines[i+1].startswith('        </div>'):
            # Double check it's the right place (inside #services)
            # We can check if previous lines contain service-card
            if 'service-card' in lines[i-1] or '</div>' in lines[i-1]: # It's the closing of v-for or service-card
                 lines.insert(i+1, '            <p class="swipe-indicator">Desliza &rarr;</p>\n')
                 found_template = True
                 break

if not found_template:
    print("Error: Could not find template insertion point")

# 2. Insert Global CSS
# Insert before .services-subtitle
found_global_css = False
for i in range(len(lines)):
    if '.services-subtitle {' in lines[i]:
        lines.insert(i, '.swipe-indicator {\n    display: none;\n}\n\n')
        found_global_css = True
        break

if not found_global_css:
    print("Error: Could not find global CSS insertion point")

# 3. Insert Mobile CSS
# Insert inside @media (max-width: 768px)
# We can look for the end of that block, or just insert after .service-card p
found_mobile_css = False
for i in range(len(lines)):
    if '/* ===== SPECIALIZED AREAS - Apiladas full width ===== */' in lines[i]:
        # Insert before this comment, which is inside the media query
        css_block = """
    .swipe-indicator {
        display: block;
        text-align: center;
        color: #c9a961;
        font-size: 1rem;
        margin-top: 1rem;
        font-weight: 600;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 0.6; transform: translateX(0); }
        50% { opacity: 1; transform: translateX(5px); }
        100% { opacity: 0.6; transform: translateX(0); }
    }
"""
        lines.insert(i, css_block)
        found_mobile_css = True
        break

if not found_mobile_css:
    print("Error: Could not find mobile CSS insertion point")

if found_template and found_global_css and found_mobile_css:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Successfully updated HomeView.vue")
else:
    print("Failed to update all sections")
