"""
Тестовый файл обновления базы знаний WinCC Log Analyzer
Все поля содержат тестовые значения для проверки системы обновлений
"""
from dataclasses import dataclass

@dataclass
class MessageInfo:
    en_desc: str
    ru_desc: str
    en_fix: str
    ru_fix: str
    severity: str = 'INFO'
    category: str = 'General'
    details_en: str = ''
    details_ru: str = ''


def get_update_data():
    """Возвращает тестовые данные для обновления базы знаний"""
    return {
        'KB': {
            'TEST_001111111111111111111111': MessageInfo(
                'Test: Test error code',
                'Тест: Тестовый код ошибки',
                'Test fix instruction',
                'Тестовая инструкция по исправлению',
                'INFO', 'Test',
                'Test detailed description in English',
                'Тестовое подробное описание на русском'
            ),



        }
    }