import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class SkillScore:
    level: int
    progress: float
    kpis: dict

class SkillScribe:
    def __init__(self):
        self.skills = {}

    def add_skill(self, name, level=1, progress=0.0):
        self.skills[name] = SkillScore(level, progress, {})

    def update_skill(self, name, level=None, progress=None, kpis=None):
        if name not in self.skills:
            raise ValueError("Skill not found")
        if level is not None:
            self.skills[name].level = level
        if progress is not None:
            self.skills[name].progress = progress
        if kpis is not None:
            self.skills[name].kpis = kpis

    def get_skill(self, name):
        if name not in self.skills:
            raise ValueError("Skill not found")
        return self.skills[name]

    def get_dashboard(self, name):
        skill = self.get_skill(name)
        return {
            "level": skill.level,
            "progress": skill.progress,
            "kpis": skill.kpis
        }

    def update_dashboard(self, name, exercises_completed, new_input):
        skill = self.get_skill(name)
        skill.progress += exercises_completed / 100
        skill.kpis["exercises_completed"] = exercises_completed
        skill.kpis["new_input"] = new_input
        if skill.progress >= 1.0:
            skill.level += 1
            skill.progress = 0.0
        return self.get_dashboard(name)
