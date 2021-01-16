from DataExplorer import DataExplorer
from DataLoader import DataLoader
from sklearn.linear_model import LinearRegression

# First of all we load dataset and normalize it using DataLoader
from Plotter import Plotter

data_loader = DataLoader()

data_loader.load_and_normalize_data()

train_data = data_loader.get_train_data()
test_data = data_loader.get_test_data()


# Then we use DataExplorer to explore data. Info allows us to see how many null values exists. We also c
data_explorer = DataExplorer()
data_to_visualize = train_data[['WoodDeckSF', 'SalePrice']]

data_explorer.describe(train_data)
data_explorer.info(train_data)

# And we use Plotter to create some data visualization
plotter = Plotter()

# plotter.plot(data_to_visualize, 'WoodDeckSF')
# plotter.show_histogram(data_to_visualize)
# plotter.show_box_plot(data_to_visualize)

# Create model
model = LinearRegression().fit(train_data, train_data['SalePrice'])
r_sq = model.score(train_data, train_data['SalePrice'])

print()