from pydoc import describe
import gradio as gr
from main import Main


main = Main()

def parse_cv(cv):
    return main.parse_cv(cv.name)
    

description = """A demo for a CV parser."""
article = "Resume Parser by Sybghat (sybghatallah@gmail.com)"
file_input = gr.inputs.File(file_count="single", type="file", label="Upload a CV: .PDF Or .TXT", optional=False)
iface = gr.Interface(fn=parse_cv, inputs=file_input, outputs="json", allow_flagging="never",
                    allow_screenshot=False, title="CV Parser", theme="seafoam", description=description, article=article)

iface.launch()