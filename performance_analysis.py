import json
import random
from datetime import datetime

# ---- STEP A: Simulate performance data directly ----
print("Generating performance data...")

personas = [
    {
        "persona": "Creative Agency Owner",
        "subject_line": "Save 10 Hours a Week — Without Hiring Anyone New"
    },
    {
        "persona": "Freelance Designer or Marketer",
        "subject_line": "Stop Doing the Boring Stuff. Let AI Handle It."
    },
    {
        "persona": "Tech-Savvy Operations Manager",
        "subject_line": "Integrate. Automate. Optimize. NovaMind for Ops Teams."
    }
]

performance_data = []

for p in personas:
    data = {
        "persona": p["persona"],
        "subject_line": p["subject_line"],
        "send_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "emails_sent": 100,
        "open_rate": round(random.uniform(0.20, 0.55), 2),
        "click_rate": round(random.uniform(0.05, 0.25), 2),
        "unsubscribe_rate": round(random.uniform(0.01, 0.05), 2)
    }
    performance_data.append(data)
    print(f"✅ Performance data generated for: {p['persona']}")

# ---- STEP B: Save performance data ----
with open("performance_log.json", "w") as f:
    json.dump(performance_data, f, indent=2)

print("\nPerformance log saved!")

# ---- STEP C: Generate summary ----
print("\nGenerating performance summary...")

best_persona = max(performance_data, key=lambda x: x["click_rate"])
worst_persona = min(performance_data, key=lambda x: x["click_rate"])

summary_lines = []
summary_lines.append("=== NOVAMIND CAMPAIGN PERFORMANCE SUMMARY ===")
summary_lines.append(f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

for d in performance_data:
    summary_lines.append(f"Persona: {d['persona']}")
    summary_lines.append(f"  Subject: {d['subject_line']}")
    summary_lines.append(f"  Open Rate: {int(d['open_rate']*100)}%")
    summary_lines.append(f"  Click Rate: {int(d['click_rate']*100)}%")
    summary_lines.append(f"  Unsubscribe Rate: {int(d['unsubscribe_rate']*100)}%")
    summary_lines.append("")

summary_lines.append("=== AI RECOMMENDATIONS ===")
summary_lines.append(f"🏆 Best performing: {best_persona['persona']} with {int(best_persona['click_rate']*100)}% click rate.")
summary_lines.append(f"   → Recommend more content like this for this audience next week.\n")
summary_lines.append(f"⚠️  Lowest performing: {worst_persona['persona']} with {int(worst_persona['click_rate']*100)}% click rate.")
summary_lines.append(f"   → Recommend testing a new subject line and adding visual case studies.\n")
summary_lines.append("📌 Next blog topic: 'How Creative Agencies Cut Costs by 30% Using AI Automation'")
summary_lines.append("📌 Alternative topic: '5 Zapier-Style Automations Every Freelancer Should Set Up Today'")

summary_text = "\n".join(summary_lines)

with open("performance_summary.txt", "w", encoding="utf-8") as f:
    f.write(summary_text)

print(summary_text)
print("\n✅ Done! Summary saved to performance_summary.txt")