import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd
from src.data_validation import validate
from src.data_processing import transform

def test_validation_removes_invalid_rows():
    df = pd.DataFrame({
        "date":["2026-01-01","2026-01-01"],
        "city":["Test","Test"],
        "state":["X","X"],
        "temperature_c":[25,25],
        "humidity_pct":[50,120],
        "wind_speed_kmh":[10,10],
        "precipitation_mm":[0,0],
        "condition":["Clear","Clear"]
    })
    result = validate(df)
    assert len(result) == 1

def test_transform_adds_analytics_columns():
    df = pd.DataFrame({
        "date":["2026-01-01"], "city":["Test"], "state":["X"],
        "temperature_c":[25], "humidity_pct":[50],
        "wind_speed_kmh":[10], "precipitation_mm":[0],
        "condition":["Clear"]
    })
    result = transform(validate(df))
    assert "temperature_f" in result.columns
    assert "year" in result.columns
    assert result.iloc[0]["temperature_f"] == 77
