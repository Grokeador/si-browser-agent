# SI-Browser-Agent: Browser-Use + Local Ollama 16k Setup Kit for Windows

**Created by [SI NEWS](https://www.youtube.com/channel/UC4m6veQiZdc_pAfxKQluRgA) • Official companion repo for *"Browser Use and Local AI: Automate Any Web Task on Your PC with Zero API Cost"*.**

Why do local Ollama models get stuck in click loops inside Browser-Use? Because Ollama defaults to a **2,048-token context window**, which truncates the numbered DOM element list!

`si-browser-agent` fixes that in one command on Windows 10/11:
1. **Generates a 16k/32k Context Ollama Modelfile** (`qwen2.5-agent-16k`) with `temperature 0.1` so DOM bounding-box indices (`[1]`, `[2]`, `[3]`) never truncate.
2. **Generates a Zero-API `.env` file** pre-configured for local Ollama (`http://localhost:11434`) or the free Gemini Flash fallback tier.
3. **Creates an Isolated Chrome CDP Launcher (`launch_agent_chrome.bat`)** on port `9222` so your agent can automate tasks inside a dedicated logged-in profile without touching your personal browser tabs.

## Quick Start (Windows PowerShell)
```powershell
git clone https://github.com/Grokeador/si-browser-agent
cd si-browser-agent
python -m unittest discover -s tests -v
python si_browser_setup.py --vram 12 --out-dir .
```

MIT Licensed — Built by [SI NEWS](https://www.youtube.com/channel/UC4m6veQiZdc_pAfxKQluRgA).
