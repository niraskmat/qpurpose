import pytest
from app.schemas import TaskUpdate
from datetime import datetime


def test_parse_dates_accepts_valid_formats():
    inputs = [
        {"title": "Task 1", "start_date": "2023-05-01"},
        {"title": "Task 2", "start_date": "2023/05/01"},
        {"title": "Task 3", "start_date": "01-05-2023"},
        {"title": "Task 4", "start_date": "01/05/2023"},
        {"title": "Task 5", "start_date": "2023-05-01T19:04:19.286Z"}
    ]
    for input_data in inputs:
        task = TaskUpdate(**input_data)
        assert isinstance(task.start_date, datetime)
        assert task.start_date.day == 1
        assert task.start_date.month == 5
        assert task.start_date.year == 2023

def test_parse_dates_handles_missing_fields():
    task = TaskUpdate(title="No dates here")
    assert task.start_date is None
    assert task.due_date is None

def test_parse_dates_allows_datetime_objects():
    dt = datetime(2023, 5, 1)
    task = TaskUpdate(title="Datetime input", start_date=dt)
    assert task.start_date == dt

def test_validator_receives_model_instance_for_non_dict():
    result = TaskUpdate.parse_dates(TaskUpdate(title="foo"))
    assert result == TaskUpdate(title="foo")
