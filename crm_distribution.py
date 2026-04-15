import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import json
from datetime import datetime

API_KEY = "your-mailchimp-api-key-here"
AUDIENCE_ID = "your-audience-id-here"

# Load the content we generated in Step 1
with open("content_output.json", "r") as f:
    content = json.load(f)

# Set up Mailchimp client
client = MailchimpMarketing.Client()
client.set_config({
    "api_key": API_KEY,
    "server": "us7"
})

# 3 fake contacts, one per persona
contacts = [
    {
        "email": "sarah.jones@creativeagency.com",
        "first_name": "Sarah",
        "last_name": "Jones",
        "persona": "Creative Agency Owner"
    },
    {
        "email": "mike.chen@freelance.com",
        "first_name": "Mike",
        "last_name": "Chen",
        "persona": "Freelance Designer or Marketer"
    },
    {
        "email": "lisa.patel@opsmanager.com",
        "first_name": "Lisa",
        "last_name": "Patel",
        "persona": "Tech-Savvy Operations Manager"
    }
]

# ---- STEP A: Add contacts to Mailchimp ----
print("Adding contacts to Mailchimp...")

for contact in contacts:
    try:
        client.lists.add_list_member(AUDIENCE_ID, {
            "email_address": contact["email"],
            "status": "subscribed",
            "merge_fields": {
                "FNAME": contact["first_name"],
                "LNAME": contact["last_name"]
            },
            "tags": [contact["persona"]]
        })
        print(f"✅ Added contact: {contact['email']}")
    except ApiClientError as error:
        print(f"Note: {contact['email']} may already exist — skipping.")

# ---- STEP B: Create and send a campaign for each persona ----
print("\nCreating campaigns...")

campaign_log = []

for newsletter in content["newsletters"]:
    persona = newsletter["persona"]
    subject = newsletter["subject_line"]
    body = newsletter["body"]

    # Find matching contact
    matching_contact = next(
        (c for c in contacts if c["persona"] == persona), None
    )

    try:
        # Create campaign
        campaign = client.campaigns.create({
            "type": "regular",
            "recipients": {
                "list_id": AUDIENCE_ID,
                "segment_opts": {
                    "match": "all",
                    "conditions": [{
                        "condition_type": "StaticSegment",
                        "field": "static_segment",
                        "op": "static_is",
                        "value": []
                    }]
                }
            },
            "settings": {
                "subject_line": subject,
                "from_name": "NovaMind",
                "reply_to": "hello@novamind.ai"
            }
        })

        campaign_id = campaign["id"]

        # Set email content
        client.campaigns.set_content(campaign_id, {
            "plain_text": body
        })

        print(f"✅ Campaign created for: {persona}")

        # Log the campaign
        campaign_log.append({
            "persona": persona,
            "campaign_id": campaign_id,
            "subject_line": subject,
            "send_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "created"
        })

    except ApiClientError as error:
        print(f"Error creating campaign for {persona}: {error.text}")

# ---- STEP C: Save campaign log ----
with open("campaign_log.json", "w") as f:
    json.dump(campaign_log, f, indent=2)

print("\n✅ Done! Campaigns created and logged in campaign_log.json")