---
name: si-browser-agent
description: Configure Browser-Use WebUI with 16k-context local Ollama models and Chrome CDP port 9222 on Windows at $0.00 API cost.
---

# SI-Browser-Agent Skill

1. **Hardware Tier Check**: Run `python si_browser_setup.py --vram <GB>` to select the optimal model (`qwen2.5:7b` for 6-8GB VRAM, `qwen2.5:14b` for 12GB+ VRAM, or free Gemini Flash for 4GB laptops).
2. **Context Expansion**: Always build the 16,384-token Ollama Modelfile (`ollama create qwen-agent-16k -f Modelfile.agent16k`) before starting WebUI.
3. **Persistent CDP Session**: Launch Chrome with `--remote-debugging-port=9222` and a separate `--user-data-dir` so login cookies persist safely.
