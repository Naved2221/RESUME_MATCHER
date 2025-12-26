from app.utils.resume_parser import extract_text


def process_resume(filename: str, file_bytes: bytes) -> dict:
    text = extract_text(filename, file_bytes)

    cleaned_text = text.strip()

    return {
        "text": cleaned_text,
        "length": len(cleaned_text),
        "preview": cleaned_text[:300]
    }

