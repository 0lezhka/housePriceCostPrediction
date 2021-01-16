import matplotlib.pyplot as plt


class Plotter:
    def plot(self, xy_df, sort_column=None, x_label=None, y_label=None):
        if sort_column is not None:
            xy_df = xy_df.sort_values([sort_column])

        plt.plot(xy_df.iloc[:, 0], xy_df.iloc[:, 1].to_list())

        if x_label is not None:
            plt.xlabel(x_label)

        if y_label is not None:
            plt.ylabel(y_label)

        plt.show()

    def show_histogram(self, df):
        df.hist()
        plt.show()

    def show_box_plot(self, df):
        plt.figure(figsize=(8, 4), dpi=288)
        df.plot(kind='box', subplots=True)
        plt.show()
