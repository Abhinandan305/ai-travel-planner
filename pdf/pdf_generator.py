from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(text):

    doc = SimpleDocTemplate(
        "trip_itinerary.pdf"
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "AI Travel Itinerary",
        styles['Title']
    )

    body = Paragraph(
        text.replace("\n", "<br/>"),
        styles['BodyText']
    )

    elements.append(title)
    elements.append(Spacer(1, 20))
    elements.append(body)

    doc.build(elements)