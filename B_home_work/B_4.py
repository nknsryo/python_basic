def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています

    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)_
    total_weather = 0
    for area_temperature in range(0, 8):
        total_weather += weather_information[area_temperature]['temperature']

    print(total_weather / len(range(0, 8)))

    print()
    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    for area_temperature in range(0, 8):
        if weather_information[area_temperature]['prefecture'] == '大阪府' \
                and weather_information[area_temperature]['station'] == '堺':
            print(weather_information[area_temperature]['station'])
        elif weather_information[area_temperature]['prefecture'] == '大阪府':
            print(weather_information[area_temperature]['station'] + ",", end=' ')
        else:
            pass

    print()
    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    total_weather = 0
    for area_temperature in range(0, 8):
        if weather_information[area_temperature]['prefecture'] == '福岡県':
            total_weather += weather_information[area_temperature]['temperature']
        else:
            pass
    print(total_weather / 2)


if __name__ == '__main__':
    main()
