"""Create UploadedDocument from uploads: text stored in DB only (no disk file). Railway-safe."""
from __future__ import annotations

import hashlib
from pathlib import Path

from django.core.files.uploadedfile import UploadedFile

from api.models import UploadedDocument
from api.services.document_extract import extract_text_from_bytes

SUPPORTED_SUFFIXES = frozenset({".pdf", ".txt", ".md", ".markdown", ".docx"})


def store_uploaded_file(f: UploadedFile) -> tuple[UploadedDocument | None, str | None]:
    """
    Read upload in memory, extract text, save UploadedDocument.
    Does not write under data/uploads/ (avoids read-only / ephemeral disk issues on Railway).
    """
    name = getattr(f, "name", "upload") or "upload"
    suffix = Path(name).suffix.lower()
    if suffix not in SUPPORTED_SUFFIXES:
        return None, f"Unsupported type. Use one of: {', '.join(sorted(SUPPORTED_SUFFIXES))}"

    digest = hashlib.sha256()
    chunks: list[bytes] = []
    for chunk in f.chunks():
        digest.update(chunk)
        chunks.append(chunk)
    data = b"".join(chunks)
    content_hash = digest.hexdigest()

    try:
        text = extract_text_from_bytes(data, suffix)
    except ValueError as e:
        return None, str(e)
    except Exception as e:
        return None, f"Could not read this document (corrupt or unsupported content): {e}"

    stored_path = f"inline/{content_hash}{suffix}"
    try:
        doc = UploadedDocument.objects.create(
            original_name=name,
            stored_path=stored_path,
            content_hash=content_hash,
            text_extracted=text,
        )
    except Exception as e:
        return None, f"Could not save document record: {e}"
    return doc, None
