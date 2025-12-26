from app.utils.skill_dictionary import SKILLS


def extract_skills(text: str) -> list[str]:
    text = text.lower()
    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return sorted(set(found))

