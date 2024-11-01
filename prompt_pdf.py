import json
import textwrap
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Extracting Data from Config
job_post_url = config["ad_creative_details"]["link_data"]["link"]
campaign_details = config["campaign_details"]
ad_set_details = config["ad_set_details"]
ad_creative_details = config["ad_creative_details"]
audience_segment = ad_set_details["targeting"]
tracking_metrics = ["Impressions", "Reach", "Clicks", "CTR"]
insights_data = {
    "impressions": "1500",
    "reach": "1200",
    "clicks": "300",
    "ctr": "2.5%"
}

# Define margins
left_margin = 50
right_margin = 50
top_margin = 50
line_height = 14

# Function to wrap text within specified width
def draw_wrapped_text(c, text, x, y, max_width):
    wrapped_text = textwrap.wrap(text, width=max_width)
    for line in wrapped_text:
        c.drawString(x, y, line)
        y -= line_height
    return y

# Function to create the PDF report
def create_assessment_report(filename="AdCampaign_Assessment_Report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Cover Page
    c.setFont("Helvetica-Bold", 24)
    c.drawString(left_margin, height - top_margin, "Ads Automation Engineer Assessment Report")
    c.setFont("Helvetica", 12)
    c.drawString(left_margin, height - top_margin - 40, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(left_margin, height - top_margin - 60, "Candidate Name: Yuliana Alejandra Gonzalez Baena")
    c.drawString(left_margin, height - top_margin - 80, "Position: Torre Ads Automation Engineer")
    c.showPage()

    # Objective Section
    c.setFont("Helvetica-Bold", 16)
    c.drawString(left_margin, height - top_margin, "1. Campaign Objective")
    c.setFont("Helvetica", 12)
    y_position = height - top_margin - 30
    y_position = draw_wrapped_text(
        c,
        "The goal of this campaign is to attract candidates for the position of Product-Minded "
        "Tech Lead at Torre, leveraging audience segmentation and ad creatives to target suitable "
        "candidates effectively."
        "Additionally, leveraging the SDK calls for the Facebook Marketing API to automate the process through Python Scripts.",
        left_margin,
        y_position,
        max_width=85
    )
    c.showPage()

    # Setup Process Section
    c.setFont("Helvetica-Bold", 16)
    c.drawString(left_margin, height - top_margin, "2. Setup Process")
    c.setFont("Helvetica", 12)
    y_position = height - top_margin - 30
    setup_process_text = [
        "Step 1: Created a sandbox app on Facebook's Developer Platform.",
        "Step 2: Used Facebook Marketing API to set up campaign parameters, segmentation and ad creatives."
    ]
    for line in setup_process_text:
        y_position = draw_wrapped_text(c, line, left_margin, y_position, max_width=85)
    c.showPage()

    # Campaign Details Section
    c.setFont("Helvetica-Bold", 16)
    c.drawString(left_margin, height - top_margin, "3. Campaign Details")

    # Audience Segmentation
    c.setFont("Helvetica-Bold", 14)
    c.drawString(left_margin, height - top_margin - 30, "3.1 Audience Segmentation")
    c.setFont("Helvetica", 12)
    y_position = height - top_margin - 50
    y_position = draw_wrapped_text(
        c,
        f"Location: {', '.join(audience_segment['geo_locations']['countries'])}",
        left_margin,
        y_position,
        max_width=85
    )
    interests = [interest["name"] for interest in audience_segment["interests"]]
    y_position = draw_wrapped_text(
        c,
        f"Interests: {', '.join(interests)}",
        left_margin,
        y_position,
        max_width=85
    )
    y_position = draw_wrapped_text(
        c,
        f"Age Range: {audience_segment['age_min']} - {audience_segment['age_max']}",
        left_margin,
        y_position,
        max_width=85
    )
    genders = ['Male' if g == 1 else 'Female' for g in audience_segment["genders"]]
    y_position = draw_wrapped_text(
        c,
        f"Genders: {', '.join(genders)}",
        left_margin,
        y_position,
        max_width=85
    )

    # Ad Creative Details
    c.setFont("Helvetica-Bold", 14)
    y_position -= 30
    c.drawString(left_margin, y_position, "3.2 Ad Creative")
    y_position -= 20
    c.setFont("Helvetica", 12)
    y_position = draw_wrapped_text(
        c,
        f"Title: {ad_creative_details['name']}",
        left_margin,
        y_position,
        max_width=85
    )
    y_position = draw_wrapped_text(
        c,
        f"Headline: {ad_creative_details['link_data']['message'][:50]}...",  # Shortened for display
        left_margin,
        y_position,
        max_width=85
    )
    y_position = draw_wrapped_text(
        c,
        f"Description: {ad_creative_details['link_data']['message']}",
        left_margin,
        y_position,
        max_width=85
    )
    y_position = draw_wrapped_text(
        c,
        f"Image URL: {ad_creative_details['link_data']['picture']}",
        left_margin,
        y_position,
        max_width=85
    )
    c.showPage()

    # Tracking Effectiveness Section
    c.setFont("Helvetica-Bold", 16)
    c.drawString(left_margin, height - top_margin, "4. Tracking Effectiveness")
    c.setFont("Helvetica", 12)
    y_position = height - top_margin - 30
    y_position = draw_wrapped_text(
        c,
        "The following metrics were tracked to evaluate ad performance:",
        left_margin,
        y_position,
        max_width=85
    )
    for metric in tracking_metrics:
        y_position = draw_wrapped_text(c, f"- {metric}", left_margin + 20, y_position, max_width=85)
    c.showPage()

    # Insights Summary Section
    c.setFont("Helvetica-Bold", 16)
    c.drawString(left_margin, height - top_margin, "5. Insights Summary (Mock Data)")
    y_position = height - top_margin - 30
    c.setFont("Helvetica", 12)
    for key, value in insights_data.items():
        y_position = draw_wrapped_text(c, f"{key.capitalize()}: {value}", left_margin, y_position, max_width=85)
    c.showPage()

    # Conclusion Section
    c.setFont("Helvetica-Bold", 16)
    c.drawString(left_margin, height - top_margin, "6. Conclusion")
    c.setFont("Helvetica", 12)
    y_position = height - top_margin - 30
    y_position = draw_wrapped_text(
        c,
        "This document outlines the setup and execution of an ad campaign on Meta’s platform "
        "for the purpose of attracting candidates for a Tech Lead position at Torre. "
        "The campaign was structured using the Marketing API and sandbox environment. "
        "The provided audience segmentation and ad creatives demonstrate targeting capabilities."
        "I hope to hear back from you soon.",
        left_margin,
        y_position,
        max_width=85
    )
    
    # Save PDF
    c.save()
    print(f"PDF report created: {filename}")

# Generate the PDF report
create_assessment_report("AdCampaign_Assessment_Report.pdf")
