
import data
import json
from time import strftime, gmtime


def convertTime(seconds: int) -> str:
    return strftime("%b/%Y",
                    gmtime(seconds))


def parse_data() -> None:
    # Parse each collection individually
    japan_wiiU: dict[str, int] = parse_collection(
        json.loads(data.japanWiiU_data)['data'])

    japan_NS: dict[str, int] = parse_collection(
        json.loads(data.japanNS_data)['data'])

    europe_wiiU: dict[str, int] = parse_collection(
        json.loads(data.europeWiiu_data)['data'])

    us_wiiU: dict[str, int] = parse_collection(
        json.loads(data.usWiiU_data)['data'])
    """ print("-----------------------------------------")
    print("Japan WiiU Hardware Comparisons")
    print(japan_wiiU)
    print("-----------------------------------------")
    print("Japan NS Hardware Comparisons")
    print(japan_NS)
    print("-----------------------------------------")
    print("Europe WiiU Hardware Comparisons")
    print(europe_wiiU)
    print("-----------------------------------------")
    print("USA WiiU Hardware Comparisons")
    print(us_wiiU) """
    print_dict(japan_wiiU)


def parse_collection(data) -> dict[str, int]:
    months = {}
    for obj in data:
        date = convertTime(int(obj['x']) / 1000)
        if date not in months:
            months[date] = int(obj['y'])
        else:
            months[date] += int(obj['y'])
    return months


def print_dict(dictionary):
    for item in dictionary.items():
        print(item)
