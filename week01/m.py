import pandas as pd
def main():
    content = pd.read_csv("Housing.csv")
    data = pd.DataFrame(content)
    # content.info()
    missing_values = data.isnull().sum()
    # print(missing_values)
    # print(data.describe())
    data = data.drop_duplicates()
    data = data.dropna()
    print(data)
if __name__ == "__main__":
    main()