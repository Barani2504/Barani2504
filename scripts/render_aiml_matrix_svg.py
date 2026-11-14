#!/usr/bin/env python3
"""
Render Barani S's AI / ML Expertise as a high-tech terminal matrix SVG card
with animated glowing progress bars, dots ratings, and telemetry details.

Preserves 100% of the original content:
- On-Device Inference (●●●●○, 80%): Core ML & TensorFlow Lite deployment for offline, private, real-time predictions on iOS
- Computer Vision (●●●●○, 80%): YOLOv8-based detection pipeline for medical CT image analysis (kidney stone detection)
- RAG Systems (●●●○○, 60%): Retrieval-Augmented Generation for code assistant & multi-language platform support
- AI Chatbot Development (●●●●○, 80%): Conversational health-monitoring chatbot with real-time vitals context
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "assets", "aiml-matrix.svg")

W, H = 860, 390
PAD = 20
TITLEBAR_H = 32

BG = "#090d16"
BG2 = "#111722"
CARD_BG = "#131922"
FRAME = "#30363d"
MUTED = "#7d8590"
TEXT = "#e6edf3"
CYAN = "#38bdf8"
VIOLET = "#8b5cf6"
GREEN = "#059669"
GREEN_BRIGHT = "#39d353"
AMBER = "#f59e0b"

DOMAINS = [
    {
        "title": "On-Device Inference",
        "badge": "CORE ML · TFLITE",
        "rating_dots": "●●●●○",
        "pct": 80,
        "color": CYAN,
        "desc": "Core ML & TensorFlow Lite deployment for offline, private, real-time predictions on iOS",
        "delay": "0.15s"
    },
    {
        "title": "Computer Vision",
        "badge": "YOLOV8 · RADIOLOGY CT",
        "rating_dots": "●●●●○",
        "pct": 80,
        "color": VIOLET,
        "desc": "YOLOv8-based detection pipeline for medical CT image analysis (kidney stone detection)",
        "delay": "0.25s"
    },
    {
        "title": "RAG Systems",
        "badge": "CODEGO COMPILER · RETRIEVAL",
        "rating_dots": "●●●○○",
        "pct": 60,
        "color": AMBER,
        "desc": "Retrieval-Augmented Generation for code assistant & multi-language platform support",
        "delay": "0.35s"
    },
    {
        "title": "AI Chatbot Development",
        "badge": "CORECARE · CONVERSATIONAL",
        "rating_dots": "●●●●○",
        "pct": 80,
        "color": GREEN_BRIGHT,
        "desc": "Conversational health-monitoring chatbot with real-time vitals context",
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
    f'    <stop offset="0%" stop-color="{BG2}"/>',
    f'    <stop offset="100%" stop-color="{BG}"/>',
    f'  </linearGradient>',
    '</defs>',
    # Window Shell
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
    # Traffic lights
    '<circle cx="20" cy="16" r="5" fill="#ff5f56"/>',
    '<circle cx="36" cy="16" r="5" fill="#ffbd2e"/>',
    '<circle cx="52" cy="16" r="5" fill="#27c93f"/>',
    f'<text x="{W/2}" y="20" fill="{MUTED}" font-size="12" text-anchor="middle">barani@simats: ~$ ./ai_engine.py --precision=fp16 --target=AppleNeuralEngine</text>',
    # Sub-header Status Ribbon
    f'<g class="card" style="animation-delay: 0.05s;">',
    f'  <circle cx="26" cy="52" r="4" fill="{GREEN_BRIGHT}" class="pulse"/>',
    f'  <text x="36" y="56" fill="{GREEN_BRIGHT}" font-size="11" font-weight="700">NEURAL ENGINE: ACTIVE</text>',
    f'  <text x="210" y="56" fill="{MUTED}" font-size="11">● RUNTIME: CORE ML &amp; TFLITE</text>',
    f'  <text x="440" y="56" fill="{MUTED}" font-size="11">● ZERO CLOUD LATENCY (OFFLINE)</text>',
    f'  <text x="{W-24}" y="56" fill="{CYAN}" font-size="11" text-anchor="end">VISION &amp; RAG SUITE</text>',
    f'  <line x1="20" y1="68" x2="{W-20}" y2="68" stroke="#21262d" stroke-dasharray="3,3"/>',
    f'</g>',
]

# Corner HUD Accents
parts.append(f'<path d="M 22 44 L 32 44 M 22 44 L 22 54" stroke="{CYAN}" stroke-width="1.5" fill="none" opacity="0.4"/>')
parts.append(f'<path d="M {W-22} 44 L {W-32} 44 M {W-22} 44 L {W-22} 54" stroke="{CYAN}" stroke-width="1.5" fill="none" opacity="0.4"/>')

# Render 4 domain rows
row_y_start = 82
row_h = 68
gap = 8

for i, d in enumerate(DOMAINS):
    ry = row_y_start + i * (row_h + gap)
    anim_cls = "bar-grow-80" if d["pct"] == 80 else "bar-grow-60"
    bar_width = int(220 * (d["pct"] / 100))

    parts.append(f'<g class="card" style="animation-delay: {d["delay"]};">')
    # Card background
    parts.append(f'  <rect x="20" y="{ry}" width="{W-40}" height="{row_h}" rx="8" fill="{CARD_BG}" stroke="{FRAME}"/>')
    
    # Title & Badge
    parts.append(f'  <text x="36" y="{ry + 26}" fill="{TEXT}" font-size="14" font-weight="700">{d["title"]}</text>')
    
    # Badge Pill
    badge_x = 240
    parts.append(f'  <rect x="{badge_x}" y="{ry + 13}" width="165" height="18" rx="9" fill="{d["color"]}18" stroke="{d["color"]}55"/>')
    parts.append(f'  <text x="{badge_x + 82}" y="{ry + 26}" fill="{d["color"]}" font-size="9.5" font-weight="600" text-anchor="middle">{d["badge"]}</text>')

    # Dots + Progress Bar on the Right
    right_zone_x = W - 320
    parts.append(f'  <text x="{right_zone_x}" y="{ry + 26}" fill="{MUTED}" font-size="12">Rating: <tspan fill="{d["color"]}" font-weight="700">{d["rating_dots"]}</tspan> ({d["pct"]}%)</text>')
    
    # Progress Track & Fill
    bar_x = right_zone_x + 135
    bar_y = ry + 18
    parts.append(f'  <rect x="{bar_x}" y="{bar_y}" width="120" height="9" rx="4.5" fill="#21262d"/>')
    parts.append(f'  <rect class="{anim_cls}" x="{bar_x}" y="{bar_y}" width="{int(120 * d["pct"] / 100)}" height="9" rx="4.5" fill="{d["color"]}"/>')
    
    # Description
    parts.append(f'  <text x="36" y="{ry + 50}" fill="{MUTED}" font-size="11">{d["desc"]}</text>')
    parts.append('</g>')

parts.append('</svg>')

svg = "\n".join(parts)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Generated {OUT}: {W}x{H}, {len(svg)} bytes")
