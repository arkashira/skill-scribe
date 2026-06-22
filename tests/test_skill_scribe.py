import pytest
from skill_scribe import SkillScribe, SkillGap, Resource

def test_get_roadmap():
    code_gaps = ["python", "javascript"]
    skill_scribe = SkillScribe(code_gaps)
    roadmap = skill_scribe.get_roadmap()
    assert len(roadmap) == 2
    assert len(roadmap[0].resources) == 5
    assert len(roadmap[1].resources) == 5

def test_update_roadmap():
    code_gaps = ["python", "javascript"]
    skill_scribe = SkillScribe(code_gaps)
    new_code_gaps = ["java", "c++"]
    updated_roadmap = skill_scribe.update_roadmap(new_code_gaps)
    assert len(updated_roadmap) == 2
    assert len(updated_roadmap[0].resources) == 5
    assert len(updated_roadmap[1].resources) == 5

def test_get_roadmap_empty_code_gaps():
    code_gaps = []
    skill_scribe = SkillScribe(code_gaps)
    roadmap = skill_scribe.get_roadmap()
    assert len(roadmap) == 0

def test_update_roadmap_empty_code_gaps():
    code_gaps = ["python", "javascript"]
    skill_scribe = SkillScribe(code_gaps)
    new_code_gaps = []
    updated_roadmap = skill_scribe.update_roadmap(new_code_gaps)
    assert len(updated_roadmap) == 0
