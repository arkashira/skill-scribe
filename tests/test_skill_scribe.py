import pytest
from skill_scribe import SkillScribe

def test_add_skill():
    scribe = SkillScribe()
    scribe.add_skill("python")
    assert scribe.get_skill("python").level == 1
    assert scribe.get_skill("python").progress == 0.0

def test_update_skill():
    scribe = SkillScribe()
    scribe.add_skill("python")
    scribe.update_skill("python", level=2, progress=0.5)
    assert scribe.get_skill("python").level == 2
    assert scribe.get_skill("python").progress == 0.5

def test_get_skill():
    scribe = SkillScribe()
    scribe.add_skill("python")
    assert scribe.get_skill("python").level == 1
    assert scribe.get_skill("python").progress == 0.0

def test_get_dashboard():
    scribe = SkillScribe()
    scribe.add_skill("python")
    dashboard = scribe.get_dashboard("python")
    assert dashboard["level"] == 1
    assert dashboard["progress"] == 0.0
    assert dashboard["kpis"] == {}

def test_update_dashboard():
    scribe = SkillScribe()
    scribe.add_skill("python")
    dashboard = scribe.update_dashboard("python", 50, "new input")
    assert dashboard["level"] == 1
    assert dashboard["progress"] == 0.5
    assert dashboard["kpis"] == {"exercises_completed": 50, "new_input": "new input"}

def test_update_dashboard_level_up():
    scribe = SkillScribe()
    scribe.add_skill("python")
    dashboard = scribe.update_dashboard("python", 100, "new input")
    assert dashboard["level"] == 2
    assert dashboard["progress"] == 0.0
    assert dashboard["kpis"] == {"exercises_completed": 100, "new_input": "new input"}

def test_get_skill_not_found():
    scribe = SkillScribe()
    with pytest.raises(ValueError):
        scribe.get_skill("java")

def test_update_skill_not_found():
    scribe = SkillScribe()
    with pytest.raises(ValueError):
        scribe.update_skill("java", level=2)

def test_get_dashboard_not_found():
    scribe = SkillScribe()
    with pytest.raises(ValueError):
        scribe.get_dashboard("java")

def test_update_dashboard_not_found():
    scribe = SkillScribe()
    with pytest.raises(ValueError):
        scribe.update_dashboard("java", 50, "new input")
