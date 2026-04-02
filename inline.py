import os

def inline_css():
    html_path = r'c:\Users\satou\.gemini\antigravity\scratch\job_hunting_prep\index.html'
    css_path = r'c:\Users\satou\.gemini\antigravity\scratch\job_hunting_prep\styles.css'
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    with open(css_path, 'r', encoding='utf-8') as f:
        css_lines = f.readlines()
        
    # Fix the stray bracket in CSS (remove line 554 which is ")
    # The '}' on line 554 closes the 768px media query early.
    # We find the specific media query block closing and remove it.
    fixed_css = ""
    for i, line in enumerate(css_lines):
        if i == 553 and line.strip() == "}":  # line 554 is 0-indexed 553
            continue
        fixed_css += line

    # Create the <style> block
    style_block = "<style>\n" + fixed_css + "\n    </style>"
    
    # Replace the link tag
    new_html = html_content.replace('<link rel="stylesheet" href="styles.css">', style_block)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

if __name__ == '__main__':
    inline_css()
