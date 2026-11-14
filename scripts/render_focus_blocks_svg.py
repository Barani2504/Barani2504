#!/usr/bin/env python3
"""
Render Barani S's Current Focus as a 2x2 terminal-window building blocks SVG.
Directly inspired by kaushalboii's building-blocks.svg.

Preserves 100% of the YAML content:
learning:
  - Advanced Swift Concurrency & SwiftData
  - On-Device LLM & Vision Transformer Optimization
building:
  - Production AI-integrated healthcare & diagnostic iOS apps
  - RAG-powered developer compilation & mentorship tooling
exploring:
  - Cross-platform AI feature parity (iOS + Android)
  - Edge deployment of computer vision models (Core ML & YOLOv8)
open_to:
  - Native iOS Developer / Mobile Engineer roles
  - AI/ML-driven mobile engineering collaborations
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "assets", "focus-blocks.svg")

W, H = 860, 530

BG = "#090d16"
BG2 = "#111722"
FRAME = "#30363d"
MUTED = "#7d8590"
TEXT = "#e6edf3"
CYAN = "#38bdf8"
VIOLET = "#8b5cf6"
GREEN_BRIGHT = "#39d353"
AMBER = "#f59e0b"

CARDS = [
    {
        "id": "01",
        "title": "LEARNING",
        "badge": "CONCURRENCY · TRANSFORMERS",
        "badge_color": CYAN,
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
        "badge_color": GREEN_BRIGHT,
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
        "badge_color": VIOLET,
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
        "badge_color": AMBER,
        "lines": [
            ("├──", "Native iOS Developer / Mobile Engineer roles"),
            ("└──", "AI/ML-driven mobile engineering collaborations")
        ],
        "metric_label": "AVAILABILITY",
        "metric_val": "Open to Opportunities"
    }
]

svg_parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    f'font-family="\'Fira Code\', \'JetBrains Mono\', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    '<defs>',
    f'  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">',
    f'    <stop offset="0%" stop-color="{BG2}"/>',
    f'    <stop offset="100%" stop-color="{BG}"/>',
    f'  </linearGradient>',
    '  <linearGradient id="card-grad" x1="0" y1="0" x2="0" y2="1">',
    '    <stop offset="0%" stop-color="#161b22"/>',
    '    <stop offset="100%" stop-color="#0d1117"/>',
    '  </linearGradient>',
    '</defs>',
    '<style>',
    '  .card { opacity: 0; animation: in 0.45s ease-out both; }',
    '  .pulse { animation: blink 2s infinite ease-in-out; }',
    '  @keyframes in {',
    '    0% { opacity: 0; transform: translateY(14px); }',
    '    100% { opacity: 1; transform: translateY(0); }',
    '  }',
    '  @keyframes blink {',
    '    0%, 100% { opacity: 0.35; }',
    '    50% { opacity: 1; }',
    '  }',
    '  @media (prefers-reduced-motion: reduce) {',
    '    .card, .pulse { animation: none !important; opacity: 1 !important; transform: none !important; }',
    '  }',
    '</style>',
    # Terminal Window Background
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}" stroke-width="1"/>',
    # Titlebar
    f'<line x1="0" y1="32" x2="{W}" y2="32" stroke="{FRAME}"/>',
    '<circle cx="20" cy="16" r="5" fill="#ff5f56"/>',
    '<circle cx="36" cy="16" r="5" fill="#ffbd2e"/>',
    '<circle cx="52" cy="16" r="5" fill="#27c93f"/>',
    f'<text x="{W/2}" y="20" fill="{MUTED}" font-size="12" text-anchor="middle">barani@simats: ~$ ./building-blocks.sh --focus=current_cycle</text>',
    # Sub-header status ribbon
    f'<g class="card" style="animation-delay: 0.05s;">',
    f'  <circle cx="26" cy="53" r="4" fill="{GREEN_BRIGHT}" class="pulse"/>',
    f'  <text x="36" y="57" fill="{GREEN_BRIGHT}" font-size="11" font-weight="700">SYSTEM: ACTIVE</text>',
    f'  <text x="160" y="57" fill="{MUTED}" font-size="11">● NODES: 4/4 INITIALIZED</text>',
    f'  <text x="350" y="57" fill="{MUTED}" font-size="11">● FOCUS: HEALTHCARE &amp; APPLIED AI</text>',
    f'  <text x="{W-24}" y="57" fill="{CYAN}" font-size="11" text-anchor="end">CYCLE: 2025–PRESENT</text>',
    f'  <line x1="20" y1="68" x2="{W-20}" y2="68" stroke="#21262d" stroke-dasharray="3,3"/>',
    f'</g>',
]

# Corner HUD Accents
svg_parts.append(f'<path d="M 22 44 L 32 44 M 22 44 L 22 54" stroke="{CYAN}" stroke-width="1.5" fill="none" opacity="0.4"/>')
svg_parts.append(f'<path d="M {W-22} 44 L {W-32} 44 M {W-22} 44 L {W-22} 54" stroke="{CYAN}" stroke-width="1.5" fill="none" opacity="0.4"/>')

# Render Cards (2 x 2 grid)
card_w = 398
card_h = 178
start_x = 22
start_y = 80
gap_x = 20
gap_y = 16
delays = [0.15, 0.25, 0.35, 0.45]

for i, c in enumerate(CARDS):
    col = i % 2
    row = i // 2
    cx = start_x + col * (card_w + gap_x)
    cy = start_y + row * (card_h + gap_y)
    delay = delays[i]

    svg_parts.append(f'<g class="card" style="animation-delay: {delay}s;">')
    svg_parts.append(f'  <rect x="{cx}" y="{cy}" width="{card_w}" height="{card_h}" rx="10" fill="url(#card-grad)" stroke="{FRAME}"/>')
    
    # ID + Title
    svg_parts.append(f'  <text x="{cx + 18}" y="{cy + 28}" fill="{MUTED}" font-size="12" font-weight="700">{c["id"]}</text>')
    svg_parts.append(f'  <text x="{cx + 42}" y="{cy + 28}" fill="{TEXT}" font-size="13" font-weight="700" letter-spacing="0.5">{c["title"]}</text>')
    
    # Badge Pill
    badge_w = len(c["badge"]) * 7.2 + 16
    badge_x = cx + card_w - badge_w - 18
    svg_parts.append(f'  <rect x="{badge_x}" y="{cy + 14}" width="{badge_w}" height="18" rx="9" fill="{c["badge_color"]}1a" stroke="{c["badge_color"]}55"/>')
    svg_parts.append(f'  <text x="{badge_x + badge_w/2}" y="{cy + 27}" fill="{c["badge_color"]}" font-size="9" font-weight="700" text-anchor="middle">{c["badge"]}</text>')
    
    # Divider
    svg_parts.append(f'  <line x1="{cx + 18}" y1="{cy + 42}" x2="{cx + card_w - 18}" y2="{cy + 42}" stroke="#21262d"/>')
    
    # Lines
    for j, (glyph, text_val) in enumerate(c["lines"]):
        ly = cy + 68 + j * 24
        svg_parts.append(f'  <text x="{cx + 18}" y="{ly}" fill="{c["badge_color"]}" font-size="11" font-weight="700">{glyph}</text>')
        svg_parts.append(f'  <text x="{cx + 44}" y="{ly}" fill="{TEXT}" font-size="11">{text_val}</text>')
        
    # Card Metric Footer
    svg_parts.append(f'  <line x1="{cx + 18}" y1="{cy + card_h - 38}" x2="{cx + card_w - 18}" y2="{cy + card_h - 38}" stroke="#21262d"/>')
    svg_parts.append(f'  <text x="{cx + 18}" y="{cy + card_h - 18}" fill="{MUTED}" font-size="10" font-weight="700" letter-spacing="0.8">{c["metric_label"]}</text>')
    svg_parts.append(f'  <text x="{cx + card_w - 18}" y="{cy + card_h - 18}" fill="{c["badge_color"]}" font-size="11" font-weight="700" text-anchor="end">{c["metric_val"]}</text>')
    svg_parts.append('</g>')

# Footer status
svg_parts.append(f'<g class="card" style="animation-delay: 0.55s;">')
svg_parts.append(f'  <line x1="22" y1="{H - 42}" x2="{W - 22}" y2="{H - 42}" stroke="{FRAME}" stroke-dasharray="2,2"/>')
svg_parts.append(f'  <text x="24" y="{H - 18}" fill="{MUTED}" font-size="11">Architecture: <tspan fill="{TEXT}">Clean MVVM · Offline-First · Core Data · Combine</tspan></text>')
svg_parts.append(f'  <text x="{W - 24}" y="{H - 18}" fill="{GREEN_BRIGHT}" font-size="11" text-anchor="end">Status: IN PRODUCTION</text>')
svg_parts.append('</g>')

svg_parts.append('</svg>')

svg = "\n".join(svg_parts)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Generated {OUT}: {W}x{H}, {len(svg)} bytes")
