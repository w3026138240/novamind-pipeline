# NovaMind AI Marketing Content Pipeline

An automated marketing pipeline that generates, distributes, and analyzes blog and newsletter content for NovaMind — a fictional AI startup helping creative agencies automate their workflows.

---

## What This Project Does

1. **Generates Content** — Creates a blog post and 3 personalized newsletter versions targeting different audience personas
2. **Distributes via CRM** — Adds contacts to Mailchimp and creates campaigns for each persona segment
3. **Analyzes Performance** — Simulates engagement data and generates an AI-powered performance summary with recommendations

---

## Architecture Overview
Topic Input
↓
generate_content.py
→ Generates blog post + 3 newsletters
→ Saves to content_output.json
↓
crm_distribution.py
→ Adds 3 contacts to Mailchimp (one per persona)
→ Creates a campaign for each persona
→ Saves campaign log to campaign_log.json
↓
performance_analysis.py
→ Simulates open rate, click rate, unsubscribe rate
→ Saves metrics to performance_log.json
→ Generates recommendations to performance_summary.txt

---

## Target Personas

| Persona | Description |
|---|---|
| Creative Agency Owner | Busy, ROI-focused, wants big-picture business benefits |
| Freelance Designer or Marketer | Hands-on, wants practical how-to tips |
| Tech-Savvy Operations Manager | Detail-oriented, wants integrations and efficiency gains |

---

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python 3.13 | Core programming language |
| Google Gemini API | AI content generation (gemini-2.0-flash) |
| Mailchimp API | CRM contact management and campaign distribution |
| mailchimp-marketing | Python SDK for Mailchimp |
| google-genai | Python SDK for Gemini API |

---

## Project Structure
novamind-pipeline/
├── generate_content.py      # Step 1: AI content generation
├── crm_distribution.py      # Step 2: Mailchimp CRM integration
├── performance_analysis.py  # Step 3: Performance logging & analysis
├── content_output.json      # Generated blog post + newsletters
├── campaign_log.json        # Record of created campaigns
├── performance_log.json     # Simulated performance metrics
└── performance_summary.txt  # AI-generated recommendations report

---

## How to Run Locally

### Prerequisites
- Python 3.10+
- A Mailchimp account (free tier works)
- A Google AI Studio account (for Gemini API)

### Installation

1. Clone or download this repository
2. Open a terminal in the project folder
3. Install dependencies:

```bash
pip install google-genai mailchimp-marketing
```

4. Add your API keys to each script:
   - In `generate_content.py`: replace `API_KEY` with your Gemini API key
   - In `crm_distribution.py`: replace `API_KEY` and `AUDIENCE_ID` with your Mailchimp credentials

### Running the Pipeline

Run each script in order:

```bash
python generate_content.py
python crm_distribution.py
python performance_analysis.py
```

---

## Assumptions & Notes

- **Mocked AI responses**: Due to Gemini API free tier rate limits during development, the content in `generate_content.py` uses pre-written realistic mock data. The script is structured to swap in live API calls once quota is restored.
- **Simulated performance data**: Email engagement metrics (open rate, click rate, unsubscribe rate) are randomly simulated in `performance_analysis.py` to represent realistic campaign results.
- **Mock contacts**: The 3 contacts added to Mailchimp use fictional email addresses for testing purposes.
- **Mailchimp free tier**: Campaigns are created but not actually sent, as the free tier requires a verified domain to send emails.

---

## Sample Output

### Performance Summary (sample)
=== NOVAMIND CAMPAIGN PERFORMANCE SUMMARY ===
Persona: Creative Agency Owner
Open Rate: 48%
Click Rate: 9%
Unsubscribe Rate: 4%
=== AI RECOMMENDATIONS ===
🏆 Best performing: Creative Agency Owner with 9% click rate.
→ Recommend more content like this for this audience next week.
⚠️ Lowest performing: Tech-Savvy Operations Manager with 6% click rate.
→ Recommend testing a new subject line and adding visual case studies.
📌 Next blog topic: 'How Creative Agencies Cut Costs by 30% Using AI Automation'