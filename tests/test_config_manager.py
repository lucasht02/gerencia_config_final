import json
from src.config_manager import ConfigManager

def test_load_and_save(tmp_path):
    cfg_file = tmp_path / "cfg.json"
    sample = {"x": 1, "y": 2}
    cfg_file.write_text(json.dumps(sample))
    mgr = ConfigManager(str(cfg_file))
    loaded = mgr.load()
    assert loaded == sample
    mgr.config["z"] = 3
    mgr.save()
    reloaded = json.loads(cfg_file.read_text())
    assert reloaded["z"] == 3