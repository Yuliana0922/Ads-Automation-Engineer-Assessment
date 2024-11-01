# Meta Ads Automation Assessment

This project was created as part of an assessment for the Ads Automation Engineer position. It demonstrates the use of Meta's Marketing API to set up and manage an ad campaign, including audience segmentation, ad creatives, and performance tracking, within a sandbox environment. The final result is a Python script that automates the ad setup and generates a PDF report detailing the campaign configuration.

## Project Structure

- `techjobad.py`: Python script to set up and manage the ad campaign.
- `generate_report.py`: Script to create a PDF report summarizing the campaign setup and parameters.
- `config.json`: Configuration file with all campaign settings and credentials (excluded from Git with `.gitignore`).
- `README.md`: This document, describing the setup and usage of the project.
- `.gitignore`: Specifies files to be excluded from version control, including `config.json`.

## Setup and Configuration

1. **Create and Configure `config.json`**:
   - Place your credentials, campaign details, and ad creative parameters in a `config.json` file.
   - **Sample Configuration**:
     ```json
     {
         "credentials": {
             "app_id": "<your_app_id>",
             "app_secret": "<your_app_secret>",
             "access_token": "<your_access_token>"
         },
         "ad_account_id": "act_<your_ad_account_id>",
         "campaign_details": {
             "name": "Job Posting Campaign",
             "objective": "OUTCOME_TRAFFIC",
             "status": "PAUSED",
             "special_ad_categories": ["EMPLOYMENT"]
         },
         "ad_set_details": {
             "name": "Targeted Audience for Tech Job Post",
             "daily_budget": 5000,
             "billing_event": "IMPRESSIONS",
             "optimization_goal": "LINK_CLICKS",
             "bid_strategy": "LOWEST_COST_WITH_BID_CAP",
             "bid_amount": 2,
             "bid_cap": 5000,
             "targeting": {
                 "geo_locations": {"countries": ["US", "GB"]},
                 "interests": [
                     {"id": "6003985771306", "name": "Technology"},
                     {"id": "6003164535634", "name": "Information technology"}
                 ],
                 "age_min": 20,
                 "age_max": 50,
                 "genders": [1, 2]
             }
         },
         "ad_creative_details": {
             "name": "Creative for Job Post",
             "page_id": "<your_page_id>",
             "link_data": {
                 "picture": "https://example.com/your-image.jpg",
                 "link": "https://torre.ai/post/awyJqjad-torre-product-minded-tech-lead",
                 "message": "Apply for the position of Tech Lead at Torre!"
             }
         }
     }
     ```

2. **Create a `.gitignore` File**:
   - To prevent sensitive data from being uploaded to GitHub, create a `.gitignore` file with the following entry:
     ```
     config.json
     ```

3. **Install Required Dependencies**:
   - Install the necessary packages listed in the `requirements.txt` file (e.g., `facebook_business`, `reportlab`):
     ```bash
     pip install -r requirements.txt
     ```

4. **Running the Ad Script**:
   - Run the `techjobad.py` script to set up the campaign, ad set, and ad creative using Meta’s API:
     ```bash
     python techjobad.py
     ```

5. **Generating the PDF Report**:
   - Run `generate_report.py` to create a PDF report that summarizes the campaign’s configuration, audience segmentation, and tracking metrics:
     ```bash
     python generate_report.py
     ```
   - The PDF report, `AdCampaign_Assessment_Report.pdf`, will be generated in the project root.

## Key Steps in Development Process

1. **Initial Setup**: We created and tested a Python script using Meta's Marketing API, setting up credentials and initializing API access.
2. **Dynamic Configuration**: All hardcoded parameters were moved to `config.json`, allowing flexibility and easier updates.
3. **Text Wrapping and PDF Formatting**: For the PDF report, we implemented margins and text wrapping to improve readability.
4. **Error Handling**: Addressed and handled API errors related to development mode and existing ad images.
5. **Final Testing**: Verified the script functionality in a sandbox environment to ensure it met the requirements of the Ads Automation Engineer position.

## Troubleshooting

- **Invalid Credentials Error**: Ensure that your app ID, secret, and access token are correctly set in `config.json`.
- **Development Mode Limitations**: Ensure your app is set to public if testing in a live environment.
- **API Errors**: Verify that API calls are using the correct parameters as specified in Meta's [API Documentation](https://developers.facebook.com/docs/marketing-apis).

## License

This project is intended for educational and assessment purposes only.

---

### Step 2: Setting Up `.gitignore`

To ensure that sensitive files like `config.json` aren’t uploaded to GitHub:

1. **Create a `.gitignore` File** in the root directory (if it doesn't exist).
2. Add the following lines to `.gitignore`:

   ```plaintext
   config.json
   *.pdf
