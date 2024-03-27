import sys
import xml.etree.ElementTree as ET
from rich.text import Text
from textual.app import App, ComposeResult
from textual.screen import ModalScreen
from textual.containers import Container, ScrollableContainer
from textual.widgets import Header, Footer, Static, Button, DataTable, Label

class JUnitData:
    def __init__(self, path):
        self.path = path
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()
        self.tests = int(self.root.get('tests', 0))
        self.failures = int(self.root.get('failures', 0))
        self.errors = int(self.root.get('errors', 0))
        self.time = float(self.root.get('time', 0))

        self.skipped = 0
        self.passed = 0

        self.failed_tests = []
        self.skipped_tests = []
        self.passed_tests = []

        for testcase in self.root.iter('testcase'):
            if testcase.find('skipped') is not None:
                self.skipped_tests.append(testcase)
                self.skipped += 1
            elif testcase.find('failure') is not None:
                self.failed_tests.append(testcase)
            else:
                self.passed_tests.append(testcase)
                self.passed += 1
        
        self.selected = None

class LogDetails(ModalScreen[None]):
    BINDINGS = [("escape", "pop_screen"), ("q", "quit", "Quit")]

    DEFAULT_CSS = """
    LogDetails {
        align: center middle;
    }

    #log-details-container {
        width: auto;
        height: auto;
        min-width: 50%;
        max-width: 70%;
        max-height: 80%;
        background: $panel;
        align: center middle;
        padding: 4 6;

        & > Static#title {
            margin-bottom: 2;
        }

        & > Label#exit {
            margin-top: 1;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Container(id="log-details-container"):
            if data.selected.find('failure') is not None:
                yield Static(f"FAILED: {data.selected.get('classname')}")
                yield Static(f"Module: {data.selected.get('name')}", id="title")
                with ScrollableContainer():
                    yield Static(data.selected.find('failure').text)
            elif data.selected.find('skipped') is not None:
                yield Static(f"SKIPPED: {data.selected.get('classname')}")
                yield Static(f"Module: {data.selected.get('name')}", id="title")
                with ScrollableContainer():
                    yield Static(data.selected.find('skipped').text)
            else:
                yield Static(f"PASSED: {data.selected.get('classname')}")
                yield Static(f"Module: {data.selected.get('name')}", id="title")
            yield Label("Press ESC to exit", id="exit")

class Testing(App):
    CSS_PATH = "bb-testing.tcss"
    TITLE = "Summary of " + sys.argv[1]
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="summary"):
            with Container(classes="metric"):
                yield Static("Tests", id="tests", classes="type")
                yield Static(f"{data.tests}", id="value")
            with Container(classes="metric"):
                yield Static("Passed", id="pass", classes="type")
                yield Static(f"{data.passed}", id="value")
            with Container(classes="metric"):
                yield Static("Failed", id="fail", classes="type")
                yield Static(f"{data.failures}", id="value")
            with Container(classes="metric"):
                yield Static("Skipped", id="skip", classes="type")
                yield Static(f"{data.skipped}", id="value")
            with Container(classes="metric"):
                yield Static("Errors", id="errors", classes="type")
                yield Static(f"{data.errors}", id="value")
            with Container(classes="metric"):
                yield Static("Time Taken", id="time", classes="type")
                yield Static(f"{data.time}s", id="value")
        with Container(id="testcases"):
            with Container(id="failed-tests", classes="tests"):
                yield Static("Failed Tests", id="fail")
                with ScrollableContainer():
                    yield DataTable(cursor_type="row", zebra_stripes=True, id="failed-table")
            with Container(id="skipped-tests", classes="tests"):
                yield Static("Skipped Tests", id="skip")
                with ScrollableContainer():
                    yield DataTable(cursor_type="row", zebra_stripes=True, id="skipped-table")
            with Container(id="passed-tests", classes="tests"):
                yield Static("Passed Tests", id="pass")
                yield DataTable(cursor_type="row", zebra_stripes=True, id="passed-table")
        yield Footer()

    def on_mount(self) -> None:
        COLUMNS = ("Test Name", "Module", "Time")
        failed_table = self.query_one("#failed-table")
        failed_table.add_columns(*COLUMNS)
        failed_table.focus()
        for number, testcase, in enumerate(data.failed_tests, start=1):
            label = Text(str(number), style="#B0FC38 italic")
            row = (testcase.get('classname'), testcase.get('name'), testcase.get('time'))
            failed_table.add_row(*row, label=label)

        skipped_table = self.query_one("#skipped-table")
        skipped_table.add_columns(*COLUMNS)
        for number, testcase in enumerate(data.skipped_tests, start=1):
            label = Text(str(number), style="#B0FC38 italic")
            row = (testcase.get('classname'), testcase.get('name'), testcase.get('time'))
            skipped_table.add_row(*row, label=label)

        passed_table = self.query_one("#passed-table")
        passed_table.add_columns(*COLUMNS)
        for number, testcase in enumerate(data.passed_tests, start=1):
            label = Text(str(number), style="#B0FC38 italic")
            row = (testcase.get('classname'), testcase.get('name'), testcase.get('time'))
            passed_table.add_row(*row, label=label)
    
    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        event.stop()
        if event.data_table.id == "failed-table":
            data.selected = data.failed_tests[event.cursor_row]
            self.push_screen(LogDetails())
        elif event.data_table.id == "skipped-table":
            data.selected = data.skipped_tests[event.cursor_row]
            self.push_screen(LogDetails())
        else:
            data.selected = data.passed_tests[event.cursor_row]
            self.push_screen(LogDetails())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Missing path to JUnit XML file as argument")
        sys.exit(1)
    if sys.argv[1][-4:] != ".xml":
        print("Error: Argument is not a JUnit XML file")
        sys.exit(2)
    
    data = JUnitData(sys.argv[1])
    Testing().run()