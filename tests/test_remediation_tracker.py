import pytest
import json
from remediation_tracker import RemediationTracker, RemediationTask

def test_add_task():
    tracker = RemediationTracker()
    task = RemediationTask(1, "Task 1")
    tracker.add_task(task)
    assert len(tracker.tasks) == 1
    assert tracker.tasks[0].id == 1
    assert tracker.tasks[0].name == "Task 1"

def test_update_task_status():
    tracker = RemediationTracker()
    task = RemediationTask(1, "Task 1")
    tracker.add_task(task)
    tracker.update_task_status(1, True)
    assert tracker.tasks[0].completion_status
    assert tracker.get_notifications() == ["Task Task 1 completed"]

def test_get_progress():
    tracker = RemediationTracker()
    task1 = RemediationTask(1, "Task 1")
    task2 = RemediationTask(2, "Task 2")
    tracker.add_task(task1)
    tracker.add_task(task2)
    tracker.update_task_status(1, True)
    assert tracker.get_progress() == 0.5

def test_save_to_database():
    tracker = RemediationTracker()
    task = RemediationTask(1, "Task 1")
    tracker.add_task(task)
    data = tracker.save_to_database()
    assert json.loads(data) == [{"id": 1, "name": "Task 1", "completion_status": False}]

def test_load_from_database():
    tracker = RemediationTracker()
    data = '[{"id": 1, "name": "Task 1", "completion_status": true}]'
    tracker.load_from_database(data)
    assert len(tracker.tasks) == 1
    assert tracker.tasks[0].id == 1
    assert tracker.tasks[0].name == "Task 1"
    assert tracker.tasks[0].completion_status
