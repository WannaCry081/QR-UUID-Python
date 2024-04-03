import os
from pathlib import Path
from datetime import datetime
from src import uuid_generator, qr_generator


def main():
    try:
        uuid=uuid_generator()
        
        base_dir=os.path.dirname(os.path.abspath(__file__))
        uuid_dir=os.path.join(base_dir, "assets", str(uuid))
        
        Path(uuid_dir).mkdir(parents=True, exists_ok=False)
        
        qr_file=os.path.join(uuid_dir, f"{uuid}.png")
        data_file=os.path.join(uuid_dir, f"data.txt")
        
        qr_generator(qr_file)
        with open(data_file, "w") as file:
            file.write(f"{uuid}\n{datetime.now()}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()