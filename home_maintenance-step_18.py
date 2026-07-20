# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: HomeMaintenance
class Tag:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Tag name must be a non-empty string")
        self.name = name.strip().lower()

    def __repr__(self):
        return f"Tag({self.name!r})"


class TagManager:
    _all_tags = {}
    _room_tags = {}
    _work_tags = {}

    @staticmethod
    def add_tag(tag_name, target_type="room"):
        tag = Tag(tag_name)
        if target_type == "room":
            TagManager._room_tags.setdefault(tag.name, []).append(tag)
        elif target_type == "work":
            TagManager._work_tags.setdefault(tag.name, []).append(tag)
        else:
            raise ValueError(f"Unknown target type: {target_type}")
        return tag

    @staticmethod
    def remove_tag(tag_name, target_type="room"):
        if target_type == "room":
            tags = TagManager._room_tags.pop(tag_name.lower(), [])
        elif target_type == "work":
            tags = TagManager._work_tags.pop(tag_name.lower(), [])
        else:
            raise ValueError(f"Unknown target type: {target_type}")
        for item in list(TagManager._all_tags.values()):
            if isinstance(item, Tag) and item.name == tag_name.lower():
                return tag_name
        return None

    @staticmethod
    def get_tags(target_type="room"):
        if target_type == "room":
            return TagManager._room_tags
        elif target_type == "work":
            return TagManager._work_tags
        else:
            raise ValueError(f"Unknown target type: {target_type}")

    @staticmethod
    def has_tag(tag_name, target_type="room"):
        if target_type == "room":
            return tag_name.lower() in TagManager._room_tags
        elif target_type == "work":
            return tag_name.lower() in TagManager._work_tags
        else:
            raise ValueError(f"Unknown target type: {target_type}")

    @staticmethod
    def clear_all():
        TagManager._all_tags.clear()
        TagManager._room_tags.clear()
        TagManager._work_tags.clear()
