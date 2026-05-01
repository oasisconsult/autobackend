import os
import zipfile
from datetime import datetime


def build_zip(project_path: str, output_dir: str = "exports") -> str:
    """
    Packages generated backend into downloadable ZIP
    """

    os.makedirs(output_dir, exist_ok=True)

    filename = f"backend_{datetime.utcnow().timestamp()}.zip"
    zip_path = os.path.join(output_dir, filename)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:

        for root, dirs, files in os.walk(project_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, project_path)
                zipf.write(full_path, arcname)

    return zip_path