import json

def read_json_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data

data = read_json_file('slides.json')

presentation_title = data['presentationTitle']
slides = data['slide']
def generate_latex_code(template, title, slide):
    latex_code = template.replace("<<title>>",title)

    slides_code = ""
    for s in slide:
        slide_title = s['title']
        slide_points = '\n'.join([f'\\item {point}' for point in s['points']])

        slide_code = f"""
        \\begin{{frame}}
            \\frametitle{{{slide_title}}}
            \\begin{{itemize}}
                {slide_points}
            \\end{{itemize}}
        \\end{{frame}}
        """

        slides_code += slide_code

    latex_code = latex_code.replace("<<slides>>", slides_code)
    return latex_code

latex_template = r'''
\documentclass{beamer}

\title{<<title>>}
\author{Author}
\date{\today}

\begin{document}

\begin{frame}
    \titlepage
\end{frame}

<<slides>>

\end{document}
'''

latex_code = generate_latex_code(latex_template, presentation_title, slides)
def save_latex_code(latex_code, file_path):
    with open(file_path, 'w') as file:
        file.write(latex_code)

save_latex_code(latex_code, 'presentation.tex')