import pytest
from diagnostics import create_diagnostics, Feedback

def test_provide_feedback():
    diagnostics = create_diagnostics()
    feedback = Feedback(5, "Great experience!")
    assert diagnostics.provide_feedback(feedback) == "Thank you for your feedback!"

def test_store_feedback():
    diagnostics = create_diagnostics()
    feedback = {"rating": 4, "comment": "Good experience"}
    assert diagnostics.store_feedback(feedback) == "Feedback stored successfully"

def test_get_feedback():
    diagnostics = create_diagnostics()
    feedback = Feedback(5, "Great experience!")
    diagnostics.provide_feedback(feedback)
    assert diagnostics.get_feedback() == [{"rating": 5, "comment": "Great experience!"}]

def test_review_workflow():
    diagnostics = create_diagnostics()
    feedback = {"rating": 2, "comment": "Bad experience"}
    assert diagnostics.review_workflow(feedback) == "Review workflow triggered"

def test_review_workflow_no_trigger():
    diagnostics = create_diagnostics()
    feedback = {"rating": 4, "comment": "Good experience"}
    assert diagnostics.review_workflow(feedback) == "No review workflow triggered"

def test_edge_case_provide_feedback():
    diagnostics = create_diagnostics()
    with pytest.raises(ValueError):
        Feedback(-1, "Invalid rating")
