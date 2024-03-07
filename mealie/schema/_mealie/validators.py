def validate_locale(locale: str) -> bool:
    valid = {
        # CODE_GEN_ID: MESSAGE_LOCALES
        "ro-RO",
        "it-IT",
        "no-NO",
        "sl-SI",
        "lv-LV",
        "zh-TW",
        "ca-ES",
        "da-DK",
        "pl-PL",
        "nl-NL",
        "sr-SP",
        "fr-CA",
        "en-US",
        "vi-VN",
        "ar-SA",
        "fr-FR",
        "ru-RU",
        "gl-ES",
        "en-GB",
        "lt-LT",
        "ko-KR",
        "zh-CN",
        "cs-CZ",
        "bg-BG",
        "is-IS",
        "hr-HR",
        "pt-BR",
        "tr-TR",
        "uk-UA",
        "pt-PT",
        "fi-FI",
        "el-GR",
        "sk-SK",
        "ja-JP",
        "de-DE",
        "he-IL",
        "sv-SE",
        "hu-HU",
        "es-ES",
        "af-ZA",
        # END: MESSAGE_LOCALES
    }

    return locale in valid
