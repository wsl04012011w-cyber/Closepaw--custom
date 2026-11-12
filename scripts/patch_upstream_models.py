import json
from pathlib import Path

path = Path("upstream/app/src/main/assets/llm_models.json")
models = json.loads(path.read_text(encoding="utf-8"))

# Keep the existing selection key so installations that saved gpt-5.2-codex
# continue selecting the same entry, but point it at the Free-tier Codex model.
models["gpt-5.2-codex"] = {
    "display_name": "GPT-5.6 Terra (ChatGPT sign-in)",
    "provider": "OPENAI_CODEX",
    "api": "response",
    "model_id": "gpt-5.6-terra"
}

# Remove other outdated ChatGPT-sign-in model entries from the picker.
for key in ("gpt-5.4-codex", "gpt-5.5-codex"):
    models.pop(key, None)

path.write_text(
    json.dumps(models, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8"
)
print("Applied ChatGPT Free Codex model mapping: gpt-5.2-codex -> gpt-5.6-terra")
