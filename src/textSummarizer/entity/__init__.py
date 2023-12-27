from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig: #from config.yaml file the value is the variable while the key is the output format type
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

#from the above code whenever root_dir or any of the mentioned variables will be called it will return the assigned path as per the config.yaml file