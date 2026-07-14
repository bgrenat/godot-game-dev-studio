import sys
import os
import json

def generate_premium_certificate(project_name, scores):
    """
    Generates an EXTREME PREMIMUM glassmorphic HTML certificate for Godot Excellence.
    'scores' is a dictionary: {category: score}
    """
    total_score = sum(scores.values()) / len(scores)
    tier = "LEGACY ARCHITECTURE"
    if total_score >= 95: tier = "VISIONARY: ZENITH (S-TIER)"
    elif total_score >= 90: tier = "VISIONARY: ELITE (A-TIER)"
    elif total_score >= 80: tier = "VISIONARY: ADVANCED"
    elif total_score >= 60: tier = "VISIONARY: COMPETENT"
    elif total_score >= 40: tier = "TRANSITIONARY"

    score_color = "#ff4d4d"
    if total_score >= 80: score_color = "#00f2fe"
    elif total_score >= 60: score_color = "#f9d423"

    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GDSkills Visionary Certificate | {project_name}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@200;400;700&family=Inter:wght@300;600&display=swap');
        
        :root {{
            --primary: #4facfe;
            --secondary: #00f2fe;
            --accent: {score_color};
            --glass: rgba(255, 255, 255, 0.03);
            --glass-border: rgba(255, 255, 255, 0.1);
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            background: #0a0a0f;
            color: #ffffff;
            font-family: 'Outfit', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow: hidden;
            background: 
                radial-gradient(circle at 20% 30%, rgba(79, 172, 254, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 80% 70%, rgba(0, 242, 254, 0.1) 0%, transparent 40%),
                #050508;
        }}

        .container {{
            position: relative;
            z-index: 10;
        }}

        .certificate {{
            background: var(--glass);
            backdrop-filter: blur(40px);
            -webkit-backdrop-filter: blur(40px);
            border: 1px solid var(--glass-border);
            border-radius: 60px;
            padding: 80px;
            max-width: 1000px;
            width: 95vw;
            box-shadow: 0 40px 100px rgba(0,0,0,0.8);
            text-align: center;
            position: relative;
            animation: fadeIn 1.2s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(40px) scale(0.95); }}
            to {{ opacity: 1; transform: translateY(0) scale(1); }}
        }}

        .header {{ margin-bottom: 60px; }}

        h1 {{
            font-size: 4.5rem;
            font-weight: 700;
            margin-bottom: 15px;
            background: linear-gradient(135deg, #ffffff 30%, rgba(255,255,255,0.4) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-transform: uppercase;
            letter-spacing: 12px;
            animation: slideUp 1s ease-out;
        }}

        @keyframes slideUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .subtitle {{
            font-size: 1.1rem;
            color: rgba(255,255,255,0.4);
            letter-spacing: 4px;
            font-weight: 200;
            text-transform: uppercase;
        }}

        .tier-section {{
            margin-bottom: 60px;
            position: relative;
        }}

        .tier-badge {{
            display: inline-block;
            padding: 20px 45px;
            background: rgba(255,255,255,0.05);
            border-radius: 100px;
            font-weight: 700;
            font-size: 1.8rem;
            color: var(--accent);
            border: 1px solid rgba(255,255,255,0.1);
            text-shadow: 0 0 20px rgba(0, 242, 254, 0.4);
            letter-spacing: 2px;
            transition: all 0.5s ease;
        }}

        .metrics {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 30px;
            margin-bottom: 80px;
        }}

        .metric-card {{
            background: rgba(255,255,255,0.02);
            padding: 30px;
            border-radius: 30px;
            border: 1px solid rgba(255,255,255,0.05);
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        .metric-card:hover {{
            background: rgba(255,255,255,0.05);
            transform: translateY(-10px);
            border-color: rgba(255,255,255,0.2);
        }}

        .metric-val {{
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 8px;
            color: #fff;
        }}

        .metric-label {{
            font-size: 0.75rem;
            color: rgba(255,255,255,0.3);
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 600;
        }}

        .score-display {{
            position: absolute;
            bottom: 40px;
            right: 60px;
            text-align: right;
            opacity: 0.5;
        }}

        .final-score {{
            font-size: 7rem;
            font-weight: 700;
            line-height: 1;
            margin-top: 20px;
            background: linear-gradient(to bottom, #fff, rgba(255,255,255,0.1));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .footer-logo {{
            position: absolute;
            bottom: 60px;
            left: 60px;
            text-align: left;
            opacity: 0.6;
        }}

        .signature {{
            font-family: 'Brush Script MT', cursive;
            font-size: 2.5rem;
            margin-bottom: 5px;
            opacity: 0.8;
        }}

        .meta-text {{
            font-size: 0.8rem;
            color: rgba(255,255,255,0.3);
            letter-spacing: 1px;
        }}

        /* Animated Blobs */
        .blob {{
            position: absolute;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(79, 172, 254, 0.2) 0%, transparent 70%);
            border-radius: 50%;
            z-index: -1;
            filter: blur(80px);
            animation: move 20s infinite alternate;
        }}

        @keyframes move {{
            from {{ transform: translate(-30%, -30%); }}
            to {{ transform: translate(30%, 30%); }}
        }}

    </style>
</head>
<body>
    <div class="blob"></div>
    <div class="container">
        <div class="certificate">
            <div class="header">
                <h1>Visionary</h1>
                <p class="subtitle">Awarded for Elite Godot 4.6 Architecture & Synthesis</p>
            </div>
            
            <div class="tier-section">
                <div class="tier-badge">{tier}</div>
            </div>
            
            <div class="metrics">
                {"".join([f'<div class="metric-card"><div class="metric-val">{v}%</div><div class="metric-label">{k}</div></div>' for k,v in scores.items()])}
            </div>

            <div class="final-score">{int(total_score)}</div>

            <div class="footer-logo">
                <div class="signature">Anara</div>
                <div class="meta-text">GDSkills Proto-Architect Registry | ID: {project_name.upper()}_VISION</div>
            </div>
            
            <div class="score-display">
                <div class="meta-text">Project Compliance Verified</div>
                <div class="meta-text" style="margin-top: 5px;">Aurelius & Anara Protocol | v0.0.7</div>
            </div>
        </div>
    </div>
</body>
</html>
    """

    filename = "GDSkills_Visionary_Certificate.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Certificate generated: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Default demo data
        generate_premium_certificate("Project Phoenix", {{
            "Modernity": 98,
            "Scalability": 92,
            "Composition": 89,
            "Logic": 95,
            "VFX": 91
        }})
    else:
        # Logic to take scores from separate scripts
        pass
