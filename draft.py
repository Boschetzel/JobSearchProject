def filter_results(self):
    if self.ui_results.filter_col_btn.isChecked():
        # Display GUI for column search
        self.show_filter_column_window()

        # Get user input
        col_name = self.ui_filter_col.ui_column_name.text()

        # Select column based on user input
        df = self.df[col_name]

        # Make df
        temp = pd.DataFrame(df)

        # Make pandas model and display it
        model = PandasModel(temp)
        self.ui_results.tableView.setModel(model)
    else:
        print("Error ....1")

    if self.ui_results.filter_row_btn.isChecked():
        # Display GUI for row  search
        self.show_filter_row_window()

        # Get user input
        col_name = self.ui_filter_row.ui_column_name.text()
        row_name = self.ui_filter_row.ui_row_name.text()

        # Select column and row  based on user input
        df = self.df.loc[self.df[col_name] == row_name]

        # Make df
        temp = pd.DataFrame(df)

        # Make pandas model and display it
        model = PandasModel(temp)
        self.ui_results.tableView.setModel(model)
    else:
        print("Error ...2")