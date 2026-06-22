import json
from dataclasses import dataclass
from typing import List

@dataclass
class Resource:
    name: str
    difficulty: str
    estimated_time: int
    url: str

@dataclass
class SkillGap:
    name: str
    resources: List[Resource]

class SkillScribe:
    def __init__(self, code_gaps: List[str]):
        self.code_gaps = code_gaps
        self.resources = self.load_resources()

    def load_resources(self) -> List[Resource]:
        # Simulate loading resources from a public API
        resources = [
            Resource("Python Basics", "easy", 2, "https://example.com/python-basics"),
            Resource("Python Advanced", "hard", 5, "https://example.com/python-advanced"),
            Resource("JavaScript Basics", "easy", 3, "https://example.com/javascript-basics"),
            Resource("JavaScript Advanced", "hard", 6, "https://example.com/javascript-advanced"),
            Resource("Data Structures", "medium", 4, "https://example.com/data-structures"),
            Resource("Algorithms", "hard", 7, "https://example.com/algorithms"),
            Resource("Web Development", "easy", 2, "https://example.com/web-development"),
            Resource("Machine Learning", "hard", 8, "https://example.com/machine-learning"),
            Resource("Database Systems", "medium", 5, "https://example.com/database-systems"),
            Resource("Computer Networks", "hard", 6, "https://example.com/computer-networks"),
        ]
        return resources

    def get_roadmap(self) -> List[SkillGap]:
        roadmap = []
        for gap in self.code_gaps:
            resources = [resource for resource in self.resources if resource.name.lower().find(gap.lower()) != -1]
            if len(resources) < 5:
                # Add more resources to fill the gap
                resources += [resource for resource in self.resources if resource.name.lower().find(gap.lower()) == -1][:5-len(resources)]
            roadmap.append(SkillGap(gap, resources[:5]))
        return roadmap

    def update_roadmap(self, new_code_gaps: List[str]) -> List[SkillGap]:
        self.code_gaps = new_code_gaps
        return self.get_roadmap()
