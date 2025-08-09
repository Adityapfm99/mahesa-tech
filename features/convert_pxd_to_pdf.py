import os
import re
import io
import base64
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfMerger

def extract_svg_by_regex(pxd_content):
    svg_pattern = re.compile(r'(<svg.*?>.*?</svg>)', re.DOTALL)
    return svg_pattern.findall(pxd_content)

def fix_svg_namespaces(svg_content):
    return re.sub(r'xmlns="[^"]+"', 'xmlns="http://www.w3.org/2000/svg"', svg_content)

def process_embedded_images(svg_content):
    def replace_image_with_placeholder(match):
        image_data = match.group(1)
        image_format = match.group(2)
        image_b64 = base64.b64encode(image_data).decode('utf-8')
        return f'<image xlink:href="data:image/{image_format};base64,{image_b64}" />'

    image_pattern = re.compile(r'<image.*?xlink:href="data:image/(.*?);base64,(.*?)".*?/>', re.DOTALL)
    return image_pattern.sub(replace_image_with_placeholder, svg_content)

def fix_svg_fonts(svg_content):
    return re.sub(r'font-family:"?([^";]+)"?', r'font-family="\1"', svg_content)

def svg_to_pdf(svg_content, output_path):
    drawing = svg2rlg(io.BytesIO(svg_content.encode('utf-8')))
    renderPDF.drawToFile(drawing, output_path)

def merge_backgrounds(svg_content, background_svg):
    svg_content = fix_svg_namespaces(svg_content)
    background_svg = fix_svg_namespaces(background_svg)

    svg_content = process_embedded_images(svg_content)
    background_svg = process_embedded_images(background_svg)

    svg_content = fix_svg_fonts(svg_content)
    background_svg = fix_svg_fonts(background_svg)

    content_pdf = io.BytesIO()
    svg_to_pdf(svg_content, content_pdf)
    content_pdf.seek(0)

    background_pdf = io.BytesIO()
    svg_to_pdf(background_svg, background_pdf)
    background_pdf.seek(0)

    merger = PdfMerger()
    merger.append(background_pdf)
    merger.append(content_pdf)
    merged_pdf_path = 'merged_temp.pdf'
    merger.write(merged_pdf_path)
    merger.close()

    return merged_pdf_path

def convert_pxd_to_pdf(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        pxd_content = file.read()

    svg_contents = extract_svg_by_regex(pxd_content)

    if not svg_contents:
        print("No SVG content found in the PXD file.")
        return

    merged_pdf_path = None

    for i, svg_content in enumerate(svg_contents):
        svg_content = fix_svg_namespaces(svg_content)
        svg_content = process_embedded_images(svg_content)
        svg_content = fix_svg_fonts(svg_content)

        pdf_path = f'output_{i}.pdf'
        svg_to_pdf(svg_content, pdf_path)

        if merged_pdf_path is None:
            merged_pdf_path = pdf_path
        else:
            merged_pdf_path = merge_backgrounds(svg_content, merged_pdf_path)

    os.rename(merged_pdf_path, output_file)
    print(f"Converted {input_file} to {output_file}.")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Convert PXD file to PDF.")
    parser.add_argument("input", help="Input PXD file.")
    parser.add_argument("output", help="Output PDF file.")

    args = parser.parse_args()

    convert_pxd_to_pdf(args.input, args.output)

if __name__ == "__main__":
    main()