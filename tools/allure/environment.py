import platform
import sys

from config import settings


def create_allure_environment_file():
    all_properties_data = settings.model_dump()
    all_properties_data['os_info'] = f"{platform.system()}, {platform.release()}"
    all_properties_data['python_version'] = sys.version

    properties_lines = [f'{key}={value}' for key, value in all_properties_data.items()]

    properties_content = '\n'.join(properties_lines)

    with open(settings.allure_results_dir.joinpath("environment.properties"), 'w+') as file:
        file.write(properties_content)






