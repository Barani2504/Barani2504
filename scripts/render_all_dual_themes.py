import os
import re
import xml.etree.ElementTree as ET

BASE_DIR = r"c:\Users\baran\Downloads\Barani2504-main"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

# ==============================================================================
# 1. GENERATE DUAL-THEME DEV SYSTEM SVGs (FIX TEXT OVERLAP)
# ==============================================================================
def render_dev_system(mode="dark"):
    is_dark = mode == "dark"
    W, H = 860, 520
    PAD = 20
    TITLEBAR_H = 32

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
        bg = "#ffffff"
        bg2 = "#f6f8fa"
        card_bg = "#f6f8fa"
        inner_card_bg = "#ffffff"
        frame = "#d0d7de"
        frame_inner = "#e1e4e8"
        muted = "#57606a"
        text = "#1f2328"
        cyan = "#0284c7"
        violet = "#7c3aed"
        deep_violet = "#6c2bd9"
        green = "#16a34a"
        green_bright = "#16a34a"
        pill_role_bg = "#f3e8ff"
        pill_role_border = "#a855f7"
        pill_simats_bg = "#dcfce7"
        pill_simats_border = "#16a34a"
        status_banner_bg = "#dcfce7"
        status_banner_border = "#16a34a"

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'font-family="\'Fira Code\', \'JetBrains Mono\', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        '<style>',
        '  .fade-in { opacity: 0; animation: in 0.6s ease-out both; }',
        '  .pulse { animation: blink 2s infinite ease-in-out; }',
        '  .cursor { animation: blink 1s step-start infinite; }',
        '  @keyframes in { 0% { opacity: 0; transform: translateY(8px); } 100% { opacity: 1; transform: translateY(0); } }',
        '  @keyframes blink { 0%, 100% { opacity: 0.35; } 50% { opacity: 1; } }',
        '  @media (prefers-reduced-motion: reduce) {',
        '    .fade-in { opacity: 1 !important; transform: none !important; animation: none !important; }',
        '    .pulse, .cursor { animation: none !important; }',
        '  }',
        '</style>',
        '<defs>',
        f'  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">',
        f'    <stop offset="0%" stop-color="{bg2}"/>',
        f'    <stop offset="100%" stop-color="{bg}"/>',
        f'  </linearGradient>',
        '</defs>',
        f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{frame}"/>',
        f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{frame}"/>',
        '<circle cx="20" cy="16" r="5" fill="#ff5f56"/>',
        '<circle cx="36" cy="16" r="5" fill="#ffbd2e"/>',
        '<circle cx="52" cy="16" r="5" fill="#27c93f"/>',
        f'<text x="{W/2}" y="20" fill="{muted}" font-size="12" text-anchor="middle">barani@simats: ~$ systemctl status barani.profile</text>',
        f'<g transform="translate({W - PAD - 130}, 16)">',
        f'  <circle cx="0" cy="0" r="4" fill="{green_bright}" class="pulse"/>',
        f'  <text x="10" y="4" fill="{green_bright}" font-size="11" font-weight="600">SYSTEM ONLINE</text>',
        '</g>',
        f'<g class="fade-in" style="animation-delay: 0.1s">',
        f'  <text x="{PAD}" y="{TITLEBAR_H + 24}" fill="{cyan}" font-size="11" font-weight="700">⚡ INITIALIZING DEV SYSTEM</text>',
        f'  <text x="{PAD + 400}" y="{TITLEBAR_H + 24}" fill="{muted}" font-size="11" text-anchor="end">BOOT: 100%</text>',
        f'  <line x1="{PAD}" y1="{TITLEBAR_H + 32}" x2="{PAD + 400}" y2="{TITLEBAR_H + 32}" stroke="{violet}" stroke-width="2"/>',
        '</g>'
    ]

    left_x = PAD
    left_y = TITLEBAR_H + 46
    left_w = 400
    left_h = H - left_y - PAD

    parts.append(f'<g class="fade-in" style="animation-delay: 0.2s">')
    parts.append(f'  <rect x="{left_x}" y="{left_y}" width="{left_w}" height="{left_h}" rx="10" '
                 f'fill="{card_bg}" stroke="{frame}"/>')
    parts.append(f'  <text x="{left_x + 18}" y="{left_y + 26}" fill="{muted}" font-size="10" font-weight="700" letter-spacing="1.2">🧠 CORE IDENTITY</text>')
    parts.append(f'  <text x="{left_x + 18}" y="{left_y + 54}" fill="{text}" font-size="22" font-weight="700">Barani S</text>')

    parts.append(f'  <rect x="{left_x + 18}" y="{left_y + 68}" width="195" height="24" rx="12" fill="{pill_role_bg}" stroke="{pill_role_border}"/>')
    parts.append(f'  <text x="{left_x + 115}" y="{left_y + 84}" fill="{cyan}" font-size="11" font-weight="600" text-anchor="middle">Native iOS &amp; AI/ML Engineer</text>')

    parts.append(f'  <rect x="{left_x + 221}" y="{left_y + 68}" width="135" height="24" rx="12" fill="{pill_simats_bg}" stroke="{pill_simats_border}"/>')
    parts.append(f'  <circle cx="{left_x + 233}" cy="{left_y + 80}" r="3" fill="{green_bright}"/>')
    parts.append(f'  <text x="{left_x + 293}" y="{left_y + 84}" fill="{green_bright}" font-size="10" font-weight="600" text-anchor="middle">SIMATS · INTERN</text>')

    parts.append(f'  <line x1="{left_x + 18}" y1="{left_y + 106}" x2="{left_x + left_w - 18}" y2="{left_y + 106}" stroke="{frame_inner}"/>')

    parts.append(f'  <text x="{left_x + 18}" y="{left_y + 126}" fill="{muted}" font-size="10" font-weight="700" letter-spacing="1.2">⚙ PRIMARY STACK</text>')
    parts.append(f'  <rect x="{left_x + 18}" y="{left_y + 138}" width="{left_w - 36}" height="54" rx="8" fill="{inner_card_bg}" stroke="{frame}"/>')
    parts.append(f'  <text x="{left_x + 30}" y="{left_y + 160}" fill="{text}" font-size="13" font-weight="600">📱 Native iOS Engineering</text>')
    parts.append(f'  <text x="{left_x + 30}" y="{left_y + 178}" fill="{muted}" font-size="11">Swift · SwiftUI · UIKit · Combine · Core Data</text>')
    parts.append(f'  <circle cx="{left_x + left_w - 32}" cy="{left_y + 162}" r="3.5" fill="{cyan}"/>')

    parts.append(f'  <rect x="{left_x + 18}" y="{left_y + 200}" width="{left_w - 36}" height="54" rx="8" fill="{inner_card_bg}" stroke="{frame}"/>')
    parts.append(f'  <text x="{left_x + 30}" y="{left_y + 222}" fill="{text}" font-size="13" font-weight="600">🧠 On-Device AI / ML</text>')
    parts.append(f'  <text x="{left_x + 30}" y="{left_y + 240}" fill="{muted}" font-size="11">Core ML · TensorFlow Lite · YOLOv8 · RAG</text>')
    parts.append(f'  <circle cx="{left_x + left_w - 32}" cy="{left_y + 224}" r="3.5" fill="{violet}"/>')

    parts.append(f'  <line x1="{left_x + 18}" y1="{left_y + 268}" x2="{left_x + left_w - 18}" y2="{left_y + 268}" stroke="{frame_inner}"/>')
    parts.append(f'  <text x="{left_x + 18}" y="{left_y + 288}" fill="{muted}" font-size="10" font-weight="700" letter-spacing="1.2">🛠 ARCHITECTURE &amp; RELEASE</text>')

    specs = [
        ("⚡ Healthcare Apps", "→ On-Device CT Vision · TestFlight"),
        ("⚙ Backend &amp; APIs", "→ REST APIs · PHP · MySQL · Redis"),
        ("🏆 Mentorship", "→ 100+ Engineers Guided · Code Reviews")
    ]
    for i, (k, v) in enumerate(specs):
        sy = left_y + 310 + i * 24
        parts.append(f'  <text x="{left_x + 18}" y="{sy}" fill="{text}" font-size="11" font-weight="600">{k}</text>')
        parts.append(f'  <text x="{left_x + 135}" y="{sy}" fill="{muted}" font-size="11">{v}</text>')

    parts.append('</g>')

    right_x = left_x + left_w + 20
    right_w = W - right_x - PAD
    rt_y = left_y
    rt_h = 195

    parts.append(f'<g class="fade-in" style="animation-delay: 0.3s">')
    parts.append(f'  <rect x="{right_x}" y="{rt_y}" width="{right_w}" height="{rt_h}" rx="10" '
                 f'fill="{card_bg}" stroke="{frame}"/>')
    parts.append(f'  <text x="{right_x + 18}" y="{rt_y + 26}" fill="{muted}" font-size="10" font-weight="700" letter-spacing="1.2">📊 DEPLOYMENT LOGS</text>')
    parts.append(f'  <text x="{right_x + right_w - 18}" y="{rt_y + 26}" fill="{green_bright}" font-size="10" font-weight="700" text-anchor="end">STATUS: STABLE</text>')

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
    # Clean non-colliding layout
    parts.append(f'  <text x="{right_x + 18}" y="{rt_y + 156}" fill="{green_bright}" font-size="11">✔ App Releases: TestFlight &amp; App Store Connect</text>')
    parts.append(f'  <text x="{right_x + 18}" y="{rt_y + 178}" fill="{muted}" font-size="11">✔ Neural Vision: Core ML &amp; YOLOv8 · 100% On-Device</text>')
    parts.append('</g>')

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

    parts.append(f'  <rect x="{right_x + 18}" y="{rc_y + 38}" width="{right_w - 36}" height="24" rx="4" fill="{status_banner_bg}" stroke="{status_banner_border}"/>')
    parts.append(f'  <circle cx="{right_x + 28}" cy="{rc_y + 50}" r="3" fill="{green_bright}"/>')
    parts.append(f'  <text x="{right_x + 38}" y="{rc_y + 54}" fill="{green_bright}" font-size="10" font-weight="700">STATUS: DEVELOPING ON-DEVICE VISION PIPELINES</text>')

    logs = [
        "> Loading Swift concurrency &amp; SwiftUI state engine...",
        "> Quantizing YOLOv8 &amp; Core ML neural weights for ANE...",
        "> Running real-time inference &amp; TestFlight deployment..."
    ]
    for i, log in enumerate(logs):
        ly = rc_y + 80 + i * 20
        parts.append(f'  <text x="{right_x + 18}" y="{ly}" fill="{muted}" font-size="10">{log}</text>')
    parts.append('</g>')

    rb_y = rc_y + rc_h + 12
    rb_h = left_h - rt_h - rc_h - 24

    parts.append(f'<g class="fade-in" style="animation-delay: 0.5s">')
    parts.append(f'  <rect x="{right_x}" y="{rb_y}" width="{right_w}" height="{rb_h}" rx="10" '
                 f'fill="{card_bg}" stroke="{frame}"/>')
    parts.append(f'  <text x="{right_x + 18}" y="{rb_y + 22}" fill="{cyan}" font-size="10" font-weight="700" letter-spacing="1.2">⚡ SIGNAL OUTPUT</text>')
    parts.append(f'  <text x="{right_x + 18}" y="{rb_y + 44}" fill="{text}" font-size="11" font-style="italic">"Engineering production iOS apps with on-device intelligence"</text>')
    parts.append(f'  <rect x="{right_x + 386}" y="{rb_y + 34}" width="7" height="12" fill="{cyan}" class="cursor"/>')
    parts.append('</g>')

    parts.append('</svg>')
    return "\n".join(parts)


# ==============================================================================
# 2. GENERATE DUAL-THEME AI/ML EXPERTISE MATRIX SVGs
# ==============================================================================
def render_aiml_matrix(mode="dark"):
    is_dark = mode == "dark"
    W, H = 860, 390
    PAD = 20
    TITLEBAR_H = 32

    if is_dark:
        bg = "#090d16"
        bg2 = "#111722"
        card_bg = "#131922"
        frame = "#30363d"
        muted = "#7d8590"
        text = "#e6edf3"
        cyan = "#38bdf8"
        violet = "#8b5cf6"
        green = "#059669"
        green_bright = "#39d353"
        amber = "#f59e0b"
        bar_bg = "#21262d"
    else:
        bg = "#ffffff"
        bg2 = "#f6f8fa"
        card_bg = "#f6f8fa"
        frame = "#d0d7de"
        muted = "#57606a"
        text = "#1f2328"
        cyan = "#0284c7"
        violet = "#7c3aed"
        green = "#16a34a"
        green_bright = "#16a34a"
        amber = "#d97706"
        bar_bg = "#e1e4e8"

    DOMAINS = [
        {
            "title": "On-Device Inference",
            "badge": "CORE ML · TFLITE",
            "rating_dots": "●●●●○",
            "pct": 80,
            "color": cyan,
            "desc": "Core ML &amp; TensorFlow Lite deployment for offline, private, real-time predictions on iOS",
            "delay": "0.15s"
        },
        {
            "title": "Computer Vision",
            "badge": "YOLOV8 · RADIOLOGY CT",
            "rating_dots": "●●●●○",
            "pct": 80,
            "color": violet,
            "desc": "YOLOv8-based detection pipeline for medical CT image analysis (kidney stone detection)",
            "delay": "0.25s"
        },
        {
            "title": "RAG Systems",
            "badge": "CODEGO COMPILER · RETRIEVAL",
            "rating_dots": "●●●○○",
            "pct": 60,
            "color": amber,
            "desc": "Retrieval-Augmented Generation for code assistant &amp; multi-language platform support",
            "delay": "0.35s"
        },
        {
            "title": "AI Chatbot Development",
            "badge": "CORECARE IOS · VITALS",
            "rating_dots": "●●●●○",
            "pct": 80,
            "color": green_bright,
            "desc": "Conversational health-monitoring chatbot with real-time vitals context &amp; offline cache",
            "delay": "0.45s"
        }
    ]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'font-family="\'Fira Code\', \'JetBrains Mono\', ui-monospace, monospace">',
        '<style>',
        '  .card { opacity: 0; animation: in 0.5s ease-out both; }',
        '  .pulse { animation: blink 2s infinite ease-in-out; }',
        '  .bar-grow-80 { transform-box: fill-box; transform-origin: left; animation: grow80 1.2s cubic-bezier(0.16, 1, 0.3, 1) both; }',
        '  .bar-grow-60 { transform-box: fill-box; transform-origin: left; animation: grow60 1.2s cubic-bezier(0.16, 1, 0.3, 1) both; }',
        '  @keyframes in { 0% { opacity: 0; transform: translateY(10px); } 100% { opacity: 1; transform: translateY(0); } }',
        '  @keyframes blink { 0%, 100% { opacity: 0.35; } 50% { opacity: 1; } }',
        '  @keyframes grow80 { 0% { transform: scaleX(0); } 100% { transform: scaleX(1); } }',
        '  @keyframes grow60 { 0% { transform: scaleX(0); } 100% { transform: scaleX(1); } }',
        '  @media (prefers-reduced-motion: reduce) {',
        '    .card, .bar-grow-80, .bar-grow-60 { opacity: 1 !important; transform: none !important; animation: none !important; }',
        '    .pulse { animation: none !important; }',
        '  }',
        '</style>',
        '<defs>',
        f'  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">',
        f'    <stop offset="0%" stop-color="{bg2}"/>',
        f'    <stop offset="100%" stop-color="{bg}"/>',
        f'  </linearGradient>',
        '</defs>',
        f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{frame}"/>',
        f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{frame}"/>',
        '<circle cx="20" cy="16" r="5" fill="#ff5f56"/>',
        '<circle cx="36" cy="16" r="5" fill="#ffbd2e"/>',
        '<circle cx="52" cy="16" r="5" fill="#27c93f"/>',
        f'<text x="{W/2}" y="20" fill="{muted}" font-size="12" text-anchor="middle">barani@simats: ~$ ./ai_engine.py --precision=fp16 --target=AppleNeuralEngine</text>'
    ]

    top_y = TITLEBAR_H + 16
    parts.append(f'<g class="card" style="animation-delay: 0.05s;">')
    parts.append(f'  <circle cx="26" cy="{top_y + 8}" r="4" fill="{green_bright}" class="pulse"/>')
    parts.append(f'  <text x="38" y="{top_y + 12}" fill="{cyan}" font-size="13" font-weight="700">⚡ ON-DEVICE AI / ML ACCELERATION MATRIX</text>')
    parts.append(f'  <text x="{W - PAD}" y="{top_y + 12}" fill="{muted}" font-size="11" text-anchor="end">TARGET: Apple Neural Engine (ANE)</text>')
    parts.append('</g>')

    cols = 2
    cw = (W - PAD * 2 - 16) / cols
    ch = 135
    start_y = top_y + 30

    for i, dom in enumerate(DOMAINS):
        r = i // cols
        c = i % cols
        x = PAD + c * (cw + 16)
        y = start_y + r * (ch + 12)
        pct = dom["pct"]
        grow_class = "bar-grow-80" if pct == 80 else "bar-grow-60"
        bar_w = cw - 32
        fill_w = bar_w * (pct / 100.0)

        parts.append(f'<g class="card" style="animation-delay: {dom["delay"]};">')
        parts.append(f'  <rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="8" fill="{card_bg}" stroke="{frame}"/>')
        parts.append(f'  <circle cx="{x + 16}" cy="{y + 22}" r="4" fill="{dom["color"]}"/>')
        parts.append(f'  <text x="{x + 28}" y="{y + 26}" fill="{text}" font-size="14" font-weight="600">{dom["title"]}</text>')
        parts.append(f'  <text x="{x + cw - 16}" y="{y + 25}" fill="{dom["color"]}" font-size="10" font-weight="700" text-anchor="end">{dom["badge"]}</text>')

        by = y + 42
        parts.append(f'  <rect x="{x + 16}" y="{by}" width="{bar_w}" height="8" rx="4" fill="{bar_bg}"/>')
        parts.append(f'  <rect x="{x + 16}" y="{by}" width="{fill_w:.1f}" height="8" rx="4" fill="{dom["color"]}" class="{grow_class}"/>')

        parts.append(f'  <text x="{x + 16}" y="{by + 24}" fill="{dom["color"]}" font-size="12" font-weight="700">{dom["rating_dots"]}</text>')
        parts.append(f'  <text x="{x + cw - 16}" y="{by + 24}" fill="{muted}" font-size="11" text-anchor="end">{pct}% Proficiency</text>')

        parts.append(f'  <line x1="{x + 16}" y1="{by + 34}" x2="{x + cw - 16}" y2="{by + 34}" stroke="{frame}"/>')
        parts.append(f'  <text x="{x + 16}" y="{by + 52}" fill="{muted}" font-size="10">{dom["desc"]}</text>')
        parts.append('</g>')

    parts.append('</svg>')
    return "\n".join(parts)


# ==============================================================================
# 3. GENERATE DUAL-THEME ACHIEVEMENTS SVGs
# ==============================================================================
def render_achievements(mode="dark"):
    is_dark = mode == "dark"
    W, H = 860, 370
    PAD = 20
    TITLEBAR_H = 32

    if is_dark:
        bg = "#090d16"
        bg2 = "#111722"
        card_bg = "#131922"
        frame = "#30363d"
        muted = "#7d8590"
        text = "#e6edf3"
        cyan = "#38bdf8"
        violet = "#8b5cf6"
        green_bright = "#39d353"
        blue = "#0078d4"
        amber = "#f59e0b"
        badge_bg = "#090d16"
    else:
        bg = "#ffffff"
        bg2 = "#f6f8fa"
        card_bg = "#f6f8fa"
        frame = "#d0d7de"
        muted = "#57606a"
        text = "#1f2328"
        cyan = "#0284c7"
        violet = "#7c3aed"
        green_bright = "#16a34a"
        blue = "#0284c7"
        amber = "#d97706"
        badge_bg = "#ffffff"

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'font-family="\'Fira Code\', \'JetBrains Mono\', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        '<style>',
        '  .fade-in { opacity: 0; animation: in 0.5s ease-out both; }',
        '  .pulse { animation: blink 2s infinite ease-in-out; }',
        '  @keyframes in { 0% { opacity: 0; transform: translateY(10px); } 100% { opacity: 1; transform: translateY(0); } }',
        '  @keyframes blink { 0%, 100% { opacity: 0.35; } 50% { opacity: 1; } }',
        '  @media (prefers-reduced-motion: reduce) {',
        '    .fade-in { opacity: 1 !important; transform: none !important; animation: none !important; }',
        '    .pulse { animation: none !important; }',
        '  }',
        '</style>',
        '<defs>',
        f'  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">',
        f'    <stop offset="0%" stop-color="{bg2}"/>',
        f'    <stop offset="100%" stop-color="{bg}"/>',
        f'  </linearGradient>',
        '</defs>',
        f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{frame}"/>',
        f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{frame}"/>',
        '<circle cx="20" cy="16" r="5" fill="#ff5f56"/>',
        '<circle cx="36" cy="16" r="5" fill="#ffbd2e"/>',
        '<circle cx="52" cy="16" r="5" fill="#27c93f"/>',
        f'<text x="{W/2}" y="20" fill="{muted}" font-size="12" text-anchor="middle">barani@simats: ~$ ./achievements.sh --verify-production-records</text>'
    ]

    sb_y = TITLEBAR_H + 16
    parts.append(f'<g class="fade-in" style="animation-delay: 0.05s;">')
    parts.append(f'  <circle cx="26" cy="{sb_y + 8}" r="4" fill="{green_bright}" class="pulse"/>')
    parts.append(f'  <text x="38" y="{sb_y + 12}" fill="{green_bright}" font-size="11" font-weight="700">VERIFIED RECORDS: CONFIRMED</text>')
    parts.append(f'  <circle cx="210" cy="{sb_y + 8}" r="3" fill="{muted}"/>')
    parts.append(f'  <text x="220" y="{sb_y + 12}" fill="{muted}" font-size="11">AUDIT: TESTFLIGHT &amp; CODE REVIEWS</text>')
    parts.append(f'  <text x="{W - PAD}" y="{sb_y + 12}" fill="{cyan}" font-size="11" font-weight="700" text-anchor="end">STATUS: ACTIVE INGENUITY</text>')
    parts.append('</g>')

    tiles = [
        ("PRODUCTION APPS", "3–5", "Healthcare Shipped", cyan),
        ("PEER MENTORSHIP", "100+", "Engineers Guided", violet),
        ("ON-DEVICE AI/ML", "Core ML", "Vision Pipelines", green_bright),
        ("CROSS-PLATFORM", "iOS | And", "Mobile &amp; Web", amber),
    ]

    tw = (W - PAD * 2 - 12 * 3) / 4
    th = 84
    ty = sb_y + 28

    for i, (label, val, desc, accent) in enumerate(tiles):
        tx = PAD + i * (tw + 12)
        parts.append(f'<g class="fade-in" style="animation-delay: {0.1 + i*0.08:.2f}s;">')
        parts.append(f'  <rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="8" fill="{card_bg}" stroke="{frame}"/>')
        parts.append(f'  <text x="{tx + tw/2}" y="{ty + 22}" fill="{muted}" font-size="10" font-weight="700" text-anchor="middle">{label}</text>')
        parts.append(f'  <text x="{tx + tw/2}" y="{ty + 52}" fill="{accent}" font-size="20" font-weight="700" text-anchor="middle">{val}</text>')
        parts.append(f'  <text x="{tx + tw/2}" y="{ty + 70}" fill="{text}" font-size="11" text-anchor="middle">{desc}</text>')
        parts.append('</g>')

    rows = [
        ("🏥", "Healthcare App Delivery", "Shipped 3–5 production healthcare apps to TestFlight &amp; App Store Connect", "TESTFLIGHT · APP STORE", blue),
        ("🧑‍🏫", "Peer Mentorship", "Guided and reviewed code for 100+ student developers across iOS, Android &amp; web stacks", "CODE REVIEWS · 100+ DEVS", violet),
        ("🧠", "AI-Integrated Platforms", "Built on-device Core ML vision pipelines &amp; RAG-powered developer platforms", "CORE ML · YOLOV8 · RAG", green_bright)
    ]

    ry = ty + th + 18
    rw = W - PAD * 2
    rh = 46

    for i, (emoji, title, detail, tag, tag_color) in enumerate(rows):
        cur_y = ry + i * (rh + 8)
        parts.append(f'<g class="fade-in" style="animation-delay: {0.4 + i*0.1:.2f}s;">')
        parts.append(f'  <rect x="{PAD}" y="{cur_y}" width="{rw}" height="{rh}" rx="8" fill="{card_bg}" stroke="{frame}"/>')
        parts.append(f'  <text x="{PAD + 16}" y="{cur_y + 29}" font-size="16">{emoji}</text>')
        parts.append(f'  <text x="{PAD + 44}" y="{cur_y + 22}" fill="{text}" font-size="13" font-weight="600">{title}</text>')
        parts.append(f'  <text x="{PAD + 44}" y="{cur_y + 37}" fill="{muted}" font-size="10">{detail}</text>')
        tag_w = len(tag) * 6.5 + 20
        parts.append(f'  <rect x="{PAD + rw - tag_w - 16}" y="{cur_y + 13}" width="{tag_w}" height="20" rx="10" fill="{badge_bg}" stroke="{tag_color}"/>')
        parts.append(f'  <text x="{PAD + rw - tag_w/2 - 16}" y="{cur_y + 27}" fill="{tag_color}" font-size="9" font-weight="700" text-anchor="middle">{tag}</text>')
        parts.append('</g>')

    parts.append('</svg>')
    return "\n".join(parts)


# ==============================================================================
# 4. GENERATE DUAL-THEME CURRENT FOCUS BLOCKS SVGs
# ==============================================================================
def render_focus_blocks(mode="dark"):
    is_dark = mode == "dark"
    W, H = 860, 530
    PAD = 20
    TITLEBAR_H = 32

    if is_dark:
        bg = "#090d16"
        bg2 = "#111722"
        frame = "#30363d"
        card_bg = "#131922"
        muted = "#7d8590"
        text = "#e6edf3"
        cyan = "#38bdf8"
        violet = "#8b5cf6"
        green_bright = "#39d353"
        amber = "#f59e0b"
        badge_bg = "#090d16"
    else:
        bg = "#ffffff"
        bg2 = "#f6f8fa"
        frame = "#d0d7de"
        card_bg = "#f6f8fa"
        muted = "#57606a"
        text = "#1f2328"
        cyan = "#0284c7"
        violet = "#7c3aed"
        green_bright = "#16a34a"
        amber = "#d97706"
        badge_bg = "#ffffff"

    CARDS = [
        {
            "id": "01",
            "title": "LEARNING",
            "badge": "CONCURRENCY · TRANSFORMERS",
            "badge_color": cyan,
            "lines": [
                ("├──", "Advanced Swift Concurrency &amp; SwiftData"),
                ("└──", "On-Device LLM &amp; Vision Transformer Optimization")
            ],
            "metric_label": "KNOWLEDGE DEPTH",
            "metric_val": "Active Deep Dive"
        },
        {
            "id": "02",
            "title": "BUILDING",
            "badge": "HEALTHCARE · RAG COMPILER",
            "badge_color": green_bright,
            "lines": [
                ("├──", "Production AI-integrated healthcare iOS apps"),
                ("└──", "RAG-powered developer compilation &amp; tooling")
            ],
            "metric_label": "DEPLOYMENTS",
            "metric_val": "3–5 Shipped Apps"
        },
        {
            "id": "03",
            "title": "EXPLORING",
            "badge": "CORE ML · YOLOV8 · EDGE",
            "badge_color": violet,
            "lines": [
                ("├──", "Cross-platform AI feature parity (iOS + Android)"),
                ("└──", "Edge computer vision models (Core ML &amp; YOLOv8)")
            ],
            "metric_label": "ARCHITECTURE",
            "metric_val": "On-Device Inference"
        },
        {
            "id": "04",
            "title": "OPEN TO",
            "badge": "CAREER &amp; COLLABORATION",
            "badge_color": amber,
            "lines": [
                ("├──", "Native iOS Developer / Mobile Engineer roles"),
                ("└──", "AI/ML-driven mobile engineering collaborations")
            ],
            "metric_label": "AVAILABILITY",
            "metric_val": "Open to Opportunities"
        }
    ]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'font-family="\'Fira Code\', \'JetBrains Mono\', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        '<style>',
        '  .block { opacity: 0; animation: in 0.5s ease-out both; }',
        '  .pulse { animation: blink 2s infinite ease-in-out; }',
        '  @keyframes in { 0% { opacity: 0; transform: translateY(10px); } 100% { opacity: 1; transform: translateY(0); } }',
        '  @keyframes blink { 0%, 100% { opacity: 0.35; } 50% { opacity: 1; } }',
        '  @media (prefers-reduced-motion: reduce) {',
        '    .block { opacity: 1 !important; transform: none !important; animation: none !important; }',
        '    .pulse { animation: none !important; }',
        '  }',
        '</style>',
        '<defs>',
        f'  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">',
        f'    <stop offset="0%" stop-color="{bg2}"/>',
        f'    <stop offset="100%" stop-color="{bg}"/>',
        f'  </linearGradient>',
        '</defs>',
        f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{frame}"/>',
        f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{frame}"/>',
        '<circle cx="20" cy="16" r="5" fill="#ff5f56"/>',
        '<circle cx="36" cy="16" r="5" fill="#ffbd2e"/>',
        '<circle cx="52" cy="16" r="5" fill="#27c93f"/>',
        f'<text x="{W/2}" y="20" fill="{muted}" font-size="12" text-anchor="middle">barani@simats: ~$ ./building-blocks.sh --focus=current_cycle</text>'
    ]

    sb_y = TITLEBAR_H + 16
    parts.append(f'<g class="block" style="animation-delay: 0.05s;">')
    parts.append(f'  <circle cx="26" cy="{sb_y + 8}" r="4" fill="{green_bright}" class="pulse"/>')
    parts.append(f'  <text x="38" y="{sb_y + 12}" fill="{green_bright}" font-size="11" font-weight="700">SYSTEM: ACTIVE</text>')
    parts.append(f'  <circle cx="150" cy="{sb_y + 8}" r="3" fill="{muted}"/>')
    parts.append(f'  <text x="160" y="{sb_y + 12}" fill="{muted}" font-size="11">NODES: 4/4 INITIALIZED</text>')
    parts.append(f'  <circle cx="330" cy="{sb_y + 8}" r="3" fill="{muted}"/>')
    parts.append(f'  <text x="340" y="{sb_y + 12}" fill="{muted}" font-size="11">FOCUS: HEALTHCARE &amp; APPLIED AI</text>')
    parts.append(f'  <text x="{W - PAD}" y="{sb_y + 12}" fill="{cyan}" font-size="11" font-weight="700" text-anchor="end">CYCLE: 2025–PRESENT</text>')
    parts.append('</g>')

    bw = (W - PAD * 2 - 16) / 2
    bh = 175
    by_start = sb_y + 28

    for i, card in enumerate(CARDS):
        r = i // 2
        c = i % 2
        bx = PAD + c * (bw + 16)
        by = by_start + r * (bh + 14)
        delay = 0.12 * (i + 1)

        parts.append(f'<g class="block" style="animation-delay: {delay:.2f}s;">')
        parts.append(f'  <rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="10" fill="{card_bg}" stroke="{frame}"/>')
        parts.append(f'  <text x="{bx + 16}" y="{by + 26}" fill="{muted}" font-size="12" font-weight="700">{card["id"]}</text>')
        parts.append(f'  <text x="{bx + 38}" y="{by + 26}" fill="{text}" font-size="13" font-weight="700">{card["title"]}</text>')

        badge_w = len(card["badge"]) * 6.5 + 24
        badge_x = bx + bw - badge_w - 16
        parts.append(f'  <rect x="{badge_x}" y="{by + 12}" width="{badge_w}" height="20" rx="10" fill="{badge_bg}" stroke="{card["badge_color"]}"/>')
        parts.append(f'  <text x="{badge_x + badge_w/2}" y="{by + 26}" fill="{card["badge_color"]}" font-size="9" font-weight="700" text-anchor="middle">{card["badge"]}</text>')

        parts.append(f'  <line x1="{bx + 16}" y1="{by + 40}" x2="{bx + bw - 16}" y2="{by + 40}" stroke="{frame}"/>')

        for idx, (sym, line) in enumerate(card["lines"]):
            ly = by + 68 + idx * 24
            parts.append(f'  <text x="{bx + 16}" y="{ly}" fill="{card["badge_color"]}" font-size="13" font-weight="700">{sym}</text>')
            parts.append(f'  <text x="{bx + 42}" y="{ly}" fill="{text}" font-size="11">{line}</text>')

        parts.append(f'  <line x1="{bx + 16}" y1="{by + 130}" x2="{bx + bw - 16}" y2="{by + 130}" stroke="{frame}"/>')
        parts.append(f'  <text x="{bx + 16}" y="{by + 150}" fill="{muted}" font-size="10" font-weight="700">{card["metric_label"]}</text>')
        parts.append(f'  <text x="{bx + bw - 16}" y="{by + 150}" fill="{card["badge_color"]}" font-size="11" font-weight="700" text-anchor="end">{card["metric_val"]}</text>')
        parts.append('</g>')

    ft_y = H - PAD - 18
    parts.append(f'<g class="block" style="animation-delay: 0.6s;">')
    parts.append(f'  <line x1="{PAD}" y1="{ft_y - 12}" x2="{W - PAD}" y2="{ft_y - 12}" stroke="{frame}" stroke-dasharray="2,3"/>')
    parts.append(f'  <text x="{PAD}" y="{ft_y + 2}" fill="{muted}" font-size="10">Architecture: <tspan fill="{text}">Clean MVVM · Offline-First · Core Data · Combine</tspan></text>')
    parts.append(f'  <text x="{W - PAD}" y="{ft_y + 2}" fill="{green_bright}" font-size="10" font-weight="700" text-anchor="end">Status: IN PRODUCTION</text>')
    parts.append('</g>')

    parts.append('</svg>')
    return "\n".join(parts)


# ==============================================================================
# 5. GENERATE DUAL-THEME TERMINAL HEADERS SVGs
# ==============================================================================
HEADERS = [
    ("header-about", "👨‍💻 About Me", 205),
    ("header-skills", "🛠️ Technical Skills", 230),
    ("header-aiml", "🧠 AI / ML Expertise", 230),
    ("header-projects", "🚀 Featured Projects", 235),
    ("header-experience", "💼 Work Experience", 235),
    ("header-stats", "📊 GitHub Statistics", 235),
    ("header-achievements", "🏆 Achievements & Recognition", 295),
    ("header-3dgraph", "🧊 3D Isometric Contribution Graph", 355),
    ("header-snake", "🕹️ GitHub Contribution Snake", 305),
    ("header-certs", "⚡ Coding Profiles & Problem Solving", 360),
    ("header-focus", "🎯 Current Focus", 215)
]

def render_header(title, uline_w, mode="dark"):
    is_dark = mode == "dark"
    bg = "#0d1117" if is_dark else "#f6f8fa"
    frame = "#30363d" if is_dark else "#d0d7de"
    text_color = "#e6edf3" if is_dark else "#1f2328"
    prompt_color = "#8B5CF6" if is_dark else "#6c2bd9"
    cursor_color = "#38BDF8" if is_dark else "#0284c7"

    # Escape title XML
    title_escaped = title.replace("&", "&amp;")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="46" viewBox="0 0 860 46">
  <defs>
    <linearGradient id="uGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#8B5CF6"/>
    </linearGradient>
  </defs>
  <style>
    .cursor {{ animation: blink 1s step-start infinite; }}
    @keyframes blink {{ 0%,100%{{opacity:1}} 50%{{opacity:0}} }}
    .uline {{ animation: slideIn 0.7s ease-out both; transform-origin: left center; }}
    @keyframes slideIn {{ from{{transform:scaleX(0)}} to{{transform:scaleX(1)}} }}
    @media (prefers-reduced-motion: reduce) {{ .cursor, .uline {{ animation: none !important; }} }}
  </style>
  <rect width="860" height="46" rx="8" fill="{bg}"/>
  <rect width="860" height="46" rx="8" fill="none" stroke="{frame}" stroke-width="1"/>
  <circle cx="20" cy="20" r="5" fill="#ff5f56"/>
  <circle cx="36" cy="20" r="5" fill="#ffbd2e"/>
  <circle cx="52" cy="20" r="5" fill="#27c93f"/>
  <line x1="68" y1="8" x2="68" y2="38" stroke="{frame}" stroke-width="1"/>
  <text x="76" y="25" fill="{prompt_color}" font-family="'Fira Code','JetBrains Mono','SF Mono',Consolas,monospace" font-size="12">~ $</text>
  <text x="106" y="25" fill="{text_color}" font-family="'Fira Code','JetBrains Mono','SF Mono',Consolas,monospace" font-size="14" font-weight="600">{title_escaped}</text>
  <text x="{106 + uline_w + 8}" y="25" fill="{cursor_color}" font-family="'Fira Code',monospace" font-size="14" class="cursor">&#x25ae;</text>
  <rect x="106" y="39" width="{uline_w}" height="2" rx="1" fill="url(#uGrad)" class="uline"/>
</svg>'''
    return svg


# ==============================================================================
# MAIN EXECUTION: WRITE ALL FILES AND VALIDATE XML
# ==============================================================================
print("1. Rendering dev-system-dark.svg & dev-system-light.svg...")
dev_dark = render_dev_system("dark")
dev_light = render_dev_system("light")
with open(os.path.join(ASSETS_DIR, "dev-system-dark.svg"), "w", encoding="utf-8") as f:
    f.write(dev_dark)
with open(os.path.join(ASSETS_DIR, "dev-system-light.svg"), "w", encoding="utf-8") as f:
    f.write(dev_light)
with open(os.path.join(ASSETS_DIR, "dev-system.svg"), "w", encoding="utf-8") as f:
    f.write(dev_dark)

print("2. Rendering aiml-matrix-dark.svg & aiml-matrix-light.svg...")
aiml_dark = render_aiml_matrix("dark")
aiml_light = render_aiml_matrix("light")
with open(os.path.join(ASSETS_DIR, "aiml-matrix-dark.svg"), "w", encoding="utf-8") as f:
    f.write(aiml_dark)
with open(os.path.join(ASSETS_DIR, "aiml-matrix-light.svg"), "w", encoding="utf-8") as f:
    f.write(aiml_light)
with open(os.path.join(ASSETS_DIR, "aiml-matrix.svg"), "w", encoding="utf-8") as f:
    f.write(aiml_dark)

print("3. Rendering achievements-card-dark.svg & achievements-card-light.svg...")
ach_dark = render_achievements("dark")
ach_light = render_achievements("light")
with open(os.path.join(ASSETS_DIR, "achievements-card-dark.svg"), "w", encoding="utf-8") as f:
    f.write(ach_dark)
with open(os.path.join(ASSETS_DIR, "achievements-card-light.svg"), "w", encoding="utf-8") as f:
    f.write(ach_light)
with open(os.path.join(ASSETS_DIR, "achievements-card.svg"), "w", encoding="utf-8") as f:
    f.write(ach_dark)

print("4. Rendering focus-blocks-dark.svg & focus-blocks-light.svg...")
foc_dark = render_focus_blocks("dark")
foc_light = render_focus_blocks("light")
with open(os.path.join(ASSETS_DIR, "focus-blocks-dark.svg"), "w", encoding="utf-8") as f:
    f.write(foc_dark)
with open(os.path.join(ASSETS_DIR, "focus-blocks-light.svg"), "w", encoding="utf-8") as f:
    f.write(foc_light)
with open(os.path.join(ASSETS_DIR, "focus-blocks.svg"), "w", encoding="utf-8") as f:
    f.write(foc_dark)

print("5. Rendering dual-theme headers...")
for stem, title, uw in HEADERS:
    h_dark = render_header(title, uw, "dark")
    h_light = render_header(title, uw, "light")
    with open(os.path.join(ASSETS_DIR, f"{stem}-dark.svg"), "w", encoding="utf-8") as f:
        f.write(h_dark)
    with open(os.path.join(ASSETS_DIR, f"{stem}-light.svg"), "w", encoding="utf-8") as f:
        f.write(h_light)
    with open(os.path.join(ASSETS_DIR, f"{stem}.svg"), "w", encoding="utf-8") as f:
        f.write(h_dark)

print("6. Validating XML of all generated SVGs...")
all_valid = True
for fname in os.listdir(ASSETS_DIR):
    if fname.endswith(".svg"):
        fpath = os.path.join(ASSETS_DIR, fname)
        try:
            ET.parse(fpath)
        except Exception as e:
            print(f"  ❌ XML ERROR in {fname}: {e}")
            all_valid = False

if all_valid:
    print("  ✅ ALL SVGs are 100% well-formed, valid XML!")

print("Dual theme generation complete.")
