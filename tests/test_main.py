import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import apply_filter, aggregate, parse_condition


sample_data = [
    {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
    {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
    {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    {"name": "poco x5 pro", "brand": "xiaomi", "price": "299", "rating": "4.4"},
]

def test_filter_greater_than():
    result = apply_filter(sample_data, "rating>4.7")
    assert len(result) == 2
    assert result[0]["name"] == "iphone 15 pro"

def test_filter_equals():
    result = apply_filter(sample_data, "brand=apple")
    assert len(result) == 1
    assert result[0]["price"] == "999"

def test_filter_less_than():
    result = apply_filter(sample_data, "price<500")
    assert len(result) == 2
    assert result[0]["brand"] == "xiaomi"

def test_invalid_condition():
    with pytest.raises(ValueError):
        parse_condition("rating~4.5")

def test_aggregate_avg():
    result = aggregate(sample_data, "rating=avg")
    assert result[0]["avg"] == pytest.approx(4.675, rel=1e-2)

def test_aggregate_min():
    result = aggregate(sample_data, "price=min")
    assert result[0]["min"] == 199.0

def test_aggregate_max():
    result = aggregate(sample_data, "price=max")
    assert result[0]["max"] == 1199.0

def test_aggregate_empty():
    result = aggregate([], "rating=avg")
    assert "avg" in result[0]
    assert result[0]["avg"] == "no valid values"
