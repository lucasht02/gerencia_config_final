import os
import json
from src.report import Report

def test_generate():
    data = [1, 2, 3]
    rpt = Report(data)
    assert rpt.generate() == "Report with 3 entries"

def test_export_csv(tmp_path):
    data = [4, 5, 6]
    rpt = Report(data)
    fp = tmp_path / "out.csv"
    rpt.export_csv(str(fp))
    content = fp.read_text().strip()
    assert content == "4,5,6"