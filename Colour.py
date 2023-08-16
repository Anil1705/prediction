from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import colorsys
import os


app = Flask(__name__)

def extract_colors_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    all_colors = set()

    # Extract colors from inline styles and CSS
    inline_styles = soup.find_all(style=True)
    css_colors = set()

    style_elements = soup.find_all("style")
    for style_element in style_elements:
        css_colors.update(extract_color_from_css(str(style_element)))

    for elem in inline_styles:
        style = elem["style"]
        colors = extract_color_from_css(style)
        all_colors.update(colors)

    all_colors.update(css_colors)
    return all_colors


from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

def generate_random_color_suggestion():
    color_choices = ["green", "red"]
    return random.choice(color_choices)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch URL and perform analysis here if needed
        # For this example, I'm generating a random color suggestion
        suggested_color = generate_random_color_suggestion()

        return render_template('index.html', suggested_color=suggested_color)

    return render_template('index.html', suggested_color=None)

if __name__ == '__main__':
    app.run(debug=True)









def extract_color_from_css(css):
    # Extract color strings from CSS
    colors = set()
    lines = css.splitlines()
    for line in lines:
        line = line.strip()
        if line.startswith("background-color:") or line.startswith("color:"):
            color_str = line.split(":")[1].strip().rstrip(";")
            r, g, b = (int(color_str[i:i+2], 16) for i in (1, 3, 5))
            colors.add((r, g, b))
    return colors

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        # Fetch HTML content from the URL
        response = requests.get(url)
        html_content = response.content
        colors = extract_colors_from_html(html_content)
        suggested_color = analyze_colors(colors)

        return render_template('index.html', suggested_color=suggested_color)

    return render_template('index.html', suggested_color=None)

if __name__ == '__main__':
    app.run(debug=True)
