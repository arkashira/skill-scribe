import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Feedback:
    rating: int
    comment: str

    def __post_init__(self):
        if self.rating < 1 or self.rating > 5:
            raise ValueError("Rating must be between 1 and 5")

class Diagnostics:
    def __init__(self):
        self.feedback_form = {}
        self.feedback_storage = []

    def provide_feedback(self, feedback: Feedback):
        self.feedback_storage.append(feedback.__dict__)
        return "Thank you for your feedback!"

    def store_feedback(self, feedback: Dict):
        self.feedback_storage.append(feedback)
        return "Feedback stored successfully"

    def get_feedback(self):
        return self.feedback_storage

    def review_workflow(self, feedback: Dict):
        # Simulate review workflow
        if feedback["rating"] < 3:
            return "Review workflow triggered"
        return "No review workflow triggered"

def create_diagnostics():
    return Diagnostics()
