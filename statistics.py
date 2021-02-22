class Statistics:
    def __init__(self, filename: str):
        self.__values_list = []
        self.name = filename
        with open(filename, 'r') as f:
            for line in f.readlines():
                self.__values_list.append(int(line))

    def average(self) -> float:
        sum = 0
        for number in self.__values_list:
            sum += number
        return sum / len(self.__values_list)

    def set(self) -> set:
        return set(self.__values_list)

    def list(self) -> list:
        return self.__values_list

    def add_number(self, number: int) -> None:
        self.__values_list.append(number)


class StatisticsLibrary:
    def __init__(self, filenames):
        self.__statistics = []
        for file in filenames:
            self.__statistics.append(Statistics(file))

    def total_average(self) -> float:
        sum = 0
        total_size = 0
        for stat in self.__statistics:
            size = len(stat.list())
            total_size += size
            sum += stat.average() * total_size

        return sum / total_size

    def files(self):
        filenames = []
        for stat in self.__statistics:
            filenames.append(stat.name)
        return filenames


if __name__ == '__main__':
    s = Statistics(filename="data.csv")
    print(s.average())

    avg_check = Statistics(filename='average_check.csv')
    print(avg_check.average())

    avg_check.add_number(100)
    print(avg_check.average())

    print(avg_check.set())
    print(avg_check.list())

    collection = StatisticsLibrary(["data.csv", "average_check.csv"])
    print(collection.total_average())
    print(collection.files())