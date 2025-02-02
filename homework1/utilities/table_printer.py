class TablePrinter:

  def __init__(self, data) -> None:
    errors = self.check_keys(data)
    if len(errors):
      raise ValueError(f"Missing required keys: '{"', '".join(errors)}'")

    self.data = data

    self.headers = data.get("headers", [])
    self.header_separator = data.get("header_separator", "-")
    self.header_alignments = data.get("header_alignments", [])
    self.show_headers = data.get("show_headers", True)
    self.show_header_separator = data.get("show_header_separator", True)

    self.rows = data.get("rows", [[]])
    self.row_alignments = data.get("row_alignments", [])

    self.column_min_width = 3
    self.column_padding = data.get("column_padding", 1) # The amount of whitespace between columns
    self.column_count = 0
    self.column_widths = data.get("column_widths", [])

    self.set_table_attributes()

    # It is valid to print an empty table, so always print
    # the headers if the option has been enabled even if
    # there are no rows.
    if self.show_headers:
      self.print_headers()

    self.print_rows()

  def set_table_attributes(self) -> None:
    '''
    Set the required attributes in the class for printing to function correctly
    '''

    column_count = 0
    column_widths = self.column_widths

    # Set the count to the number of headers
    header_count = len(self.headers)
    if header_count > column_count:
      column_count += header_count - column_count

    ###
    # Set the widths of the columns based on the header values
    for header_number, header in enumerate(self.headers):

      if len(column_widths) <= header_number:
        column_widths.append(self.column_min_width)

      if column_widths[header_number] < len(str(header)):
        column_widths[header_number] = len(str(header))


    ###
    # Now set the column count and column widths based on the data
    for row in self.rows:
      num_row_fields = len(row)
      if num_row_fields > column_count:
        column_count += num_row_fields - column_count

      for row_field_number, row_field_data in enumerate(row):

        if len(column_widths) <= row_field_number:
          column_widths.append(self.column_min_width)

        len_data = len(str(row_field_data))
        if len_data > column_widths[row_field_number]:
          column_widths[row_field_number] = len_data

    self.column_count = column_count
    self.column_widths = column_widths

  def print_headers(self) -> None:
    '''
    Print the headers and separator
    '''

    ###
    # Headers
    line_to_print = ""

    for column_number in range(self.column_count):

      # Create a header if one does not exist (there could be more
      # columns in the rows than the header)).
      if len(self.headers) <= column_number:
        self.headers.append(f"C{column_number}")

      # Get the format parameters
      if len(self.header_alignments) <= column_number:
        self.header_alignments.append("<")
      alignment = self.header_alignments[column_number]

      # Expand the width if necessary based on the header's length.
      # Note: The header may have been added in this function if one
      # was not supplied for each column of data.
      column_width = self.column_widths[column_number]
      required_column_width =len(str(self.headers[column_number]))
      if column_width < required_column_width:
        self.column_widths[column_number] = required_column_width

      # Concatenate the substring
      line_to_print += f"{self.headers[column_number]:{alignment}{column_width}}"
      line_to_print += " " * self.column_padding

    print(line_to_print)

    ###
    # Separators
    if not self.show_header_separator:
      return

    line_to_print = ""

    for column_number in range(self.column_count):
      alignment = self.header_alignments[column_number]
      column_width = self.column_widths[column_number]

      line_to_print += f"{self.header_separator * (column_width):{alignment}{column_width}}"
      line_to_print += " " * self.column_padding

    print(line_to_print)

  def print_rows(self) -> None:
    '''
    Print the rows
    '''

    for row_number, row_data in enumerate(self.rows):

      line_to_print = ""

      for column_number in range(self.column_count):
        #for row_column_number, row_column_data in enumerate(row_data):

        data_to_print = "" if len(row_data) <= column_number else row_data[column_number]

        # Get the format parameters
        if len(self.row_alignments) <= column_number:
          self.row_alignments.append("<")
        alignment = self.row_alignments[column_number]

        column_width = self.column_widths[column_number]

        # Concatenate the substring
        line_to_print += f"{data_to_print:{alignment}{column_width}}"
        line_to_print += " " * self.column_padding

      print(line_to_print)

  def check_keys(self, data: dict) -> list:
    '''
    Validate the input to be sure enough data has been provided
    '''

    required_keys = [
      "rows",
    ]

    optional_keys = [
      "show_headers",
      "show_header_separator",
      "headers",
      "header_separator",
      "header_alignments",
      "row_alignments",
      "column_widths",
      "column_padding",
    ]

    keys = data.keys()

    errors = []
    for key in required_keys:
      if key not in keys:
        errors.append(key)

    extra_keys = set(keys).difference(required_keys + optional_keys)
    if len(extra_keys):
      print(f"[WARNING] Extra keys: '{"','".join(list(extra_keys))}'")

    return errors

if __name__ == "__main__":
  data = {
    "headers": ["Name", "Age", "ID"],
    "rows": [
      ["Bob", "27", "123",],
      ["Bert", "31", "456",],
    ]
  }
  TablePrinter(data)

  print()

  data = {
    "headers": ["Name", "Age", "ID"],
    "header_alignments": ["<", "^", ">"],
    "header_separator": "=",
    "show_headers": True,
    "show_header_separator": True,
    "column_padding": 2,
    "column_widths": [10, 7, 6],
    "row_alignments": ["^", "<", ">"],
    "rows": [
      ["Bob", "27", "123",],
      ["Bert", "31", "456",],
    ]
  }
  TablePrinter(data)

  print()

  data = {
    "headers": ["Name", "Age", "ID"],
    "rows": [
      ["Bob", "27", "123", "abc", 20.5],
      ["Bert", "31", "456",],
    ]
  }
  TablePrinter(data)