from app.utils.text_cleaner import clean_text


def process_job_description(description: str) -> dict:
    cleaned = clean_text(description)

    return {
        "original_length": len(description),
        "cleaned_length": len(cleaned),
        "cleaned_preview": cleaned[:300]
    }

