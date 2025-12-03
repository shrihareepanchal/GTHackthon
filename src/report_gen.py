from pptx import Presentation
from pptx.util import Inches

def export_ppt(title, summary, metrics, images, outpath):
    prs = Presentation()

    s1 = prs.slides.add_slide(prs.slide_layouts[0])
    s1.shapes.title.text = title
    s1.placeholders[1].text = ""

    s2 = prs.slides.add_slide(prs.slide_layouts[1])
    s2.shapes.title.text = "AI Summary"
    tb = s2.placeholders[1].text_frame
    for line in summary.split("\n"):
        p = tb.add_paragraph(); p.text = line

    s3 = prs.slides.add_slide(prs.slide_layouts[1])
    s3.shapes.title.text = "Metrics"
    tb = s3.placeholders[1].text_frame
    for k,v in metrics.items():
        p = tb.add_paragraph(); p.text = f"{k}: {v}"

    for img in images:
        s = prs.slides.add_slide(prs.slide_layouts[5])
        s.shapes.title.text = "Visualization"
        s.shapes.add_picture(img, Inches(1), Inches(1), width=Inches(6))

    prs.save(outpath)
    return outpath
