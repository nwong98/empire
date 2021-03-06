[
  {
    "reader": "excel",
    "path": "Data handler/europe_v50/Storage.xlsx",
    "reader_config": {
      "sheet_name": "InitialPowerCapacity",
      "skiprows": 2,
      "usecols": "A:D"
    },
    "group_by_cols": ["Nodes", "StorageTypes", "Period"],
    "agg_col": "InitialPowerCapacity",
    "agg_strat": "sum"
  },
  {
    "reader": "csv",
    "path": "Data handler/europe_v50/ScenarioData/electricload.csv"
  }
]