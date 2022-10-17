from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    raw_data_URL: str
    tar_filepath: Path
    untar_filepath: Path
    prepared_datapath: Path