import json

TOPIC = "AI in creative automation"

# ---- MOCK: Simulated Blog Post ----
blog_content = {
    "outline": [
        "Introduction: The Rise of AI in Creative Workflows",
        "What Creative Automation Actually Looks Like",
        "Top Tools Powering the Shift",
        "Real-World Results from Agencies Using AI",
        "How to Get Started with NovaMind"
    ],
    "draft": """Artificial intelligence is no longer a futuristic concept for creative agencies — it's a present-day competitive advantage. From automating repetitive design tasks to generating first drafts of marketing copy, AI is reshaping how creative teams operate at every level.

Creative automation refers to the use of AI-powered tools to handle tasks that once required significant human time and effort. This includes everything from resizing assets for multiple platforms to personalizing email campaigns at scale. For small agencies especially, this shift means being able to do more with less — without sacrificing quality.

Some of the most impactful tools in this space include workflow automation platforms, AI writing assistants, and smart project management systems. NovaMind combines the best of these into a single, unified platform designed specifically for creative teams.

Agencies that have adopted AI-assisted workflows report significant gains. Teams save an average of 10 hours per week on manual tasks, campaigns are launched faster, and client satisfaction scores improve because teams spend more time on strategy and creativity.

Getting started doesn't require a massive overhaul. NovaMind lets agencies plug in their existing tools and automate one workflow at a time. Whether it's auto-scheduling social posts, generating copy variations, or syncing client feedback — the platform grows with your team. The future of creative work is automated, personalized, and powered by AI."""
}

# ---- MOCK: Simulated Newsletters ----
newsletters = [
    {
        "persona": "Creative Agency Owner",
        "subject_line": "Save 10 Hours a Week — Without Hiring Anyone New",
        "body": """Hi [Name],

Running a creative agency means wearing a dozen hats at once. But what if AI could take a few of those hats off your hands?

NovaMind helps agency owners like you automate the time-consuming workflows that slow your team down — from client reporting to content scheduling. Our platform integrates with your existing tools, so there's no steep learning curve.

Agencies using NovaMind report saving 10+ hours per week and launching campaigns up to 40% faster. That's more time for strategy, more time for clients, and more time for growth.

Ready to see what automation can do for your bottom line?

👉 Start your free trial at novamind.ai

Best,
The NovaMind Team"""
    },
    {
        "persona": "Freelance Designer or Marketer",
        "subject_line": "Stop Doing the Boring Stuff. Let AI Handle It.",
        "body": """Hey [Name],

As a freelancer, your time is your most valuable asset. So why spend it on repetitive tasks?

NovaMind is built for creative independents who want to spend more time doing great work — and less time managing it. Auto-generate content variations, schedule posts, and keep clients updated without lifting a finger.

Our AI understands creative briefs, adapts to your brand voice, and helps you deliver faster without burning out. Whether you're managing 2 clients or 20, NovaMind scales with you.

Try it free for 14 days — no credit card required.

👉 novamind.ai/freelancers

Cheers,
The NovaMind Team"""
    },
    {
        "persona": "Tech-Savvy Operations Manager",
        "subject_line": "Integrate. Automate. Optimize. NovaMind for Ops Teams.",
        "body": """Hi [Name],

If you're managing creative operations, you know the bottlenecks: approval delays, tool switching, manual status updates. NovaMind eliminates them.

Our platform connects with your existing stack — Slack, Notion, HubSpot, and more — to automate content workflows end to end. Set triggers, define rules, and let the system handle the rest.

Track performance metrics in real time, identify inefficiencies, and continuously optimize your pipeline. NovaMind gives ops teams the visibility and control they need to run creative at scale.

Book a technical demo with our integrations team.

👉 novamind.ai/enterprise

Thanks,
The NovaMind Team"""
    }
]

# ---- Save to JSON ----
output = {
    "topic": TOPIC,
    "blog": blog_content,
    "newsletters": newsletters
}

with open("content_output.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ Done! Check content_output.json for your output.")