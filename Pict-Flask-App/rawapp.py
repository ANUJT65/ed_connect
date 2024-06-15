import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import json
import requests
import schemdraw

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename, text):
    c = canvas.Canvas(filename, pagesize=letter)
    y_position = 750
    for line in text.split('\n'):
        c.drawString(100, y_position, line)
        y_position -= 20
    c.save()

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))



def gen_summary(article_text):
    GOOGLE_API_KEY="AIzaSyBtsmDXZBwuEM7mKoycKhirwoxoAewKb_o"

    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(["summarise text using bullets with multiple titles ",article_text])
    final_text=response.text
    to_markdown(final_text)
    filename = "hello_pdf.pdf"
    create_pdf(filename,final_text)
    print(f"PDF file '{filename}' created successfully.")





text="U in August 1947, India gained independence after 200 years of british rule. What followed was one of the largest and bloodiest forced migrations in history. An estimated 1 million people lost their lives before british colonization. The indian subcontinent was a patchwork of regional kingdoms known as princely states. Populated by Hindus, Muslims, Sikhs, Jains, Buddhists, Christians, Parsis and Jews, each princely state had its own traditions, caste backgrounds and leadership. Starting in the 15 hundreds, a series of european powers colonized India with coastal trading settlements. By the mid 18th century, the English East India Company emerged as the primary colonial power in India. The British ruled some provinces directly and ruled the princely states indirectly. Under indirect rule, the princely states remained sovereign but made political and financial concessions to the British. In the 19th century, the British began to categorize Indians by religious identity, a gross simplification of the communities in India. They counted Hindus as majorities and all other religious communities as distinct minorities, with Muslims being the largest minority. Sikhs were considered part of the hindu community by everyone but themselves. In elections, people could only vote for candidates of their own religious identification. These practice exaggerated differences, sowing distrust between communities that had previously coexisted. The 20th century began with decades of anticolonial movement where Indians fought for independence from Britain in the aftermath of World War II. Under enormous financial strain from the war, Britain finally. Indian political leaders had differing views on what an independent India should look like. Mohan Das Gandhi and Jawaharlal Nehru represented the hindu majority and wanted one united India. Muhammad Ali Jinnah, who led the muslim minority, thought the rifts created by colonization were too deep to repair. Jinnah argued for a two nation division where Muslims would have a homeland called Pakistan. You. Following riots in 1946 and 1947, the British expedited their retreat, planning indian independence behind closed doors. In June 1947, the british viceroy announced that India would gain independence by August and be partitioned into Hindu India and Muslim Pakistan, but gave little explanation of how exactly this would happen. Using outdated maps, inaccurate census numbers and minimal knowledge of the land, in a mere five weeks, the boundary committee drew a border dividing three provinces under direct british rule Bengal, Punjab and Assam. The border took into account where Hindus and Muslims were majority, but also factors like location and population percentages. So if a hindu majority area bordered another hindu majority area, it would be included in India. But if a hindu majority area bordered muslim majority areas, it might become part of Pakistan. Princely states on the border had to choose which of the new nations to join, losing their sovereignty in the process. While the boundary committee worked on the new map, Hindus and Muslims began moving to areas where they thought they'd be a part of the religious majority. But they couldn't be sure. Families divided themselves. Fearing sexual violence, parents sent young daughters and wives to regions they perceived to be safe. The new map wasn't revealed until August 17, 1947. Two days after independence, the provinces of Punjab and Bengal became the geographically."
gen_summary(text)





