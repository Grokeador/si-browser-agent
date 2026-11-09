import tempfile
import unittest
from pathlib import Path
import si_browser_setup as m


class TestSiBrowser(unittest.TestCase):
    def test_vram_recommendations(self):
        self.assertEqual(m.recommend_model_for_vram(16)["base_model"], "qwen2.5:14b")
        self.assertEqual(m.recommend_model_for_vram(8)["base_model"], "qwen2.5:7b")
        self.assertEqual(m.recommend_model_for_vram(4)["provider"], "google")

    def test_modelfile_contains_16k_context(self):
        mf = m.generate_ollama_modelfile("qwen2.5:7b", 16384)
        self.assertIn("FROM qwen2.5:7b", mf)
        self.assertIn("PARAMETER num_ctx 16384", mf)

    def test_env_generation(self):
        env = m.generate_browser_use_env(12, 9222)
        self.assertIn("OLLAMA_NUM_CTX=16384", env)
        self.assertIn("KEEP_BROWSER_OPEN=true", env)
        self.assertIn("http://localhost:9222", env)

    def test_chrome_bat_contains_port_and_profile(self):
        bat = m.generate_chrome_cdp_bat("C:/AgentProfile", 9222)
        self.assertIn("--remote-debugging-port=9222", bat)
        self.assertIn("C:/AgentProfile", bat)

    def test_cli_writes_all_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            rc = m.main(["--vram", "12", "--out-dir", tmp])
            self.assertEqual(rc, 0)
            self.assertTrue((Path(tmp) / ".env.example").exists())
            self.assertTrue((Path(tmp) / "Modelfile.agent16k").exists())
            self.assertTrue((Path(tmp) / "launch_agent_chrome.bat").exists())


if __name__ == "__main__":
    unittest.main()
