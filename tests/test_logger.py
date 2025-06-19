from src.logger import Logger

def test_log_info(capsys):
    log = Logger("Test")
    log.log_info("msg")
    captured = capsys.readouterr()
    assert "[INFO] Test: msg" in captured.out

def test_log_error(capsys):
    log = Logger("Test")
    log.log_error("erro")
    captured = capsys.readouterr()
    assert "[ERROR] Test: erro" in captured.out