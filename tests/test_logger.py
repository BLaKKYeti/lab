import pytest

from core.logger import Logger


def test_logger_import():
    assert Logger is not None


def test_default_level_is_info():
    logger = Logger()
    assert logger.level == "info"


def test_invalid_level_raises():
    with pytest.raises(ValueError):
        Logger(level="trace")


def test_debug_filtered_at_default_level(capsys):
    logger = Logger()
    logger.debug("detail")
    assert logger.records == []
    assert capsys.readouterr().out == ""


def test_info_recorded_at_default_level():
    logger = Logger()
    logger.info("started")
    record = logger.records[-1]
    assert record["level"] == "info"
    assert record["message"] == "started"
    assert record["timestamp"]


def test_level_filter_respects_configured_threshold(capsys):
    logger = Logger(level="error")
    logger.warning("skipped")
    logger.error("fatal")
    assert [record["level"] for record in logger.records] == ["error"]


def test_debug_enabled_when_level_is_debug(capsys):
    logger = Logger(level="debug")
    logger.debug("trace detail")
    assert logger.records[-1]["level"] == "debug"
    assert "DEBUG trace detail" in capsys.readouterr().out


def test_context_is_captured():
    logger = Logger()
    logger.info("executed", plugin="time", action="current_time")
    assert logger.records[-1]["context"] == {
        "plugin": "time",
        "action": "current_time",
    }


def test_stdout_format(capsys):
    logger = Logger(level="debug")
    logger.warning("low disk")
    out = capsys.readouterr().out
    assert "WARNING low disk" in out


def test_file_output(tmp_path):
    output = tmp_path / "axis.log"
    logger = Logger(output=str(output))
    logger.info("boot", plugins=["time", "filesystem"])
    content = output.read_text(encoding="utf-8")
    assert "INFO boot" in content
    assert "plugins" in content


def test_file_output_appends(tmp_path):
    output = tmp_path / "axis.log"
    logger = Logger(output=str(output))
    logger.info("first")
    logger.error("second")
    content = output.read_text(encoding="utf-8")
    assert content.count("INFO first") == 1
    assert content.count("ERROR second") == 1


def test_clear_empties_records():
    logger = Logger()
    logger.info("one")
    logger.clear()
    assert logger.records == []
