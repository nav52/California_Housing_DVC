from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    raw_data_URL: str
    tar_filepath: Path
    untar_filepath: Path
    prepared_datapath: Path

@dataclass(frozen=True)
class DataProcessConfig:
    root_dir: Path
    data_filepath: Path
    scaled_pickle_file: Path