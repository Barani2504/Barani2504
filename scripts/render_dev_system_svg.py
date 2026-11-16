#!/usr/bin/env python3
"""
Generate both dark and light mode versions of dev-system.svg for Barani S.
- dev-system-dark.svg: Black/dark cyberpunk aesthetic (#090d16 / #0d1117)
- dev-system-light.svg: Crisp white/light aesthetic (#ffffff / #f6f8fa)
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")

W, H = 860, 520
PAD = 20
TITLEBAR_H = 32

def render_svg(mode="dark"):
    is_dark = mode == "dark"
    
    # Palette
    if is_dark:
        bg = "#090d16"
        bg2 = "#111722"
        card_bg = "#131922"
        inner_card_bg = "#090d16"
        frame = "#30363d"
        frame_inner = "#21262d"
        muted = "#7d8590"
        text = "#e6edf3"
        cyan = "#38bdf8"
        violet = "#8b5cf6"
        deep_violet = "#6c2bd9"
        green = "#059669"
        green_bright = "#39d353"
        pill_role_bg = "#6c2bd922"
        pill_role_border = "#8b5cf6"
        pill_simats_bg = "#05966922"
        pill_simats_border = "#059669"
        status_banner_bg = "#05966922"
        status_banner_border = "#059669"
    else:
        # Light mode: White / crisp clean theme
        bg = "#ffffff"
        bg2 = "#f6f8fa"
        card_bg = "#f6f8fa"
        inner_card_bg = "#ffffff"
        frame = "#d0d7de"
        frame_inner = "#e1e4e8"
        muted = "#57606a"
        text = "#1f2328"
        cyan = "#0284c7"         # vibrant dark-sky blue
        violet = "#7c3aed"       # rich purple
        deep_violet = "#6c2bd9"
        green = "#16a34a"        # rich green
        green_bright = "#16a34a"
        pill_role_bg = "#7c3aed18"
        pill_role_border = "#7c3aed66"
        pill_simats_bg = "#16a34a18"
        pill_simats_border = "#16a34a66"
        status_banner_bg = "#16a34a18"
        status_banner_border = "#16a34a66"

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'font-family="\'Fira Code\', \'JetBrains Mono\', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace">',
        '<style>',
        '  .fade-in { opacity: 0; animation: fadeIn 0.5s ease-out both; }',
        '  .pulse-fast { animation: pulse 1.8s ease-in-out infinite; }',
        '  .pulse-glow { animation: pulseGlow 2.2s ease-in-out infinite; }',
        '  .cursor { animation: blink 1s step-start infinite; }',
        '  .bar-grow { transform-box: fill-box; transform-origin: left; animation: barGrow 1.2s cubic-bezier(0.16, 1, 0.3, 1) both; }',
        '  @keyframes fadeIn { 0% { opacity: 0; transform: translateY(8px); } 100% { opacity: 1; transform: translateY(0); } }',
        '  @keyframes pulse { 0%, 100% { opacity: 0.95; transform: scale(1); } 50% { opacity: 0.45; transform: scale(0.92); } }',
        '  @keyframes pulseGlow { 0% { r: 3.5px; opacity: 0.9; } 50% { r: 8px; opacity: 0; } 100% { r: 3.5px; opacity: 0.9; } }',
        '  @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }',
        '  @keyframes barGrow { 0% { transform: scaleX(0); } 100% { transform: scaleX(1); } }',
        '  @media (prefers-reduced-motion: reduce) {',
        '    .fade-in, .bar-grow { opacity: 1 !important; transform: none !important; animation: none !important; }',
        '    .pulse-fast, .pulse-glow, .cursor { animation: none !important; }',
        '  }',
        '</style>',
        '<defs>',
        f'  <linearGradient id="win-bg-{mode}" x1="0" y1="0" x2="0" y2="1">',
        f'    <stop offset="0%" stop-color="{bg2}"/>',
        f'    <stop offset="100%" stop-color="{bg}"/>',
        f'  </linearGradient>',
        f'  <linearGradient id="bar-grad-{mode}" x1="0" y1="0" x2="1" y2="0">',
        f'    <stop offset="0%" stop-color="{cyan}"/>',
        f'    <stop offset="50%" stop-color="{violet}"/>',
        f'    <stop offset="100%" stop-color="{deep_violet}"/>',
        f'  </linearGradient>',
        '</defs>',
        # Window shell
        f'<rect width="{W}" height="{H}" rx="12" fill="url(#win-bg-{mode})"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{frame}"/>',
        f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{frame}"/>',
    ]

    # Traffic lights
    for i, col in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{col}"/>')

    # Titlebar
    parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{muted}" font-size="12" '
                 f'text-anchor="middle">barani@simats: ~$ systemctl status barani.profile</text>')

    # Live System Badge
    parts.append(
        f'<g transform="translate({W - 145}, {TITLEBAR_H/2})">'
        f'  <circle cx="0" cy="0" r="3.5" fill="{green_bright}"/>'
        f'  <circle cx="0" cy="0" r="3.5" fill="none" stroke="{green_bright}" stroke-width="1.5" class="pulse-glow"/>'
        f'  <text x="12" y="3.5" fill="{green_bright}" font-size="11" font-weight="700" letter-spacing="1">SYSTEM ONLINE</text>'
        f'</g>'
    )

    # HUD Tech Crosshairs / Corner brackets
    parts.append(f'<path d="M 22 44 L 34 44 M 22 44 L 22 56" stroke="{cyan}" stroke-width="1.5" fill="none" opacity="0.6"/>')
    parts.append(f'<path d="M {W-22} 44 L {W-34} 44 M {W-22} 44 L {W-22} 56" stroke="{cyan}" stroke-width="1.5" fill="none" opacity="0.6"/>')
    parts.append(f'<path d="M 22 {H-22} L 34 {H-22} M 22 {H-22} L 22 {H-34}" stroke="{cyan}" stroke-width="1.5" fill="none" opacity="0.6"/>')
    parts.append(f'<path d="M {W-22} {H-22} L {W-34} {H-22} M {W-22} {H-22} L {W-22} {H-34}" stroke="{cyan}" stroke-width="1.5" fill="none" opacity="0.6"/>')

    # Left column: Core Identity & Stack
    left_x = 22
    left_y = 48
    left_w = 428
    left_h = H - left_y - 20

    parts.append(f'<g class="fade-in" style="animation-delay: 0.1s">')
    parts.append(f'  <rect x="{left_x}" y="{left_y}" width="{left_w}" height="{left_h}" rx="10" '
                 f'fill="{card_bg}" stroke="{frame}"/>')
    # Header
    parts.append(f'  <text x="{left_x + 18}" y="{left_y + 28}" fill="{cyan}" font-size="13" font-weight="700" letter-spacing="1.2">⚡ INITIALIZING DEV SYSTEM</text>')
    parts.append(f'  <text x="{left_x + left_w - 18}" y="{left_y + 28}" fill="{green_bright}" font-size="11" text-anchor="end">BOOT: 100%</text>')

    # Boot Progress Bar
    bar_x = left_x + 18
    bar_y = left_y + 40
    bar_w = left_w - 36
    bar_h = 6
    parts.append(f'  <rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="3" fill="{frame_inner}"/>')
    parts.append(f'  <rect class="bar-grow" x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="3" fill="url(#bar-grad-{mode})"/>')

    # Divider
    parts.append(f'  <line x1="{left_x + 18}" y1="{left_y + 60}" x2="{left_x + left_w - 18}" y2="{left_y + 60}" stroke="{frame}" stroke-dasharray="3,3"/>')

    # Identity section
    parts.append(f'  <text x="{left_x + 18}" y="{left_y + 82}" fill="{muted}" font-size="11" font-weight="700" letter-spacing="1">🧠 CORE IDENTITY</text>')
    parts.append(f'  <text x="{left_x + 18}" y="{left_y + 106}" fill="{text}" font-size="19" font-weight="700">Barani S</text>')

    # Role pill
    pill_x = left_x + 18
    pill_y = left_y + 118
    parts.append(f'  <rect x="{pill_x}" y="{pill_y}" width="215" height="22" rx="11" fill="{pill_role_bg}" stroke="{pill_role_border}"/>')
    parts.append(f'  <text x="{pill_x + 10}" y="{pill_y + 15}" fill="{cyan}" font-size="11" font-weight="600">Native iOS &amp; AI/ML Engineer</text>')

    # Mode indicator
    mode_x = pill_x + 225
    parts.append(f'  <rect x="{mode_x}" y="{pill_y}" width="145" height="22" rx="11" fill="{pill_simats_bg}" stroke="{pill_simats_border}"/>')
    parts.append(f'  <circle cx="{mode_x + 12}" cy="{pill_y + 11}" r="3" fill="{green_bright}"/>')
    parts.append(f'  <text x="{mode_x + 22}" y="{pill_y + 15}" fill="{green_bright}" font-size="10" font-weight="600">SIMATS · INTERN</text>')

    # System Configuration / Stack
    parts.append(f'  <line x1="{left_x + 18}" y1="{left_y + 156}" x2="{left_x + left_w - 18}" y2="{left_y + 156}" stroke="{frame}"/>')
    parts.append(f'  <text x="{left_x + 18}" y="{left_y + 178}" fill="{muted}" font-size="11" font-weight="700" letter-spacing="1">⚙️ PRIMARY STACK</text>')

    # Stack Cards
    c1_y = left_y + 192
    parts.append(f'  <rect x="{left_x + 18}" y="{c1_y}" width="{left_w - 36}" height="56" rx="8" fill="{inner_card_bg}" stroke="{frame}"/>')
    parts.append(f'  <text x="{left_x + 30}" y="{c1_y + 24}" fill="{text}" font-size="13" font-weight="700">📱 Native iOS Engineering</text>')
    parts.append(f'  <text x="{left_x + 30}" y="{c1_y + 44}" fill="{muted}" font-size="11">Swift · SwiftUI · UIKit · Combine · Core Data</text>')
    parts.append(f'  <circle cx="{left_x + left_w - 34}" cy="{c1_y + 28}" r="4" fill="{cyan}"/>')

    c2_y = c1_y + 64
    parts.append(f'  <rect x="{left_x + 18}" y="{c2_y}" width="{left_w - 36}" height="56" rx="8" fill="{inner_card_bg}" stroke="{frame}"/>')
    parts.append(f'  <text x="{left_x + 30}" y="{c2_y + 24}" fill="{text}" font-size="13" font-weight="700">🧠 On-Device AI / ML</text>')
    parts.append(f'  <text x="{left_x + 30}" y="{c2_y + 44}" fill="{muted}" font-size="11">Core ML · TensorFlow Lite · YOLOv8 · RAG Systems</text>')
    parts.append(f'  <circle cx="{left_x + left_w - 34}" cy="{c2_y + 28}" r="4" fill="{violet}"/>')

    cap_y = c2_y + 72
    parts.append(f'  <text x="{left_x + 18}" y="{cap_y + 14}" fill="{muted}" font-size="11" font-weight="700" letter-spacing="1">🛠️ ARCHITECTURE &amp; RELEASE</text>')

    caps = [
        ("⚡ Healthcare Apps", "→ On-Device CT Vision · TestFlight"),
        ("⚙️ Backend &amp; APIs", "→ REST APIs · PHP · MySQL · Redis"),
        ("🏆 Mentorship", "→ 100+ Engineers Guided · Code Reviews"),
    ]
    for j, (title, desc) in enumerate(caps):
        cy = cap_y + 30 + j * 26
        parts.append(f'  <text x="{left_x + 22}" y="{cy}" fill="{text}" font-size="11" font-weight="600">{title}</text>')
        parts.append(f'  <text x="{left_x + 175}" y="{cy}" fill="{muted}" font-size="11">{desc}</text>')

    parts.append('</g>')

    # Right column
    right_x = left_x + left_w + 14
    right_w = W - right_x - 22
    rt_y = left_y
    rt_h = 195

    parts.append(f'<g class="fade-in" style="animation-delay: 0.25s">')
    parts.append(f'  <rect x="{right_x}" y="{rt_y}" width="{right_w}" height="{rt_h}" rx="10" '
                 f'fill="{card_bg}" stroke="{frame}"/>')
    parts.append(f'  <text x="{right_x + 18}" y="{rt_y + 28}" fill="{cyan}" font-size="13" font-weight="700" letter-spacing="1.2">📊 DEPLOYMENT LOGS</text>')
    parts.append(f'  <text x="{right_x + right_w - 18}" y="{rt_y + 28}" fill="{green_bright}" font-size="11" text-anchor="end">STATUS: STABLE</text>')

    tile_w = (right_w - 36 - 16) / 3
    tile_h = 76
    metrics = [
        ("3–5", "Healthcare Apps", "Shipped &amp; Live", cyan),
        ("100+", "Engineers", "Guided &amp; Mentored", violet),
        ("8.0", "CGPA", "SIMATS Engineering", green_bright),
    ]

    for i, (val, title, caption, accent) in enumerate(metrics):
        tx = right_x + 18 + i * (tile_w + 8)
        ty = rt_y + 44
        parts.append(f'  <rect x="{tx:.1f}" y="{ty}" width="{tile_w:.1f}" height="{tile_h}" rx="8" fill="{inner_card_bg}" stroke="{frame}"/>')
        parts.append(f'  <text x="{tx + tile_w/2:.1f}" y="{ty + 34}" fill="{accent}" font-size="22" font-weight="700" text-anchor="middle">{val}</text>')
        parts.append(f'  <text x="{tx + tile_w/2:.1f}" y="{ty + 52}" fill="{text}" font-size="11" font-weight="600" text-anchor="middle">{title}</text>')
        parts.append(f'  <text x="{tx + tile_w/2:.1f}" y="{ty + 66}" fill="{muted}" font-size="9" text-anchor="middle">{caption}</text>')

    parts.append(f'  <line x1="{right_x + 18}" y1="{rt_y + 134}" x2="{right_x + right_w - 18}" y2="{rt_y + 134}" stroke="{frame}"/>')
    parts.append(f'  <text x="{right_x + 18}" y="{rt_y + 156}" fill="{green_bright}" font-size="12">✔ Production Releases: TESTFLIGHT / APP STORE</text>')
    parts.append(f'  <text x="{right_x + right_w - 18}" y="{rt_y + 156}" fill="{muted}" font-size="11" text-anchor="end">Reliability: HIGH</text>')
    parts.append(f'  <text x="{right_x + 18}" y="{rt_y + 178}" fill="{muted}" font-size="11">✔ Neural Vision: CORE ML &amp; YOLOV8 · 100% On-Device</text>')
    parts.append('</g>')

    # Right middle: Current Runtime Process
    rc_y = rt_y + rt_h + 12
    rc_h = 155

    parts.append(f'<g class="fade-in" style="animation-delay: 0.4s">')
    parts.append(f'  <rect x="{right_x}" y="{rc_y}" width="{right_w}" height="{rc_h}" rx="10" '
                 f'fill="{card_bg}" stroke="{frame}"/>')
    parts.append(f'  <text x="{right_x + 18}" y="{rc_y + 26}" fill="{cyan}" font-size="13" font-weight="700" letter-spacing="1.2">🔄 CURRENT PROCESS</text>')

    parts.append(f'  <g transform="translate({right_x + right_w - 82}, {rc_y + 22})">'
                 f'    <circle cx="0" cy="0" r="3.5" fill="{green_bright}"/>'
                 f'    <text x="10" y="3.5" fill="{green_bright}" font-size="11" font-weight="600">RUNNING</text>'
                 f'  </g>')

    sb_y = rc_y + 38
    parts.append(f'  <rect x="{right_x + 18}" y="{sb_y}" width="{right_w - 36}" height="26" rx="6" fill="{status_banner_bg}" stroke="{status_banner_border}"/>')
    parts.append(f'  <text x="{right_x + 30}" y="{sb_y + 17}" fill="{green_bright}" font-size="11" font-weight="700">🟢 STATUS: DEVELOPING ON-DEVICE VISION PIPELINES</text>')

    logs = [
        "&gt; Loading Swift concurrency &amp; SwiftUI state engine...",
        "&gt; Quantizing YOLOv8 &amp; Core ML neural weights for ANE...",
        "&gt; Running real-time inference &amp; TestFlight deployment...",
    ]
    for k, l in enumerate(logs):
        parts.append(f'  <text x="{right_x + 18}" y="{sb_y + 44 + k * 18}" fill="{muted}" font-size="11">{l}</text>')

    parts.append('</g>')

    # Right bottom: Signal Output Quote
    rq_y = rc_y + rc_h + 10
    rq_h = left_h - (rt_h + 12 + rc_h + 10)

    parts.append(f'<g class="fade-in" style="animation-delay: 0.55s">')
    parts.append(f'  <rect x="{right_x}" y="{rq_y}" width="{right_w}" height="{rq_h}" rx="8" '
                 f'fill="{card_bg}" stroke="{frame}"/>')
    parts.append(f'  <text x="{right_x + 16}" y="{rq_y + 22}" fill="{cyan}" font-size="11" font-weight="700" letter-spacing="1">⚡ SIGNAL OUTPUT</text>')
    parts.append(f'  <text x="{right_x + 16}" y="{rq_y + 44}" fill="{text}" font-size="11.5" font-style="italic">"Engineering production iOS apps with on-device intelligence."</text>')
    parts.append(f'  <rect class="cursor" x="{right_x + right_w - 24}" y="{rq_y + 33}" width="7" height="13" fill="{cyan}"/>')
    parts.append('</g>')

    parts.append('</svg>')
    return "\n".join(parts)

# Generate dark mode
dark_svg = render_svg("dark")
with open(os.path.join(ASSETS, "dev-system-dark.svg"), "w", encoding="utf-8") as f:
    f.write(dark_svg)
with open(os.path.join(ASSETS, "dev-system.svg"), "w", encoding="utf-8") as f:
    f.write(dark_svg)
print("Generated dev-system-dark.svg and dev-system.svg")

# Generate light mode
light_svg = render_svg("light")
with open(os.path.join(ASSETS, "dev-system-light.svg"), "w", encoding="utf-8") as f:
    f.write(light_svg)
print("Generated dev-system-light.svg")
