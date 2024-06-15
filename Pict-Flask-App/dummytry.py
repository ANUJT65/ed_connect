import google.generativeai as genai
import textwrap
import markdown2
from weasyprint import HTML

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

def gen_summary(article_text):
    GOOGLE_API_KEY = "AIzaSyBtsmDXZBwuEM7mKoycKhirwoxoAewKb_o"  # Replace with your actual API key

    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(["You are tasked with generates detailed notes in Markdown format based on transcription extracted from educational videos provided. The program should analyze the transcription and create comprehensive notes using multiple bullet points, tables, and other appropriate formatting elements. The generated notes should effectively summarize the content of the video, breaking down key concepts, examples, and explanations into digestible sections. Ensure that the notes maintain clarity, coherence, and accuracy in representing the video's educational content. Your goal is to create a tool that enhances learning by condensing video content into structured and accessible notes.\n Subtitle file content :   ", article_text])
    final_text = response.text
    final_text = to_markdown(final_text)
    print(final_text)
    with open("summary.md", "w") as f:
        f.write(final_text)

    # Convert Markdown to HTML
    html_content = markdown2.markdown(final_text)

    # Convert HTML to PDF
    HTML(string=html_content).write_pdf("summary.pdf")
    print("PDF generated successfully.")

article_texts = "India, a land of myriad cultures, colors, and contrasts, encapsulates a rich tapestry of history, spirituality, and diversity. With its ancient civilizations dating back thousands of years, India stands as a testament to resilience and continuity. From the snow-capped peaks of the Himalayas to the sun-kissed beaches of Goa, and from bustling metropolises like Mumbai and Delhi to tranquil villages dotting the countryside, India offers a sensory overload like no other. Its cultural kaleidoscope manifests in vibrant festivals, sumptuous cuisines, and intricate art forms. Beyond its physical beauty, India's spiritual legacy, epitomized by sites like Varanasi and the majestic temples of Khajuraho, continues to draw seekers from around the globe. Amidst its challenges and complexities, India's spirit of unity in diversity remains its most enduring hallmark, ensuring that it continues to captivate and inspire the world."

gen_summary(article_texts)